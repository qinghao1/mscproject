import itertools as it

import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.data import load
from collections import Counter

from model.base import StatelessTransform
from model.utils import get_stanparse_data, \
    get_cosine_similarity_data, get_hungarian_alignment_score_data, find_negated_word_idxs, \
    get_stanparse_depths, get_dataset, get_svo_triples, get_ppdb_data, cosine_sim

from model.baseline.transforms import _refuting_words, _hedging_words


class Word2VecSimilaritySemanticTransform(StatelessTransform):

    def transform(self, X):
        cos_add, cos_mult = get_cosine_similarity_data()
        mat = np.zeros((len(X), 1))
        for i, (_, s) in enumerate(X.iterrows()):
            if np.isnan(mat[i, 0]):
                print s.claimId, s.articleId,
            mat[i, 0] = cos_mult[(s.claimId, s.articleId)]
        return mat

class PartOfSpeechTransform(StatelessTransform):

    _tagdict = load('help/tagsets/upenn_tagset.pickle')

    @staticmethod
    def _count_tags(sentence):
        # remove punctuations
        # sentence = sentence.translate(string.maketrans("", ""), string.punctuation)

        # Part-of-Speech tagging
        tokens = nltk.word_tokenize(sentence.lower())
        text = nltk.Text(tokens)
        tags = nltk.pos_tag(text)

        # count tags
        counts = Counter(tag for word, tag in tags)
        count = np.zeros(len(PartOfSpeechTransform._tagdict.keys()))
        i = 0
        for tag in PartOfSpeechTransform._tagdict.keys():
            count[i] = 0 if counts.get(tag) is None else counts.get(tag)
            i += 1

        return count


    def transform(self, X):
        mat = np.zeros((len(X), 1))
        for i, (_, s) in enumerate(X.iterrows()):
            article_arr = self._count_tags(s.articleHeadline)
            claim_arr = self._count_tags(s.claimHeadline)
            mat[i, 0] = cosine_sim(article_arr, claim_arr)

        return mat

class SentimentTransform(StatelessTransform):

    sentAnalyzer = SentimentIntensityAnalyzer();

    def transform(self, X):
        mat = np.zeros((len(X), 4,)) # compound, neg, neu, pos
        for i, (_, s) in enumerate(X.iterrows()):
            sentScores = SentimentTransform.sentAnalyzer.polarity_scores(s.articleHeadline)
            mat[i, 0] = sentScores['compound']
            mat[i, 1] = sentScores['neg']
            mat[i, 2] = sentScores['neu']
            mat[i, 3] = sentScores['pos']
        return mat

class AverageWordLengthTransform(StatelessTransform):

    @staticmethod
    def remove_punctuation(word):
        return ''.join([c for c in word if c.isalpha()])

    @staticmethod
    def get_average_word_length(sentence):
        words = sentence.split()
        words = map(AverageWordLengthTransform.remove_punctuation, words)
        words = filter(lambda x: len(x) > 0, words)
        return sum([len(word) for word in words]) / len(words)

    def transform(self, X):
        mat = np.zeros((len(X), 1,))
        for i, (_, s) in enumerate(X.iterrows()):
            avg_len = AverageWordLengthTransform.get_average_word_length(s.articleHeadline)
            mat[i, 0] = avg_len
        return mat

class LenRatioTransform(StatelessTransform):

    def transform(self, X):
        mat = np.zeros((len(X), 1,))
        for i, (_, s) in enumerate(X.iterrows()):
            ratio = len(s.articleHeadline) / len(s.claimHeadline)
            mat[i, 0] = ratio
        return mat

_hungarian = get_hungarian_alignment_score_data()


class AlignedPPDBSemanticTransform(StatelessTransform):

    _bins = np.arange(-10.0, 10.05, 0.05)

    def transform(self, X):
        mat = np.zeros((len(X), 1))
        for i, (_, s) in enumerate(X.iterrows()):
            # mat[i, 0] = _hungarian[(s.claimId, s.articleId)][1]
            mat[i, 0] = np.digitize([_hungarian[(s.claimId, s.articleId)][1]], self._bins)[0]
        return mat


class AlignedPPDBSemanticTransform(StatelessTransform):

    def transform(self, X):
        mat = np.zeros((len(X), 1))
        for i, (_, s) in enumerate(X.iterrows()):
            mat[i, 0] = _hungarian[(s.claimId, s.articleId)][1]
        return mat


class NegationAlignmentTransform(StatelessTransform):

    def transform(self, X):
        mat = np.zeros((len(X), 1))
        for i, (_, s) in enumerate(X.iterrows()):
            claim_negated_idxs = find_negated_word_idxs(s.claimId)
            article_negated_idxs = find_negated_word_idxs(s.articleId)
            if not claim_negated_idxs and not article_negated_idxs:
                continue

            for a, b in _hungarian[(s.claimId, s.articleId)][0]:
                if (a in claim_negated_idxs and b not in article_negated_idxs) or \
                        (a not in claim_negated_idxs and b in article_negated_idxs):
                    mat[i, 0] = 1
        return mat


class DependencyRootDepthTransform(StatelessTransform):

    @staticmethod
    def _find_matching(lemmas, words):
        return [h if lem in words else 0 for (h, lem) in lemmas]

    def transform(self, X):
        stanparse_depths = get_stanparse_depths()
        stanparse_data = get_stanparse_data()

        mat = np.zeros((len(X), 2))
        for i, (_, s) in enumerate(X.iterrows()):
            try:
                sp_data = stanparse_data[s.articleId]
                sp_depths = stanparse_depths[s.articleId]
                min_hedge_depth = min_refute_depth = 100

                for j, sentence in enumerate(sp_data['sentences']):
                    grph, grph_labels, grph_depths = sp_depths[j]
                    lemmas = list(enumerate([d[1]['Lemma'].lower() for d in sentence['words']], start=1))
                    hedge_match = self._find_matching(lemmas, _hedging_words)
                    refute_match = self._find_matching(lemmas, _refuting_words)

                    hedge_depths = [grph_depths[d] for d in hedge_match if d > 0]
                    refute_depths = [grph_depths[d] for d in refute_match if d > 0]

                    hedge_depths.append(min_hedge_depth)
                    refute_depths.append(min_refute_depth)

                    min_hedge_depth = min(hedge_depths)
                    min_refute_depth = min(refute_depths)
            except:
                pass
            mat[i, 0] = min_hedge_depth
            mat[i, 1] = min_refute_depth
        return mat


class SVOTransform(StatelessTransform):

    _entailment_map = {
        'ReverseEntailment': 0,
        'ForwardEntailment': 1,
        'Equivalence': 2,
        'OtherRelated': 2,
        'Independence': 3
    }

    @staticmethod
    def _calc_entailment_vec(v, w):
        vec = np.zeros((1, len(set(SVOTransform._entailment_map.values()))))

        if v == w:
            vec[0, SVOTransform._entailment_map['Equivalence']] = 1
            return vec

        ppdb_data = get_ppdb_data()
        relationships = [(x, s, e) for (x, s, e) in ppdb_data.get(v, [])
                         if e in SVOTransform._entailment_map.keys() and x == w]

        if relationships:
            relationship = max(relationships, key=lambda t: t[1])[2]
            vec[0, SVOTransform._entailment_map[relationship]] = 1

        return vec

    @staticmethod
    def _get_word_in_sentence_at_pos(id, s_num, pos):
        stanparse_data = get_stanparse_data()
        sentence = stanparse_data[id]['sentences'][s_num]
        return sentence['words'][pos-1][1]['Lemma'].lower()

    def transform(self, X):
        ll = 3*len(set(SVOTransform._entailment_map.values()))
        mat = np.zeros((len(X), ll))
        for i, (_, s) in enumerate(X.iterrows()):
            try:
                claim_svos = get_svo_triples(s.claimId)
                article_svos = get_svo_triples(s.articleId)

                vec = np.zeros((1, ll))
                for (csvo, asvo) in it.product(claim_svos, article_svos):
                    s_num_c, svo_pos_c = csvo
                    s_num_a, svo_pos_a = asvo

                    nsubj_entailment = self._calc_entailment_vec(
                        self._get_word_in_sentence_at_pos(s.claimId, s_num_c, svo_pos_c['nsubj'][1]),
                        self._get_word_in_sentence_at_pos(s.articleId, s_num_a, svo_pos_a['nsubj'][1])
                    )

                    # use first element of nsubj entry to get verb pos
                    verb_entailment = self._calc_entailment_vec(
                        self._get_word_in_sentence_at_pos(s.claimId, s_num_c, svo_pos_c['nsubj'][0]),
                        self._get_word_in_sentence_at_pos(s.articleId, s_num_a, svo_pos_a['nsubj'][0])
                    )

                    dobj_entailment = self._calc_entailment_vec(
                        self._get_word_in_sentence_at_pos(s.claimId, s_num_c, svo_pos_c['dobj'][1]),
                        self._get_word_in_sentence_at_pos(s.articleId, s_num_a, svo_pos_a['dobj'][1])
                    )

                    vec[0, 0:4] += nsubj_entailment[0]
                    vec[0, 4:8] += verb_entailment[0]
                    vec[0, 8:] += dobj_entailment[0]
                mat[i, :] = vec
            except:
                pass
        return mat



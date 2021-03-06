import argparse
import sys
import os

sys.path.append(os.path.join('..', 'src'))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve


from model.classifiers.lr_predictors import LogitPredictor, CompoundPredictor
from model.classifiers.rf_predictors import RandomForestPredictor
from model.utils import get_dataset, split_data, RunCV, run_test

from model.baseline.transforms import (
    RefutingWordsTransform,
    QuestionMarkTransform,
    HedgingWordsTransform,
    InteractionTransform,
    NegationOfRefutingWordsTransform,
    BoWTransform,
    PolarityTransform,
    BrownClusterPairTransform
)

from model.ext.transforms import (
    AlignedPPDBSemanticTransform,
    NegationAlignmentTransform,
    Word2VecSimilaritySemanticTransform,
    DependencyRootDepthTransform,
    SVOTransform,
    PartOfSpeechTransform,
    SentimentTransform,
    AverageWordLengthTransform,
    LenRatioTransform,
    WordLengthPercentageTransform
)


DEFAULT_FEATURES = 'Q,BoW,W2V,PPDB,RootDep,NegAlgn,SVO'

def draw_learning_curve(p, X, y):
    # Create CV training and test scores for various training set sizes
    train_sizes, train_scores, test_scores = learning_curve(p,
                                                            X,
                                                            y,
                                                            # Number of folds in cross-validation
                                                            cv=10,
                                                            # Evaluation metric
                                                            scoring='accuracy',
                                                            # Use all computer cores
                                                            n_jobs=-1,
                                                            # 50 different sizes of the training set
                                                            train_sizes=np.linspace(0.01, 1.0, 50))

    # Create means and standard deviations of training set scores
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)

    # Create means and standard deviations of test set scores
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    # Draw lines
    plt.plot(train_sizes, train_mean, '--', color="#111111", label="Training score")
    plt.plot(train_sizes, test_mean, color="#111111", label="Cross-validation score")

    # Draw bands
    plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color="#DDDDDD")
    plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color="#DDDDDD")

    # Create plot
    plt.title("Learning Curve")
    plt.xlabel("Training Set Size"), plt.ylabel("Accuracy Score"), plt.legend(loc="best")
    plt.tight_layout()
    plt.show()
    plt.savefig('result.png')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='run_baseline cmd-line arguments.')

    # inc_transforms = [
    #     'Q',                # 1             1
    #     'BoW-Hed',          # 2-36         35
    #     'BoW-Ref',          # 37-48         12
    #     'I',                # 49-1272       1,224
    #     'BoW',              # 1273-1772     500
    #     'Sim-Algn-W2V',     # 1773-1773     1
    #     'Sim-Algn-PPDB',    # 1774-1774     1
    #     'Root-Dist',        # 1775-1776     2
    #     'Neg-Algn',         # 1777-1779     3
    #     'SVO',              # 1780-1788     9
    #     ]

    parser.add_argument('-f',
                        default=DEFAULT_FEATURES,
                        type=str)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', action='store_true')
    group.add_argument('-a', action='store_true')

    args = parser.parse_args()

    predictor = LogitPredictor

    train_data = get_dataset('url-versions-2015-06-14-clean-train.csv')
    X, y = split_data(train_data)

    test_data = get_dataset('url-versions-2015-06-14-clean-test.csv')

    transforms = {
        'BoW': lambda: BoWTransform(),
        'Q': QuestionMarkTransform,
        'W2V': Word2VecSimilaritySemanticTransform,
        'PPDB': AlignedPPDBSemanticTransform,
        'NegAlgn': NegationAlignmentTransform,
        'RootDep': DependencyRootDepthTransform,
        'SVO': SVOTransform,
        'PoS': PartOfSpeechTransform,
        'Sent': SentimentTransform,
        'AvgWordLen': AverageWordLengthTransform,
        'LenRatio': LenRatioTransform,
        'Perc': WordLengthPercentageTransform
    }

    inc_transforms = args.f.split(',')
    diff = set(inc_transforms).difference(transforms.keys())
    if diff:
        print 'Unrecognised features:', diff
        sys.exit(1)
    print 'Feature set:', inc_transforms
    if args.i:
        # incremental
        print 'Incremental test'
        df_out = pd.DataFrame(index=inc_transforms,
                              columns=['accuracy-cv', 'accuracy-test'], data=np.nan)
        inc_transforms_cls = []
        for i, k in enumerate(inc_transforms):
            inc_transforms_cls.append(transforms[k])
            print 'Using features:', inc_transforms[:i+1]

            p = predictor(inc_transforms_cls)
            cv_score = RunCV(X, y, p, display=True).run_cv()
            test_score = run_test(X, y, test_data, p, display=True)

            df_out.ix[k, 'accuracy-cv'] = cv_score.accuracy
            df_out.ix[k, 'accuracy-test'] = test_score.accuracy
        print(df_out)
    elif args.a:
        # ablation
        print 'Ablation test'

        if args.f:
            features = args.f
        else:
            features = DEFAULT_FEATURES
        ablations = [[x] for x in features.split(',')]
        df_out = pd.DataFrame(index=['-' + str(a) for a in ablations],
                              columns=['accuracy-cv', 'accuracy-test'], data=np.nan)
        inc_transforms_cls = [transforms[t] for t in inc_transforms]
        p = predictor(inc_transforms_cls)
        cv_score = RunCV(X, y, p, display=False).run_cv()
        test_score = run_test(X, y, test_data, p, display=False)
        print 'CV score: :{0:f}'.format(cv_score.accuracy)
        print 'Test score: :{0:f}'.format(test_score.accuracy)

        for ablation in ablations:
            print 'Ablating: ' + str(ablation)
            inc_transforms_ablate = list(inc_transforms)
            for a in ablation:
                try:
                    inc_transforms_ablate.remove(a)
                except:
                    pass
            print 'Ablated feature set:' + str(inc_transforms_ablate)
            inc_transforms_cls_ablate = [transforms[t] for t in inc_transforms_ablate]
            p = predictor(inc_transforms_cls_ablate)
            cv_score_ablate = RunCV(X, y, p, display=False).run_cv()
            test_score_ablate = run_test(X, y, test_data, p, display=False)

            key = '-' + str(ablation)
            print 'Ablated CV score:', cv_score_ablate.accuracy
            print 'Ablated test score:', test_score_ablate.accuracy
            df_out.ix[key, 'accuracy-cv'] = cv_score.accuracy - cv_score_ablate.accuracy
            df_out.ix[key, 'accuracy-test'] = test_score.accuracy - test_score_ablate.accuracy
        print(df_out * 100.0)
    else:
        p = predictor([transforms[t] for t in inc_transforms])
        test_score = run_test(X, y, test_data, p, display=True)
        draw_learning_curve(p, X, y)

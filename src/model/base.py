from sklearn.base import BaseEstimator
from sklearn.metrics import accuracy_score

from model.utils import calc_confusion_matrix, calc_measures, Score


class StatelessTransform(object):
    def fit(self, X, y=None):
        return self


class AbstractPredictor(BaseEstimator):

    def fit(self, X, y=None):
        Z = self.pipeline.fit_transform(X, y)
        self.classifier.fit(Z, y)
        return self

    def predict(self, X):
        Z = self.pipeline.transform(X)
        labels = self.classifier.predict(Z)
        return labels

    def predict_proba(self, X):
        Z = self.pipeline.transform(X)
        probabilities = self.classifier.predict_proba(Z)
        return probabilities

    def score(self, X, y):
        y_predicted = self.predict(X)
        misclassified_idxs = y_predicted != y
        alldata = X.copy()
        alldata['pred_label'] = y_predicted
        print "Misclassifications\n============="
        print alldata[misclassified_idxs]
        for _,misclassified in alldata[misclassified_idxs].iterrows():
            print misclassified['claimHeadline']
            print misclassified['articleHeadline']
            print 'Real stance: ' + misclassified['articleHeadlineStance']
            print 'Pred stance: ' + misclassified['pred_label']
            print '----'
        accuracy = accuracy_score(y, y_predicted)
        cm = calc_confusion_matrix(y, y_predicted)
        measures = calc_measures(cm)
        score = Score(cm, accuracy, measures)
        return score

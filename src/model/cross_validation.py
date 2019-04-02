import numpy as np

from sklearn.model_selection import KFold

class ClaimKFold(KFold):

    def __init__(self, data, n_splits=10, shuffle=False):
        self.kfold = KFold(n_splits, shuffle, None)
        self.shuffle = shuffle
        self.data = data.copy()
        self.n_splits = n_splits
        self.data['iloc_index'] = range(len(self.data))

    def _iter_test_indices(self, *unused):
        claim_ids = np.unique(self.data.claimId)
        cv = self.kfold.split(claim_ids)

        for _, test in cv:
            test_claim_ids = claim_ids[test]
            test_data = self.data[self.data.claimId.isin(test_claim_ids)]
            yield test_data.iloc_index.values

    def __len__(self):
        return self.n_splits

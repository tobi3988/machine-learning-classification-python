import unittest
import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
from importer.Import import Importer
from sklearn import preprocessing
from sklearn.cross_validation import KFold


class Learner:
    def __init__(self):
        pass

    def crossvalidation(self, clf, trainingFeatures, trainingLabels):
        kf = KFold(trainingLabels.size, n_folds=10)
        for train, test in kf:
            trainCLF = clf = svm.SVC(kernel='rbf', C=1)

            X_train, X_test, y_train, y_test = trainingFeatures[train], trainingFeatures[test], trainingLabels[train], trainingLabels[test]
        scores = cross_validation.cross_val_score(
            clf, trainingFeatures, trainingLabels, cv=10)
        print scores

    def learn(self):
        importer = Importer()
        trainingData = importer.read("../importer/training.csv")
        trainingLabels = trainingData[:, 27]
        trainingFeatures = trainingData[:, :27]
        trainingFeatures = preprocessing.scale(trainingFeatures)

        validationFeatures = importer.read("../importer/validation.csv")
        validationFeatures = preprocessing.scale(validationFeatures)
        clf = svm.SVC(kernel='rbf', C=1)
        #clf = svm.SVC(kernel='rbf', C=1)
        self.crossvalidation(clf, trainingFeatures, trainingLabels)
        clf.fit(trainingFeatures, trainingLabels)
        validationResults =  clf.predict(validationFeatures)
        np.savetxt("validationresult.csv", validationResults , delimiter=",")


class LearnerTests(unittest.TestCase):
    def testCrossValidation(self):
        learner = Learner()
        learner.learn()

def main():
    unittest.main()


if __name__ == '__main__':
    main()
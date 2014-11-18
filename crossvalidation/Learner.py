from scipy import stats
import unittest
import numpy as np
from sklearn import cross_validation
from sklearn import svm
from importer.Import import Importer
from sklearn import preprocessing
from sklearn.cross_validation import KFold


class Learner:
    def __init__(self):
        pass

    def kernelType(self):
        return 'rbf'

    def folds(self):
        return 10

    def slack(self):
        return 10


    def learn(self):
        importer = Importer()
        trainingData, validationFeatures = self.readData(importer)
        trainingFeatures, trainingLabels = self.splitFeaturesAndLabels(trainingData)
        trainingFeatures, validationFeatures = self.normalizeData(trainingFeatures, validationFeatures)
        self.crossvalidation(trainingFeatures, trainingLabels)

        validationResults = self.trainAndPredict(validationFeatures, trainingFeatures, trainingLabels)
        self.saveToCSV(validationResults)

    def trainAndPredict(self, X_test, X_train, y_train):
        trainCLF = svm.SVC(kernel=self.kernelType(), C=self.slack(), )
        trainCLF.fit(X_train, y_train)
        y_predict = trainCLF.predict(X_test)
        return y_predict

    def crossvalidation(self, trainingFeatures, trainingLabels):
        kf = KFold(trainingLabels.size, n_folds=self.folds())
        totalScores = 0
        for train, test in kf:
            X_train, X_test, y_train, y_test = trainingFeatures[train], trainingFeatures[test], trainingLabels[train], trainingLabels[test]
            y_predict = self.trainAndPredict(X_test, X_train, y_train)
            scores = self.calculateScores(y_predict, y_test)
            totalScores += scores
        print totalScores/self.folds()

    def calculateScores(self, predicted, test):
        difference = predicted - test
        lengthOfTest = test.shape[0]
        scores = (5*sum(difference == 2) + sum(difference == -2)) / float(lengthOfTest)
        return scores

    def readData(self, importer):
        trainingData = importer.read("../importer/training.csv")
        validationFeatures = importer.read("../importer/validation.csv")
        return trainingData, validationFeatures

    def splitFeaturesAndLabels(self, trainingData):
        trainingLabels = trainingData[:, 27]
        trainingFeatures = trainingData[:, :27]
        return trainingFeatures, trainingLabels

    def normalizeData(self, trainingFeatures, validationFeatures):
        trainingFeatures = preprocessing.scale(trainingFeatures)
        validationFeatures = preprocessing.scale(validationFeatures)

        return trainingFeatures, validationFeatures

    def saveToCSV(self, validationResults):
        np.savetxt("validationresult.csv", validationResults, delimiter=",")



class LearnerTests(unittest.TestCase):
    def testCrossValidation(self):
        learner = Learner()
        learner.learn()

def main():
    unittest.main()


if __name__ == '__main__':
    main()
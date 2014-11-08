import unittest
import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
from importer.Import import Importer
from sklearn import preprocessing


class Learner:
    def __init__(self):
        pass

    def learn(self):
        importer = Importer()
        trainingData = importer.read("../importer/training.csv")
        trainingLabels = trainingData[:, 27]
        trainingFeatures = trainingData[:, :27]
        trainingFeatures = preprocessing.scale(trainingFeatures)

        validationFeatures = importer.read("../importer/validation.csv")
        validationFeatures = preprocessing.scale(validationFeatures)
        #clf = svm.SVC(kernel='rbf',  class_weight={1:5})
        clf = svm.SVC(kernel='rbf', C=1)
        scores = cross_validation.cross_val_score(
        clf, trainingFeatures, trainingLabels, cv=10)
        clf.fit(trainingFeatures, trainingLabels)
        validationResults =  clf.predict(validationFeatures)
        np.savetxt("validationresult.csv", validationResults , delimiter=",")

        print scores

class LearnerTests(unittest.TestCase):
    def testCrossValidation(self):
        learner = Learner()
        learner.learn()

def main():
    unittest.main()


if __name__ == '__main__':
    main()
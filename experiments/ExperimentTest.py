import unittest
from experiments.Experiment import Experiment


class FooTests(unittest.TestCase):
    def testMatches(self):
        experiment = Experiment()
        experiment.test()

def main():
    unittest.main()


if __name__ == '__main__':
    main()
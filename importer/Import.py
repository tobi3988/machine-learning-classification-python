__author__ = 'tobi'

import unittest
import csv
import numpy as np


class Importer:
    def __init__(self):
        pass

    def read(self, csvName):
        reader = csv.reader(open(csvName, "rb"), delimiter=',')
        x = list(reader)
        result = np.array(x).astype('float')
        return result


class ImportTests(unittest.TestCase):
    def testReadCsv(self):
        importer = Importer()
        self.failUnless(np.array_equal(importer.read("unittest.csv"), np.array(([1, 2, 3, 4], [5, 6, 7, 8])).astype('float')))

    def testReadOtherCsv(self):
        importer = Importer()
        self.failUnless(np.array_equal(importer.read("another.csv"), np.array(([2, 2, 2, 2], [0, 0, 0, 0])).astype('float')))



def main():
    unittest.main()


if __name__ == '__main__':
    main()
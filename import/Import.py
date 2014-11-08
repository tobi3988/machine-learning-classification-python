__author__ = 'tobi'

import unittest
import datetime
import csv
import numpy as np


class Importer:
    def __init__(self, csvName):
        self.csvName = csvName

    def read(self):
        reader = csv.reader(open(self.csvName, "rb"), delimiter=',')
        x = list(reader)
        result = np.array(x).astype('float')
        print result.all()
        return result


class ImportTests(unittest.TestCase):
    def testReadCsv(self):
        importer = Importer("unittest.csv")
        self.failUnless(np.array_equal(importer.read(), np.array(([1, 2, 3, 4], [5, 6, 7, 8])).astype('float')))

    def testReadOtherCsv(self):
        importer = Importer("another.csv")
        self.failUnless(np.array_equal(importer.read(), np.array(([2, 2, 2, 2], [0, 0, 0, 0])).astype('float')))



def main():
    unittest.main()


if __name__ == '__main__':
    main()
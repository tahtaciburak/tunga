import unittest

from tunga.retrieval import CSVReader

class TestCSV(unittest.TestCase):
    def test_something(self):
        df = CSVReader("../datasetss/test.csv").read()
        print(df)

if __name__ == '__main__':
    unittest.main()

#
# usage: python Testn71.py
#


import unittest
from n71 import jadge_stopword


class Testn70(unittest.TestCase):
    def test_n70(self):
        with open('english') as stopWords:
            stopWords = [sw.strip() for sw in stopWords.readlines()]
            expected = True
            for sw in stopWords:
                result = jadge_stopword(sw)
                self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

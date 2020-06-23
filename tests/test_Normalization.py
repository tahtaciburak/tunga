import unittest

from tunga.preprocessing import normalization


class TestNormalization(unittest.TestCase):
    def test_remove_punctuation(self):
        actual = normalization.remove_punctuations(
            "Ahmet! Pazardan gelirken domates, peynir, biber ve kimyon al. Kalmazsa; patates al.")
        expected = "Ahmet Pazardan gelirken domates peynir biber ve kimyon al Kalmazsa patates al"
        self.assertEqual(actual, expected)

    def test_remove_digits(self):
        actual = normalization.remove_digits("24 yaşında 1.86 boyunda harbiyeden mezun bir komutan vardı sene 2012ydi")
        expected = "yaşında . boyunda harbiyeden mezun bir komutan vardı sene ydi"
        self.assertEqual(actual, expected)

    def test_remove_digits_type_mismatch(self):
        actual = normalization.remove_digits(3872812341234)
        expected = ""
        self.assertEqual(actual, expected)

    def test_remove_stopwords(self):
        actual = normalization.remove_stopwords("sen ve ben ayni duvarda asili duran bir civi ve fotograf gibiyiz")
        expected = "sen ben ayni duvarda asili duran bir civi fotograf gibiyiz"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

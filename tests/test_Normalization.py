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

    def test_remove_emojis(self):
        actual = normalization.remove_emojis("bugün biraz hastayım 🦠😵😳😱😨😎")
        expected = "bugün biraz hastayım "
        self.assertEqual(actual, expected)

    def test_remove_email(self):
        actual = normalization.remove_email("beyzanın mail adresi olduğu için beyzacanbay34@gmail")
        expected = "beyzanın mail adresi olduğu için "
        self.assertEqual(actual, expected)

    def test_remove_person_names(self):
        actual = normalization.remove_person_names("beyza bilgisayar mühendisi")
        expected = "bilgisayar mühendisi"
        self.assertEqual(actual, expected)

    def test_remove_url(self):
        actual = normalization.remove_url("beyzanın internet adresi http:beyzacanbay")
        expected = "beyzanın internet adresi "
        self.assertEqual(actual, expected)

    def test_remove_mentions(self):
        actual = normalization.remove_mentions("@beyzacanbay @buraktahtaci birlikte çalışıyor")
        expected = "  birlikte çalışıyor"
        self.assertEqual(actual, expected)

    def test_remove_hastag(self):
        actual = normalization.remove_hastag("#beyza çalışıyor #CRYPTTECH")
        expected = " çalışıyor "
        self.assertEqual(actual, expected)

    def test_asciify(self):
        actual = normalization.asciify("çok çalışmak")
        expected = "cok-calismak"
        self.assertEqual(actual, expected)

        actual = normalization.asciify("Koşarcasına eğlenen çocuklar gibi şendik")
        expected = "kosarcasina-eglenen-cocuklar-gibi-sendik"
        self.assertEqual(actual, expected)


    def test_deasciify(self):
        actual = normalization.deasciify("Cok calisiyor")
        expected = "Çok çalışıyor"
        self.assertEqual(actual, expected)

        actual = normalization.deasciify("Aydinlik yarinlarimizin acik zihinleri")
        expected = "Aydınlık yarınlarımızın açık zihinleri"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

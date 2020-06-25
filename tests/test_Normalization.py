import unittest

from tunga.preprocessing import normalization


class TestNormalization(unittest.TestCase):
    def test_remove_punctuation(self):
        actual = normalization.remove_punctuations(
            "Ahmet! Pazardan gelirken domates, peynir, biber ve kimyon al. Kalmazsa; patates al.")
        expected = "Ahmet Pazardan gelirken domates peynir biber ve kimyon al Kalmazsa patates al"
        self.assertEqual(actual, expected)

        actual = normalization.remove_punctuations("-Bu anahtar köşkü de açar, dedi.")
        expected = "Bu anahtar köşkü de açar dedi"
        self.assertEqual(actual, expected)

        actual = normalization.remove_punctuations(
            "Doğduğu yere, Erzurum'a gitmişti")
        expected = "Doğduğu yere Erzuruma gitmişti"
        self.assertEqual(actual, expected)

    def test_remove_digits(self):
        actual = normalization.remove_digits("24 yaşında 1.86 boyunda harbiyeden mezun bir komutan vardı sene 2012ydi")
        expected = "yaşında . boyunda harbiyeden mezun bir komutan vardı sene ydi"
        self.assertEqual(actual, expected)

        actual = normalization.remove_digits("2012 yılında 10 Temmuzda saat 13:40 da gördüm")
        expected = "yılında  Temmuzda saat : da gördüm"
        self.assertEqual(actual, expected)

        actual = normalization.remove_digits("42 yaşındaki adam evine gidiyordu.3 küçük çocuğu yanındaydı")
        expected = "yaşındaki adam evine gidiyordu. küçük çocuğu yanındaydı"
        self.assertEqual(actual, expected)

    def test_remove_digits_type_mismatch(self):
        actual = normalization.remove_digits(3872812341234)
        expected = ""
        self.assertEqual(actual, expected)

        actual = normalization.remove_digits("Bu sene onuncu yaş gününü kutladı")
        expected = "Bu sene onuncu yaş gününü kutladı"
        self.assertEqual(actual, expected)

    def test_remove_stopwords(self):
        actual = normalization.remove_stopwords("sen ve ben ayni duvarda asili duran bir civi ve fotograf gibiyiz")
        expected = "ayni duvarda asili duran civi fotograf gibiyiz"
        self.assertEqual(actual, expected)

        actual = normalization.remove_stopwords("Ne kralların tacı, ne kısa günün kazancı")
        expected = "kralların tacı, kısa günün kazancı"
        self.assertEqual(actual, expected)

        actual = normalization.remove_stopwords("Ya bende sevdiğin şeyden dolayı benden nefret ediyorsan")
        expected = "bende sevdiğin nefret ediyorsan"
        self.assertEqual(actual, expected)

    def test_remove_emojis(self):
        actual = normalization.remove_emojis("bugün biraz hastayım 🦠😵😳😱😨😎")
        expected = "bugün biraz hastayım "
        self.assertEqual(actual, expected)

        actual = normalization.remove_emojis("geçen gün bahçeden meyve 🍏🍎🍐🍋🍌🍉🍇🍓🍈🍒🍑 topladım")
        expected = "geçen gün bahçeden meyve  topladım"
        self.assertEqual(actual, expected)

        actual = normalization.remove_emojis("Bu sene yurtdışına 🧳✈️🛄 tatile 👙🏖️⛵ gideceğim ")
        expected = "Bu sene yurtdışına  tatile  gideceğim "
        self.assertEqual(actual, expected)

    def test_remove_email(self):
        actual = normalization.remove_email("beyzanın mail adresi olduğu için beyzacanbay34@gmail")
        expected = "beyzanın mail adresi olduğu için "
        self.assertEqual(actual, expected)

        actual = normalization.remove_email("beyza@gmail.com burak@gmail ayşe@gmail.com")
        expected = "  "
        self.assertEqual(actual, expected)

    def test_remove_person_names(self):
        actual = normalization.remove_person_names("Beyza bilgisayar mühendisi")
        expected = "bilgisayar mühendisi"
        self.assertEqual(actual, expected)

        actual = normalization.remove_person_names("Ali Ayşe Ahmet ve Mehmet yakın arkadaş")
        expected = "ve yakın arkadaş"
        self.assertEqual(actual, expected)

        actual = normalization.remove_person_names(
            "fatma arkadaşları gül ve yağmur birlikte oyun oynarken düştü annesi semiha hanım hastaneye götürdü")
        expected = "arkadaşları ve birlikte oyun oynarken düştü annesi hanım hastaneye götürdü"
        self.assertEqual(actual, expected)

    def test_remove_url(self):
        actual = normalization.remove_url("beyzanın internet adresi http:beyzacanbay")
        expected = "beyzanın internet adresi "
        self.assertEqual(actual, expected)

    def test_remove_mentions(self):
        actual = normalization.remove_mentions("@beyzacanbay @buraktahtaci birlikte çalışıyor")
        expected = "  birlikte çalışıyor"
        self.assertEqual(actual, expected)

    def test_remove_hashtag(self):
        actual = normalization.remove_hashtag("#beyza çalışıyor #CRYPTTECH")
        expected = " çalışıyor "
        self.assertEqual(actual, expected)

        actual = normalization.remove_hashtag("#parkta #oturuyoruz #köpek #seviyoruz")
        expected = "   "
        self.assertEqual(actual, expected)

        actual = normalization.remove_hashtag("dışarıda #kar ve #yağmur var")
        expected = "dışarıda  ve  var"
        self.assertEqual(actual, expected)

    def test_asciify(self):
        actual = normalization.asciify("çok çalışmak")
        expected = "cok calismak"
        self.assertEqual(actual, expected)

        actual = normalization.asciify("Koşarcasına eğlenen çocuklar gibi şendik")
        expected = "Kosarcasina eglenen cocuklar gibi sendik"
        self.assertEqual(actual, expected)

    def test_deasciify(self):
        actual = normalization.deasciify("Cok calisiyor")
        expected = "Çok çalışıyor"
        self.assertEqual(actual, expected)

        actual = normalization.deasciify("Aydinlik yarinlarimizin acik zihinleri")
        expected = "Aydınlık yarınlarımızın açık zihinleri"
        self.assertEqual(actual, expected)

    def test_correct_typo(self):
        actual = normalization.correct_typo("vri kümsi idrae edre ancaka daha güezl oalbilir")
        expected = "veri kümesi idare eder ancak daha güzel olabilir"
        self.assertEqual(actual, expected)

    def test_stem(self):
        actual = normalization.stem("arkadaşları aralarında konuşuyorlar")
        expected = "arkadaş ara konuşuyor"
        self.assertEqual(actual, expected)

        actual = normalization.stem("sınıftakiler ve okuldakiler")
        expected = "sınıf ve okul"
        self.assertEqual(actual, expected)

        actual = normalization.stem("aşağıdakilerden biri midir")
        expected = "aşağı bir mi"
        self.assertEqual(actual, expected)

    def test_deduplication(self):
        actual = normalization.deduplication("merhaba merhaba nasılsın")
        expected = "merhaba nasılsın"
        self.assertEqual(actual, expected)

        actual = normalization.deduplication("hep ama hep bunu izlerim")
        expected = "hep ama bunu izlerim"
        self.assertEqual(actual, expected)

    def test_remove_outlier(self):
        actual = normalization.remove_outlier(1, 2, "Merhaba bugün hava çok güzel")
        expected = "Metin istediğiniz karakter boyutunda değil"
        self.assertEqual(actual, expected)

        actual = normalization.remove_outlier(15, 35, "Merhaba bugün hava çok güzel")
        expected = "Merhaba bugün hava çok güzel"
        self.assertEqual(actual, expected)

    def test_custom_regex_removal(self):
        actual = normalization.custom_regex_removal('\S', "Merhaba bugün hava çok güzel")
        expected = "    "
        self.assertEqual(actual, expected)

        actual = normalization.custom_regex_removal('\D', "20 Temmuz 2020 Pazartesi")
        expected = "202020"
        self.assertEqual(actual, expected)

        actual = normalization.custom_regex_removal('\w', "Hey! Buraya baksana. Sana dedim. ")
        expected = "!  .  . "
        self.assertEqual(actual, expected)


"""   
    def test_syllable(self):
        actual = normalization.syllable("merhaba")
        expected= "mer ha ba"
        self.assertEqual(actual, expected)
"""
if __name__ == '__main__':
    unittest.main()

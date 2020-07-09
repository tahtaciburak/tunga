import unittest

from tunga.preprocessing import extraction


class TestNormalization(unittest.TestCase):
    def test_extract_emoji(self):
        actual = extraction.extract_emoji("Bugün çok rahatsızlandım 🦠😵🤒🤮👩🥼💊")
        expected = "🦠 😵 🤒 🤮 👩 🥼 💊"
        self.assertEqual(actual, expected)

    def test_extract_email(self):
        actual = extraction.extract_email("beyza@gmail.com beyzanın mail adresidir")
        expected = "beyza@gmail.com"
        self.assertEqual(actual, expected)

    def test_extract_url(self):
        actual = extraction.extract_url("Kişisel web sitem http://beyzacanbay.com.tr dir")
        expected = "http://beyzacanbay.com.tr"
        self.assertEqual(actual, expected)

        actual = extraction.extract_url("Web için https://buraktahtaci.com dir")
        expected = "https://buraktahtaci.com"
        self.assertEqual(actual, expected)

    def test_extract_hastag(self):
        actual = extraction.extract_hashtags("#herkese #günaydın demek ne güzel")
        expected = "herkese günaydın"
        self.assertEqual(actual, expected)

    def test_extract_language(self):
        actual = extraction.extract_language("как тебя зовут")
        expected = "ru"
        self.assertEqual(actual, expected)

        actual = extraction.extract_language("Merhaba")
        expected = "tr"
        self.assertEqual(actual, expected)

        actual = extraction.extract_language("Sveiki")
        expected = "lt"
        self.assertEqual(actual, expected)

    def test_extract_prices(self):
        actual = extraction.extract_price("Geçen gün aldığım kahve 13.5 liraydı")
        expected = "13.5 None"
        self.assertEqual(actual, expected)

        actual = extraction.extract_price("Geçen gün aldığım tişört 5$")
        expected = "5 $"
        self.assertEqual(actual,expected)



if __name__ == '__main__':
    unittest.main()

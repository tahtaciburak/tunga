import unittest


class TestMachineLearning(unittest.TestCase):
    def test_sentiment(self):
        from tunga.machine_learning.sentiment_analysis import bert_sentiment
        res = bert_sentiment("çok iyi bir yorum yapacağım")
        self.assertIsNotNone(res)

    def test_product_sentiment(self):
        from tunga.machine_learning.sentiment_analysis import product_sentiment
        res = product_sentiment.get_sentiment("harika bir araba")
        print(res)
        self.assertTrue(True)

    def test_keyword_extraction(self):
        from tunga.machine_learning.keyword_extraction import rake
        actual = rake.extract_keywords("yemeğin tadı mükemmeldi ama fiyatlar çok yüksek")
        self.assertIsNotNone(actual)
        expected = "yemeğin tadı mükemmeldi ; fiyatlar ; yüksek"
        self.assertEqual(expected, actual)

    def test_topic_modelling(self):
        from tunga.machine_learning.topic_modelling import topic_modeller
        res = topic_modeller(["test", "topic", "mopic"])
        self.assertIsNotNone(res)


if __name__ == '__main__':
    unittest.main()

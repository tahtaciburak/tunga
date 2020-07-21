import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.feature_extraction.text import CountVectorizer


def topic_extract(data_path, data_column, topic_number, number_word):
    data = pd.read_csv(data_path)
    count_vectorizer = CountVectorizer()
    count_data = count_vectorizer.fit_transform(data[data_column])

    def print_topics(model, count_vectorizer, n_top_words):
        words = count_vectorizer.get_feature_names()
        for topic_idx, topic in enumerate(model.components_):
            print("Topic_Num: {} ".format(topic_idx))
            print(" ".join([words[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))

    number_topics = topic_number
    number_words = number_word

    lda = LDA(n_components=number_topics, n_jobs=16)
    lda.fit(count_data)

    return ("Topics found via LDA: ", print_topics(lda, count_vectorizer, number_words))


print(topic_extract("../../../datasets/haberler.csv", "text", 7, 15))

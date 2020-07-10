import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_csv("../../../datasets/haberler.csv")
count_vectorizer = CountVectorizer()
count_data = count_vectorizer.fit_transform(data['text'])


def print_topics(model, count_vectorizer, n_top_words):
    words = count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        print("Topic_Num: {} ".format(topic_idx))
        print(" ".join([words[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))


number_topics = 7
number_words = 50

lda = LDA(n_components=number_topics, n_jobs=16)
lda.fit(count_data)

print("Topics found via LDA:")
print_topics(lda, count_vectorizer, number_words)

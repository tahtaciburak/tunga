import warnings
import numpy as np

warnings.simplefilter("ignore", DeprecationWarning)

from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.feature_extraction.text import CountVectorizer


def __get_topic_info(model, count_vectorizer, n_top_words):
    words = count_vectorizer.get_feature_names()
    topic_info = {}
    for topic_idx, topic in enumerate(model.components_):
        topic_info[topic_idx] = [words[i] for i in topic.argsort()[:-n_top_words - 1:-1]]

    return topic_info


def topic_modeller(column, num_topics=10, num_words=10):
    count_vectorizer = CountVectorizer()
    count_data = count_vectorizer.fit_transform([str(item) for item in column])
    lda = LDA(n_components=num_topics, n_jobs=-1)
    m = lda.fit_transform(count_data)
    topic_info = __get_topic_info(lda, count_vectorizer, num_words)
    new_column = []
    for item in m:
        new_column.append(np.argmax(item))
    return new_column, topic_info

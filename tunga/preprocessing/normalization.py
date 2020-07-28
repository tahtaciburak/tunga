from bs4 import BeautifulSoup
import os
import re
import sys
# from Dictionary.Word import Word
# from turkish.deasciifier import Deasciifier
# from Deasciifier.SimpleAsciifier import SimpleAsciifier
from TurkishStemmer import TurkishStemmer
import grpc
import zemberek_grpc.preprocess_pb2_grpc as z_preprocess_g
import zemberek_grpc.preprocess_pb2 as z_preprocess
import zemberek_grpc.morphology_pb2_grpc as z_morphology_g
import zemberek_grpc.morphology_pb2 as z_morphology
import zemberek_grpc.language_id_pb2_grpc as z_langid_g
import zemberek_grpc.language_id_pb2 as z_langid
import zemberek_grpc.normalization_pb2 as z_normalization
import zemberek_grpc.normalization_pb2_grpc as z_normalization_g

channel = grpc.insecure_channel('localhost:6789')
preprocess_stub = z_preprocess_g.PreprocessingServiceStub(channel)
morphology_stub = z_morphology_g.MorphologyServiceStub(channel)
langid_stub = z_langid_g.LanguageIdServiceStub(channel)
normalization_stub = z_normalization_g.NormalizationServiceStub(channel)

__remove_punctuations = str.maketrans('', '', '.,-*!?%\t\n/][₺;_')
__remove_digits = str.maketrans('', '', '0123456789')

stopwords = []
try:
    with open("~/tunga/datasets/stopwords.txt", "r") as f:
        for line in f.readlines():
            stopwords.append(line.strip())
except:
    os.makedirs("~/tunga")
    os.makedirs("~/tunga/datasets")

    print("stopwords not found download it from web")
    pass

name = []
try:
    with open("../datasets/name.txt", "r") as f:
        for line in f.readlines():
            line = line.lower()
            name.append(line.strip())
except:
    print("not use person name")
    pass


def remove_stopwords(text):
    """
    Removes stopwords from text.
    :param text:
    :return: stop_words_removed
    """
    new_tokens = []
    for token in text.split(" "):
        if token.strip().lower() not in stopwords:
            new_tokens.append(token.strip())
    return " ".join(new_tokens).strip()


def remove_digits(text):
    # TODO: Add docstring...
    text = str(text)
    return text.translate(__remove_digits).strip()


def remove_punctuations(text):
    text = str(text)
    if len(text) == 0:
        return text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for punc in text.lower():
        if punc in punctuations:
            text = text.replace(punc, "")
    return text


def remove_html_tags(text):
    return BeautifulSoup(text, "lxml").text


def remove_emojis(text):
    regrex_pattern = re.compile(pattern="["
                                        u"\U0001F600-\U0001F64F"  # emoticons
                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                        u"\U00002702-\U000027B0"
                                        u"\U000024C2-\U0001F251"
                                        u"\U0001f926-\U0001f937"
                                        u"\U00010000-\U0010ffff"
                                        u"\u200d"
                                        u"\u2640-\u2642"
                                        u"\u2600-\u2B55"
                                        u"\u23cf"
                                        u"\u23e9"
                                        u"\u231a"
                                        u"\u3030"
                                        u"\ufe0f"

                                        "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


def remove_email(text):
    text = re.sub(r'\S+@\S+', '', text)
    return text


def remove_person_names(text):
    new_names = []
    for names in text.split(" "):
        names = names.lower()
        if names.strip() not in name:
            new_names.append(names.strip())
    return " ".join(new_names).strip()


def remove_url(text):
    text = re.sub(r'http\S+', '', text)
    return text


def remove_mentions(text):
    text = re.sub(r'@\S+', '', text)
    return text


def remove_hashtag(text):
    text = re.sub(r'#\S+', '', text)
    return text


def remove_price(text):
    text = re.sub(r'\d+', '', text)
    return text


def asciify(text):
    asciifier = SimpleAsciifier()
    result = []
    for word in text.split(" "):
        result.append(asciifier.asciifyWord(Word(word)))
    return " ".join(result)


def syllable(sentence):
    syllables = []
    for word in sentence.split(" "):
        boundaries = __get_syllable_boundaries(word)
        result = []
        for i in range(0, len(boundaries) - 1):
            result.append(word[boundaries[i]:boundaries[i + 1]])
        if len(boundaries) > 0:
            result.append(word[boundaries[len(boundaries) - 1]:])

        for item in result:
            syllables.append(item)
    return " ".join(syllables).strip()


def __get_syllable_boundaries(word):
    size = len(word)
    boundary_indexes = []
    last_index = size
    index = 0
    while last_index > 0:
        letter_count = __letter_count_for_last_syllable(word, last_index)
        if letter_count == -1:
            return [0]

        boundary_indexes.append(last_index - letter_count)
        index += 1
        last_index -= letter_count
    result = []
    for i in range(0, index):
        result.append(boundary_indexes[index - i - 1])
    return result


def __is_vowel(character):
    if character in "aeiıoöuü":
        return True
    return False


def __letter_count_for_last_syllable(chrs, end_index):
    if end_index == 0:
        return -1

    if __is_vowel(chrs[end_index - 1]):
        if end_index == 1:
            return 1
        if __is_vowel(chrs[end_index - 2]):
            return 1
        if end_index == 2:
            return 2
        if not __is_vowel(chrs[end_index - 3]) and end_index == 3:
            return 3
        return 2
    else:
        if end_index == 1:
            return -1
        if __is_vowel(chrs[end_index - 2]):
            if end_index == 2 or __is_vowel(chrs[end_index - 3]):
                return 2
            if end_index == 3 or __is_vowel(chrs[end_index - 4]):
                return 3
            if end_index == 4:
                return -1
            if not __is_vowel(chrs[end_index - 5]):
                return 3
            return 3
        else:
            if not __is_vowel(chrs[end_index - 2]):
                return -1
            if end_index == 2 or not __is_vowel(chrs[end_index - 2]):
                return -1
            if end_index > 3 and not __is_vowel(chrs[end_index - 4]):
                return 4
            return 3


def stem(text):
    turkStem = TurkishStemmer()
    result = []
    for word in text.split(" "):
        result.append(turkStem.stem(word))
    return " ".join(result)


def deasciify(text):
    deasci = Deasciifier(text)
    result = deasci.convert_to_turkish()
    return result


def deduplication(text):
    result = []
    for word in text.split(" "):
        result.append(word)
    new_text = list(dict.fromkeys(result))
    return " ".join(new_text)


def remove_outlier(min, max, text):
    counter = len(text)
    if counter > min and counter < max:
        return text
    else:
        return "Metin istediğiniz karakter boyutunda değil"


def custom_regex_removal(regex, text):
    text = re.sub(r'{}'.format(regex), '', text)
    return text


def fix_decode(text):
    if sys.version_info < (3, 0):
        return text.decode('utf-8')
    else:
        return text


def tokenize(text):
    response = preprocess_stub.Tokenize(z_preprocess.TokenizationRequest(input=text))
    return response.tokens


def tokenization(text):
    tokens = tokenize(text)
    new_txt = ""
    for t in tokens:
        new_txt += t.token + ':' + t.type + " "
    return new_txt


def __analyze(text):
    response = morphology_stub.AnalyzeSentence(z_morphology.SentenceAnalysisRequest(input=text))
    return response


def lemmatization(text):
    fix_text = fix_decode(text)
    analysis_result = __analyze(fix_text)
    new_txt = []
    for a in analysis_result.results:
        best = a.best
        new_txt.append(best.lemmas[0].strip())
    return " ".join(new_txt)


def __find_lang_id(text):
    response = langid_stub.Detect(z_langid.LanguageIdRequest(input=text))
    return response.langId


def find_lang(text):
    lang_id = __find_lang_id(text)
    return lang_id


def __normalize(text):
    response = normalization_stub.Normalize(z_normalization.NormalizationRequest(input=text))
    return response


def correct_typo(text):
    normalization_input = fix_decode(text)
    n_response = __normalize(normalization_input)
    if n_response.normalized_input:
        return n_response.normalized_input
    else:
        print("err")
        return text


def lowercase(text):
    return text.lower()


def uppercase(text):
    return text.upper()

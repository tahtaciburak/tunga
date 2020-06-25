from bs4 import BeautifulSoup
import re
from Dictionary.Word import Word
from turkish.deasciifier import Deasciifier
from Deasciifier.SimpleAsciifier import SimpleAsciifier
from turkishnlp import detector
from TurkishStemmer import TurkishStemmer
import grpc
import zemberek_grpc.preprocess_pb2_grpc as z_preprocess_g
import zemberek_grpc.preprocess_pb2 as z_preprocess
import zemberek_grpc.morphology_pb2_grpc as z_morphology_g
import zemberek_grpc.morphology_pb2 as z_morphology
import sys

obj = detector.TurkishNLP()
obj.create_word_set()

channel = grpc.insecure_channel('localhost:6789')
preprocess_stub = z_preprocess_g.PreprocessingServiceStub(channel)
morphology_stub = z_morphology_g.MorphologyServiceStub(channel)

__remove_punctuations = str.maketrans('', '', '.,-*!?%\t\n/][₺;_')
__remove_digits = str.maketrans('', '', '0123456789')

stopwords = []
try:
    with open("../datasets/stopwords.txt", "r") as f:
        for line in f.readlines():
            stopwords.append(line.strip())
except:
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
    new_tokens = []
    for token in text.split(" "):
        if token.strip().lower() not in stopwords:
            new_tokens.append(token.strip())
    return " ".join(new_tokens).strip()


def remove_digits(text):
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


def asciify(text):
    asciifier = SimpleAsciifier()
    result = []
    for word in text.split(" "):
        result.append(asciifier.asciifyWord(Word(word)))
    return " ".join(result)


def correct_typo(text):
    lwords = obj.list_words(text)
    return " ".join(obj.auto_correct(lwords))


def syllable(text):
    return text


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


def _analyze(text):
    response = morphology_stub.AnalyzeSentence(z_morphology.SentenceAnalysisRequest(input=text))
    return response


def lemmatization(text):
    fix_text = fix_decode(text)
    analysis_result = _analyze(fix_text)
    new_txt = ""
    for a in analysis_result.results:
        best = a.best
        lemmas = ""
        for l in best.lemmas:
            lemmas = lemmas + " " + l
        new_txt += "Word = " + a.token + ", Lemmas = " + lemmas + ", POS = [" + best.pos + "], Full Analysis = {" + best.analysis + "}"

    return new_txt

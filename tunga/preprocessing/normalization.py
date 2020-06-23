from bs4 import BeautifulSoup

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


def remove_stopwords(text):
    new_tokens = []
    for token in text.split(" "):
        if token.strip() not in stopwords:
            new_tokens.append(token.strip())
    return " ".join(new_tokens).strip()


def remove_digits(text):
    text = str(text)
    return text.translate(__remove_digits).strip()


def remove_punctuations(text):
    text = str(text)
    if len(text) == 0:
        return text
    return text.translate(__remove_punctuations).strip()


def remove_html_tags(text):
    return BeautifulSoup(text, "lxml").text


def remove_emojis(text):
    # TODO: Text icinde gecen emojileri sil
    pass


def remove_email(text):
    # TODO: Text icinde gecen email adreslerini sil
    pass


def remove_person_names(text):
    # TODO: Turkce isimlerin oldugu bir kaynak var. Bir cumle icinde turkce kisi ismi geciyorsa kisi isimlerini silip return et.
    pass

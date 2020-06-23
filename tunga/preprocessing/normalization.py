from bs4 import BeautifulSoup
import re
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
            line=line.lower()
            name.append(line.strip())
except:
    print("not use person name")
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
    removing = ""
    lst = re.findall('\S+@\S+', text)
    for word in lst:
        if word in text:
            removing += text.replace(word, "")
    return removing


def remove_person_names(text):
    new_names = []
    for names in text.split(" "):
        if names.strip() not in name:
            new_names.append(names.strip())
    return " ".join(new_names).strip()

def remove_url(text):
    text = re.sub(r'http\S+', '', text)
    return text
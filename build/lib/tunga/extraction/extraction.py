import emoji
import re
from textblob import TextBlob
from price_parser import Price
from collections import OrderedDict

def extract_emoji(text):
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
    text = regrex_pattern.findall(text)
    return ' '.join(OrderedDict.fromkeys(text))

    #return ' '.join(c for c in text if c in emoji.UNICODE_EMOJI)


def extract_email(text):
    text = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    return ' '.join(OrderedDict.fromkeys(text))


def extract_url(text):
    text = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
    return ' '.join(OrderedDict.fromkeys(text))


def extract_hashtags(text):
    text = re.findall(r"#(\w+)", text)
    return ' '.join(OrderedDict.fromkeys(text))


def extract_language(text):
    lang = TextBlob(text)
    detect_lang = lang.detect_language()
    return detect_lang


def extract_price(text):
    price = Price.fromstring(text)
    text = str(price.amount) + " " + str(price.currency)
    return str(text)

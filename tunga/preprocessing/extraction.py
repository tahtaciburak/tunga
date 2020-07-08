import emoji
import re
from textblob import TextBlob
from price_parser import Price


def extract_emoji(text):
    return ' '.join(c for c in text if c in emoji.UNICODE_EMOJI)


def extract_email(text):
    text = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    return ' '.join(text)


def extract_url(text):
    text = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
    return ' '.join(text)


def extract_hashtags(text):
    text = re.findall(r"#(\w+)", text)
    return ' '.join(text)


def extract_language(text):
    lang = TextBlob(text)
    detect_lang = lang.detect_language()
    return detect_lang


def extract_price(text):
    text = Price.fromstring(text)
    return str(text)

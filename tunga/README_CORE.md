# Tunga Kütüphane Kullanımı

## Kurulum
Tunga'nın sahip olduğu tüm özellikler tek bir python kütüphanesinde toplanmış ve PyPI'da kullanıma sunulmuştur. Web uygulaması kullanmadan özelliklere erişmek için bu kütüphaneyi kullanabilirsiniz. Kütüphaneyi aşağıdaki komutu çalıştırarak kurabilrsiniz.
```bash
CFLAGS="-Wno-narrowing" pip3 install tunga
```

## Kullanım

Tunga kütüphanesi kendi içerisinde 4 temel alt modüle sahiptir. Bu modüllerin kullanım detayları aşağıdaki gibidir. Kullanım hakkında daha fazla bilgi için birim testlerini inceleyebilirsiniz.

### Veri Temizleme Modülü

```python
>>> from tunga.preprocessing import normalization

>>> normalization.correct_typo("şen büyüyünce doktoy mı olçan")
'sen büyüyünce doktor mı olacaksın'

>>> normalization.lemmatization("Bizler aslında yolcuyuz bu dünyada")
'biz aslında yolcu bu dünya'

>>> normalization.stem("Gül senin tenin ben de güller içinde kafesteyim")
'Gül sen ten ben de gül iç kafes'

>>> normalization.syllable("Gözümde nursun başımda tacım muhtacım")
'Gö züm de nur sun ba şım da ta cım muh ta cım'

>>> normalization.remove_stopwords("Bu ve bunun gibi projeler desteklenirse Türkiye 5 yıl içerisinde insansız hava araçları kategorisinde dünyada bir numara olur")
'projeler desteklenirse Türkiye 5 yıl içerisinde insansız hava araçları kategorisinde dünyada numara'

>>> normalization.remove_digits("Yıldız Teknik Üniversitesi 100 yıl önce eğitim hayatına başlamıştır.")
'Yıldız Teknik Üniversitesi yıl önce eğitim hayatına başlamıştır.'

>>> normalization.remove_punctuations("Kim bu gözlerindeki yabancı? Yaralar beni yüreğimden. Hani sen olacaktın yalancı!")
'Kim bu gözlerindeki yabancı Yaralar beni yüreğimden Hani sen olacaktın yalancı'

>>> normalization.remove_hashtag("Sevdiklerimle gün batışını izliyorum #kankalarla #haftasonu #myfriends")
'Sevdiklerimle gün batışını izliyorum'

>>> normalization.remove_mentions("Dostumla güzel bir gün @btahtaci")
'Dostumla güzel bir gün'

>>> normalization.remove_html_tags("<html><body>Heştiemel gövdesine koydular beni.</body></html>")
'Heştiemel gövdesine koydular beni.'

>>> normalization.remove_email("Bana mail atmak istersen burak@burak.com adresine yaz")
'Bana mail atmak istersen  adresine yaz'

>>> normalization.remove_url("Tunga diye mükemmel bir doğal dil işleme ürünü var daha önce hiç duymadıysan hemen http://tunga.ml adresine bir göz at")
'Tunga diye mükemmel bir doğal dil işleme ürünü var daha önce hiç duymadıysan hemen  adresine bir göz at'


```

### Makine Öğrenmesi Modülleri

#### Duygu Durum Analizi
```python
from tunga.machine_learning.sentiment_analysis import bert_sentiment

>>> bert_sentiment.get_sentiment("mükemmel bir ürün çok hoşuma gitti")
('positive', 0.9904009699821472)
>>> 

```

#### Konu Modelleme

#### Anahtar Kelime Tespiti

#### Varlık Adı Tanımlama

#### Metin Özetleme

#### Türkçe-İngilizce Çeviri

### Veri Erişim Modülü

```python
from tunga.retrieval import Twitter

API_KEY = "<YOUR_TWITTER_API_KEY>"
API_SECRET = "<YOUR_TWITTER_API_SECRET>"
ACCESS_TOKEN = "<YOUR_TWITTER_ACCESS_TOKEN>"
TOKEN_SECRET = "<YOUR_TWITTER_TOKEN_SECRET>"
USERNAME = ""
HASHTAG = ""

tweets_uname = Twitter.read_tweets_from_user(API_KEY, API_SECRET, ACCESS_TOKEN, TOKEN_SECRET, USERNAME, 200)

tweets_hashtag = Twitter.read_tweets_from_hashtag(API_KEY, API_SECRET, ACCESS_TOKEN, TOKEN_SECRET, HASHTAG, 200)

```
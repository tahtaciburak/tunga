import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq
import nltk
nltk.download('punkt')


all_news = pd.read_csv("../../../datasets/haberler.csv", sep=",")

nltk.data.load('../../../datasets/turkish.pickle')

all_news['Tokenized_Text'] = all_news['text'].apply(word_tokenize)
all_news['Tokenized_Sentence'] = all_news['text'].apply(sent_tokenize)


def summarize_func(words, sentences):
    word2count = {}
    for word in words:
        if word.lower() not in word2count.keys():
            word2count[word.lower()] = 1
        else:
            word2count[word.lower()] += 1

    maxi = max(word2count.values())

    for key in word2count.keys():
        word2count[key] = word2count[key] / maxi

    sent2score = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word2count.keys():
                if len(sentence.split(' ')) < 15:
                    if sentence not in sent2score.keys():
                        sent2score[sentence] = word2count[word]
                    else:
                        sent2score[sentence] += word2count[word]

    best_sentences = heapq.nlargest(5, sent2score, key=sent2score.get)
    return [' '.join(best_sentences)]

text = """Bir iklim bilimcinin açıklamasına göre, aşırı küresel sıcaklıklar insan vücudunu termal sınırlara doğru itiyor.
Geçtiğimiz hafta Avrupa genelinde rekor sıcaklıklara şahit olundu. Birkaç ülkede sıcaklık 40 derecenin üstüne çıktı. Öte yandan Güney Asya ve Basra Körfezi gibi yerlerde yaşayan insanlar 54 derecelere varan sıcaklıklarla mücadele ediyor. Loughborough Üniversitesi’nde iklim bilimci olarak çalışan Dr. Tom Matthews “İnsan vücudundaki tüm ısıl verime rağmen Güney Asya ve Basra Körfezi gibi yerler yakın zamanda yaşanmaz hale gelebilir.” dedi.
Hava sıcaklığı 35 dereceyi geçtiğinde vücut, vücut ısısını güvenli seviyede tutmak için terler. Ancak nemin buharlaşabilme yetisini gösteren ıslak sıcaklık 35 dereceyi aştığında bu sistem çalışmaz hale gelir. Dr. Matthews “Islak sıcaklık, termometreden buharlaşan suyun soğuma etkisini de içerir. Bu yüzden doğal olarak hava durumlarında verilen normal (kuru ampul sıcaklığı) sıcaklıktan daha düşük olur. Bu ıslak sıcaklık eşiği aşıldığında, hava o kadar çok su buharıyla dolar ki ter buharlaşmaz hale gelir.” diyor.
Bu da, insan vücudunun kendini birkaç saatten fazla hayatta kalabilecek kadar soğutamayacağı anlamına geliyor. Matthews’a göre 21. yüzyılın sonunda Dünya üzerindeki en yoğun nüfuslu yerlerden bazıları da dahil olmak üzere kimi bölgeler bu eşiği geçecek. İklim değişikliğinin hava sistemlerini derinden etkilemeye başlamasıyla, artan sıcaklıklar yakında dünyanın bazı yerlerini yaşanmaz hale getirebilir. Eğer elektrik sistemi düzgün işletilirse kronik şekilde sıcaktan etkilenen ülkelerde yaşamak mümkün olabilir ancak elektrik kesintisi olması durumunda felaket yaşanır. Bu yüzden Dr. Matthews’a göre konuyla ilgili en sağlıklı hamle, Paris İklim Değişikliği Anlaşması’yla belirlenen sınırları korumak adına seragazı salınımını kesmek."""
summary = summarize_func(word_tokenize(text),sent_tokenize(text))
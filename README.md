<p align="center">
    <img src="images/tunga.png" width="300" height="150" />
</p>


# TUNGA: Agile Text Analytics Platform
Tunga, düzensiz metin veri setlerinden değerli bilgiler üretebilmek için geliştirilmiş ve tüm metin işleme sürecini 
hızlandıran web tabanlı ve açık kaynak bir SaaS uygulamasıdır. 
> Bu proje Açık Kaynak Doğal Dil İşleme Hackathon'u sürecinde
geliştirilmiştir. www.acikhack.com



<a href="https://github.com/badges/tunga/graphs/contributors" alt="Contributors">
<img src="https://img.shields.io/github/contributors/badges/shields" /></a>
<img src="https://travis-ci.com/tahtaciburak/tunga.svg?token=nnqL1e1pEDHAHFsZzkNx&branch=master"></img>    

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![Python Version](https://img.shields.io/pypi/pyversions/tunga?style=plastic)](https://img.shields.io/pypi/pyversions/sadedegel) [![pypi Version](https://img.shields.io/pypi/v/tunga?style=plastic&logo=PyPI)](https://pypi.org/project/tunga/) [![License](https://img.shields.io/pypi/l/tunga)](https://github.com/GlobalMaksimum/sadedegel/blob/master/LICENSE)

</div>

## İçindekiler
- [TUNGA: Agile Text Analytics Platform](#tunga-agile-text-analytics-platform)
  - [İçindekiler](#i̇çindekiler)
  - [:question: Problem Tanımı](#question-problem-tanımı)
  - [:gear: Çözüm Önerisi](#gear-çözüm-önerisi)
  - [:dancers: Takım](#dancers-takım)
  - [:house: Projenin Teknik Mimarisi](#house-projenin-teknik-mimarisi)
    - [:book: Kütüphane](#book-kütüphane)
    - [:satellite: Backend](#satellite-backend)
    - [:tada: Frontend](#tada-frontend)
  - [Kullandığımız Kaynaklar](#kullandığımız-kaynaklar)
  - [📝 Lisans](#-lisans)

## :question: Problem Tanımı
Doğal dil işleme, sosyal medyanın da etkisiyle artık her kurumun büyük bir ihtiyacı haline gelmiş durumda. Özellikle B2C(İşletmeden tüketiciye)  iş modellerinde müşterileri ve trendleri anlamak kritik bir öneme sahip. Bu bağlamda işletmelerin metin verilerinden öngörüler oluşturmalı ve anlam çıkarmaları gerek. Tüm bu süreçte çevik olunmalı ve değişen veri ve model ihtiyaçları hızlıca giderilebilmelidir.

## :gear: Çözüm Önerisi
Kurumsal ihtiyaçlara cevap verebilen ve neredeyse hiç kod yazmadan düzensiz verisetlerinde sık kullanılan doğal dil işleme işlevlerinin çalıştırılabileceği düşük masraflı, açık kaynak bir SaaS (Software as a Service) platformu oluşturmaktır. Bu platformda sık kullanılan ve state-of-the-art düzeyindeki algoritmaların birkaç tık ile çalıştırılmasıyla bu alana ayrılan insan kaynağının azaltılması da hedeflenmektedir.

## :dancers: Takım

**Burak Tahtacı**  
Bilgisayar Mühendisliği mezunu ve ARGE işleriyle uğraşan bir mühendis. Uğraş aşanları `Backend Development`, `Machine Learning`,`DevOps`,`NLP`,`Anomaly Detection`

**Beyzanur Canbay**
Bilgisayar Mühendisliği öğrencisi. Uğraş alanları `Deep Learning`,`Machine Learning`,`NLP`,`Text Cleaning`

## :house: Projenin Teknik Mimarisi

Proje temel olarak üç bileşenden oluşmaktadır. `Kütüphane`, `Backend` ve `Frontend` isimlerinde üç temel alt proje geliştirilmiştir. 

<p align="center">
    <img src="images/tunga_system_diagram.png" width="480"\>
</p>

### :book: Kütüphane
Bu kısım bir python modülü, makine öğrenmesi ve doğal dil işleme hakkındaki tüm fonksiyonlar bu modülün içinde yer almaktadır. Kütüphane modülü hakkında daha fazla bilgi almak için tunga dizinine gidebilir ya da PyPi'daki proje sayfasını ziyaret edebilirsiniz.

### :satellite: Backend
Flask ile kodlanmış bir REST web servisidir. Tunga kütüphanesindeki metodları kapsayan ve HTTP methodları sayesinde dışarıya açan bir yapıdadır. Aynı zamanda kendi içerisinde kullanıcı doğrulama ve konfigürasyon kaydetme modülü de bulunmaktadır.

### :tada: Frontend
ReactJS ile geliştirilmiş bir web uygulamasıdır. Kullanıcıların kütüphanedeki metodlara verilerini gönderip işlemesi için gerekli önyüz bileşenleri içermektedir. Ön yüz elemanlarının kullanımlarını incelemek için youtube kanalımızdaki videolara göz atabilirsiniz.

## Kullandığımız Kaynaklar
For deasciify methods : ``` pip3 install git+https://github.com/emres/turkish-deasciifier.git```

For asciify methods: ``` git clone https://github.com/starlangsoftware/TurkishDeasciifier-Py.git```

Turkish name list : ``` https://gist.github.com/emrekgn/b4049851c88e328c065a```

Stop word: ```https://github.com/ahmetax/trstop/blob/master/dosyalar/turkce-stop-words```

Kufur tespit list: ```https://github.com/ooguz/turkce-kufur-karaliste/blob/master/karaliste.txt```

For Summary : ```https://github.com/Eruimdas/turkish_text_summarization/blob/master/Extraction_Based_Text_Summarization.ipynb```
## 📝 Lisans
MIT

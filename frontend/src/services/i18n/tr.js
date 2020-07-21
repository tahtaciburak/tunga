export default {
    header_dropdown: {
        account: "Hesap",
        logout: "Çıkış Yap"
    },
    nav: {
        my_datasets: "Verisetlerim",
        data_ret: {
            data_retrieval: "Veri Yükleme",
            import_from_local: "Bilgisayardan yükle",
            import_from_url: "URL'den yükle",
            import_from_twitter: "Twitter'dan yükle",
            import_from_api: "API oluştur"
        },
        preprocessing: "Veri Önişleme",
        machine_learning: "Makine Öğrenmesi"
    },
    datasets: {
        my_datasets: "Verisetlerim",
        import_from_local: "Bilgisayardan yükle",
        import_from_url: "URL'den yükle",
        import_from_twitter: "Twitter'dan yükle",
        import_from_api: "API oluştur",
        inspect_dataset: {
            header: "Dataseti Incele",
            dataset_name: "Veriseti Adı",
            dataset_description: "Veriseti Açıklaması",
            metadata: "Veriseti Üstbilgileri",
            data: "Veri"
        }
    },
    retrieval: {
        import_from_local: {
            file_metadata: "Dosya Üstbilgileri",
            file_upload: "Dosya Yükleme",
            dataset_name: "Veriseti İsmi",
            dataset_name_placeholder: "Verisetinize isim verin.",
            dataset_description: "Veriseti Açıklaması",
            dataset_description_placeholder: "Verisetinize açıklama yazın.",
            upload: "Karşıya Yükle",
            upload_and_analyze: "Karşıya Yükle ve Analiz Et",
            choose_dataset_file: "Verisetini Yükleyin",
            choose_file: "Dosya Seçin",
            analysis: "Analiz",
            file_upload_success: "Dosya Yükleme Başarılı !",
            file_upload_fail: "Dosya Yükleme Sırasında Hata Oluştu !",
            total_row_count: "Satır Sayısı",
            total_field_count: "Sütun Sayısı",
            total_word_count: "Kelime Sayısı",
            total_distinct_word_count: "Farklı Kelime Sayısı",
            total_missing_values: "Eksik Değer Sayısı",
            upload_new_file: "Yeni Dosya Yükle"
        },
        import_from_url: {
            enter_fıle_remote_path: "Uzak Dosyanın Adresi",
            remote_path: "Verisetinin bulunduğu URL:",
            remote_path_placeholder: "http(s)://",
            fetch_data: "Veriyi Getir",
            dataset_name: "Veriseti Adı:",
            dataset_description: "Veriseti Açıklaması:"
        },
        import_from_twitter: {
            apikey_not_found: "API KEY bulunamadı Konfigürasyon sayfasından TWITTER_API_KEY değişkenini ekleyin."
        }
    },
    preprocessing: {
        preprocessing_header: "Veri Önişleme",
        choose_dataset: "Verisetini Seçin",
        dataset: "Veriseti",
        column: "Kolon",
        please_choose: "Lütfen Seçin",
        choose_column: "Kolon Seçin",
        choose_operations: "Uygulanacak İşlemler",
        lowercase: "Küçük harfleri kullan",
        uppercase: "Büyük harfleri kullan",
        remove_stopwords: "Dolgu kelimelerini sil",
        remove_punctuations: "Noktalama işaretlerini sil",
        remove_digits: "Sayıları sil",
        remove_emojis: "Emojileri sil",
        remove_hashtags: "Hashtag'leri sil",
        remove_mentions: "Mention'ları sil",
        remove_urls: "URL'leri sil",
        remove_emails: "Email Adreslerini sil",
        remove_non_turkish_words: "Türkçe olmayan kelimeleri sil",
        correct_typos: "Yazım hatalarını gider",
        lemmatize: "Kelimelerin yalın hallerini kullan",
        stem: "Kelimelerin kök hallerini kullan",
        deasciify: "ASCII karakterleri Türkçe karakterlerle değiştir",
        asciify: "Türkçe karakterleri ASCII karakterlerle değiştir",
        remove_person_names: "Kişi isimlerini sil",
        start_preprocessing: "Önişlemeye Başla!",
        waiting: "Ön işleme sürüyor...",
        successful: "Ön işleme başarılı",
        inspect_dataset: "Verisetine Gözat"
    },
    machine_learning: {
        sentiment: {
            header: "Duygu Durumu Analizi"
        },
        topic_modelling: {
            choose_dataset: "Verisetinizi seçin",
            choose_column: "İşlem yapmak istediğiniz sütunu seçin",
            header: "Konu Modelleme"
        },
        keyword_extraction: {
            header: "Anahtar Kelime Çıkarımı",
            dataset: "Veriseti",
            choose_dataset: "Verisetinizi seçin",
            choose_column: "İşlem yapmak istediğiniz sütunu seçin",
            please_choose: "Lütfen Seçin",
            column: "Kolon"

        },
        summarization: {
            header: "Metin Özetleme"
        },
        language_identification: {
            header: "Dil Tanıma"
        },
        machine_translation: {
            header: "Makine Çevirisi"
        },
        ner: {
            header: "Varlık İsmi Çıkarımı"
        }
    },
    visualization: {
        header: "Veri Görselleştirme",
        choose_dataset: "Görselleştirmek istediğiniz verisetini seçin"
    },
    configuration: {
        configuration_header: "Ayarlar",
        twitter_api_configuration: "Twitter API Ayarları",
        add_new_configuration: "Yeni Ayar Ekle",
        my_configurations: "Ayarlarım",
        add_config: "Ayarı Kaydet",
        key: "Ayar Adı (Anahtar):",
        key_placeholder: "Ayar Adınızı Giriniz",
        value: "Değer:",
        value_placeholder: "Ayar Değerini Giriniz"
    }
}

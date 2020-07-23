from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
model = AutoModelForTokenClassification.from_pretrained("savasy/bert-base-turkish-ner-cased")
tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-ner-cased")
ner=pipeline('ner', model=model, tokenizer=tokenizer)

def get_result(text):
    return ner(text)

print(get_result("Mustafa Kemal Atatürk 19 Mayıs 1919'da Samsun'a ayak bastı ve Birinci Dünya Savaşı sonlandı."))
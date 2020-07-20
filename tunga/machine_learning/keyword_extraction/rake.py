from multi_rake import Rake


def extract_keywords(text):
    rake = Rake()
    keywords = rake.apply(text)
    return keywords[:10]

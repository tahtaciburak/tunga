from multi_rake import Rake
import pandas as pd

df = pd.read_csv("../datasets/hepsiburada_review.csv")
texts = list(df["texts"].fillna(""))

for text in texts:
    rake = Rake()
    keywords = rake.apply(text)
    print(text)
    print()
    print(keywords[:10])
    print("===========================================")

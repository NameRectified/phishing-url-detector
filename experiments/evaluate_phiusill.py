import pandas as pd

df = pd.read_csv("../datasets/phiusiil-phishing-url.csv")

print(df.shape)
print(df.columns.tolist())
print(df.head())
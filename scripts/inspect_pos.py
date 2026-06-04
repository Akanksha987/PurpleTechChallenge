import pandas as pd

df = pd.read_csv("data/pos/POS-sample-transactions.csv")

print(df.head())
print()
print(df.columns)
print()
print(df.shape)
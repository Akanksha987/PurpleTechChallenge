import pandas as pd

df = pd.read_csv("data/pos/Brigade_Bangalore_10_April_26.csv")

print("\nStores:")
print(df["store_id"].unique())

print("\nCities:")
print(df["city"].unique())

print("\nRows:", len(df))

print("\nUnique Orders:")
print(df["order_id"].nunique())

print("\nDate Range:")
print(df["order_date"].min())
print(df["order_date"].max())

print("\nColumns with Null %")
print((df.isnull().mean()*100).sort_values(ascending=False))
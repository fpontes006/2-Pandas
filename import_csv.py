import pandas as pd

df = pd.read_csv("data/pedidos.csv")
print(df)
print(type(df))


df2 = pd.read_csv("data/pedidos2.csv", sep=";")
print(df2)


print(df.tail())

print(df.shape())

print(df.dtypes())


print(df.sort_values(by='Unidades',ascending=False))

print(df['Estado'].value_counts())
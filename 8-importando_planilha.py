import pandas as pd

df = pd.read_excel("data/livros.xlsx")
print(df)

print(df.dtypes)

print(df.describe())

print(df[['Preço (R$)', 'Quantidade']].describe())
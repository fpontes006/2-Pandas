import pandas as pd

df = pd.read_excel("data/livros.xlsx")
print(df)

genero_info = df.groupby('Gênero').agg({
    'Título': 'count',
    'Preço (R$)': 'mean'})
print(genero_info)


# 2- Livro Mais caro e mais barato
print(df['Preço (R$)'].max())
print(df['Preço (R$)'].min())

# 3- Distribuição dos livros por Ano de Publicação
print(df['Ano de Publicação'].value_counts())

# 4- Correlação entre preço e quantidade
print(df['Preço (R$)'].corr(df['Quantidade']))
import pandas as pd

df = pd.read_csv("data/Pedidos.csv")

#
df['Unidades'] = pd.to_numeric(df['Unidades'])
df['ProcoUnidade'] = pd.to_numeric(df['ProcoUnidade'])


# 1- Vendas Por Regiao
vendas_regiao = df.groupby('Regiao')['Unidades'].sum()
print(vendas_regiao)

# 2- Vendedor mais produtivo
vendas_vendedor = df.groupby('Vendedor')['Unidades'].sum()
print(vendas_vendedor.idxmax())


# 3- Total de Unidades vendidas por item
vendas_item = df.groupby('Item')['Unidades'].sum()
print(vendas_item)

# 4- medida preco por Item
preco_item = df.groupby('Item')['ProcoUnidade'].mean()
print(preco_item)

# 5 - Correlação entre Unidades Vendidas e Preço Unitario
Correlacao = df['Unidades'].corr(df['ProcoUnidade'])
print(Correlacao)

# converter Series em Dataframe
vendas_regiao = pd.DataFrame(vendas_regiao)


# 6- Exportando para csv
df.to_csv('data/resultado.csv', index=False)
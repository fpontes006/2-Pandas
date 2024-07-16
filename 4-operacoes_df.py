import pandas as pd
import matplotlib.pyplot as plt 

data = {
    "Nome":['Alice','Bob','Charlie','David','Emily'],
    "Idade":[25,30,35,40,27],
    "Cargo":['Analista','Gerente','Ceo','Analista','Coordenador'],
    "Salario": [5000,8000,15000,4800,6000]
}

df = pd.DataFrame(data)

print(df.describe())

print(df[df['Salario']> 5000])

print(df.sort_values(by='Idade', ascending=False))


df['Bonus'] = df['Salario'] * 0.1
print(df)


print(df.groupby('Cargo')['Salario'].mean())


df.plot(
    kind='bar',
    x='Nome',
    y='Salario',
    title='Salarios dos Funcionarios',
    rot=45
)

plt.show()
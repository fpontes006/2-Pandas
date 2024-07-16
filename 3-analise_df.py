import pandas as pd

dados = {
    'Real Madrid': 34,
    'Barcelona': 26,
    'Bayern Munich': 19,
    'Liverpool': 30,
    'Manchester United': 20
}

dados_anos = {
    'Real Madrid': [1956,1957,1958,1959,1960],
    'Barcelona': [1992,2006,2009,2011,2015],
    'Liverpool':[1977,1978,1981,1984,2005],
    'Bayern Munich': [1958,1985,1996,2011,2015],
    'Manchester United': [1974,1975,1976,2001,2013]
}

series_times = pd.Series(dados)
series_anos = pd.Series(dados_anos)
print(series_times)
print(series_anos)

data =  {'Titulos': series_times,'Anos': series_anos}
dataframe_times = pd.DataFrame(data)

print(dataframe_times)

media_titulos = dataframe_times['Titulos'].mean()
print(f'Media de Titulos: {media_titulos}')

mais_titulos = dataframe_times['Titulos'].idxmax()
qtd_titulos = dataframe_times['Titulos'].max()
print(f'Time com mais titulos: {mais_titulos} com {qtd_titulos} titulos')


todos_anos = dataframe_times['Anos'].explode()
ano_mais_titulos = todos_anos.mode()[0]
print(f'Ano com mais titulos: {ano_mais_titulos}')




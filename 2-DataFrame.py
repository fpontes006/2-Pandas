import pandas as pd

dados = {
    'Real Madrid': 34,
    'Barcelona': 26,
    'Bayern Munich': 19,
    'Liverpool': 30,
    'Manchester United': 20
}

dados_anos = {
    'Real Madrid': [34, 33, 32, 31, 30,],
    'Barcelona': [26, 25, 24, 23, 22,],
    'Liverpool':[20,23,44,55,66],
    'Bayern Munich': [56,44,33,66,52],
    'Manchester United': [62,23,11,33,42]
}

series_times = pd.Series(dados)
series_anos = pd.Series(dados_anos)
print(series_times)
print(series_anos)

data =  {'Titulos': series_times,'Anos': series_anos}
dataframe_times = pd.DataFrame(data)

print(dataframe_times)

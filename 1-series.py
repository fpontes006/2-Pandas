import pandas as pd


#1- Dados de times e suas quantidades de titulos

dados = {
    'Real Madrid': 34,
    'Barcelona': 26,
    'Bayern Munich': 19,
    'Liverpool': 30,
    'Manchester United': 20
}

series_times = pd.Series(dados)
print(series_times)

print(series_times[series_times >= 30])


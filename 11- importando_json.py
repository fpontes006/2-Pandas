import pandas as pd

df = pd.read_json("data/series.json")

print(df) 

# 2 - Utilizando o Json_normalize
df_series = pd.json_normalize(df['series'],
                              'temporadas',
                              ['titulo','genero','ano_lancamento'])
print(df_series)
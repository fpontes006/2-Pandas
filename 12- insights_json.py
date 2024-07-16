import pandas as pd

df = pd.read_json('data/series.json')
print(df)

# 1- Analise Total de Episodos por Series
temporadas_espandidas = []
for serie in df['series']:
    total_episodios = sum(temporada['episodios'] for temporada in serie['temporadas'])
    serie_info = {
        'titulo': serie['titulo'],
        'genero': serie['genero'],
        'total_episodios': total_episodios
    }
    temporadas_espandidas.append(serie_info)
    df_expandido = pd.DataFrame(temporadas_espandidas)
    print(df_expandido)
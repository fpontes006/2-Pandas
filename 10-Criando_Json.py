import json

#1-Dados fictícios sobre séries
dados_series = {
    "series":[
        {
            "titulo":"Stranger Things",
            "genero":"Ficção Científica",
            "ano_lancamento":2016,
            "temporadas":[
                {"numero":1, "episodios":8},
                {"numero":2, "episodios":9},
                {"numero":3, "episodios":8},
                {"numero":4, "episodios":9},
            ]
        },
        {
            "titulo":"Breaking Bad",
            "genero":"Drama",
            "ano_lancamento":2008,
            "temporadas":[
                {"numero":1, "episodios":7},
                {"numero":2, "episodios":13},
                {"numero":3, "episodios":13},
                {"numero":4, "episodios":13},
                {"numero":5, "episodios":16},
            ]
        },
        
    ]
}

# exportando para JSON
nome_arquivo = 'data/series.json'
with open(nome_arquivo, 'w') as fp:
    json.dump(dados_series, fp)
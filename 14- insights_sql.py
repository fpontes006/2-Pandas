import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

try:
    engine = create_engine('sqlite:///bd.db')
    consulta1 = "SELECT Título, SUM([Preço (R$)]) AS total FROM livros GROUP BY Título"
    df = pd.read_sql_query(consulta1, engine)
    print(df)
except SQLAlchemyError as e:
    print(f"An error occurred: {e}")

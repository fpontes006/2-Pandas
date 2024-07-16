import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('sqlite:///bd.db')
df = pd.read_excel('data/livros.xlsx')
df.to_sql('livros', engine, index=False)
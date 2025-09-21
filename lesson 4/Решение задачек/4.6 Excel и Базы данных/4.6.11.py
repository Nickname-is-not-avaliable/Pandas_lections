import pandas as pd
import sqlalchemy as sql

url = f'local_db.db'

con = sql.create_engine(f'sqlite:///{url}')

query = 'SELECT Name, cast(StationCapacity as integer)StationCapacity, Location FROM stations ORDER BY StationCapacity desc, Name'

df = pd.read_sql_query(query, con=con)

df.to_csv('4.6.11.csv',index=False, sep = ';', encoding='utf8')

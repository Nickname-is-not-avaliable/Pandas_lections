import pandas as pd

url = f'https://stepik.org/media/attachments/lesson/755302/users.csv'

df = pd.read_csv(url, sep = ';')
print(df)
df2 = df[['username', 'name', 'sex']]
df2.to_json('data.json')
import pandas as pd

url = f'https://stepik.org/media/attachments/lesson/755301/users.csv'

df = pd.read_csv(url, sep = ';')

df[df['sex'] == 'F'].to_csv('meh.csv',index=None, encoding='utf8', columns=['username','mail'],sep=';')
import pandas as pd

url = f'https://stepik.org/media/attachments/lesson/755301/users.csv'

df = pd.read_csv(url, sep = ';',nrows=50)

print(df[df['sex'] == 'M'].value_counts().sum())
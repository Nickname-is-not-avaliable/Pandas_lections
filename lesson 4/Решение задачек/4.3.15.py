import pandas as pd

url = f'https://stepik.org/media/attachments/lesson/755301/users.csv'

stream = pd.read_csv(url, sep = ';',chunksize=30)
i=0

for df in stream:
    i+=1
    if i == 5:
        print(df[df['blood_group'] == 'A+'].value_counts().sum())
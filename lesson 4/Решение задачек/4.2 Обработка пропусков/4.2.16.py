import pandas as pd

url = f'https://stepik.org/media/attachments/lesson/755300/%D0%9F%D0%B0%D1%81%D1%81%D0%B0%D0%B6%D0%B8%D1%80%D0%BE%D0%BF%D0%BE%D1%82%D0%BE%D0%BA_%D0%9C%D0%BE%D1%81%D0%9C%D0%B5%D1%82%D1%80%D0%BE_4.csv'

df = pd.read_csv(url, na_values={'IncomingPassengers' : [0, 'не указано']}, sep ='|')
result = df['IncomingPassengers'].isnull().sum()

print(result)
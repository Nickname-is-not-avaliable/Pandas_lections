import pandas as pd

#skiprows нужен, чтобы пропустить строку со вторым заголовком (она все данные спутывает). Тым ещё в решениях кидали usecols. Это для подгрузки только нужных колонок
df = pd.read_csv(r'https://stepik.org/media/attachments/lesson/745992/%D0%9F%D0%B0%D1%81%D1%81%D0%B0%D0%B6%D0%B8%D1%80%D0%BE%D0%BF%D0%BE%D1%82%D0%BE%D0%BA_%D0%9C%D0%BE%D1%81%D0%9C%D0%B5%D1%82%D1%80%D0%BE_2.csv', \
                  sep = ';', skiprows=[1])

result = df.loc[(df['Year'] == 2021) & (df['Quarter'] == 'IV квартал')].groupby('NameOfStation').IncomingPassengers.sum().idxmax()

print(result)
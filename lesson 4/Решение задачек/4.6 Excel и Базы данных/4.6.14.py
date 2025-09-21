import pandas as pd

url = 'https://stepik.org/media/attachments/lesson/755362/%D0%97%D0%B0%D1%80%D1%8F%D0%B4%D0%BD%D1%8B%D0%B5_%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D0%B8_%D0%B4%D0%BB%D1%8F_%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D0%B5%D0%B9.xlsx'

file = pd.ExcelFile(url) #Лучшая практика: если достать из файла в переменную, то работает быстрее

df0 = pd.read_excel(file, sheet_name='0', usecols=['Район', 'Код'], skiprows=1) #первый листик
df1 = pd.read_excel(file, sheet_name='1', usecols=['Район', 'Код'], skiprows=10) #второй листик

df = df0.merge(right=df1,how='outer') #Соединяем наши данные (этого на курсе не было, но без этой операции никуда) 
df = df.groupby('Район').agg(amount=('Код', 'count')) #Тут создаетсся новый столбец amount с количеством заправок по районам
print(df.sort_values(by='amount', ascending=False))
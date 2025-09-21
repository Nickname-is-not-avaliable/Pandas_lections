import pandas as pd
import numpy as np

data = [['Girev', 'Andrey', 'ВИП', 2815, 29, 58, 6358, 'Moscow', 'Xiaomi'],
       ['Bykin', 'Stas', 'Все за 300', 3634, 37, 78, 602, 'Kazan', 'Samsung'],
       ['Ivanov', 'Alex', 'Всё за 800', 410, 47, 81, 3582, 'Moscow', 'Huawei'],
       ['Andreev', 'Sergey', 'Всё за 500', 1981, 75, 98, 5442, 'Kazan', 'Apple'],
       ['Girev', 'Stas', 'Всё за 800', 4969, 43, 61, 8510, 'Moscow', 'Samsung'],
       ['Bykin', 'Andrey', 'Всё за 500', 4308, 49, 39, 2525, 'Moscow', 'Xiaomi'],
       ['Kozlov', 'Igor', 'Всё за 800', 300, 60, 31, 8543, 'Yakutsk', 'Samsung'],
       ['Girev', 'Alex', 'Промо', 4199, 47, 90, 3925, 'Kazan', 'Apple'],
       ['Petrov', 'Nikolay', 'ВИП', 4810, 72, 88, 7188, 'Moscow', 'Apple'],
       ['Andreev', 'Sergey', 'Всё за 800', 4118, 52, 53, 419, 'Yakutsk', 'Apple'],
       ['Smolov', 'Stas', 'Промо', 1991, 28, 67, 5016, 'Kazan', 'Xiaomi'], 
        ['Girev', 'Igor', 'Корпоративный', 1430, 69, 19, 9520, 'Yakutsk', 'Samsung'],
       ['Kozlov', 'Andrey', 'Корпоративный', 113, 71, 82, 2785, 'Kazan', 'Apple'],
       ['Ivanov', 'Sergey', 'Промо', 3394, 39, 12, 2718, 'Yakutsk', 'Xiaomi'],
       ['Smolov', 'Sergey', 'Всё за 250 (архив)', 3493, 32, 6, 8959, 'Yakutsk', 'Huawei'],
       ['Kozlov', 'Stas', 'Всё за 800', 4565, 59, 82, 3168, 'Moscow', 'Apple'],
       ['Vlasov', 'Andrey', 'Всё за 800', 3192, 29, 74, 2852, 'Yakutsk', 'Xiaomi'],
       ['Smolov', 'Alex', 'Корпоративный', 3764, 71, 22, 2768, 'Moscow', 'Huawei'],
       ['Vlasov', 'Sergey', 'Всё за 800', 3816, 28, 35, 5734, 'Vladivostok', 'Apple'],
       ['Bykin', 'Alex', 'Промо', 817, 65, 34, 2131, 'Vladivostok', 'Samsung'],
       ['Andreev', 'Nikolay', 'Всё за 500', 385, 49, 62, 1815, 'Kazan', 'Xiaomi'],
       ['Bykin', 'Igor', 'Всё за 500', 2642, 38, 11, 3787, 'Moscow', 'Xiaomi'],
       ['Girev', 'Sergey', 'Все за 300', 4230, 62, 68, 5512, 'Vladivostok', 'Samsung'],
       ['Bykin', 'Sergey', 'Всё за 800', 4100, 48, 39, 227, 'Moscow', 'Xiaomi'],
       ['Girev', 'Stas', 'Все за 300', 3371, 53, 24, 7946, 'Kazan', 'Apple'],
       ['Smolov', 'Sergey', 'Корпоративный', 3577, 70, 71, 8847, 'Yakutsk', 'Huawei'],
       ['Mezov', 'Nikolay', 'Всё за 250 (архив)', 2742, 28, 19, 7115, 'Yakutsk', 'Huawei'],
       ['Smolov', 'Stas', 'Всё за 500', 2644, 41, 33, 8341, 'Moscow', 'Xiaomi'],
       ['Vlasov', 'Andrey', 'Всё за 500', 4725, 26, 93, 9441, 'Vladivostok', 'Xiaomi'],
       ['Ivanov', 'Nikolay', 'Всё за 500', 2785, 41, 5, 2901, 'Moscow', 'Samsung']]

df = pd.DataFrame(data, columns = ['surname', 'name', 'tarif', 'balance', 'age', 'sms', 'voice', 'city', 'phone'])

#3.13.1 Средний возраст Тут я чет перемудрил
#print(df['age'].mean())

#3.13.2 Минимальный средний возраст по тарифам
#https://pythonru.com/uroki/osnovy-pandas-2-agregacija-i-gruppirovka про group by
#print(df.groupby('tarif').age.mean().idxmin())

#3.13.3 Города по кол-ву клиентов (плохое решение)
#print(df.groupby('city').count().idxmax())

#3.13.4 Тариф по смс
#print(df.groupby('tarif').sms.sum().idxmax())

#3.13.5 Марки смартфонов по пользователям с фильтром
#print(df[df.age <= 40].phone.value_counts().idxmax())

#3.13.6 Смс по городам
#print(df.groupby('city').sms.sum().idxmin())

#3.13.7 Минуты по городам
#print(df.groupby('city').voice.sum().idxmax())

#3.13.8 Сколько всего сообщений (умножаем на 3 паприколу)
#print(df.sms.sum() * 3)

#3.13.8 Сколько всего сообщений. Умножаем в зависимости от тарифов

tarif_sms_payments = pd.Series({'ВИП': 1,
     'Все за 300': 2,
     'Всё за 500': 3,
     'Всё за 800': 4,
     'Промо': 7,
     'Корпоративный': 0,
     'Всё за 250 (архив)': 5
     })

#print((df['tarif'].map(tarif_sms_payments) * df['sms']).sum())

#3.14.10 Пересчет по курсу
df['balance_usd'] = round(df['balance'] / 60, 2)

#3.14.11 Добавляем знак после строки
#df.balance_usd = df.balance_usd.astype(str) + ' $'


print(df['balance_usd'])

#3.14.12 Определите сколько всего было отправлено СМС, а затем расcчитайте отношение отправленных смс клиента к общему количеству. Столбец назовите sms_volume. Оставьте TOP-3
#df['sms_volume'] = df['sms'] / df['sms'].sum()

#3.14.13
#print(df.loc[df['city'] == 'Kazan', 'age'].mean() > df.loc[df['city'] == 'Vladivostok', 'age'].mean())

#3.14.14
#df.index = df['name'].str.upper() + '_' + df['surname'].str.upper()
#df.drop(columns = ['name', 'surname'], inplace = True)



print(df.index.is_unique)
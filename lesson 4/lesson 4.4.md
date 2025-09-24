### 4.4 Кто такой [JSON](https://developer.mozilla.org/ru/docs/Glossary/JSON) и как с ним подружиться?

---
#### 4.4.1-4.4.3 Что такое JSON?

**JSON (JavaScript Object Notation)** — это легковесный текстовый формат для обмена данными. Он основан на синтаксисе JavaScript и представляет данные в виде пар **ключ-значение**, что очень похоже на словари в Python.

Несмотря на название, JSON является языково-независимым и широко используется для обмена данными между веб-серверами и клиентами (например, браузерами или мобильными приложениями).

**--- Пример файла `data.json` ---**
```json
[
  {
    "id": 1,
    "name": "Alice",
    "city": "New York"
  },
  {
    "id": 2,
    "name": "Bob",
    "city": "Los Angeles"
  },
  {
    "id": 3,
    "name": "Charlie",
    "city": "Chicago"
  }
]
```
*В этом примере JSON представляет собой **список словарей**, что напрямую соответствует структуре `DataFrame`.*

---
#### 4.4.4-4.4.6 Чтение и запись JSON с помощью Pandas

**1. [`pd.read_json()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html) — чтение файла**
```python
# --- Чтение файла data.json ---
df_from_json = pd.read_json('data.json')

print("DataFrame, прочитанный из data.json:")
print(df_from_json)
```
**Вывод:**
```
DataFrame, прочитанный из data.json:
   id     name         city
0   1    Alice     New York
1   2      Bob  Los Angeles
2   3  Charlie      Chicago
```

**2. [`df.to_json()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html) — запись в файл и параметр `orient`**
Метод `.to_json()` сохраняет `DataFrame`. Параметр `orient` контролирует структуру выходного JSON.

**--- Исходные данные для сохранения ---**
```python
df_to_save = pd.DataFrame({
    'ticker': ['AAPL', 'GOOG'],
    'price': [150.5, 2800.7]
})
```

**Поведение по умолчанию (`orient='columns'`):**
```python
df_to_save.to_json('output_default.json')

# --- Содержимое 'output_default.json' ---
# {"ticker":{"0":"AAPL","1":"GOOG"},"price":{"0":150.5,"1":2800.7}}
# (Словарь столбцов, неудобно для API)
```

**С `orient='records'` (часто предпочтительнее):**
```python
df_to_save.to_json('output_records.json', orient='records')

# --- Содержимое 'output_records.json' ---
# [{"ticker":"AAPL","price":150.5},{"ticker":"GOOG","price":2800.7}]
# (Список словарей, идеально для API)
```
---
#### 4.4.8-4.4.9 Работа с JSON из веб-источников ([`requests`](https://requests.readthedocs.io/en/latest/))

Часто данные в формате JSON получают по URL с помощью HTTP-запроса. Для этого используется библиотека `requests`.

**Если у вас не установлен `requests`, выполните:** `pip install requests`

**Пример: Загрузка данных о пользователях с тестового API**
```python
import requests
import pandas as pd

# 1. Указываем URL, который возвращает JSON
url = 'https://jsonplaceholder.typicode.com/users'

# 2. Делаем GET-запрос
response = requests.get(url)

# 3. Преобразуем ответ в формат JSON (получаем список словарей)
data = response.json()

# 4. Создаем DataFrame из полученных данных
df_api = pd.DataFrame(data)

print("DataFrame, созданный из данных по URL:")
# Выведем только несколько столбцов для наглядности
print(df_api[['id', 'name', 'email', 'company']].head())

# 5. (п. 4.4.8) Часто после загрузки нужно исправить типы данных.
# Например, столбец 'company' здесь - это словарь. Его можно "распаковать".
# Преобразуем столбец 'company' в отдельный столбец с названием компании
df_api['company_name'] = df_api['company'].apply(lambda x: x['name'])
print("\nDataFrame с извлеченным названием компании:")
print(df_api[['id', 'name', 'company_name']].head())
```
**Вывод:**
```
DataFrame, созданный из данных по URL:
   id               name                    email  \
0   1       Leanne Graham    Sincere@april.biz   
1   2        Ervin Howell  Shanna@melissa.tv   
2   3    Clementine Bauch   Nathan@yesenia.net   
3   4         Patricia Lebsack  Julianne.OConner@kory.org   
4   5          Chelsey Dietrich   Lucio_Hettinger@annie.ca   

                                           company  
0  {'name': 'Romaguera-Crona', 'catchPhrase': 'Mu...  
1  {'name': 'Deckow-Crist', 'catchPhrase': 'Prot...  
2  {'name': 'Romaguera-Jacobson', 'catchPhrase':...  
3  {'name': 'Robel-Corkery', 'catchPhrase': 'Mul...  
4  {'name': 'Keebler LLC', 'catchPhrase': 'User-...  

DataFrame с извлеченным названием компании:
   id               name         company_name
0   1       Leanne Graham      Romaguera-Crona
1   2        Ervin Howell       Deckow-Crist
2   3    Clementine Bauch  Romaguera-Jacobson
3   4         Patricia Lebsack     Robel-Corkery
4   5          Chelsey Dietrich       Keebler LLC
```

### 4.6 Старый добрый Excel и немного про базы данных

---
#### 4.6.1-4.6.2 Чтение из Excel

**1. `pd.read_excel()` — основная функция**

Эта функция является основным инструментом для чтения данных из `.xlsx` или `.xls` файлов.

**Новые параметры для разбора:**
*   `sheet_name`: Позволяет указать, какой лист (worksheet) из Excel-книги нужно прочитать. Можно передать:
    *   **Строку:** Имя листа (например, `'Orders'`).
    *   **Число:** Порядковый номер листа (начиная с 0).
    *   **`None`:** Загрузить все листы в виде словаря DataFrame'ов.
    *   **Список:** Загрузить указанные листы.
*   `header`: Указывает, какую строку в файле использовать в качестве заголовка для столбцов (нумерация с 0). Это важно, если в файле есть "мусорные" строки над таблицей (например, название отчета).

**--- Подготовка файла `example.xlsx` для примеров ---**
```python
# Создадим файл Excel с двумя листами
with pd.ExcelWriter('example.xlsx') as writer:
    pd.DataFrame({'order_id': [1, 2], 'product': ['A', 'B']}).to_excel(writer, sheet_name='Orders', index=False)
    pd.DataFrame({'customer_id': [101, 102], 'name': ['Alice', 'Bob']}).to_excel(writer, sheet_name='Customers', index=False)

# Создадим второй файл с "мусором" в начале
with pd.ExcelWriter('report.xlsx') as writer:
    df = pd.DataFrame({'Year': [2022], 'Region': ['NA']})
    # Записываем данные со сдвигом, имитируя пустые строки и заголовок отчета
    df.to_excel(writer, sheet_name='SalesData', index=False, startrow=2)
    # Добавим "заголовок" отчета в первую ячейку
    writer.sheets['SalesData'].cell(1, 1).value = 'Quarterly Sales Report'
```

**--- Примеры чтения ---**
```python
# Пример 1: Чтение конкретного листа по имени
print("--- Чтение листа 'Customers' из example.xlsx ---")
df_customers = pd.read_excel('example.xlsx', sheet_name='Customers')
print(df_customers)

# Пример 2: Использование параметра 'header'
print("\n--- Неправильное чтение report.xlsx (без header) ---")
df_wrong_header = pd.read_excel('report.xlsx')
print(df_wrong_header) # Заголовки будут неправильными

print("\n--- Правильное чтение report.xlsx (с header=2) ---")
# Указываем, что настоящие заголовки находятся в 3-й строке (индекс 2)
df_correct_header = pd.read_excel('report.xlsx', header=2)
print(df_correct_header)
```
**Вывод:**
```
--- Чтение листа 'Customers' из example.xlsx ---
   customer_id   name
0          101  Alice
1          102    Bob

--- Неправильное чтение report.xlsx (без header) ---
  Unnamed: 0 Unnamed: 1
0        NaN        NaN
1       Year     Region
2       2022         NA

--- Правильное чтение report.xlsx (с header=2) ---
   Year Region
0  2022     NA
```
---
#### 4.6.3-4.6.4 Запись в Excel

**1. `df.to_excel()` — сохранение одного DataFrame**

Сохраняет DataFrame в Excel-файл.

**Новые параметры для разбора:**
*   `index=False`: Очень частый параметр. Указывает **не записывать** индекс DataFrame в первую колонку файла.
*   `sheet_name='MySheet'`: Задает имя для листа, на который будут записаны данные.

**2. `pd.ExcelWriter` — сохранение нескольких DataFrame в один файл**

`ExcelWriter` — это объект, который управляет процессом записи в один Excel-файл, позволяя добавлять данные на разные листы. **Файл не будет создан/изменен, пока вы не вызовете `.close()` или `.save()`**.

**--- Пример записи нескольких листов ---**
```python
df1 = pd.DataFrame({'data1': [1, 2]})
df2 = pd.DataFrame({'data2': [3, 4]})

# Создаем объект writer
with pd.ExcelWriter('output_multisheet.xlsx') as writer:
    print("Запись df1 на лист 'ReportData'...")
    df1.to_excel(writer, sheet_name='ReportData', index=False)
    
    print("Запись df2 на лист 'MetaData'...")
    df2.to_excel(writer, sheet_name='MetaData', index=False)

print("\nФайл 'output_multisheet.xlsx' успешно создан.")
```
---
#### 4.6.8-4.6.9 Работа с базами данных через `SQLAlchemy`

`SQLAlchemy` — это библиотека, которая предоставляет универсальный способ взаимодействия с различными СУБД (SQLite, PostgreSQL, MySQL и др.) из Python. Pandas использует ее "под капотом" для своих SQL-функций.

**Функции и аргументы:**
*   `sql.create_engine('connection_string')`: Создает "движок" — объект, который управляет подключением к базе данных. Строка подключения зависит от типа БД. Для SQLite это просто `sqlite:///filename.db`.
*   `df.to_sql(name, con, ...)`: Записывает DataFrame в SQL-таблицу.
    *   `name`: Имя SQL-таблицы.
    *   `con`: Объект подключения (движок).
    *   `if_exists`: Что делать, если таблица уже существует.
        *   `'fail'` (по умолчанию): Вызвать ошибку.
        *   `'replace'`: Удалить старую таблицу и создать новую.
        *   `'append'`: Добавить данные в конец существующей таблицы.

**--- Пример чтения и записи ---**
```python
import sqlalchemy as sql

# 1. Создаем движок для файла my_database.db
engine = sql.create_engine('sqlite:///my_database.db')

# 2. ИСХОДНЫЕ ДАННЫЕ: Записываем DataFrame в таблицу 'products'
products_df = pd.DataFrame({'product_name': ['A', 'B'], 'price': [100, 150]})
products_df.to_sql('products', engine, index=False, if_exists='replace')
print("--- Исходная таблица 'products' в БД ---")
print(pd.read_sql('SELECT * FROM products', engine))

# 3. ЧТЕНИЕ: Выполняем SQL-запрос и сразу получаем DataFrame
query = "SELECT * FROM products WHERE price > 120"
df_from_sql = pd.read_sql(query, engine)
print("\n--- Результат чтения (price > 120) ---")
print(df_from_sql)

# 4. ПЕРЕЗАПИСЬ: Создаем новый DataFrame и заменяем им старую таблицу
new_products_df = pd.DataFrame({'product_name': ['C'], 'price': [200]})
new_products_df.to_sql('products', engine, index=False, if_exists='replace')
print("\n--- Таблица 'products' после перезаписи ---")
print(pd.read_sql('SELECT * FROM products', engine))
```
**Вывод:**
```
--- Исходная таблица 'products' в БД ---
  product_name  price
0            A    100
1            B    150

--- Результат чтения (price > 120) ---
  product_name  price
0            B    150

--- Таблица 'products' после перезаписи ---
  product_name  price
0            C    200
```

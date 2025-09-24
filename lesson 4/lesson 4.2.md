### 4.2 Поподробнее про обработку пропусков

---
#### 4.2.1 [Мультииндекс](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#multiindex-advanced-indexing) при чтении файла

Параметр `index_col` может принимать список столбцов, создавая иерархический индекс ([`MultiIndex`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.html)).

**--- Исходные данные (`data_multi_index.csv`) ---**
```csv
year,quarter,state,population
2020,1,CA,39.2
2020,2,CA,39.3
2021,1,NY,19.8
2021,2,NY,19.7
```
**--- Чтение с мультииндексом ---**
```python
df_multi = pd.read_csv('data_multi_index.csv', index_col=['year', 'quarter'])

print("DataFrame с мультииндексом:")
print(df_multi)
```
**Вывод:**
```
DataFrame с мультииндексом:
             state  population
year quarter                  
2020 1          CA        39.2
     2          CA        39.3
2021 1          NY        19.8
     2          NY        19.7
```
---
#### 4.2.2-4.2.3 `sep` с регулярными выражениями

Если разделителем является один или несколько пробелов/табуляций, можно использовать регулярное выражение `\s+`.

**--- Исходные данные (`data_regex_sep.csv`) ---**
```
name age score
Alice   25  9.5
Bob    30   8.0
```
**--- Чтение с `sep='\s+'` ---**
```python
df_regex = pd.read_csv('data_regex_sep.csv', sep='\s+')

print("DataFrame, прочитанный с помощью regex-разделителя:")
print(df_regex)
```
**Вывод:**
```
DataFrame, прочитанный с помощью regex-разделителя:
    name  age  score
0  Alice   25    9.5
1    Bob   30    8.0
```
---
#### 4.2.4 `skiprows` — пропуск строк

Пропускает указанные строки при чтении (нумерация с 0). Полезно для файлов с комментариями или пустыми строками в начале.

**--- Исходные данные (`data_with_comments.csv`) ---**
```
# Data report for Q3
user_id,name,value
# User data below
101,Alice,150
102,Bob,200
```
**--- Чтение с пропуском строк ---**
```python
# Пропускаем первую (0) и третью (2) строки
df_skipped = pd.read_csv('data_with_comments.csv', skiprows=[0, 2])

print("DataFrame после пропуска строк 0 и 2:")
print(df_skipped)
```
**Вывод:**
```
DataFrame после пропуска строк 0 и 2:
   user_id   name  value
0      101  Alice    150
1      102    Bob    200
```
---
#### 4.2.5-4.2.9 Обработка пропущенных значений (`na_values`)

Pandas по умолчанию распознает стандартные маркеры (`NA`, `NULL`, `NaN`, пустые поля) как `NaN`. Параметр `na_values` позволяет расширить этот список.

**--- Исходные данные (`data_custom_na.csv`) ---**
```
id,name,age,city
1,Alice,25,NY
2,Bob,-99,LA
3,--,30,--
4,Charlie,N/A,SF
```
**--- Чтение с кастомными `na_values` ---**
```python
# Указываем, что -99 в столбце 'age' и '--' в столбце 'city' - это пропуски.
# 'N/A' pandas распознает по умолчанию.
custom_na = {
    'age': [-99],
    'city': ['--'],
    'name': ['--']
}

df_na = pd.read_csv('data_custom_na.csv', na_values=custom_na)

print("DataFrame после обработки кастомных NA:")
print(df_na)
print("\nПроверка на null:")
print(pd.isnull(df_na))
```
**Вывод:**
```
DataFrame после обработки кастомных NA:
   id     name   age city
0   1    Alice  25.0   NY
1   2      Bob   NaN   LA
2   3      NaN  30.0  NaN
3   4  Charlie   NaN   SF

Проверка на null:
      id   name    age   city
0  False  False  False  False
1  False  False   True  False
2  False   True  False   True
3  False  False   True  False
```
---
#### 4.2.10 `nrows` — чтение части файла

Читает только первые `n` строк данных. Полезно для быстрого знакомства с огромным файлом.

**--- Исходные данные (`data_large.csv`) ---**
```
c1,c2,c3
1,2,3
4,5,6
7,8,9
... (и еще миллион строк)
```
**--- Чтение первых 2 строк ---**
```python
df_rows = pd.read_csv('data_large.csv', nrows=2)

print("DataFrame, содержащий только первые 2 строки:")
print(df_rows)
```
**Вывод:**
```
DataFrame, содержащий только первые 2 строки:
   c1  c2  c3
0   1   2   3
1   4   5   6
```
---
### Дополнение: `chunksize` — обработка больших файлов по частям

Вместо `nrows`, который просто обрезает файл, `chunksize` позволяет обрабатывать огромные файлы, которые не помещаются в память, по частям (чанками).

[`read_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) с этим параметром возвращает не `DataFrame`, а итератор [`TextFileReader`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.parsers.TextFileReader.html).

**--- Исходные данные (`data_large.csv`) ---**
```
product_id,sales
101,50
102,30
103,120
104,80
105,200
106,45
```
**--- Обработка файла по чанкам ---**
```python
total_sales = 0
# Создаем итератор, который будет возвращать DataFrame'ы размером 2 строки
reader = pd.read_csv('data_large.csv', chunksize=2)

print("--- Начинаем обработку по частям ---")
for i, chunk in enumerate(reader):
    print(f"\n--- Чанк {i+1} ---")
    print(chunk)
    total_sales += chunk['sales'].sum()

print(f"\n--- Обработка завершена ---")
print(f"Общая сумма продаж: {total_sales}")
```
**Вывод:**
```
--- Начинаем обработку по частям ---

--- Чанк 1 ---
   product_id  sales
0         101     50
1         102     30

--- Чанк 2 ---
   product_id  sales
2         103    120
3         104     80

--- Чанк 3 ---
   product_id  sales
4         105    200
5         106     45

--- Обработка завершена ---
Общая сумма продаж: 525
```

### Дополнение: как НЕ считать стандартные значения (`NA`, `NULL`) пропущенными

Иногда стандартные маркеры пропусков, такие как "NA", могут быть осмысленными данными (например, "North America"). Чтобы Pandas не преобразовывал их в `NaN` автоматически, используется параметр `keep_default_na=False`.

**--- Исходные данные (`data_with_literal_na.csv`) ---**
```
region,country,value,notes
NA,USA,150,
EU,Germany,,Good
NA,Canada,120,Data OK
AS,Japan,200,NULL
```

**1. Поведение по умолчанию (неправильное для нашей задачи)**
```python
df_default = pd.read_csv('data_with_literal_na.csv')
print("Поведение по умолчанию (NA -> NaN):")
print(df_default)
```
**Вывод:** (Обратите внимание, что `NA` в `region` стало `NaN`)
```
Поведение по умолчанию (NA -> NaN):
  region  country  value     notes
0    NaN      USA  150.0       NaN
1     EU  Germany    NaN      Good
2    NaN   Canada  120.0   Data OK
3     AS    Japan  200.0       NaN
```

**2. Правильное решение: `keep_default_na=False` + `na_values`**
Мы отключаем стандартный список `NaN` и вручную указываем, что считать пропуском (в нашем случае — пустую строку и слово `NULL`).

```python
df_correct = pd.read_csv(
    'data_with_literal_na.csv', 
    keep_default_na=False, 
    na_values=['', 'NULL'] # Указываем, что пустая строка и 'NULL' - это NaN
)
print("\nПравильное чтение (NA - это строка):")
print(df_correct)
```
**Вывод:** (Теперь `NA` — это строка, а остальные пропуски корректно обработаны)
```
Правильное чтение (NA - это строка):
  region  country  value     notes
0     NA      USA  150.0       NaN
1     EU  Germany    NaN      Good
2     NA   Canada  120.0   Data OK
3     AS    Japan  200.0       NaN
```

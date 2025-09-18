### 4.1 Что такое формат CSV и как его приручить?

---

#### 4.1.1-4.1.5 Загрузка данных: от ручного парсинга до `pd.read_csv`

**Что такое CSV?**
CSV (Comma-Separated Values) — это текстовый формат для хранения табличных данных, где столбцы разделены запятыми, а строки — переносами.

**1. Ручной способ (для понимания)**
Можно прочитать файл строка за строкой, но это неэффективно и требует много кода.

```python
# --- Содержимое файла 'example.csv' ---
# a,b,c
# 1,2,3
# 4,5,6

# --- Ручной парсинг ---
f = open('example.csv')
matrix = []
for line in f:
  lst = line.strip().split(',')
  matrix.append(lst)
f.close()

# Пропускаем заголовок и создаем DataFrame
df_manual = pd.DataFrame(matrix[1:], columns=matrix[0])
```

**2. Правильный способ: `pd.read_csv()`**
Pandas предоставляет оптимизированную функцию `pd.read_csv()` для чтения CSV-файлов, которая делает всё за вас.

**Синтаксис:**
`pd.read_csv(filepath_or_buffer, ...)`

```python
# --- Содержимое файла 'example.csv' ---
# a,b,c
# 1,2,3
# 4,5,6

# --- Чтение с помощью Pandas ---
# Важно: в путях используйте / или \\ вместо \
df = pd.read_csv('example.csv')

print("Результат pd.read_csv('example.csv'):")
print(df)
```
**Вывод:**
```
Результат pd.read_csv('example.csv'):
   a  b  c
0  1  2  3
1  4  5  6
```
---
#### 4.1.6-4.1.10 Основные параметры `pd.read_csv`

**1. `sep` — указание разделителя**
Используется, если данные разделены не запятой, а другим символом (например, `;`, `\t` (табуляция), `|`).

```python
# --- Содержимое файла 'data_semicolon.csv' ---
# fruit;color;price
# apple;red;0.99
# banana;yellow;0.59

# --- Чтение с указанием sep=';' ---
df_sep = pd.read_csv('data_semicolon.csv', sep=';')

print("DataFrame из файла с разделителем ';':")
print(df_sep)
```
**Вывод:**
```
DataFrame из файла с разделителем ';':
    fruit   color  price
0   apple     red   0.99
1  banana  yellow   0.59
```

**2. `header=None` — если в файле нет заголовков**
Если в файле отсутствуют названия столбцов, `header=None` говорит Pandas, что первая строка — это данные, а не заголовок.

```python
# --- Содержимое файла 'data_no_header.csv' ---
# 1,John,Smith
# 2,Jane,Doe

# --- Чтение без заголовка ---
df_no_header = pd.read_csv('data_no_header.csv', header=None)

print("DataFrame из файла без заголовка:")
print(df_no_header)
```
**Вывод:** (Столбцы именуются автоматически: 0, 1, 2...)
```
DataFrame из файла без заголовка:
   0     1      2
0  1  John  Smith
1  2  Jane    Doe
```

**3. `names` — присвоение имен столбцам**
Идеально сочетается с `header=None` для задания собственных имен столбцам.

```python
# --- Используем тот же файл 'data_no_header.csv' ---
column_names = ['ID', 'FirstName', 'LastName']

# --- Чтение с присвоением имен ---
df_names = pd.read_csv('data_no_header.csv', names=column_names)

print("DataFrame с кастомными именами столбцов:")
print(df_names)
```
**Вывод:**
```
DataFrame с кастомными именами столбцов:
   ID FirstName LastName
0   1      John    Smith
1   2      Jane      Doe
```

**4. `index_col` — превращение столбца в индекс `DataFrame`**
Указывает, какой столбец (по имени или номеру) использовать в качестве индекса строк.

```python
# --- Содержимое файла 'data_with_id.csv' ---
# user_id,name,age
# 101,Alice,25
# 102,Bob,30

# --- Устанавливаем 'user_id' как индекс ---
df_indexed = pd.read_csv('data_with_id.csv', index_col='user_id')

print("DataFrame с 'user_id' в качестве индекса:")
print(df_indexed)
```
**Вывод:**
```
DataFrame с 'user_id' в качестве индекса:
         name  age
user_id           
101     Alice   25
102       Bob   30
```

### 5.3 Про [замену значений](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html) и [дискретизацию](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#grouping-and-discretization)

---
#### 5.3.1 Замена значений: [`.replace()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html)

Метод [`.replace()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html) ищет указанные значения и заменяет их на новые.

**--- Исходные данные ---**
```python
df = pd.DataFrame({'A': [0, 1, 2, 1], 'B': ['x', 'y', 'z', 'x']})
print("Исходный DataFrame:")
print(df)
```
**Вывод:**
```
Исходный DataFrame:
   A  B
0  0  x
1  1  y
2  2  z
3  1  x
```

**--- Применение `.replace()` ---**
```python
# 1. Замена с помощью списков
# Заменяем 1 на 100 и 'x' на 'XXX'
df_replaced_list = df.replace([1, 'x'], [100, 'XXX'])
print("\nЗамена с помощью списков:")
print(df_replaced_list)

# 2. Замена с помощью словаря (более гибко)
# Заменяем 2 на 200 и 'y' на 'YYY'
df_replaced_dict = df.replace({2: 200, 'y': 'YYY'})
print("\nЗамена с помощью словаря:")
print(df_replaced_dict)
```
**Вывод:**
```
Замена с помощью списков:
     A    B
0    0  XXX
1  100    y
2    2    z
3  100  XXX

Замена с помощью словаря:
     A    B
0    0    x
1    1  YYY
2  200    z
3    1    x
```

---
#### 5.3.2-5.3.3 Переименование индексов и столбцов ([`.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.map.html) и [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html))

**1. Использование [`.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.map.html) для полного переименования**
Метод `.map()` можно применить к объекту `Index` (строкам или столбцам) для замены всех меток.

**--- Исходные данные ---**
```python
df_rename = pd.DataFrame(np.arange(9).reshape(3, 3), 
                         index=['a', 'b', 'c'], 
                         columns=['col1', 'col2', 'col3'])
print("Исходный DataFrame:")
print(df_rename)
```
**Вывод:**
```
Исходный DataFrame:
   col1  col2  col3
a     0     1     2
b     3     4     5
c     6     7     8
```

**--- Применение `.map()` ---**
```python
# Копируем DataFrame для изменений
df_mapped = df_rename.copy()

# Переименовываем индекс с помощью лямбда-функции
df_mapped.index = df_mapped.index.map(lambda x: f'row_{x.upper()}')

# Переименовываем столбцы с помощью словаря
column_map = {'col1': 'X', 'col2': 'Y', 'col3': 'Z'}
df_mapped.columns = df_mapped.columns.map(column_map)

print("\nDataFrame после переименования через .map():")
print(df_mapped)
```
**Вывод:**
```
DataFrame после переименования через .map():
       X  Y  Z
row_A  0  1  2
row_B  3  4  5
row_C  6  7  8
```
---
**2. Использование [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html) для частичного переименования**
`.rename()` удобнее, когда нужно изменить только некоторые метки.

**--- Исходные данные те же ---**
```python
print("Исходный DataFrame:")
print(df_rename)
```
**--- Применение `.rename()` ---**
```python
# Переименовываем и строки, и столбцы в одном вызове
df_renamed = df_rename.rename(
    index={'a': 'Row_A'}, 
    columns={'col2': 'COLUMN_TWO'}
)

print("\nDataFrame после частичного переименования через .rename():")
print(df_renamed)
```
**Вывод:**
```
DataFrame после частичного переименования через .rename():
       col1  COLUMN_TWO  col3
Row_A     0           1     2
b         3           4     5
c         6           7     8
```
---
#### 5.3.4-5.3.8 Дискретизация и группировка ([`.cut()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html) и [`.qcut()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.qcut.html))

**1. [`pd.cut()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html) — разбивка по заданным интервалам**
`cut` делит данные на группы (бины) на основе заданных границ.
*   `right=True` (по умолчанию): Правая граница интервала включается `(a, b]`.
*   `right=False`: Левая граница интервала включается `[a, b)`.

**--- Исходные данные ---**
```python
ages = pd.Series([10, 18, 25, 35, 50, 65, 80])
bins = [0, 17, 30, 60, 100] # Границы для групп
```

**--- Применение `.cut()` ---**
```python
# 1. Простое разбиение
age_categories = pd.cut(ages, bins)
print("Результат pd.cut():")
print(age_categories)

# 2. Получение кодов групп и подсчет
print("\nКоды групп (.codes):", age_categories.codes)
print("\nПодсчет по группам (value_counts):")
print(pd.value_counts(age_categories))

# 3. Добавление меток (labels)
group_names = ['Child', 'Young Adult', 'Adult', 'Senior']
age_categories_labeled = pd.cut(ages, bins, labels=group_names)
print("\nРезультат pd.cut() с метками:")
print(age_categories_labeled)

# 4. Разбиение на 3 группы равной ширины
age_categories_equal_width = pd.cut(ages, 3)
print("\nРезультат pd.cut() с 3 группами равной ширины:")
print(pd.value_counts(age_categories_equal_width))
```
**Вывод:**
```
Результат pd.cut():
0      (0, 17]
1     (17, 30]
2     (17, 30]
3     (30, 60]
4     (30, 60]
5    (60, 100]
6    (60, 100]
dtype: category
Categories (4, interval[int64, right]): [(0, 17] < (17, 30] < (30, 60] < (60, 100]]

Коды групп (.codes): [0 1 1 2 2 3 3]

Подсчет по группам (value_counts):
(0, 17]      1
(17, 30]     2
(30, 60]     2
(60, 100]    2
dtype: int64

Результат pd.cut() с метками:
0          Child
1    Young Adult
2    Young Adult
3          Adult
4          Adult
5         Senior
6         Senior
dtype: category
Categories (4, object): ['Child' < 'Young Adult' < 'Adult' < 'Senior']

Результат pd.cut() с 3 группами равной ширины:
(9.93, 33.333]    3
(33.333, 56.667]    2
(56.667, 80.0]      2
dtype: int64
```
---
**2. [`pd.qcut()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.qcut.html) — разбивка по квантилям (равное количество)**
`qcut` делит данные так, чтобы в каждой группе оказалось примерно **одинаковое количество элементов**.

**--- Исходные данные ---**
```python
data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 100]) # С одним большим выбросом
```

**--- Применение `qcut()` vs `cut()` ---**
```python
# Разбиваем на 4 группы по количеству
qcut_result = pd.qcut(data, 4)
print("Результат pd.qcut(data, 4):")
print(pd.value_counts(qcut_result))

# Для сравнения, результат cut
cut_result = pd.cut(data, 4)
print("\nРезультат pd.cut(data, 4) для тех же данных:")
print(pd.value_counts(cut_result))
```
**Вывод:**
```
Результат pd.qcut(data, 4):
(0.999, 3.25]    3
(3.25, 5.5]      2
(5.5, 7.75]      2
(7.75, 100.0]    3
dtype: int64
# qcut создал группы с 2-3 элементами в каждой

Результат pd.cut(data, 4) для тех же данных:
(0.901, 25.75]    9
(75.25, 100.0]     1
(50.5, 75.25]      0
(25.75, 50.5]      0
dtype: int64
# cut создал один большой бин из-за выброса, остальные почти пустые
```

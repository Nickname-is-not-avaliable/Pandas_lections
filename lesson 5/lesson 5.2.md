### 5.2 [Заполнение пропусков](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#filling-missing-values), [дубликаты](https://pandas.pydata.org/pandas-docs/stable/user_guide/duplicates.html) и [замена значений](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#string-methods)

---
#### 5.2.1-5.2.4 Заполнение пропущенных значений ([`.fillna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html))

Метод [`.fillna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html) заменяет пропущенные значения (`NaN`) на указанные. По умолчанию возвращает новый `DataFrame`.

**--- Исходные данные ---**
```python
df_fill = pd.DataFrame({
    'A': [1, np.nan, 3, np.nan, 5],
    'B': [np.nan, 2, np.nan, 4, 5],
    'C': ['X', 'Y', np.nan, 'Z', np.nan]
})

print("Исходный DataFrame:")
print(df_fill)
```
**Вывод:**
```
Исходный DataFrame:
     A    B    C
0  1.0  NaN    X
1  NaN  2.0    Y
2  3.0  NaN  NaN
3  NaN  4.0    Z
4  5.0  5.0  NaN
```
---
**1. Заполнение одним значением или словарем**
```python
# Заполнение всех NaN нулем
df_filled_zero = df_fill.fillna(0)
print("\nЗаполнение всех NaN нулем:")
print(df_filled_zero)

# Заполнение NaN разными значениями для разных столбцов
fill_values = {'A': 99, 'B': 100, 'C': 'MISSING'}
df_filled_dict = df_fill.fillna(fill_values)
print("\nЗаполнение NaN словарем:")
print(df_filled_dict)
```
**Вывод:**
```
Заполнение всех NaN нулем:
     A    B        C
0  1.0  0.0        X
1  0.0  2.0        Y
2  3.0  0.0      0.0
3  0.0  4.0        Z
4  5.0  5.0      0.0

Заполнение NaN словарем:
     A      B        C
0  1.0  100.0        X
1  99.0  2.0        Y
2  3.0  100.0  MISSING
3  99.0  4.0        Z
4  5.0  5.0  MISSING
```
---
**2. Заполнение методом (например, `ffill`, `bfill`)**
*   `method='ffill'` (forward fill): Заполняет `NaN` значением из **предыдущей** валидной ячейки.
*   `method='bfill'` (backward fill): Заполняет `NaN` значением из **следующей** валидной ячейки.
*   `limit`: Ограничивает количество последовательных `NaN`, которые будут заполнены.

```python
# Заполнение методом 'ffill' (вперед)
df_ffill = df_fill.fillna(method='ffill')
print("\nЗаполнение методом 'ffill':")
print(df_ffill)

# Заполнение методом 'bfill' с ограничением в 1
df_bfill_limit = df_fill.fillna(method='bfill', limit=1)
print("\nЗаполнение методом 'bfill' с limit=1:")
print(df_bfill_limit)
```
**Вывод:**
```
Заполнение методом 'ffill':
     A    B    C
0  1.0  NaN    X
1  1.0  2.0    Y
2  3.0  2.0    Y
3  3.0  4.0    Z
4  5.0  5.0    Z

Заполнение методом 'bfill' с limit=1:
     A    B    C
0  1.0  2.0    X
1  3.0  2.0    Y
2  3.0  4.0    Z
3  5.0  4.0    Z
4  5.0  5.0  NaN
```
---
**3. Заполнение статистическими значениями**
Часто пропуски заполняют средним, медианой или модой.

```python
# Заполнение пропусков в столбцах 'A' и 'B' их средними значениями
df_filled_mean = df_fill.fillna(df_fill[['A', 'B']].mean())
print("\nЗаполнение пропусков средними значениями:")
print(df_filled_mean)
```
**Вывод:**
```
Заполнение пропусков средними значениями:
     A    B        C
0  1.0  NaN        X
1  3.0  2.0        Y
2  3.0  NaN      NaN
3  3.0  4.0        Z
4  5.0  5.0      NaN
```
*(Обратите внимание: `df_fill.mean()` для столбца 'A' это `(1+3+5)/3=3`)*

---
#### 5.2.5-5.2.7 Поиск и удаление дубликатов

**--- Исходные данные ---**
```python
df_duplicates = pd.DataFrame({
    'k1': ['one', 'two', 'one', 'three', 'two'],
    'k2': [1, 1, 2, 2, 1],
    'k3': ['X', 'Y', 'Z', 'X', 'Y']
})

print("DataFrame с дубликатами:")
print(df_duplicates)
```
**Вывод:**
```
DataFrame с дубликатами:
      k1  k2 k3
0    one   1  X
1    two   1  Y
2    one   2  Z
3  three   2  X
4    two   1  Y
```
---
**1. [`df.duplicated()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html) — поиск дубликатов**
Возвращает булеву `Series`, где `True` означает, что строка является дубликатом (т.е., она встречалась ранее).

```python
print("\nМаска дубликатов:")
print(df_duplicates.duplicated())
```
**Вывод:**
```
Маска дубликатов:
0    False
1    False
2    False
3    False
4     True # <-- Строка (two, 1, Y) повторяет строку (two, 1, Y)
dtype: bool
```
---
**2. [`df.drop_duplicates()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html) — удаление дубликатов**

*   По умолчанию удаляет все строки, для которых `duplicated()` вернуло `True`, оставляя только первое вхождение.
*   `subset`: Список столбцов, по которым искать дубликаты.
*   `keep`:
    *   `'first'` (по умолчанию): Оставить первое вхождение.
    *   `'last'`: Оставить последнее вхождение.
    *   `False`: Удалить все вхождения, которые являются дубликатами.

```python
# Удалить дубликаты по всем столбцам (поведение по умолчанию)
print("\nПосле .drop_duplicates():")
print(df_duplicates.drop_duplicates())

# Удалить дубликаты, считая только столбцы 'k1' и 'k2', и оставить последнее вхождение
print("\nПосле .drop_duplicates(subset=['k1', 'k2'], keep='last'):")
print(df_duplicates.drop_duplicates(subset=['k1', 'k2'], keep='last'))

# Удалить все дубликаты (т.е., оставить только уникальные строки, которые нигде не повторяются)
print("\nПосле .drop_duplicates(keep=False):")
print(df_duplicates.drop_duplicates(keep=False))
```
**Вывод:**
```
После .drop_duplicates():
      k1  k2 k3
0    one   1  X
1    two   1  Y
2    one   2  Z
3  three   2  X

После .drop_duplicates(subset=['k1', 'k2'], keep='last'):
      k1  k2 k3
0    one   1  X
2    one   2  Z
3  three   2  X
4    two   1  Y

После .drop_duplicates(keep=False):
      k1  k2 k3
0    one   1  X
2    one   2  Z
3  three   2  X
```
---
#### 5.2.8-5.2.10 Применение функций: [`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html)

Для применения функций к данным в Pandas используются методы [`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html), [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html), [`DataFrame.applymap()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.applymap.html).

**1. [`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) — для замены значений в Series**
Используется для замены каждого значения в `Series` на другое, согласно словарю или функции.

**--- Исходные данные ---**
```python
s_map = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print("Исходная Series:")
print(s_map)
```
**Вывод:**
```
Исходная Series:
a    1
b    2
c    3
d    4
e    5
dtype: int64
```
**--- Применение `.map()` ---**
```python
# Замена значений по словарю
mapping_dict = {1: 'One', 2: 'Two', 3: 'Three'}
s_mapped_dict = s_map.map(mapping_dict)
print("\n.map() со словарем:")
print(s_mapped_dict)

# Замена значений с помощью функции (подойдёт как лямбда-функция, так и обычная)
s_mapped_func = s_map.map(lambda x: f"Value_{x*10}")
print("\n.map() с лямбда-функцией:")
print(s_mapped_func)
```
**Вывод:**
```
.map() со словарем:
a      One
b      Two
c    Three
d      NaN
e      NaN
dtype: object

.map() с лямбда-функцией:
a    Value_10
b    Value_20
c    Value_30
d    Value_40
e    Value_50
dtype: object
```

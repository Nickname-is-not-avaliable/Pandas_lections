### 3.11 [Арифметика с пропусками](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#filling-missing-values), [сортировка](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#sorting) и [уникальность](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.is_unique.html)

---

#### 3.11.1-3.11.2 [Арифметика с заполнением пропусков](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#filling-missing-values)

Арифметические методы ([`.add`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.add.html), [`.sub`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sub.html) и т.д.) имеют параметр `fill_value`, который позволяет заменить пропуски (`NaN`) заданным значением **перед** выполнением операции.

**--- Исходные данные ---**
```python
df1 = pd.DataFrame(np.arange(4.).reshape(2, 2), columns=['a', 'b'], index=['A', 'C'])
df2 = pd.DataFrame(np.arange(3.).reshape(3, 1), columns=['a'], index=['A', 'B', 'D'])

print("df1:")
print(df1)
print("\ndf2:")
print(df2)
```
**Вывод:**
```
df1:
     a    b
A  0.0  1.0
C  2.0  3.0

df2:
     a
A  0.0
B  1.0
D  2.0
```
**--- Сложение ---**
```python
# Cложение с fill_value=0
result_filled = df1.add(df2, fill_value=0)

print("\nРезультат сложения с fill_value=0:")
print(result_filled)
```
**Вывод:**
```
Результат сложения с fill_value=0:
     a    b
A  0.0  1.0
B  1.0  NaN
C  2.0  3.0
D  2.0  NaN
```
*(Примечание: `NaN` в столбце `b` остался, т.к. `fill_value` применяется только там, где есть хотя бы одно значение в паре `df1`, `df2`)*

---
#### 3.11.3-3.11.5 [Операции между `DataFrame` и `Series` (Broadcasting)](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#operations-between-dataframe-and-series)

**--- Исходные данные ---**
```python
df = pd.DataFrame(np.arange(12.).reshape(4, 3), columns=['b', 'd', 'e'], index=['A', 'B', 'C', 'D'])
s_cols = pd.Series([100, 200, 300], index=['b', 'd', 'e']) # Для вычитания из столбцов
s_rows = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D']) # Для вычитания из строк

print("DataFrame (df):")
print(df)
print("\nSeries для столбцов (s_cols):")
print(s_cols)
print("\nSeries для строк (s_rows):")
print(s_rows)
```
**Вывод:**
```
DataFrame (df):
     b     d     e
A  0.0   1.0   2.0
B  3.0   4.0   5.0
C  6.0   7.0   8.0
D  9.0  10.0  11.0

Series для столбцов (s_cols):
b    100
d    200
e    300
dtype: int64

Series для строк (s_rows):
A    10
B    20
C    30
D    40
dtype: int64
```
**--- Вычитание ---**
```python
# Вычитание s_cols из каждого ряда df
result_cols = df.sub(s_cols)
print("\nРезультат: df.sub(s_cols) (по столбцам)")
print(result_cols)

# Вычитание s_rows из каждого столбца df
result_rows = df.sub(s_rows, axis='index')
print("\nРезультат: df.sub(s_rows, axis='index') (по строкам)")
print(result_rows)
```
**Вывод:**
```
Результат: df.sub(s_cols) (по столбцам)
       b      d      e
A -100.0 -199.0 -298.0
B  -97.0 -196.0 -295.0
C  -94.0 -193.0 -292.0
D  -91.0 -190.0 -289.0

Результат: df.sub(s_rows, axis='index') (по строкам)
      b     d     e
A -10.0  -9.0  -8.0
B -17.0 -16.0 -15.0
C -24.0 -23.0 -22.0
D -31.0 -30.0 -29.0
```

---
#### 3.11.6-3.11.8 [Сортировка](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#sorting)

**--- Исходные данные ---**
```python
df_sort = pd.DataFrame(np.arange(8).reshape(4, 2),
                       index=['c', 'a', 'd', 'b'],
                       columns=['two', 'one'])

print("Неотсортированный DataFrame:")
print(df_sort)
```
**Вывод:**
```
Неотсортированный DataFrame:
   two  one
c    0    1
a    2    3
d    4    5
b    6    7
```
**--- Сортировка ---**
```python
# 1. Сортировка по индексу строк
sorted_by_index = df_sort.sort_index()
print("\nПосле .sort_index():")
print(sorted_by_index)

# 2. Сортировка по значениям в столбце 'one'
sorted_by_values = df_sort.sort_values(by='one', ascending=False)
print("\nПосле .sort_values(by='one', ascending=False):")
print(sorted_by_values)
```
**Вывод:**
```
После .sort_index():
   two  one
a    2    3
b    6    7
c    0    1
d    4    5

После .sort_values(by='one', ascending=False):
   two  one
b    6    7
d    4    5
a    2    3
c    0    1
```
---
#### 3.11.9-3.11.10 Проверка на уникальность [`is_unique`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.is_unique.html)

`.is_unique` — это атрибут, который возвращает `True`, если все элементы уникальны.

**--- Исходные данные ---**
```python
df_unique_test = pd.DataFrame(index=['a', 'b', 'a'], columns=['x', 'y'])
s_unique_test = pd.Series([1, 2, 1])

print("DataFrame для теста:")
print(df_unique_test)
print("\nSeries для теста:")
print(s_unique_test)
```
**Вывод:**
```
DataFrame для теста:
     x    y
a  NaN  NaN
b  NaN  NaN
a  NaN  NaN

Series для теста:
0    1
1    2
2    1
dtype: int64
```
**--- Проверка ---**
```python
print(f"\nИндекс строк df уникален? -> {df_unique_test.index.is_unique}")
print(f"Столбцы df уникальны?    -> {df_unique_test.columns.is_unique}")
print(f"Значения в s уникальны? -> {s_unique_test.is_unique}")
```
**Вывод:**
```
Индекс строк df уникален? -> False
Столбцы df уникальны?    -> True
Значения в s уникальны? -> False
```

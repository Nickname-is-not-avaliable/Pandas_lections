### 3.12 Описательные статистики и уникальные значения

---

#### 3.12.1-3.12.2 Агрегирующие функции: `sum`, `mean` и параметры

Функции, такие как `.sum()` и `.mean()`, имеют важные параметры:
*   `axis`: Ось для вычислений (`0` для столбцов, `1` для строк).
*   `skipna` (по умолчанию `True`): Игнорировать ли `NaN` при расчетах. Если `False`, то при наличии `NaN` результат будет `NaN`.

**--- Исходные данные ---**
```python
df_stats = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
                        index=['a', 'b', 'c', 'd'],
                        columns=['one', 'two'])

print("Исходный DataFrame:")
print(df_stats)
```
**Вывод:**
```
Исходный DataFrame:
     one   two
a   1.40   NaN
b   7.10  -4.5
c    NaN   NaN
d   0.75  -1.3
```

**--- Применение функций ---**
```python
# 1. Сумма по столбцам (axis=0, по умолчанию), пропуская NaN
sum_cols = df_stats.sum(axis=0)
print("\nСумма по столбцам (пропуская NaN):")
print(sum_cols)

# 2. Сумма по строкам (axis=1), НЕ пропуская NaN
sum_rows = df_stats.sum(axis=1, skipna=False)
print("\nСумма по строкам (НЕ пропуская NaN):")
print(sum_rows)
```
**Вывод:**
```
Сумма по столбцам (пропуская NaN):
one    9.25
two   -5.80
dtype: float64

Сумма по строкам (НЕ пропуская NaN):
a     NaN  # <-- 1.4 + NaN = NaN
b    2.60
c     NaN  # <-- NaN + NaN = NaN
d   -0.55
dtype: float64
```
---
#### 3.12.3-3.12.5 Сводная статистика: `.describe()`

Метод `.describe()` генерирует сводную статистику для числовых столбцов (или `Series`).

**--- Исходные данные ---**
```python
print("Исходный DataFrame:")
print(df_stats)
```
**Вывод:**
```
Исходный DataFrame:
     one   two
a   1.40   NaN
b   7.10  -4.5
c    NaN   NaN
d   0.75  -1.3
```
**--- Применение `.describe()` ---**
```python
# 1. Для DataFrame (по столбцам)
df_description = df_stats.describe()
print("\nРезультат df.describe():")
print(df_description)

# 2. Для одного Series (столбца)
series_description = df_stats['one'].describe()
print("\nРезультат s.describe() для столбца 'one':")
print(series_description)
```
**Вывод:**
```
Результат df.describe():
            one       two
count  3.000000  2.000000  # <-- Количество не-NaN значений
mean   3.083333 -2.900000  # <-- Среднее
std    3.493685  2.262742  # <-- Стандартное отклонение
min    0.750000 -4.500000  # <-- Минимум
25%    1.075000 -3.700000  # <-- 25-й перцентиль
50%    1.400000 -2.900000  # <-- 50-й перцентиль (медиана)
75%    4.250000 -2.100000  # <-- 75-й перцентиль
max    7.100000 -1.300000  # <-- Максимум

Результат s.describe() для столбца 'one':
count    3.000000
mean     3.083333
std      3.493685
min      0.750000
25%      1.075000
50%      1.400000
75%      4.250000
max      7.100000
Name: one, dtype: float64
```
---
#### 3.12.6-3.12.8 Уникальные значения: `value_counts` и `isin`

*   `.value_counts()`: Считает, сколько раз встречается каждое уникальное значение в `Series`.
*   `.isin()`: Проверяет, какие элементы `Series` содержатся в переданной последовательности, и возвращает булеву маску.

**--- Исходные данные ---**
```python
s_unique = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
df_filter = pd.DataFrame({'letters': s_unique, 'numbers': np.arange(len(s_unique))})

print("Исходная Series:")
print(s_unique)
print("\nИсходный DataFrame:")
print(df_filter)
```
**Вывод:**
```
Исходная Series:
0    c
1    a
2    d
3    a
4    a
5    b
6    b
7    c
8    c
dtype: object

Исходный DataFrame:
  letters  numbers
0       c        0
1       a        1
2       d        2
3       a        3
4       a        4
5       b        5
6       b        6
7       c        7
8       c        8
```
**--- Применение функций ---**
```python
# 1. Подсчет уникальных значений
counts = s_unique.value_counts()
print("\nРезультат s.value_counts():")
print(counts)

# 2. Фильтрация с помощью isin
# Задача: выбрать строки, где в столбце 'letters' находятся 'b' или 'c'
mask = df_filter['letters'].isin(['b', 'c'])
print("\nМаска, созданная .isin(['b', 'c']):")
print(mask)

filtered_df = df_filter[mask]
print("\nРезультат фильтрации DataFrame по маске:")
print(filtered_df)
```
**Вывод:**
```
Результат s.value_counts():
c    3
a    3
b    2
d    1
Name: letters, dtype: int64

Маска, созданная .isin(['b', 'c']):
0     True
1    False
2    False
3    False
4    False
5     True
6     True
7     True
8     True
Name: letters, dtype: bool

Результат фильтрации DataFrame по маске:
  letters  numbers
0       c        0
5       b        5
6       b        6
7       c        7
8       c        8
```

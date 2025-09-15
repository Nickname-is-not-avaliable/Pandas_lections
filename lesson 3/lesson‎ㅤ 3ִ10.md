

### 3.10 Точный выбор данных: `loc`, `iloc`, `at`, `iat`

---

Для всех примеров в этой секции мы будем использовать следующий `DataFrame`:

```python
import pandas as pd
import numpy as np

# --- ИСХОДНЫЙ DATAFRAME ---
df = pd.DataFrame(np.arange(16).reshape((4, 4)),
                  index=['a', 'b', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'Utah', 'Oregon'])

print("Наш исходный DataFrame (df):")
print(df)
```
**Вывод:**
```
Наш исходный DataFrame (df):
   Ohio  Texas  Utah  Oregon
a     0      1     2       3
b     4      5     6       7
c     8      9    10      11
d    12     13    14      15
```
---

#### 3.10.1-3.10.4 Оператор `loc`: выбор по меткам

`loc` выбирает данные по **названиям** строк и столбцов.

**Пример 1: Выбор по списку меток**
```python
# Задача: Выбрать строки 'a' и 'd', и столбцы 'Texas' и 'Oregon'
result = df.loc[['a', 'd'], ['Texas', 'Oregon']]

print("Результат выбора по списку меток:")
print(result)
```
**Вывод:**
```
Результат выбора по списку меток:
   Texas  Oregon
a      1       3
d     13      15
```

**Пример 2: Выбор по условию (булевой маске)**
```python
# Задача: Выбрать строки, где значение в 'Utah' > 5, 
# и показать только столбцы 'Ohio' и 'Texas'

# Сначала посмотрим на само условие (маску):
mask = df['Utah'] > 5
print("Созданная маска:")
print(mask)

# Теперь применим эту маску с помощью .loc
result_conditional = df.loc[mask, ['Ohio', 'Texas']]
print("\nРезультат выбора по условию:")
print(result_conditional)
```
**Вывод:**
```
Созданная маска:
a    False
b     True
c     True
d     True
Name: Utah, dtype: bool

Результат выбора по условию:
   Ohio  Texas
b     4      5
c     8      9
d    12     13
```
---
#### 3.10.5 Оператор `iloc`: выбор по номерам

`iloc` работает аналогично `loc`, но использует **порядковые номера** (позиции) строк и столбцов, начиная с `0`.

```python
# Исходный DataFrame тот же
print("Наш исходный DataFrame (df):")
print(df)

# Задача: Выбрать 1-ю и 3-ю строки (позиции 0 и 2) 
# и 2-й и 4-й столбцы (позиции 1 и 3)
result_iloc = df.iloc[[0, 2], [1, 3]] 

print("\nРезультат выбора по номерам (iloc):")
print(result_iloc)
```
**Вывод:**
```
Наш исходный DataFrame (df):
   Ohio  Texas  Utah  Oregon
a     0      1     2       3
b     4      5     6       7
c     8      9    10      11
d    12     13    14      15

Результат выбора по номерам (iloc):
   Texas  Oregon
a      1       3
c      9      11
```
---
#### 3.10.6-3.10.7 `at`, `iat` и перезапись данных

`at` и `iat` — это сверхбыстрые версии `loc` и `iloc` для доступа к **одной ячейке**. Их также можно использовать для присваивания.

```python
# Исходный DataFrame тот же
print("Исходный DataFrame:")
print(df)

# Задача: Изменить значение в ячейке на пересечении 
# строки 'b' и столбца 'Ohio' на 99

df.at['b', 'Ohio'] = 99

print("\nDataFrame после изменения через .at:")
print(df)
```
**Вывод:**
```
Исходный DataFrame:
   Ohio  Texas  Utah  Oregon
a     0      1     2       3
b     4      5     6       7
c     8      9    10      11
d    12     13    14      15

DataFrame после изменения через .at:
   Ohio  Texas  Utah  Oregon
a     0      1     2       3
b    99      5     6       7
c     8      9    10      11
d    12     13    14      15
```
---
#### 3.10.8-3.10.10 Сложение `DataFrame` и выравнивание

При сложении двух `DataFrame` Pandas автоматически **выравнивает их по меткам строк и столбцов**.

**Сначала посмотрим на исходные `DataFrame`:**
```python
df1 = pd.DataFrame(np.arange(4).reshape((2, 2)),
                   index=['a', 'b'], columns=['A', 'B'])
df2 = pd.DataFrame(np.arange(6).reshape((3, 2)),
                   index=['a', 'c', 'd'], columns=['A', 'C'])

print("Первый DataFrame (df1):")
print(df1)
print("\nВторой DataFrame (df2):")
print(df2)
```
**Вывод:**
```
Первый DataFrame (df1):
   A  B
a  0  1
b  2  3

Второй DataFrame (df2):
   A  C
a  0  1
c  2  3
d  4  5
```
**Теперь выполним сложение:**
```python
result_add = df1 + df2
print("\nРезультат сложения (df1 + df2):")
print(result_add)
```
**Вывод и анализ результата:**
```
Результат сложения (df1 + df2):
      A   B   C
a   0.0 NaN NaN
b   NaN NaN NaN
c   NaN NaN NaN
d   NaN NaN NaN
```
*   **Ячейка `[a, A]`:** `0.0` (потому что `0` из `df1` + `0` из `df2`). Это единственная ячейка, где **и индекс, и столбец** совпали.
*   **Ячейка `[a, B]`:** `NaN`, потому что столбец `B` есть в `df1`, но его нет в `df2`.
*   **Ячейка `[b, A]`:** `NaN`, потому что индекс `b` есть в `df1`, но его нет в `df2`.
*   **Все остальные:** `NaN`, так как для них не нашлось пары с совпадающими метками строки и столбца.

### 3.5 Первое знакомство с [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

[`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) — это двумерная табличная структура данных и основной объект в Pandas. Её можно представить как таблицу Excel, SQL-таблицу или словарь, состоящий из объектов `Series`.

---

#### 3.5.1-3.5.2 Создание [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

Самый распространённый способ — из словаря, где ключи становятся названиями столбцов, а значения — списками или [`Series`](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#series).

```python
# Создадим словарь, где значения - это списки
data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}

df = pd.DataFrame(data)
print(df)
```
**Вывод:**
```
ㅤ    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9
5  Nevada  2003  3.2
```
---

#### 3.5.3-3.5.4 Неуникальные индексы в [`Series`](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#series)

В отличие от ключей словаря, индексы в `Series` (и `DataFrame`) **могут повторяться**. При обращении по такому индексу вы получите `Series` со всеми значениями, которые ему соответствуют.

**Пример:**
```python
s = pd.Series([10, 20, 30], index=['a', 'b', 'a'])
print("Исходная серия:\n", s, "\n")

# Обращение к уникальному индексу 'b' вернет число
print("s['b'] ->", s['b'])

# Обращение к неуникальному индексу 'a' вернет новую СЕРИЮ
print("\ns['a'] ->\n", s['a'])
```
**Вывод:**
```
Исходная серия:
 a    10
 b    20
 a    30
dtype: int64 

s['b'] -> 20

s['a'] ->
 a    10
 a    30
dtype: int64
```

---

#### 3.5.5-3.5.6 Гибкое создание `DataFrame` с параметрами [`columns`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html) и [`index`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.index.html)

При создании `DataFrame` можно управлять столбцами и индексами:

1.  **[`columns`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html)**: Позволяет выбирать, переупорядочивать и даже добавлять несуществующие столбцы.
2.  **[`index`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.index.html)**: Позволяет задать кастомные метки для строк.

**Правило:** Количество строк (длина списков в словаре) и количество меток в `index` **должно совпадать**.

**Пример (переформулировано и дополнено):**
```python
data = {'state': ['Ohio', 'Texas'], 'pop': [1.5, 2.4]}

# 1. Переупорядочиваем столбцы
df_reordered = pd.DataFrame(data, columns=['pop', 'state'])

# 2. Выбираем часть столбцов и добавляем новый, пустой столбец 'debt'
#    'debt' будет заполнен значениями NaN
df_new_col = pd.DataFrame(data, columns=['state', 'debt'])

# 3. Задаем кастомный индекс для строк
df_custom_index = pd.DataFrame(data, index=['one', 'two'])

print("Переупорядоченный:\n", df_reordered)
print("\nС новым столбцом:\n", df_new_col)
print("\nС кастомным индексом:\n", df_custom_index)
```
Для быстрой проверки первых строк `DataFrame` используйте [`df.head(n)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html), где `n` — количество строк.

---

#### 3.5.7-3.5.8 [Доступ к данным](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#basics)

*   **Доступ к столбцу:** Возвращает `Series`.
    1.  **Синтаксис словаря (рекомендуемый):** `df['column_name']`
    2.  **Синтаксис атрибута:** `df.column_name`. **Ограничение:** не работает, если в имени столбца есть пробелы, спецсимволы или оно совпадает с названием метода `DataFrame` (например, `df.index`).

*   **Доступ к строке по метке индекса:** Возвращает `Series`.
    Используется атрибут [`.loc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html): `df.loc[index_label]`

---

#### 3.5.9-3.5.10 [Присваивание и создание новых столбцов](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#setting-with-enlargement)

Новый столбец создается простым присваиванием.

*   **Присваивание одного значения:** Оно будет "растянуто" на все строки.
    ```python
    df['debt'] = 16.5 
    ```
*   **Присваивание списка или массива:** Длина списка должна совпадать с количеством строк в `DataFrame`.
    ```python
    df['eastern'] = [True, True, True, False, False, False]
    ```
*   **Присваивание `Series`:** Pandas **выровняет данные по индексу**. Значения будут присвоены только тем строкам, индексы которых совпадают. В остальных строках нового столбца будет `NaN`.
    ```python
    # Создадим Series только для части индексов DataFrame
    val = pd.Series([-1.2, -1.5, -1.7], index=[0, 3, 5])
    df['debt'] = val
    ```
    **Результат:** В столбце `debt` значения появятся только в строках с индексами `0`, `3` и `5`. Остальные будут `NaN`.

### 3.3 Поподробнее про серии: идексы, сложение, проверка на NaN

---

В [`Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) (и Pandas в целом) все операции автоматически **выравниваются по индексу**.

#### 3.3.1-3.3.2 Сохранение индексов и [операции](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#series)

*   **Индексы "привязаны" к значениям.** Если вы фильтруете `Series` или применяете к нему математические операции, индексы остаются с соответствующими им значениями и не пересчитываются с нуля.
*   **Проверка наличия индекса:** Оператор `in` проверяет наличие метки в **индексе**, а не в значениях.
    ```python
    s = pd.Series([10, 20], index=['a', 'b'])
    'a' in s  # -> True
    10 in s # -> False (проверяет именно индекс!)
    ```
*   **Арифметические операции:** В отличие от словарей, `Series` поддерживает векторизованные операции.
    `s + 1` прибавит 1 к каждому **значению** в `Series`.

---

#### 3.3.3-3.3.4 Создание `Series` из [словаря](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)

Ключи словаря автоматически становятся индексами.

```python
capitals = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
s_capitals = pd.Series(capitals)
```

**Управление индексами при создании:**
Вы можете передать свой список индексов. Pandas будет использовать его для формирования нового `Series`.

*   Значения для совпадающих ключей будут взяты из словаря.
*   Если в вашем списке есть индекс, которого нет в словаре, ему будет присвоено значение `NaN` (Not a Number).
*   Если в словаре есть ключ, которого нет в вашем списке, он будет проигнорирован.

```python
states = ['California', 'Ohio', 'Oregon', 'Texas']
s_with_nan = pd.Series(capitals, index=states)

print(s_with_nan)
```
**Вывод:**
```
California        NaN  # <-- 'California' нет в словаре capitals
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
dtype: float64
# 'Utah' был проигнорирован, т.к. его нет в списке states
```

---

#### 3.3.5 Работа с пропущенными данными: [`isnull`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isnull.html) и [`notnull`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.notnull.html)

`NaN` — это стандартный маркер пропущенных данных в Pandas.

*   `pd.isnull(s)` (или [`s.isnull()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isnull.html)): Возвращает булеву маску, где `True` стоит на месте `NaN`.
*   `pd.notnull(s)` (или [`s.notnull()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.notnull.html)): Возвращает обратную маску (`True` для всех значений, кроме `NaN`).

---

#### 3.3.6-3.3.8 [Арифметические операции и выравнивание данных](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#vectorized-operations-and-label-alignment-with-series)

При выполнении операций (например, сложения) между двумя `Series`, Pandas выравнивает их по меткам индекса.

*   Если индексы совпадают, значения складываются.
*   Если индекс есть только в одном из `Series`, в результате будет `NaN`.

**Пример:**
```python
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([100, 200, 300], index=['a', 'c', 'd'])

print(s1 + s2)
```
**Вывод:**
```
a    110.0  # 10 + 100
b      NaN  # 'b' есть только в s1
c    230.0  # 30 + 200
d      NaN  # 'd' есть только в s2
dtype: float64
```
Это автоматическое выравнивание — особенность Pandas. То же самое относится к вычитанию, умножению и другим операциям.

---

#### 3.3.9-3.3.10 Редактирование метаданных: [`.index`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.index.html) и [`.name`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.name.html)

*   **Изменение индекса:** Вы можете полностью заменить индекс `Series`, присвоив ему новый список. Длина нового списка **должна** совпадать с длиной `Series`.
    ```python
    s.index = ['x', 'y', 'z']
    ```

*   **Имя `Series`:** `Series` может иметь имя, которое полезно при работе с `DataFrame` (имя становится заголовком столбца).
    ```python
    s = pd.Series([1, 2, 3], name='My Numbers')
    
    # Можно присвоить имя и позже
    s.name = 'My Favorite Numbers'
    
    print(s)
    ```
    **Вывод:**
    ```
    0    1
    1    2
    2    3
    Name: My Favorite Numbers, dtype: int64
    ```

---

*В лекциях нет информации для задачки 3.4.4 [Вот ссылка на документацию `pd.concat`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html).* 


*И помни, что в реальном программировании **всегда** нужно рыться в документации*

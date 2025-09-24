### 2.9 Еще о reshape, транспонирование, унарные и бинарные функции

---

### 2.9.1-2.9.2 Представления (Views) vs Копии: [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)

Функция `.reshape()` **не создает новый массив**, а лишь меняет "представление" (view) исходных данных. Это означает, что новый и старый массив используют одну и ту же область памяти.

*   **Следствие:** При изменении данных в одном массиве, они изменятся и в другом.
*   **Причина:** Это сделано для экономии памяти и высокой производительности, так как не происходит копирования данных.

---

### 2.9.3 Транспонирование матрицы ([`.T`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html), [`.transpose()`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html))

Транспонирование меняет строки и столбцы местами. Как и `reshape`, эта операция создает **представление**, а не копию.

*   **Синтаксис (атрибут):** `arr.T`
*   **Синтаксис (метод):** `arr.transpose()`

---

### 2.9.4-2.9.5 [Унарные математические функции (ufunc)](https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs)

Эти функции выполняют поэлементные операции над одним массивом.

*   **Корень квадратный:** [`np.sqrt(arr)`](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html)
*   **Модуль (абсолютное значение):** [`np.abs(arr)`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html)
*   **Округление до ближайшего целого:** [`np.round(arr)`](https://numpy.org/doc/stable/reference/generated/numpy.round.html)
    *(Примечание: `0.5` округляется до ближайшего четного числа, например, `2.5 -> 2`, `3.5 -> 4`)*
*   **Округление вверх (потолок):** [`np.ceil(arr)`](https://numpy.org/doc/stable/reference/generated/numpy.ceil.html)
*   **Округление вниз (пол):** [`np.floor(arr)`](https://numpy.org/doc/stable/reference/generated/numpy.floor.html)

---

### 2.9.6 Работа с `NaN` и `inf` *(Пункт с inf можно найти в конце 10 лекции. Сгруппировал так из-за близости тем.)*

*   **Проверка на `NaN`:** [`np.isnan(arr)`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html)
*   **Проверка на бесконечность:** [`np.isinf(arr)`](https://numpy.org/doc/stable/reference/generated/numpy.isinf.html)

Обе функции возвращают булеву маску. NumPy обычно не выдает ошибок при вычислениях с `NaN`, а "распространяет" его дальше (например, `5 + np.nan` будет `nan`).

---

### 2.9.7 Параметр `out`

Многие функции NumPy принимают необязательный параметр `out`, который позволяет записать результат операции в уже существующий массив, вместо создания нового. Это помогает экономить память.

```python
arr1 = np.array([1, 2, 3])
arr2 = np.zeros_like(arr1) # Создаем массив-приемник той же формы

# Вместо arr2 = np.abs(arr1), делаем так:
np.abs(arr1, out=arr2) 
# Теперь arr2 содержит результат [1, 2, 3]
```

---

### 2.9.8-2.9.10 [Бинарные математические функции](https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs)

Эти функции выполняют поэлементные операции над двумя массивами. **Важно:** массивы должны быть одинаковой длины (или совместимы по правилам [broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)).

*   **Поэлементный максимум:** [`np.maximum(arr1, arr2)`](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html)
*   **Поэлементный минимум:** [`np.minimum(arr1, arr2)`](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html)

**Арифметические операции:**

*   **Сложение:** [`np.add(arr1, arr2)`](https://numpy.org/doc/stable/reference/generated/numpy.add.html) эквивалентно `arr1 + arr2`
*   **Вычитание:** [`np.subtract(arr1, arr2)`](https://numpy.org/doc/stable/reference/generated/numpy.subtract.html) эквивалентно `arr1 - arr2`
*   **Умножение:** [`np.multiply(arr1, arr2)`](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html) эквивалентно `arr1 * arr2`
*   **Деление:** [`np.divide(arr1, arr2)`](https://numpy.org/doc/stable/reference/generated/numpy.divide.html) эквивалентно `arr1 / arr2`

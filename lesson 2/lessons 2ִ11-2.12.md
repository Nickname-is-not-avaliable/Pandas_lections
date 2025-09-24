### 2.11 Логические функции и функция в функции, а еще where и статистика

---

### 2.11.1 [Поэлементное сравнение](https://numpy.org/doc/stable/reference/ufuncs.html#comparison-functions)

Для поэлементного сравнения двух массивов можно использовать как функции NumPy, так и стандартные операторы. Операторы почти всегда предпочтительнее из-за лучшей читаемости.

| Функция | Оператор | Описание |
| :--- | :---: | :--- |
| [`np.greater(arr1, arr2)`](https://numpy.org/doc/stable/reference/generated/numpy.greater.html) | `arr1 > arr2` | Больше |
| [`np.greater_equal(arr1, arr2)`](https://numpy.org/doc/stable/reference/generated/numpy.greater_equal.html)| `arr1 >= arr2`| Больше или равно |
| [`np.less(arr1, arr2)`](https://numpy.org/doc/stable/reference/generated/numpy.less.html) | `arr1 < arr2` | Меньше |
| [`np.less_equal(arr1, arr2)`](https://numpy.org/doc/stable/reference/generated/numpy.less_equal.html) | `arr1 <= arr2` | Меньше или равно |
| [`np.equal(arr1, arr2)`](https://numpy.org/doc/stable/reference/generated/numpy.equal.html) | `arr1 == arr2` | Равно |

Результатом любой из этих операций является **булев массив (маска)**.

---

### 2.11.3-2.11.5 Условная замена элементов: [`np.where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html)

Функция `np.where` — это мощный инструмент для поэлементной условной замены, аналог тернарного оператора.

**Синтаксис:**
`np.where(condition, x, y)`

*   `condition`: Булев массив (маска) или условие.
*   `x`: Значение, которое подставляется, если условие `True`.
*   `y`: Значение, которое подставляется, если условие `False`.

**Пример:**
Возвести в квадрат все положительные элементы массива, а остальные заменить нулём.
```python
arr = np.array([1, -2, 3, -4, 5])

# Если элемент > 0, берем arr**2, иначе — 0
result = np.where(arr > 0, arr ** 2, 0) 
# result -> [1, 0, 9, 0, 25]
```
Эта функция эффективно работает с массивами любой размерности.

---

### 2.11.6-2.11.8 [Статистические](https://numpy.org/doc/stable/reference/routines.statistics.html) и [агрегирующие](https://numpy.org/doc/stable/reference/routines.math.html#sums-products-differences) функции

Эти функции вычисляют одну сводную характеристику для всего массива или для его отдельных осей. Их можно вызывать как `np.function(arr)` или как метод `arr.function()`.

**Основные функции:**
*   [`sum()`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html): Сумма всех элементов.
*   [`mean()`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html): Среднее арифметическое.
*   [`min()`](https://numpy.org/doc/stable/reference/generated/numpy.min.html) / [`max()`](https://numpy.org/doc/stable/reference/generated/numpy.max.html): Минимальное / максимальное значение.
*   [`argmin()`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html) / [`argmax()`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html): Индекс минимального / максимального элемента.
*   [`std()`](https://numpy.org/doc/stable/reference/generated/numpy.std.html): Стандартное отклонение (показывает разброс данных).
*   [`var()`](https://numpy.org/doc/stable/reference/generated/numpy.var.html): Дисперсия (квадрат стандартного отклонения).

**Параметр `axis` для многомерных массивов:**
Этот параметр указывает, вдоль какой оси выполнять операцию.
*   **Без `axis` (по умолчанию):** функция применяется ко всему массиву, результат — одно число.
*   `axis=0`: Операция выполняется **вдоль столбцов**. Результат — массив, где каждый элемент — это результат операции для соответствующего столбца.
*   `axis=1`: Операция выполняется **вдоль строк**. Результат — массив, где каждый элемент — это результат операции для соответствующей строки.

---

### 2.11.9 Суммирование булевых массивов

При применении агрегирующих функций (например, [`.sum()`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html)) к булеву массиву, `True` интерпретируется как `1`, а `False` — как `0`.

Это очень удобный способ **подсчитать количество элементов**, удовлетворяющих условию.

**Пример:**
```python
arr = np.array([1, 7, 2, 8, 3, 9])

# Сколько элементов в массиве больше 5?
mask = arr > 5  # -> [False, True, False, True, False, True]
count = mask.sum()  # -> 0 + 1 + 0 + 1 + 0 + 1 = 3

# Можно записать в одну строку:
count = (arr > 5).sum() # Результат тот же
```

### 2.1 Зачем при изучении Pandas нужен Numpy?

---

**2.1.1-2.1.2 Сравнение списка Python и массива NumPy**
(Python возводит в квадрат 1 000 000 элементов за 986 ms, а NumPy — за 53.3 ms).

---

**2.1.3 Установка и проверка NumPy:**
```shell
pip install numpy
pip show numpy
```

**2.1.4 Импорт NumPy:**
```python
import numpy as np
```

---

**2.1.5 Создание двумерного массива [`np.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html):**
```python
arr = np.array([[element1, element2, ..., elementN], [element1, element2, ..., elementN]])
```
Для больших размерностей нужно просто добавить больше квадратных скобок.

*   **Длина одномерного массива:** [`len(array)`](https://docs.python.org/3/library/functions.html#len)
*   **Форма (размерности) многомерного:** [`array.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html)
*   **Количество измерений:** [`array.ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html)

**2.1.6 Тип данных:**
*   **Узнать тип данных в массиве:** [`array.dtype`](https://numpy.org/doc/stable/reference/arrays.dtypes.html)

Тип данных подбирается автоматически. Строгая типизация делает массивы очень быстрыми.

---

**2.1.7 Инициализация нулями [`np.zeros`](https://numpy.org/doc/stable/user/basics.creation.html):**
```python
# Создает массив указанной формы, заполненный нулями
arr = np.zeros((n, m, ..., z))
```
Кортеж `(n, m, ..., z)` задает форму массива. Например, `(2, 3)` создаст матрицу 2x3.

**2.1.8 Инициализация единицами [`np.ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html):**
```python
# Аналогично, но с единицами
arr = np.ones((n, m, ..., z))
```

**2.1.9 Инициализация кастомным (своим) значением [`np.full`](https://numpy.org/doc/stable/reference/generated/numpy.full.html):**
```python
# Заполняет массив значением 'x'
arr = np.full((n, m, ..., z), x)
```
`x` — это значение для заполнения.

*Вопрос: зачем нужны `zeros` и `ones`?*

**2.1.10-2.1.11 Инициализация элементами по порядку[`np.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html):**
```python
# Создает массив с элементами от 0 до n-1
arr = np.arange(n)
```
`n` — длина массива.

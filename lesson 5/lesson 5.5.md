### 5.5 Создаём матрицы фиктивных переменных

---
#### 5.5.1-5.5.2 Что такое фиктивные переменные?

**Фиктивные переменные (или [One-Hot Encoding](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html))** — это техника преобразования категориальных данных (текстовых меток) в числовой формат, понятный для моделей машинного обучения.

**Принцип:**
1.  Берется столбец с категориальными данными (например, "Город").
2.  Определяются все уникальные значения в этом столбце (например, 'NY', 'LA', 'Chicago').
3.  Для каждого уникального значения создается **новый бинарный столбец**.
4.  Для каждой строки в исходных данных ставится `1` в том новом столбце, который соответствует ее категории, и `0` во всех остальных.

**Проще говоря, мы отвечаем на вопрос "Эта строка относится к категории X?" с помощью `1` (да) или `0` (нет).**

**--- Пример "до" и "после" ---**

**ДО:**
```
   city
0    NY
1    LA
2    NY
```
**ПОСЛЕ:** (Столбец `city` превратился в два новых столбца)
```
   city_LA  city_NY
0        0        1  (Это NY? Да. Это LA? Нет.)
1        1        0  (Это NY? Нет. Это LA? Да.)
2        0        1  (Это NY? Да. Это LA? Нет.)
```
---
#### 5.5.3-5.5.4 Создание фиктивных переменных с [`pd.get_dummies`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html)

**--- Исходные данные ---**
```python
df_city = pd.DataFrame({
    'id': [101, 102, 103],
    'city': ['NY', 'LA', 'NY']
})
print("Исходный DataFrame:")
print(df_city)
```
**Вывод:**
```
Исходный DataFrame:
    id city
0  101   NY
1  102   LA
2  103   NY
```

**--- Полный цикл: [`get_dummies`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html), [`join`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html), [`drop`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html) ---**
```python
# 1. Создаем фиктивную матрицу, добавляя к новым столбцам префикс 'City'
dummies = pd.get_dummies(df_city['city'], prefix='City')

# 2. Присоединяем ее к исходному DataFrame
df_with_dummies = df_city.join(dummies)

# 3. Удаляем исходный категориальный столбец 'city'
df_final = df_with_dummies.drop('city', axis=1)


print("\nФинальный DataFrame (готовый для модели):")
print(df_final)
```
**Вывод:**
```
Финальный DataFrame (готовый для модели):
    id  City_LA  City_NY
0  101        0        1
1  102        1        0
2  103        0        1
```
---
#### 5.5.5-5.5.7 Работа с несколькими категориями в одной ячейке

**--- Исходные данные ---**
```python
df_genres = pd.DataFrame({
    'movie_id': [1, 2, 3],
    'genres': ['Action|Adventure', 'Comedy', 'Action|Thriller']
})
print("Исходный DataFrame с жанрами:")
print(df_genres)
```
**Вывод:**
```
Исходный DataFrame с жанрами:
   movie_id            genres
0         1  Action|Adventure
1         2            Comedy
2         3   Action|Thriller
```
---
**Способ 1: Использование [`Series.str.get_dummies`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.get_dummies.html) (Рекомендуемый)**

Для решения этой задачи в Pandas существует специальный, очень удобный и быстрый метод: [`.str.get_dummies()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.get_dummies.html). Он автоматически разделяет строку по указанному символу и создает фиктивную матрицу. Этот способ является предпочтительным.

```python
# 1. Создаем фиктивную матрицу, указав '|' в качестве разделителя
genre_dummies = df_genres['genres'].str.get_dummies(sep='|')

# 2. Добавляем префикс и присоединяем к исходным данным
df_final = df_genres.join(genre_dummies.add_prefix('Genre_')).drop('genres', axis=1)

print("\nФинальный DataFrame (способ .str.get_dummies):")
print(df_final)
```
**Вывод:**
```
Финальный DataFrame (способ .str.get_dummies):
   movie_id  Genre_Action  Genre_Adventure  Genre_Comedy  Genre_Thriller
0         1             1                1             0               0
1         2             0                0             1               0
2         3             1                0             0               1
```
---
**Способ 2: Ручной парсинг (для понимания)**

Хотя использование `.str.get_dummies()` является лучшей практикой, понимание ручного процесса может быть полезным. Этот метод включает создание пустой матрицы и ее заполнение в цикле.

**Объяснение ключевых функций:**
*   **[`.columns.get_indexer(labels)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.get_indexer.html)**: Эта функция принимает список меток (`labels`) и возвращает список **числовых позиций (индексов)** этих меток в `df.columns`. Например, если `df.columns` это `['A', 'B', 'C']`, то `df.columns.get_indexer(['C', 'A'])` вернет `[2, 0]`.
*   **[`.add_prefix(prefix_str)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.add_prefix.html)**: Этот метод просто добавляет строку `prefix_str` в начало **каждого имени столбца** в `DataFrame`.

```python
# 1. Получаем все уникальные жанры и создаем пустую матрицу из нулей
all_genres = set(g for s in df_genres['genres'] for g in s.split('|'))
genre_dummies_manual = pd.DataFrame(0, index=df_genres.index, columns=sorted(list(all_genres)))

# 2. Заполняем матрицу
for i, genres_str in enumerate(df_genres['genres']):
    col_indices = genre_dummies_manual.columns.get_indexer(genres_str.split('|'))
    genre_dummies_manual.iloc[i, col_indices] = 1

# 3. Добавляем префикс и присоединяем
df_final_manual = df_genres.join(genre_dummies_manual.add_prefix('Genre_')).drop('genres', axis=1)

print("\nФинальный DataFrame (ручной способ):")
print(df_final_manual)
```
**Вывод:** (Результат идентичен)
```
Финальный DataFrame (ручной способ):
   movie_id  Genre_Action  Genre_Adventure  Genre_Comedy  Genre_Thriller
0         1             1                1             0               0
1         2             0                0             1               0
2         3             1                0             0               1
```
---
#### 5.5.8 Использование [`get_dummies`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html) с [`cut`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html)

Это очень распространенный прием для преобразования непрерывных числовых данных (например, возраст) в категориальные фиктивные переменные.

**--- Исходные данные ---**
```python
df_age = pd.DataFrame({'age': [15, 25, 40, 65, 22], 'revenue': [100, 500, 1000, 1500, 600]})
print("Исходный DataFrame с возрастом:")
print(df_age)
```
**Вывод:**
```
Исходный DataFrame с возрастом:
   age  revenue
0   15      100
1   25      500
2   40     1000
3   65     1500
4   22      600
```
---
**--- Применение `cut` и `get_dummies` с последующим объединением ---**
```python
# 1. Разбиваем возраст на категории
bins = [0, 17, 30, 60, 100]
labels = ['Child', 'Young Adult', 'Adult', 'Senior']
age_categories = pd.cut(df_age['age'], bins=bins, labels=labels)

# 2. Создаем фиктивные переменные из этих категорий
age_dummies = pd.get_dummies(age_categories, prefix='Age')

# 3. Присоединяем фиктивные переменные и удаляем исходный столбец 'age'
df_final = df_age.join(age_dummies).drop('age', axis=1)

print("\nФинальный DataFrame с возрастными группами:")
print(df_final)
```
**Вывод:**
```
Финальный DataFrame с возрастными группами:
   revenue  Age_Child  Age_Young Adult  Age_Adult  Age_Senior
0      100          1                0          0           0
1      500          0                1          0           0
2     1000          0                0          1           0
3     1500          0                0          0           1
4      600          0                1          0           0
```

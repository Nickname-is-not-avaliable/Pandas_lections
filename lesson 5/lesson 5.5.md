### 5.5 Создаём матрицы фиктивных переменных (One-Hot Encoding)

---
#### 5.5.1-5.5.2 Что такое фиктивные переменные?

**Фиктивные переменные (или One-Hot Encoding)** — это техника преобразования категориальных данных (текстовых меток) в числовой формат, понятный для моделей машинного обучения.

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
#### 5.5.3-5.5.4 Создание фиктивных переменных с `pd.get_dummies`

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

**--- Полный цикл: `get_dummies`, `join`, `drop` ---**
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
**--- Ручное создание, присоединение и очистка ---**
Здесь нет встроенной функции, поэтому мы делаем это в несколько шагов.

**Объяснение ключевых функций:**
*   **`.columns.get_indexer(labels)`**: Эта функция принимает список меток (`labels`) и возвращает список **числовых позиций (индексов)** этих меток в `df.columns`. Например, если `df.columns` это `['A', 'B', 'C']`, то `df.columns.get_indexer(['C', 'A'])` вернет `[2, 0]`. Это очень удобно для использования с `.iloc`, так как позволяет быстро найти нужные столбцы по их именам.
*   **`.add_prefix(prefix_str)`**: Этот метод просто добавляет строку `prefix_str` в начало **каждого имени столбца** в `DataFrame`. Например, `['Action', 'Comedy']` станет `['Genre_Action', 'Genre_Comedy']`.

```python
# 1. Получаем все уникальные жанры и создаем пустую матрицу из нулей
all_genres = set(g for s in df_genres['genres'] for g in s.split('|'))
genre_dummies = pd.DataFrame(0, index=df_genres.index, columns=sorted(list(all_genres)))

# 2. Заполняем матрицу
for i, genres_str in enumerate(df_genres['genres']):
    # Находим числовые позиции столбцов, соответствующих жанрам в текущей строке
    col_indices = genre_dummies.columns.get_indexer(genres_str.split('|'))
    # По этим позициям вставляем 1
    genre_dummies.iloc[i, col_indices] = 1

# 3. Добавляем префикс и присоединяем к исходным данным, удаляя старый столбец
df_final = df_genres.join(genre_dummies.add_prefix('Genre_')).drop('genres', axis=1)

print("\nФинальный DataFrame с фиктивными переменными для жанров:")
print(df_final)
```
**Вывод:**
```
Финальный DataFrame с фиктивными переменными для жанров:
   movie_id  Genre_Action  Genre_Adventure  Genre_Comedy  Genre_Thriller
0         1             1                1             0               0
1         2             0                0             1               0
2         3             1                0             0               1
```
---
#### 5.5.8 Использование `get_dummies` с `cut`

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

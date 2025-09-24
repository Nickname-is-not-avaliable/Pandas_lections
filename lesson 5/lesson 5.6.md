### 5.6 [Работа со строками](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html) - проще чем кажется!

---
#### 5.6.1-5.6.3 [`.str` Accessor](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.html) vs [`.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html)

Для выполнения векторизованных строковых операций над `Series` (т.е. применения операции к каждому элементу) используется специальный accessor `.str`.

**Ключевое преимущество `.str`:** он автоматически обрабатывает пропущенные значения (`NaN`), не вызывая ошибок. `.map()` требует дополнительной обработки `NaN`.

**--- Исходные данные ---**
```python
df = pd.DataFrame({
    'product_code': ['AB-123', 'cd-456', np.nan, 'AB-789'],
    'description': ['Apple', 'banana', 'Cherry', 'Avocado']
})

print("Исходный DataFrame:")
print(df)
```
**Вывод:**
```
Исходный DataFrame:
  product_code description
0       AB-123       Apple
1       cd-456      banana
2          NaN      Cherry
3       AB-789     Avocado
```
---
**--- Применение функций ---**
```python
# 1. Замена через .str.replace() (рекомендуемый способ)
# NaN пропускается автоматически
print("\nРезультат .str.replace('-','_'):")
print(df['product_code'].str.replace('-', '_'))

# 2. Попытка замены через .map() с простой функцией (вызовет ошибку)
def replace_dash(x):
    return x.replace('-', '_')

try:
    df['product_code'].map(replace_dash)
except Exception as e:
    print(f"\nОшибка при .map() без обработки NaN: {type(e).__name__}")
    
# 3. Замена через .map() с обработкой NaN (правильный, но более громоздкий способ)
def safe_replace_dash(x):
    if pd.isna(x):
        return x
    return x.replace('-', '_')
    
print("\nРезультат .map() с безопасной функцией:")
print(df['product_code'].map(safe_replace_dash))
```
**Вывод:**
```
Результат .str.replace('-','_'):
0    AB_123
1    cd_456
2       NaN
3    AB_789
Name: product_code, dtype: object

Ошибка при .map() без обработки NaN: AttributeError

Результат .map() с безопасной функцией:
0    AB_123
1    cd_456
2       NaN
3    AB_789
Name: product_code, dtype: object
```

---
#### 5.6.4-5.6.6 [Основные строковые методы](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#string-methods)

**--- Исходные данные те же ---**
```python
print("Исходный DataFrame:")
print(df)
```
**Вывод:**
```
Исходный DataFrame:
  product_code description
0       AB-123       Apple
1       cd-456      banana
2          NaN      Cherry
3       AB-789     Avocado
```
---
**--- Примеры методов ---**
```python
# 1. Изменение регистра
print("\n.str.upper():\n", df['description'].str.upper())
print("\n.str.capitalize():\n", df['description'].str.capitalize())

# 2. Слайсинг и получение элемента по индексу
print("\n.str[0] (первая буква):\n", df['description'].str[0])
print("\n.str[:2] (первые два символа):\n", df['product_code'].str[:2])

# 3. Фильтрация с помощью .str.contains()
# Находим все строки, где в 'description' есть 'a' (без учета регистра)
mask_contains = df['description'].str.contains('a', case=False)
print("\nDataFrame, где description содержит 'a':")
print(df[mask_contains])

# 4. Фильтрация с помощью .str.startswith()
# Находим все строки, где 'product_code' начинается с 'AB'
# na=False говорит, что NaN нужно считать как False в маске
mask_starts = df['product_code'].str.startswith('AB', na=False)
print("\nDataFrame, где product_code начинается с 'AB':")
print(df[mask_starts])

# 5. Фильтрация с помощью .str.endswith()
mask_ends = df['product_code'].str.endswith('456', na=False)
print("\nDataFrame, где product_code заканчивается на '456':")
print(df[mask_ends])
```
**Вывод:**
```
.str.upper():
 0      APPLE
1     BANANA
2     CHERRY
3    AVOCADO
Name: description, dtype: object

.str.capitalize():
 0      Apple
1     Banana
2     Cherry
3    Avocado
Name: description, dtype: object

.str[0] (первая буква):
 0    A
1    b
2    C
3    A
Name: description, dtype: object

.str[:2] (первые два символа):
 0     AB
1     cd
2    NaN
3     AB
Name: product_code, dtype: object

DataFrame, где description содержит 'a':
  product_code description
1       cd-456      banana
3       AB-789     Avocado

DataFrame, где product_code начинается с 'AB':
  product_code description
0       AB-123       Apple
3       AB-789     Avocado

DataFrame, где product_code заканчивается на '456':
  product_code description
1       cd-456      banana
```

### 4.5 Знакомимся с форматами [HTML](https://developer.mozilla.org/ru/docs/Web/HTML), [XML](https://developer.mozilla.org/ru/docs/Web/XML/XML_Introduction), [PICKLE](https://docs.python.org/3/library/pickle.html), [HDF5](https://www.h5py.org/)

---
#### 4.5.1-4.5.3 Формат [HTML](https://developer.mozilla.org/ru/docs/Web/HTML) и чтение таблиц

**1. Структура HTML-таблицы**
HTML (HyperText Markup Language) — язык разметки для веб-страниц. Таблицы в HTML имеют следующую структуру:
*   `<table>`: Контейнер для всей таблицы.
*   `<thead>`: (Опционально) Секция заголовка таблицы.
*   `<tbody>`: (Опционально) Тело таблицы с основными данными.
*   `<tr>`: (Table Row) Определяет строку в таблице.
*   `<th>`: (Table Header) Определяет ячейку-заголовок (обычно в `<thead>`).
*   `<td>`: (Table Data) Определяет ячейку с данными.

**--- Пример файла `table.html` ---**
```html
<!DOCTYPE html>
<html>
<head>
<title>Пример таблицы</title>
</head>
<body>

<h2>Данные о продуктах</h2>
<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Product</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>101</td>
      <td>Apple</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td>102</td>
      <td>Banana</td>
      <td>0.59</td>
    </tr>
  </tbody>
</table>

</body>
</html>
```

**2. Чтение HTML с помощью Pandas [`pd.read_html()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html)**
Pandas может автоматически находить и считывать все таблицы (`<table>`) со страницы.

**--- Установка необходимых библиотек ---**
```bash
pip install lxml html5lib beautifulsoup4
```
**--- Чтение данных ---**
```python
# pd.read_html возвращает СПИСОК всех найденных на странице DataFrame'ов
list_of_dfs = pd.read_html('table.html')

# В нашем случае на странице только одна таблица, поэтому берем первый элемент
df_html = list_of_dfs[0]

print("DataFrame, прочитанный из HTML:")
print(df_html)
```
**Вывод:**
```
DataFrame, прочитанный из HTML:
    ID Product  Price
0  101   Apple   0.99
1  102  Banana   0.59
```
---
#### 4.5.4 Формат [XML](https://developer.mozilla.org/ru/docs/Web/XML/XML_Introduction)

XML (eXtensible Markup Language) — это формат, который хранит данные в древовидной структуре с помощью пользовательских тегов.

**--- Пример файла `data.xml` ---**
```xml
<data>
    <record>
        <id>1</id>
        <name>Alice</name>
        <age>25</age>
    </record>
    <record>
        <id>2</id>
        <name>Bob</name>
        <age>30</age>
    </record>
</data>
```

**Способ 1: Использование [`pd.read_xml`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_xml.html) (рекомендуемый, Pandas >= 1.3)**
Начиная с версии 1.3.0, Pandas включает встроенную функцию для чтения простых XML-файлов.

```python
# Для этого способа также требуется lxml
df_xml_easy = pd.read_xml('data.xml')

print("DataFrame, созданный с помощью pd.read_xml:")
print(df_xml_easy)
```
**Вывод:**
```
DataFrame, созданный с помощью pd.read_xml:
   id   name  age
0   1  Alice   25
1   2    Bob   30
```

**Способ 2: Ручной парсинг с [`lxml`](https://lxml.de/index.html) (для старых версий Pandas или сложных случаев)**
Этот метод дает больше контроля, но требует больше кода.

```python
from lxml import objectify

# 1. Парсим XML-файл в специальный объект
parsed_xml = objectify.parse('data.xml')

# 2. Получаем корневой элемент дерева (<data>)
root = parsed_xml.getroot()

# 3. Проходимся по дочерним элементам (<record>)
data_list = []
for record_element in root.getchildren():
    row_dict = {}
    # 4. Внутри каждого <record> проходимся по его дочерним элементам (<id>, <name>, <age>)
    for child in record_element.getchildren():
        # child.tag -> 'id', 'name', 'age'
        # child.pyval -> 1, 'Alice', 25
        row_dict[child.tag] = child.pyval
    data_list.append(row_dict)

# 5. Создаем DataFrame из списка словарей
df_xml_manual = pd.DataFrame(data_list)

print("\nDataFrame, созданный из XML вручную:")
print(df_xml_manual)
```
**Вывод:**
```
DataFrame, созданный из XML вручную:
   id   name  age
0   1  Alice   25
1   2    Bob   30
```
---
#### 4.5.5-4.5.6 Бинарный формат [Pickle](https://docs.python.org/3/library/pickle.html)

**Pickle** — это стандартный для Python формат бинарной сериализации. Он сохраняет объекты Python (включая DataFrame с типами данных и индексами) в байтовом виде.
*   **Плюсы:** Очень быстро, сохраняет всё "как есть".
*   **Минусы:** Работает только в Python, может быть несовместим между разными версиями Python. Это настолько существенный минус, что pickle почти не используют.

**--- Исходные данные и сохранение/чтение ---**
```python
df_pickle = pd.DataFrame({'a': [1, 2, 3], 'b': ['x', 'y', 'z']})

# Сохранение в pickle-файл
df_pickle.to_pickle('my_data.pkl')

# Чтение из pickle-файла
df_loaded_pickle = pd.read_pickle('my_data.pkl')

print("DataFrame, загруженный из Pickle:")
print(df_loaded_pickle)
```
---
#### 4.5.7-4.5.8 Бинарный формат [HDF5](https://www.h5py.org/)

**HDF5 (Hierarchical Data Format)** — это высокопроизводительный бинарный формат, предназначенный для хранения больших и сложных наборов данных.

**1. Использование `HDFStore` (для нескольких объектов)**
`HDFStore` работает как словарь, позволяя хранить несколько `DataFrame` в одном `.h5` файле под разными ключами.

```python
# Создаем два DataFrame'а
df_h5_1 = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
df_h5_2 = pd.DataFrame({'X': [1, 2, 3]})

# Создаем "хранилище"
store = pd.HDFStore('my_store.h5')

# Записываем DataFrame'ы в хранилище под ключами
store.put('data1', df_h5_1, format='table')
store.put('data2', df_h5_2)

# Можно выборочно прочитать данные
read_data1 = store.select('data1', where='A > 0')

store.close() # Важно закрывать хранилище

print("Данные, прочитанные из HDF5 с условием (A > 0):")
print(read_data1)
```

**2. Прямое сохранение: [`to_hdf`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_hdf.html) и [`read_hdf`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_hdf.html)**
Более простой способ для сохранения одного `DataFrame`.

```python
# Сохранение
df_h5_1.to_hdf('single_df.h5', key='my_data', format='table')

# Чтение
df_loaded_h5 = pd.read_hdf('single_df.h5', key='my_data')
```

**3. Отличия `format='table'` от `format='fixed'`**

| Характеристика | `format='table'` (Таблица) | `format='fixed'` (Фиксированный, по умолчанию) |
| :--- | :--- | :--- |
| **Скорость** | Медленнее | **Быстрее** |
| **Запросы** | **Поддерживает** (можно фильтровать данные при чтении, `where=...`) | Не поддерживает |
| **Дозапись** | **Поддерживает** (можно добавлять новые строки, `append=True`) | Не поддерживает |
| **Применение** | Большие наборы данных, которые нужно частично считывать или дополнять. | Быстрое сохранение и чтение небольших и средних `DataFrame` целиком. |

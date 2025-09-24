# Конспекты лекций по курсу ["Основы Pandas для начинающих"](https://stepik.org/course/120014/promo)

👋 Добро пожаловать!

**Важное примечание:** примеры кода в этих конспектах отличаются от тех, что были в лекциях. Я создавал их самостоятельно.

Этот репозиторий содержит мои личные конспекты, которые я веду по мере прохождения курса. Вся демо-часть курса законспектирована. А также самые интересные на мой взгляд задачки (из 4 части) сохранены. Пользуйтесь!

## Структура курса

*   **Часть 1: Вводная** Информация о курсе.
*   **Часть 2: Основы NumPy** — Создание, индексация и математические операции.
*   **Часть 3: Введение в Pandas** — Объекты Series и DataFrame, индексация, арифметика и базовые операции.
*   **Часть 4: Pandas: работа с источниками данных**
*   **Часть 5: Pandas: чистка и подготовка данных к анализу**

---

### 📘 Содержание Части 2: Основы NumPy

Первая часть полностью посвящена библиотеке **[NumPy](https://numpy.org/doc/stable/)** — фундаменту для всех вычислений в анализе данных и машинном обучении на Python.

**Ключевые темы, рассмотренные в конспекте:**

*   **Создание массивов:** [`np.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html), [`np.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html), [`np.ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html), [`np.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html) и другие.
*   **Атрибуты массива:** [`.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html), [`.ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html), [`.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dtype.html).
*   **Типы данных:** Явное и неявное приведение типов с помощью [`.astype()`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html).
*   **Векторизация:** Отличие арифметических операций в NumPy от стандартных списков Python.
*   **[Индексация и срезы](https://numpy.org/doc/stable/user/basics.indexing.html):**
    *   Базовые срезы (`arr[a:n]`).
    *   Многомерная индексация (`arr[x, y]`).
    *   Булевы маски и логические операции.
    *   "Причудливая" индексация (`Fancy indexing`).
*   **Манипуляции с формой:** [`.reshape()`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html), [`.T`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html) (транспонирование).
*   **[Универсальные функции (ufunc)](https://numpy.org/doc/stable/reference/ufuncs.html):** Математические, статистические и агрегирующие операции ([`np.sqrt`](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html), [`.sum()`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html), [`.mean()`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html), [`.max()`](https://numpy.org/doc/stable/reference/generated/numpy.max.html) и т.д.).
*   **Основы [линейной алгебры](https://numpy.org/doc/stable/reference/routines.linalg.html):** Матричное умножение, определитель, обратная матрица.
*   **Генерация случайных данных:** Модуль [`np.random`](https://numpy.org/doc/stable/reference/random/index.html).

### 📘 Содержание Части 3: Введение в Pandas

Этот раздел посвящен основам библиотеки **[Pandas](https://pandas.pydata.org/pandas-docs/stable/)**, ключевому инструменту для анализа данных в Python.

*   **Объект [`Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) (1D):**
    *   Создание из списков и словарей.
    *   Индексация (включая неуникальные индексы).
    *   Работа с пропущенными данными ([`NaN`](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html), [`isnull`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isnull.html)).
    *   Автоматическое выравнивание данных по индексу при арифметических операциях.
*   **Объект [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) (2D):**
    *   Создание из словарей, в том числе вложенных.
    *   Гибкое управление столбцами ([`.columns`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html)) и строками ([`.index`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.index.html)).
    *   Удаление данных (`del`, [`.drop`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)).
    *   Транспонирование ([`.T`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.T.html)).
*   **[Индексация и выбор данных](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html):**
    *   Базовый выбор `[]` (для столбцов, срезов строк и масок).
    *   Точный выбор по меткам: [`.loc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html).
    *   Точный выбор по позициям: [`.iloc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html).
    *   Быстрый скалярный доступ: [`.at`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.at.html) и [`.iat`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iat.html).
*   **Ключевые операции:**
    *   Изменение индексов: [`.reindex`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reindex.html).
    *   Сортировка: [`.sort_index()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_index.html) и [`.sort_values()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html).
    *   Арифметика с заполнением пропусков ([`.add`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.add.html) с `fill_value`).
    *   Операции между `DataFrame` и `Series` (broadcasting).
*   **Описательные статистики и уникальные значения:**
    *   Агрегирующие функции ([`.sum`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html), [`.mean`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html)) и их параметры (`axis`, `skipna`).
    *   Сводная статистика: [`.describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html).
    *   Подсчет уникальных значений: [`.value_counts()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html).
    *   Фильтрация по вхождению: [`.isin()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html).

---

### 📘 Содержание Части 4: Pandas: работа с источниками данных

Этот раздел посвящен чтению и записи данных в самых распространенных форматах.

*   **Работа с CSV:**
    *   Чтение с помощью [`pd.read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) и его ключевые параметры: `sep`, `header`, `names`, `index_col`, `skiprows`, `nrows`.
    *   Обработка пропущенных значений при чтении: `na_values`, `keep_default_na`.
    *   Обработка больших файлов с помощью `chunksize`.
    *   Запись данных с помощью [`df.to_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html).
*   **Работа с JSON:**
    *   Чтение ([`pd.read_json()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html)) и запись ([`df.to_json()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html)).
    *   Параметр `orient` для контроля структуры JSON.
    *   Получение JSON-данных из веб-источников по URL с помощью библиотеки [`requests`](https://requests.readthedocs.io/en/latest/).
*   **Чтение HTML и XML:**
    *   Чтение таблиц с веб-страниц с помощью [`pd.read_html()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html).
    *   Чтение данных из XML-файлов ([`pd.read_xml()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_xml.html) или ручной парсинг с [`lxml`](https://lxml.de/)).
*   **Бинарные форматы: Pickle и HDF5:**
    *   Быстрое сохранение/чтение объектов Python с помощью [`pickle`](https://docs.python.org/3/library/pickle.html).
    *   Работа с высокопроизводительным форматом `HDF5` для больших наборов данных ([`HDFStore`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.HDFStore.html), [`to_hdf`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_hdf.html)/[`read_hdf`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_hdf.html)).
*   **Работа с Excel:**
    *   Чтение листов из `.xlsx` файлов с помощью [`pd.read_excel()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) (`sheet_name`, `header`).
    *   Запись одного или нескольких `DataFrame` в один Excel-файл с помощью [`pd.ExcelWriter`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.ExcelWriter.html).
*   **Работа с базами данных:**
    *   Чтение данных из БД с помощью [`pd.read_sql()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html) и библиотеки [`SQLAlchemy`](https://www.sqlalchemy.org/).
    *   Запись `DataFrame` в SQL-таблицу с помощью [`df.to_sql()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html) и управление существующими таблицами (`if_exists`).

---

### 📘 Содержание Части 5: Pandas: чистка и подготовка данных к анализу

Этот раздел посвящен ключевым техникам предобработки данных, которые необходимы для подготовки данных к анализу и моделированию.

*   **[Работа с пропущенными значениями](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html):**
    *   Обнаружение пропусков: [`.isnull()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isnull.html), [`.notnull()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.notnull.html).
    *   Удаление пропусков: [`.dropna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html) с параметрами `axis`, `how`, `thresh`.
    *   Заполнение пропусков: [`.fillna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html) со значениями, словарями, методами (`ffill`, `bfill`) и статистиками ([`.mean()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html)).
*   **[Удаление дубликатов](https://pandas.pydata.org/pandas-docs/stable/user_guide/duplicates.html):**
    *   Обнаружение дублей: [`.duplicated()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html).
    *   Удаление дублей: [`.drop_duplicates()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html) с параметрами `subset` и `keep`.
*   **Преобразование данных:**
    *   Замена значений: [`.replace()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html).
    *   Переименование индексов и столбцов: [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html), [`.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html).
    *   Применение функций к данным: [`.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html).
*   **[Дискретизация и группировка](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#grouping-and-discretization):**
    *   Разбивка на интервалы: [`pd.cut()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html) для группировки по заданным границам.
    *   Разбивка по квантилям: [`pd.qcut()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.qcut.html) для создания групп с равным количеством элементов.
*   **Обнаружение и обработка выбросов:**
    *   Идентификация с помощью [`.describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) и булевых масок.
    *   Замена или ограничение выбросов с помощью [`.clip()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.clip.html).
    *   Перемешивание и случайная выборка: [`np.random.permutation()`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.permutation.html), [`.take()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.take.html), [`.sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html).
*   **Создание фиктивных переменных (One-Hot Encoding):**
    *   Автоматическое создание с помощью [`pd.get_dummies()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html).
    *   Создание для ячеек с несколькими категориями с помощью [`.str.get_dummies()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.get_dummies.html).
*   **[Векторизованные строковые операции](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html):**
    *   Использование accessor'а [`.str`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.html) для безопасной работы со строками.
    *   Методы [`.str.replace()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html), [`.str.contains()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html), [`.str.startswith()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.startswith.html), [`.str.upper()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.upper.html) и другие.
 
---

## Как использовать

Вы можете свободно просматривать файлы прямо в браузере или скачать репозиторий к себе на компьютер для локального доступа.

Для того чтобы скачать репозиторий с помощью `git`, вам сначала нужно его установить.

1.  **Установите Git:** Скачайте и установите его с [официального сайта git-scm.com](https://git-scm.com/downloads). Или в командной строке:

    ```Bash
    winget install --id Git.Git -e --source winget
    ```

2.  **Клонируйте репозиторий:** Откройте терминал (командную строку), перейдите в папку, куда хотите сохранить проект, и выполните команду:

    ```bash
    git clone https://github.com/Nickname-is-not-avaliable/Pandas_lections
    ```

### Предложения и исправления

Если вы заметили ошибку, опечатку или у вас есть предложение, как улучшить конспект, — смело создавайте **Issue** или **Pull Request**. Буду рад любой помощи.

### 4.3 Учимся читать большие файлы кусочками

---
#### 4.3.1-4.3.3 Итеративная обработка больших файлов (`chunksize`)

Для обработки файлов, которые не помещаются в оперативную память, `pd.read_csv` имеет параметр `chunksize`. Он позволяет читать файл не целиком, а последовательными "кусками" заданного размера.

При использовании `chunksize` функция возвращает не `DataFrame`, а специальный объект-итератор (`TextFileReader`), который нужно обрабатывать в цикле.

**Пример: Подсчет частоты клиентов в большом файле**

**--- Исходные данные (`client_data.csv`) ---**
```csv
id,client,value
1,apple,100
2,google,150
3,apple,200
4,msft,50
5,google,250
6,apple,300
```
**--- Чтение и обработка по частям ---**
```python
# Создаем итератор, который будет возвращать DataFrame'ы по 2 строки
chunk_iterator = pd.read_csv('client_data.csv', chunksize=2)

# Инициализируем пустую Series для хранения итоговых подсчетов
total_counts = pd.Series([], dtype=int)

print("--- Обработка файла по частям ---")
for i, chunk_df in enumerate(chunk_iterator):
    print(f"\nЧасть {i+1}:")
    print(chunk_df)
    
    # Считаем value_counts для текущей части
    chunk_counts = chunk_df['client'].value_counts()
    
    # Добавляем к общему итогу. fill_value=0 важен для первого добавления
    total_counts = total_counts.add(chunk_counts, fill_value=0)

print("\n--- Итоговый подсчет по всем частям ---")
print(total_counts)
```
**Вывод:**
```
--- Обработка файла по частям ---

Часть 1:
   id  client  value
0   1   apple    100
1   2  google    150

Часть 2:
   id client  value
2   3  apple    200
3   4   msft     50

Часть 3:
   id  client  value
4   5  google    250
5   6   apple    300

--- Итоговый подсчет по всем частям ---
apple     3.0
google    2.0
msft      1.0
dtype: float64
```
---
#### 4.3.4-4.3.8 Сохранение `DataFrame` в CSV (`.to_csv()`)

Метод `.to_csv()` позволяет записывать содержимое `DataFrame` в файл.

**--- Исходные данные для сохранения ---**
```python
df_to_save = pd.DataFrame({
    'city': ['NY', 'LA', 'Chicago'],
    'temp': [25, 30, np.nan],
    'humidity': [60, 45, 65]
}, index=['day1', 'day2', 'day3'])

print("Исходный DataFrame для сохранения:")
print(df_to_save)
```
**Вывод:**
```
Исходный DataFrame для сохранения:
         city  temp  humidity
day1       NY  25.0        60
day2       LA  30.0        45
day3  Chicago   NaN        65
```
---
**Примеры использования параметров `.to_csv()`**

**1. `sep` — изменение разделителя**
```python
# Сохраняем с разделителем ';'
df_to_save.to_csv('output_sep.csv', sep=';')
# Содержимое 'output_sep.csv':
# ;city;temp;humidity
# day1;NY;25.0;60
# day2;LA;30.0;45
# day3;Chicago;;65
```

**2. `na_rep` — замена `NaN` при записи**
```python
# Записываем NaN как 'MISSING'
df_to_save.to_csv('output_na_rep.csv', na_rep='MISSING')
# Содержимое 'output_na_rep.csv':
# ,city,temp,humidity
# day1,NY,25.0,60
# day2,LA,30.0,45
# day3,Chicago,MISSING,65
```

**3. `index`, `header`, `columns` — управление структурой файла**
Эти параметры позволяют точно контролировать, что именно будет записано.

```python
# Сохраняем только столбцы 'city' и 'humidity',
# без индекса и без заголовков
df_to_save.to_csv(
    'output_custom.csv',
    index=False,          # Не записывать индекс ('day1', 'day2'...)
    header=False,         # Не записывать названия столбцов
    columns=['city', 'humidity'] # Указываем, какие столбцы сохранить
)
# Содержимое 'output_custom.csv':
# NY,60
# LA,45
# Chicago,65
```

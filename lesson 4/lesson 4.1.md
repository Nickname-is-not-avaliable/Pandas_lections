4.1.1-4.1.5 Загрузка данных в DataFrame
Текстовый файл csv - comma separated values
Столбцы разделяются запятой, а строчки разделяются с помощью \n
f = open('file.csv')
matrix = []
for line in f:
  lst = line.split(',')
  matrix.append(lst)
f.close
#предположим, в данных 3 колонки a, b и c
df = pd.DataFrame(matrix, columns = ['a','b','c'])

Это прописать руками.

Есть для такого специальная функция read_csv(file_path)

df = read_csv('file.csv')

Путь файла можно указывать как относительно, так и абсолютно. Нельзя использовать \ для пути. Нужно использовать /, либо \\.

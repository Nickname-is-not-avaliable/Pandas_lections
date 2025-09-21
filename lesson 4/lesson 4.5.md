4.5 Знакомимся с форматами HTML, XML, PICKLE, HDF5

4.5.1-4.5.2 Формат HTML. Строение таблиц. Нужен пример таблицы на HTML с объяснениями
4.5.3 Нужны следующие бибилиотеки: 
!pip install lxml
!pip install html5lib
!pip install beautifulsoup4
table_list = pd.read_html(url)
После загрузки таблицы из html можно выгрузить её в другие форматы
4.5.4 Формат xml
Нужна библиотека lxml
from lxml import objetify
parsed = odjectify.parse(filename)
Функция parsed.getroot()
Для полного парса нужен цикл
data = []
for el in parsed.getroot().element:
  row_dict = {}
  for e in el.getchildren():
    row_dict[e.tag] = e.pyval
  data.append(row_dict)
df = pd.DataFrame(data)
по-хорошему нужно ещё проверить dtype
Необходимо подробное объяснение с примерами

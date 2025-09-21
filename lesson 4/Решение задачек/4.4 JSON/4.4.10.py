import pandas as pd

url = f'https://stepik.org/media/attachments/lesson/755302/data-399-2022-07-01.json'

df = pd.read_json(url, encoding='windows-1251', orient='records')

print(df[df['TicketCost'] == df['TicketCost'].min()]['NameOfTariff'])
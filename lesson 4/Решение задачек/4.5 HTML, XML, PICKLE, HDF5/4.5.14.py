import pandas as pd

url = f'users.xml'

df = pd.read_xml(url)

print(len(df.loc[(df.blood_group == 'B+') & (df.sex == 'F')]))
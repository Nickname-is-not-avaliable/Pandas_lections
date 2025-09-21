### Тут напрямую через интернет не выйдет. Нужно скачивать

import pandas as pd

url = 'data_store2.h5'

store = pd.HDFStore(url)

df = pd.read_hdf(store, '/parking_table')
print(store.keys())
print(df.loc[df.District == 'район Тропарёво-Никулино','Capacity'].sum())



store.close()
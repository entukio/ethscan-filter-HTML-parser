# Using statically saved HTML pages with Eth transactions to extract the data to data frames for further filtering
# In this example: need to extract all buy transactions of PEPE coin from Uniswap on April 26 with more than 2500$ value (10000000000 PEPE)

import pandas as pd
from bs4 import BeautifulSoup

pd.options.display.max_colwidth = 200

tb1 = 'Etherscan Advanced Filter.html'
HTMLFile = open(tb1, "r")
index = HTMLFile.read()
soup = BeautifulSoup(index, 'html.parser')
table = soup.find('table', {'class': 'table'})
tables = pd.read_html(str(table))
lista = tables[0]
new_cols = ['TX_hash','TX_type','Method','Age','From_address','andor','To_address','Amount','Asset']
lista.columns = new_cols

filtered = []
for i in range(len(lista)):
    if (lista.iloc[i]['Amount'] > 10000000000):
        if lista.iloc[i]['From_address'] == 'Uniswap V3: PEPE 4':
            filtered.append(lista.iloc[i])

fdf = pd.DataFrame(filtered)
#first page of wallets that bought Pepe from Uniswap V3 Pepe 4 on Apr 26 and spent more than 2.5k USD
hashes_3kusdB = []
for i in range(len(fdf)):
    a = fdf.iloc[i]['TX_hash']
    print(a)
    hashes_3kusdB.append(a)

#save hashes to txt file

wlist = ','.join(hashes_3kusdB)
path = r'my_data.txt'
with open('my_data.txt', 'w') as f:
    f.write(wlist)

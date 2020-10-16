import requests
from bs4 import BeautifulSoup
import re
url = 'https://github.com/cheran-senthil/PyRival/tree/master/pyrival/data_structures'

res = requests.get(url)

data = res.text
soup = BeautifulSoup(data,features="html5lib")

all_a_s = []

for link in soup.find_all('a'):
    all_a_s.append(link.get('href'))

temp = []
for link in all_a_s:
    if re.search('.py$', link):
        temp.append(link)

final = []
for link in temp:
    final.append("!"+"["+link.split('/')[-1][:-3]+"]" +"("+link+")" )
print('\n\n'.join(final))

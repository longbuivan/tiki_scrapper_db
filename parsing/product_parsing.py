from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib
import pandas as pd
import logging


data_df = []
all_list = []
columns_df = tuple([])

link = "https://tiki.vn/"



html = urllib.request.urlopen(link)

bs = BeautifulSoup(html, 'html.parser')

manu_list = bs.find_all("a", attrs={"class":re.compile('MenuItem_')})

for manu in manu_list:
    all_list.append(manu['href'])
    print(manu_list)

print(manu_list)
print()

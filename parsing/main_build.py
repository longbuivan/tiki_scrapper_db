from menu_parsing import menu_extract
from page_parsing import process_page
import logging
import pandas as pd

link = "https://tiki.vn/"
all_data = []
all_category = menu_extract(link)

for link in all_category:
    for i in range(1,5,1):
        print(logging.error("processing page: %s", i))
        data_df = (process_page(link, str(i)))
        category_link = link.split('/')[3]
        for data in data_df:
            all_data.append(tuple([data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9
            ]]))
            
    df = pd.DataFrame(all_data)
    df.to_csv("C:\\Users\\longbv1\\Desktop\\Tiki_Scapper\\raw\\tiki-"+category_link+".csv", header=False, encoding="utf-8-sig", index=False)


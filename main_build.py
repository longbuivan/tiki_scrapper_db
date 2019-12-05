from menu_parsing import menu_extract
from page_parsing import process_page
from config import configObject
import logging
import pandas as pd

link = configObject.website_path

all_category = menu_extract(link)

for link in all_category:
    all_data = []
    columns_df = tuple(['id','brand','category','price','title','review','rating','image_link','product_link','from_page_link'])
    all_data.append(columns_df)
    for pageID in range(1, configObject.page_number, 1):
        print(logging.info("processing page: %s", pageID))
        data_df = (process_page(link, str(pageID)))
        for data in data_df:
            all_data.append(tuple([data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]]))
    category_link = link.split('/')[3]
    print(logging.info("processinng category %s:", category_link))
    # MUST change to your local folder
    pd.DataFrame(all_data).to_csv(
        configObject.save_path+category_link+".csv",
        encoding=configObject.dataframe['encoding'],
        header=configObject.dataframe['header'],
        index=configObject.dataframe['index'])

print(logging.info("scrapping data done"))

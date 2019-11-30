from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib
import pandas as pd
import logging


data_df = []
all_data = []
columns_df = tuple(['id','brand','category','price','title','review','rating','image_link','product_link','from_page_link'])
all_data.append(columns_df)
# do gia dung
# link = "https://tiki.vn/dien-gia-dung/c1882?src=c.1882.hamburger_menu_fly_out_banner&page="
# lam dep
# link = input("please input a link here: ")

# link = "https://tiki.vn/lam-dep-suc-khoe/c1520?src=c.1520.hamburger_menu_fly_out_banner&page="

class product_info:
    def __init__(self, brand, category, price, title, review, rating, prod_id):
        self.brand = brand
        self.category =category
        self.price = price
        self.title = title
        self.review = review
        self.rating = rating
        self.prod_id = prod_id

class product_link:
    def __init__(self, image, product):
        self.image = image
        self.product = product

def process_page(link, i):
    
    tuple_data = []
    tuple_data_page = []
    html = urlopen(link+i+"&page=")
    bs = BeautifulSoup(html, 'html.parser')
    list_prod_id = bs.find_all(attrs={"data-seller-product-id": re.compile('.*')})
    
    for prod in list_prod_id:
        
        data_id = prod.find("a", attrs={"data-id":re.compile('.*'), "href":re.compile('.*')})['data-id']
        data_brand = prod.attrs['data-brand']
        data_category = prod.attrs['data-category']
        data_price = prod.attrs['data-price']
        data_title = prod.attrs['data-title']
        # the code seems perform slow here , need to optimize, ? ussing find instead of find_all
        try:
            data_review = prod.find("p", attrs={"class":"review"}).contents
            data_rating = prod.find("span", attrs={"style": re.compile('.*')})['style']
        except:
            data_review = ['null']
            data_rating = 'null'
        # logging.warning("processing item: %s", data_title)

        product_data = product_info(brand=data_brand,category=data_category,price=data_price,title=data_title,
                                review=data_review[0], rating=data_rating, prod_id=data_id)

        data_prod_link = prod.find("a", attrs={"data-id":re.compile('.*'), "href":re.compile('.*')})['href']
        data_image_link = prod.find("img", attrs={"class":"product-image img-responsive", "src":re.compile('.*')})['src']
        link_data = product_link(image=data_image_link,product=data_prod_link)

        tuple_data = tuple([
            product_data.prod_id,
            product_data.brand,
            product_data.category,
            product_data.price,
            product_data.title,
            product_data.review,
            product_data.rating,
            link_data.image,
            link_data.product,
            link+i
        ])
        tuple_data_page.append(tuple_data)
    return tuple_data_page

# for i in range(1,15,1):
#     print(logging.error("processing page: %s", i))
#     data_df = (process_page(link, str(i)))
#     for data in data_df:
#         all_data.append(tuple([data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9
#         ]]))
        
# df = pd.DataFrame(all_data)
# df.to_csv("C:\\Users\\longbv1\\Desktop\\Tiki_Scapper\\raw\\tiki-"+category_link+".csv", header=False, encoding="utf-8-sig", index=False)
print(all_data)

print()
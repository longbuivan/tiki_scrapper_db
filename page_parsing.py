from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib
import pandas as pd
import logging

# constructor contains product data
class product_info:
    def __init__(self, brand, category, price, title, review, rating, prod_id):
        self.brand = brand
        self.category =category
        self.price = price
        self.title = title
        self.review = review
        self.rating = rating
        self.prod_id = prod_id
# constructore contains links of each product
class product_link:
    def __init__(self, image, product):
        self.image = image
        self.product = product
# got link extract from menu and number of page from main_build.py
def process_page(link, i):
    tuple_data = []
    tuple_data_page = []
    # request url
    html = urlopen(link+i+"&page=")
    # html paring
    bs = BeautifulSoup(html, 'html.parser')
    list_prod_id = bs.find_all(attrs={"data-seller-product-id": re.compile('.*')})
    
    for prod in list_prod_id:
        # extracting data with pattern
        data_id = prod.find("a", attrs={"data-id":re.compile('.*'), "href":re.compile('.*')})['data-id']
        data_brand = prod.attrs['data-brand']
        data_category = prod.attrs['data-category']
        data_price = prod.attrs['data-price']
        data_title = prod.attrs['data-title']
        # fixing failed build if no review/rating data in
        try:
            data_review = prod.find("p", attrs={"class":"review"}).contents
            data_rating = prod.find("span", attrs={"style": re.compile('.*')})['style']
        except:
            data_review = ['null']
            data_rating = 'null'
        #store and append into tuple object
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

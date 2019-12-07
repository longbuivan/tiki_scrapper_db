import mysql.connector
from mysql.connector import Error

# db_execute = 'create database tiki_scrapper_db'
table_execute = 'create table products (id VARCHAR(255),\
		brand VARCHAR(255),\
		category TEXT(255),\
		price VARCHAR(255),\
		title VARCHAR(255),\
		review VARCHAR(255),\
		rating VARCHAR(255),\
		image_link TEXT(255),\
		product_link TEXT(255),\
		from_page_link TEXT(255))'

def connect():
	conn = None
	try:
		conn = mysql.connector.connect(host='localhost', database='tiki_scrapper_db', user='root',password='11121996')
		if conn.is_connected():
			print('connected to mysql database')
			cursor = conn.cursor()
			cursor.execute(table_execute)
			print('created table')
			
	except Error as e:
		print(e)
	finally:
		if conn is not None and conn.is_connected():
			conn.close()
			cursor.close()

if __name__ == '__main__':
	connect()

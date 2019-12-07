from tikidb_config import read_db_config
from mysql.connector import MySQLConnection, Error
import sys


def insert_data(data):
	query = "INSERT INTO products(id,brand,category,price,title,review,rating,image_link,product_link,from_page_link)"\
		"VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	args = [str(item) for item in data]
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)
		cursor = conn.cursor()
		cursor.execute(query, args)
		conn.commit()
	except Error as error:
		print(error)
		print(db_config)
		sys.exit(1)
	finally:
		cursor.close()
		conn.close()



from mysql.connector import MySQLConnection, Error
from tikidb_config import read_db_config

def query_with_fetchone():
	db_config = read_db_config()
	conn = None
	try:
		print('connecting to mysql database...')
		conn = MySQLConnection(**db_config)
		if conn.is_connected():
			print('connection established')
			cursor = conn.cursor()
			cursor.execute("SELECT * from products")
			row = cursor.fetchone()
			print(row)
		else:
			print('connection failed')
	except Error as error:
		print(error)
	finally:
		cursor.close()
		conn.close()

if __name__ == '__main__':
	query_with_fetchone()


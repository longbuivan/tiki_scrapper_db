from mysql.connector import MySQLConnection, Error
from tikidb_config import read_db_config

def connect_db():
	db_config = read_db_config()
	conn = None
	try:
		print('connecting to mysql database...')
		conn = MySQLConnection(**db_config)
		if conn.is_connected():
			print('connection established')
		else:
			print('connection failed')
	except Error as error:
		print(error)
#	finally:
#		if conn is not None and conn.is_connected():
#			conn.close()
#			print('connection closed')

if __name__ == '__main__':
	connect_db()


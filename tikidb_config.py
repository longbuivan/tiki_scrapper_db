
from configparser import ConfigParser

def read_db_config(filename='db_config.ini', section='mysql'):
	parser = ConfigParser()
	parser.read(filename)

	db = {}
	if parser.has_section(section):
		items = parser.items(section)
		for item in items:
			db[item[0]] = item[1]
	else:
		raise Exception('{0} not found in the {1} file'.format(section,filename))
	return db

"""
import yaml

def read_db_config():
	with open("db_config.yml",'r') as ymlfile:
		cfg = yaml.load(ymlfile)
	return cfg['mysql']

if __name__ == '__main__':
	db = read_db_config()
	print(db)
"""

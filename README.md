# Purpose: This project is trying to store data that extracting in front-end into MySQL Database.

# Technique:
  - Python
  - Framework: BeautifulSoup, urllib, pandas, pyyml
  - Database: Mysql
	- install Mysql, MysqlConnector 
  - Evironment: Linux 16.04
  - Editor: Vim

# Workflow:
  - web extract url by category, an output is list of url
  - input each input into page_parsing, which is parsing data of every products on fixed number page.
  - store raw data into MySQL
  - MySQL use for creating database and table that should was set up seprately.
  
# Output: 
  - raw data of products in tiki.vn by category store in database.

# Next step:
  - clean raw data for useable
  - create pipeline for scheduling run
  - apply model, analysis
  
# NOTES:
  - init_db.py MUST run first to initial set-up database on local.
  - main_build.py should be run after that
  - ALL INSTALLATION STEP IS NOT INCLUDED

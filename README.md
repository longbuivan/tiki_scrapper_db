# Purpose: This project is trying to extract front end data of e-commercial website (https://tiki.vn)
which one is faverous web page.

# Technique:
  - Python
  - Framework: BeautifulSoup, urllib, pandas

# Workflow:
  - web extract url by category, an output is list of url
  - input each input into page_parsing, which is parsing data of every products on fixed number page.
  - add those data into tuple object and convert to datafrae for futher cleans
  - temporary save those file into csv file and stored in local.
  
# Output: raw data of products in tiki.vn by category

# Next step:
  - add those data to cloud (data lake)
	- use mysql for storing data:
		- install and security config for mysql
		- download and use python-msql connector
		- create database and table
		- connect to databse
		- insert tiki data into table
  - clean raw data for useable
  - create pipeline for scheduling run
  - apply model, analysis

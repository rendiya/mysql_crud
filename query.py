import MySQLdb as sql
import json
import os
import time


def get_config():
	filename = 'config.json'
	with open(filename,'r') as data_file:
		data_json = json.loads(data_file.read())
	return data_json


class _query(object):
	"""docstring for _query"""
	def __init__(self):
		super(_query, self).__init__()
		data_sql = get_config()
		try:
			db = sql.connect(host=data_sql['database_host'],user=data_sql['database_user'],
			passwd=data_sql['database_pass'],db=data_sql['database_name'])
			self.db = db
		except Exception as e:
			print e
			db=sql.connect(host=data_sql['database_host'],user=data_sql['database_user'],
			passwd=data_sql['database_pass'])
			"""if db not exist create db"""
			db_sql = db.cursor()
			db_sql.execute('CREATE DATABASE {database_name}'.format(database_name=data_sql['database_name']))
			db.close()
			time.sleep(0.2)
			"""time sleep for waiting dumping effect mysql"""
			db=sql.connect(host=data_sql['database_host'],user=data_sql['database_user'],
			passwd=data_sql['database_pass'],db=data_sql['database_name'])
			self.db = db
	def version(self):
		db = self.db
		db_sql = db.cursor()
		db_sql.execute("SELECT VERSION()")
		version = db_sql.fetchone()
		db_sql.close()
		return version
	def select(self,table_name=None,table_column=None,table_filter=None):
		db = self.db
		if table_name is None:
			return "your tabble_name is None"
		if table_filter is None or table_column is None:
			query_select = "SELECT * FROM `{table_name}`".format(table_name=table_name)
		elif table_filter or table_column is not None:
			query_select = "SELECT * FROM `{table_name}` WHERE {table_column} = {table_filter} ".format(table_name=table_name,\
				table_column=table_column,table_filter=table_filter)
		print query_select
		db_sql = db.cursor()
		db_sql.execute(query_select)
		select = db_sql.fetchone()
		#select = "testis"
		return select

query= _query()
print query.select(table_name="hello",table_column="No",table_filter="1")
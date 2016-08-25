import sqlite3
from talk_local_messenger import send_message
from tabulate import tabulate


class ContactManager(object):

	def __init__(self):

		conn = sqlite3.connect('CM.db')
		conn.execute('''CREATE TABLE IF NOT EXISTS CONTACTS (
		ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
		NAME TEXT NOT NULL, 
		PHONE_NUM INT NOT NULL) 
		''')

		conn.commit()
		conn.close()


	def add_record(self, name, number):
		conn = sqlite3.connect('CM.db')
		conn.execute("INSERT INTO CONTACTS (NAME, PHONE_NUM)  VALUES ('{}', '{}')" .format(name, number));

		conn.commit()
		conn.close()

		return 'Record added'
		

	def search_record(self, name):
		conn = sqlite3.connect('CM.db')
		cursor = conn.execute("SELECT * from CONTACTS WHERE NAME='{}'" .format(name));
		data = cursor.fetchall()

		if not len(data):
			return 'No contact found with name %s' %name
		for row in cursor:
			return ('{} \t{}' .format(row[1], row[2]))

		conn.close()

	def get_number(name):
		cursor = conn.execute("SELECT PHONE_NUM from CONTACTS WHERE NAME='{}'" .format(name)); 		

		if cursor != None:
			for row in cursor:
				return ('{}' .format(row[0]))
		else:
			return 'No records found'
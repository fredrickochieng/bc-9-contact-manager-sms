import sqlite3
from talk_local_messenger import send_message
from tabulate import tabulate


class ContactManager(object):

	def __init__(self):

		conn = sqlite3.connect('contacts.db')
		conn.execute('''CREATE TABLE IF NOT EXISTS CONTACTS (
		ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
		NAME TEXT NOT NULL,
		PHONE_NUM INT NOT NULL) 
		''')

		conn.commit()
		conn.close()


	def add_record(self, name, number):
		conn = sqlite3.connect('contacts.db')
		conn.execute("INSERT INTO CONTACTS (NAME, PHONE_NUM)  VALUES ('{}', '{}')" .format(name, number));

		conn.commit()
		conn.close()

		return 'Record added'
		

	def search_record(self, name):
		conn = sqlite3.connect('contacts.db')
		cursor = conn.execute("SELECT * from CONTACTS WHERE NAME='{}'" .format(name));
		
		data = cursor.fetchall()

		if not len(data):
			return 'No contact found with name %s' %name
		elif len(data) > 1:

			print "Which %s" %name, "?" 

			results = []
			for row in data:
				each_row = []
				
				each_row.append('[' + str(row[0]) + ']')
				each_row.append(row[1])
				each_row.append(row[2])
				results.append(each_row)

			print tabulate(results, headers=["ID", "Name", "Number"])

			choice = input("\nPlease type the number corresponding to the person")

			if choice > results[len(results)-1][0] or choice <= 0:
				return 'Invalid selection'
			else:
				new_cursor = conn.execute("SELECT NAME from CONTACTS WHERE ID='{}'" .format(choice))
				theNumber = new_cursor.fetchall()
				return theNumber[0][0]

		else:

			results = []
			for row in data:
				each_row = []
				
				each_row.append(row[1])
				each_row.append(row[2])
				results.append(each_row)

			return tabulate(results, headers=["Name", "Number"])

		conn.close()


def send_text(name, message):
	conn = sqlite3.connect('contacts.db')
	cursor = conn.execute("SELECT * from CONTACTS WHERE NAME='{}'" .format(name)); 		

	data = cursor.fetchall()

	if not len(data):
		return '\nPlease add the contact before you sms'
	elif len(data) > 1:
		print "Which %s" %name, "would you love/like to text?" 

		results = []
		for row in data:
			each_row = []
			
			each_row.append('[' + str(row[0]) + ']')
			each_row.append(row[1])
			each_row.append(row[2])
			results.append(each_row)

		print tabulate(results, headers=["ID", "Name", "Number"])

		choice = input("\nPlease type the number corresponding to the person")

		if choice > results[len(results) - 1][0] or choice <= 0:
			return 'Invalid selection'
		else:
			new_cursor = conn.execute("SELECT PHONE_NUM from CONTACTS WHERE ID='{}'" .format(choice))

			theNumber = new_cursor.fetchall()
			print "\nSending message to %s %d" %(name,theNumber[0][0]) + "..."

			send_message(theNumber, message)


	else:
		to_number = data[0][2]
		print "\nSending message to %s %d" %(name, to_number)

		send_message(to_number, message)
import urllib3, json


def send_message(toNumber, message):

	try:
		http = urllib3.PoolManager()
		r = http.request('GET', 'http://api.txtlocal.com/send/', fields = {
			'username':	'allan4m@gmail.com',
			'password':	'Mypassword98', 
			'numbers':	toNumber, 
			'sender':	'Allan', 
			'message':	message
			})

	except Exception as e:
		print(e)
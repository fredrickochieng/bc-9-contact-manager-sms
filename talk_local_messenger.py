import urllib3, json

def send_message(toNumber, fromWhom, message):

	try:
		http = urllib3.PoolManager()
		r = http.request('GET', 'http://api.txtlocal.com/send/', fields = {
			'username':	'allan4444m@yahoo.com',
			'password':	'Makintosh98', 
			'numbers':	toNumber, 
			'sender':	fromWhom, 
			'message':	message
			})
		
		data = json.loads(r.data.decode('utf-8'))

		return ("\t{} \t{} \t{} \t{}".format(
			data['num_messages'], 
			data['message']['sender'], 
 			data['message']['sender']['content'],
 			data['status']
		))

	except Exception as e:
		print(e)
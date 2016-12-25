import urllib
import urllib2
import json
"""please insert your GPIO library"""

token = ''
update_id = 0
telegram_api = 'https://api.telegram.org/bot'
telegram_api_file = 'https://api.telegram.org/file/bot'
def get_message():
	response = urllib2.urlopen('{url}{token}/getUpdates'.format(url=telegram_api,token=token))
	data = json.load(response)
	return data

def get_me():
	"""get about bot name, return value is 
	{"oke":"true","result":["id":"xxxx","firsname":"xxxx","username":"xxxx"]}"""
	response = urllib2.urlopen('{url}{token}/getMe'.format(url=telegram_api,token=token))
	data = json.load(response)
	return data

def replay_message(message=None,chat_id=None,offset=None):
	if chat_id is None:
		return "please insert chat_id"
	if offset is None:
		return "please insert your offset"
	if message is None:
		message = ""
	isi = urllib.quote_plus(message)
	url = ('{api}{token}/sendMessage?chat_id={chat_id}&text={isi}'.format(api=telegram_api,chat_id=chat_id,token=token,isi=isi))
	get_update = ('{api}{token}/getUpdates?offset={offset}'.format(api=telegram_api,token=token,offset=offset))
	response = urllib2.urlopen(url=(get_update))
	response = urllib2.urlopen(url=(url))
	

def echo_message(message=None):
	if message is None:
		return ""
	elif message == "led on":
		"""for turning led on/off,please replace with yout library GPIO"""
		return "led has on"
	elif message == "led off":
		"""for turning led on/off,please replace with yout library GPIO"""
		return "led has off"
	elif message == "/start":
		return "hello from bot"
	else:
		return "comment not found"

def main():
	message = get_message()
	if message['result']==[]:
		return False
	for messaging in message['result']:
		offset = int(messaging['update_id'])+1
		message_user = messaging['message']['text']
		reply = echo_message(message_user)
		replay_message(message=reply,chat_id=messaging['message']['chat']['id'],offset=offset)
while  True:
	try:
		main()
	except Exception as e:
		print e
		pass
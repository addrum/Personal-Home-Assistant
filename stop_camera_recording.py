from urllib2 import urlopen, Request

access_token = 'ac6d1e4e-6827-4924-ba0a-f5f5fcac85da'

def start_stop(url):
	request = Request(url)
	# request.add_header('Authorization', 'token %s' % access_token)
	response = urlopen(request)
	print(response.read())

if __name__ == '__main__':
	url = 'http://192.168.0.14:8124/Json/StartStopRecording?sourceId=0&enabled=false&authToken={0}'.format(access_token)
	start_stop(url)
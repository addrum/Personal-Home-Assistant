import sys
import requests

access_token = 'ac6d1e4e-6827-4924-ba0a-f5f5fcac85da'

def start_stop(url):
	r = requests.get(url)
	print(r.text)

if __name__ == '__main__':
	source = sys.argv[1]
	enabled = sys.argv[2]
	print("Source {0}, recording {1}".format(source, enabled))
	url = 'http://192.168.0.14:8124/Json/StartStopRecording?sourceId={0}&enabled={1}&authToken={2}'.format(source, enabled, access_token)
	start_stop(url)
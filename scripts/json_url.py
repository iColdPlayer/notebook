import urllib.request
import json

def get_response(url):
	open_url = urllib.request.urlopen(url)
	if(open_url.getcode()==200):
		data = open_url.read()
		json_data = json.loads(data)

	else:
		print("Error while fetching...", open_url.getcode())
	return json_data

def main():

	url_source = 'https://kasir.herokuapp.com/auth/api/'
	json_data = get_response(url_source)


	for i in json_data['user']:
		print(f"user")

if __name__ == '__main__':
	main()

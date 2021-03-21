import json
import math
import requests

def check_user(username):
	url = "https://api.github.com/users/" + username
	# Note: if you put a / at the end of url, this will not works!
	response = requests.get(url)
	json_data = json.loads(response.text)
	return json_data

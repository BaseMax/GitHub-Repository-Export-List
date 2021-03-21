# Max Base
# 2021-03-21
# https://github.com/BaseMax/GitHub-Repository-List

import json
import math
import requests

def check_user(username):
	url = "https://api.github.com/users/" + username
	# Note: if you put a / at the end of url, this will not works!
	response = requests.get(url)
	json_data = json.loads(response.text)
	return json_data

def get_repos(username, page=1):
	url = "https://api.github.com/users/" + username + "/repos?per_page=100&page=" + page
	response = requests.get(url)
	json_data = json.loads(response.text)
	for item in json_data:
		name = item["name"]
		print(name)
	print("-----------------------")

username="basemax"
res = check_user(username)
print(res)
print(res["public_repos"])

if res["public_repos"] > 0:
	pages = math.ceil(count / 100)
	for page in range(pages):
		res = get_repos(username, page)
		print(res)

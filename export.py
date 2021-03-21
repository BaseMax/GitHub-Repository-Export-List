# Max Base
# 2021-03-21
# https://github.com/BaseMax/GitHub-Repository-Export-List

import json
import math
import requests

def check_user(username):
	url = "https://api.github.com/users/" + username
	# Note: if you put a / at the end of url, this will not works!
	response = requests.get(url)
	json_data = json.loads(response.text)
	return json_data

def get_repos(username, page):
	url = "https://api.github.com/users/" + username + "/repos?per_page=100&page=" + str(page)
	response = requests.get(url)
	json_data = json.loads(response.text)

	items = []

	for item in json_data:
		# {'id': 329726066, 'node_id': 'MDEwOlJlcG9zaXRvcnkzMjk3MjYwNjY=', 'name': 'GameNetSystemPHP', 'full_name': 'BaseMax/GameNetSystemPHP', 'private': False, 'owner': {'login': 'BaseMax', 'id': 2658040, 'node_id': 'MDQ6VXNlcjI2NTgwNDA=', 'avatar_url': 'https://avatars.githubusercontent.com/u/2658040?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/BaseMax', 'html_url': 'https://github.com/BaseMax', 'followers_url': 'https://api.github.com/users/BaseMax/followers', 'following_url': 'https://api.github.com/users/BaseMax/following{/other_user}', 'gists_url': 'https://api.github.com/users/BaseMax/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/BaseMax/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/BaseMax/subscriptions', 'organizations_url': 'https://api.github.com/users/BaseMax/orgs', 'repos_url': 'https://api.github.com/users/BaseMax/repos', 'events_url': 'https://api.github.com/users/BaseMax/events{/privacy}', 'received_events_url': 'https://api.github.com/users/BaseMax/received_events', 'type': 'User', 'site_admin': False}, 'html_url': 'https://github.com/BaseMax/GameNetSystemPHP', 'description': 'A complete system for game nets that can manage the category of console devices and also have control over rent and receiving money. (PHP + Ajax javascript JSON)', 'fork': False, 'url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP', 'forks_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/forks', 'keys_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/keys{/key_id}', 'collaborators_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/teams', 'hooks_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/hooks', 'issue_events_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/issues/events{/number}', 'events_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/events', 'assignees_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/assignees{/user}', 'branches_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/branches{/branch}', 'tags_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/tags', 'blobs_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/languages', 'stargazers_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/stargazers', 'contributors_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/contributors', 'subscribers_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/subscribers', 'subscription_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/subscription', 'commits_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/contents/{+path}', 'compare_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/merges', 'archive_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/downloads', 'issues_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/issues{/number}', 'pulls_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/labels{/name}', 'releases_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/releases{/id}', 'deployments_url': 'https://api.github.com/repos/BaseMax/GameNetSystemPHP/deployments', 'created_at': '2021-01-14T20:25:17Z', 'updated_at': '2021-03-06T11:49:23Z', 'pushed_at': '2021-03-06T11:49:20Z', 'git_url': 'git://github.com/BaseMax/GameNetSystemPHP.git', 'ssh_url': 'git@github.com:BaseMax/GameNetSystemPHP.git', 'clone_url': 'https://github.com/BaseMax/GameNetSystemPHP.git', 'svn_url': 'https://github.com/BaseMax/GameNetSystemPHP', 'homepage': '', 'size': 1953, 'stargazers_count': 0, 'watchers_count': 0, 'language': 'PHP', 'has_issues': True, 'has_projects': True, 'has_downloads': True, 'has_wiki': True, 'has_pages': False, 'forks_count': 0, 'mirror_url': None, 'archived': False, 'disabled': False, 'open_issues_count': 0, 'license': {'key': 'gpl-3.0', 'name': 'GNU General Public License v3.0', 'spdx_id': 'GPL-3.0', 'url': 'https://api.github.com/licenses/gpl-3.0', 'node_id': 'MDc6TGljZW5zZTk='}, 'forks': 0, 'open_issues': 0, 'watchers': 0, 'default_branch': 'main'}
		# print(item)

		link = "https://github.com/" + item["full_name"]
		description = item["description"]
		language = item["language"]
		name = item["name"]

		# print(name)
		# print(language)
		# print(description)
		# print(link)

		items.append({
			"name": name,
			"language": language,
			"description": description,
			"link": link,
		})
		
	# print("-----------------------")
	return items

def get_all_repos(username, public_repos):
	pages = math.ceil(public_repos / 100)

	items = []

	for page in range(pages): # page starts from 0
		# print("Download page:", page+1)
		res = get_repos(username, page+1)
		# print(res)
		items.extend(res)

	return items

def group_by_languages(repos):
	languages = {}
	for repo in repos:
		if repo["language"] == "" or repo["language"] == None:
			lang = "other"
		else:
			lang = str(repo["language"])

		if lang not in languages:
			languages[lang] = []

		# TODO: remove language field from repo
		languages[lang].append(repo)

	return languages

def generate_html(groups):
	# title
	print("<title>" + profile["name"] + " GitHub</title>")
	# h1/name
	print("<h1>" + profile["name"] + " GitHub</h1>\n")

	for language, repos in groups.items():

		print("<b>"+ language +"</b>") # TODO: upper-case first char of language name
		print("<ul>")

		for repo in repos:
			# print(repo)
			print("  <li>")
			print("    <a href=\"" + str(repo["link"]) +"\" alt=\"" + str(repo["name"]) + "\">" + str(repo["name"]) + "</a>: ")
			print("    <span>" + str(repo["description"]) + "</span>")
			print("  </li>")

		print("</ul>\n")

username="basemax"
profile = check_user(username)

try:
	# print(profile)
	# print(profile["public_repos"])
	public_repos = profile["public_repos"]
except KeyError:
	public_repos = 0

if public_repos:
	all_repos = get_all_repos(username, public_repos)

	groups = group_by_languages(all_repos)
	# print(groups)

	# generate HTML output
	generate_html(groups)
else:
	print("Error: No public repositories or maybe network problem!")

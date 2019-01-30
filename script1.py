import requests
import json
import sys
#import json
from pprint import pprint

####
# inputs
####
#username = sys.argv[1]
username='senthilkumar.kannappan@gmail.com'
# from https://github.com/user/settings/tokens
token='4c8437a9998a77df3d3eaa5e5e90adf7ecd9482a'
#token = sys.argv[2]

print("please enter the repos in $orgname/$reponame format")
data = []
for line in sys.stdin:
    data.append(line)

#repos_url = 'https://api.github.com/user/repos'

# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (username, token)

# get the list of repos belonging to me
for item in data:
    repos = json.loads(gh_session.get('https://api.github.com/orgs/steepride/repos').text)
 #   pprint(repos)
# print the repo names

for repo in repos:
    print("Name of the repo: %s Clone URL: %s " % (repo['name'], repo['clone_url']))
    
# make more requests using "gh_session" to create repos, list issues, etc.
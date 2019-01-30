import requests
import json
import sys
import urllib
#import json
from pprint import pprint

####
# inputs
####

username=raw_input("Please enter your github id : ")

# from https://github.com/user/settings/tokens
token=raw_input("Please enter your OAuth Token : ")
#'c056b0a0677e0869d03d449040dc5167ac156898'


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
   item = item.split("/")
   orgname = item[0]
   reponame = item[1]
   urltest = 'https://api.github.com/orgs/{}/repos'
   #url = 'https://api.github.com/orgs/'+ orgname + '/repos'
   print urltest.format(orgname)
   repos = json.loads(gh_session.get(urltest.format(orgname)).text)
   #pprint(repos)

   for repo in repos:
      #print repo
      print("Name of the repo: %s Clone URL: %s " % (repo['name'], repo['clone_url']))

from __future__ import print_function
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
   reponame = item[1].strip("\n")
   repos_url = 'https://api.github.com/orgs/{a}/repos'
   commits_url = 'https://api.github.com/repos/{a}/{b}'+'/commits'
   commit = 'commits'
   #url = 'https://api.github.com/orgs/'+ orgname + '/repos'
   print(repos_url.format(a=orgname))
   print(commits_url.format(a=orgname, b=reponame,))
   repos = json.loads(gh_session.get(repos_url.format(a=orgname)).text)
   #pprint(repos)

   for repo in repos:
      repo_name = repo['name']
      clone_url = repo['clone_url']
      print(repo_name, clone_url)
      commits = json.loads(gh_session.get(commits_url.format(a=orgname, b=reponame)).text)
      #for commit in commits:
      print(commits[0]["commit"]["committer"]["name"])
      print(commits[0]["commit"]["committer"]["date"])
      #print(author_name)
         #print repo
         #print("Date of the latest commit : %s , Name of the latest Author : %s" % (data[commit[0]['date']],data[commit[0]['author']]))
         #pprint(commit[0].['author'].['name'])
         #print("Name of the repo: %s, Clone URL: %s " % repo_name, clone_url)

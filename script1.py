import requests
import json
import sys
import urllib
import csv
from pprint import pprint
   
data = []
github_dic ={}

username=raw_input("Please enter your github id : ")

# from https://github.com/user/settings/tokens
token=raw_input("Please enter your OAuth Token : ")

print("please enter the repos in $orgname/$reponame format")
for line in sys.stdin:
    data.append(line)

# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (username, token)

# get the list of repos for the given org & get the commit history to find the Latest Author & date
for item in data:
   item = item.split("/")
   orgname = item[0]
   reponame = item[1].strip("\n")
# Build the Github API URLs
   repos_url = 'https://api.github.com/orgs/{a}/repos'
   commits_url = 'https://api.github.com/repos/{a}/{b}'+'/commits'
# Acces the apis
   repos = json.loads(gh_session.get(repos_url.format(a=orgname)).text)
   i=0
   for repo in repos:
      repo_name = repo['name']
      clone_url = repo['clone_url']
      commits = json.loads(gh_session.get(commits_url.format(a=orgname, b=reponame)).text)
      author_name = commits[0]["commit"]["committer"]["name"]
      latest_commit_date = commits[0]["commit"]["committer"]["date"]
      print("Repo Name : {0}, Clone URL : {1}, Author Name : {2}, Commit Date : {3} ".format(repo_name, clone_url, author_name, latest_commit_date))
      values = [repo_name, clone_url, author_name, latest_commit_date]
      github_dic[i]=values
      i=i+1

   with open("file.csv","a") as csv_file:
      csv_writer = csv.writer(csv_file)
      for i in github_dic :
         list = github_dic[i]
         csv_writer.writerow(list)
      
print(github_dic)
csv_file.close()



#writeFile.close()

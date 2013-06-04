import getpass
import sys
import argparse

# In the main directory of the repo where you are developing with PyGithub,
# type:
# git submodule add git://github.com/jacquev6/PyGithub.git PyGithub
# git submodule init
# git submodule update
#
# That will populate a PyGithub subdirectory with a clone of PyGithub
# Then, to add it to your Python path, you can do:


from github import Github
from github import GithubException

parser = argparse.ArgumentParser(description='List all repos for an org')
parser.add_argument('orgName',help='github Organization name')

args = parser.parse_args()

username = raw_input("Github Username:")
pw = getpass.getpass()
g = Github(username,pw)

#print("All repos for organization: ",args.orgName)

#org = g.get_organization(args.orgName)

## TODO: Add some error checking code here to see whether
## the lookup was successful. Do we try/except or check the return value?

repos = g.get_repos()
repo=''
for repo in repos:
  if repo.name=="OSrepo":
    break
#  print type(repo)
#  print (repo.name)

print repo.name

eventos=repo.get_events()




#branches=repo.get_branches()
#for branche in branches:
#  print branche.name
#  print type(branche)
#  commits=
#  for commit in repo.get_commits()
#    print commit.stats()
#    print commit.get_comments()

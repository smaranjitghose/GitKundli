# Script to GET Repo details from user
# @Author - Sandip Dutta
# Email - duttasandip11100@gmail.com

# IMPORTS
import json
import requests
import config

def getRepoDetails():
  # Main function
  # Set names of Repo and gets data from API Query

  config.REPONAME = input("Enter Repo Name as it appears : ")
  config.USERNAME = input("Enter the owner of the repository as it appears : ")
  # Sanity check
  assert (config.REPONAME is not None and config.USERNAME is not None), "Invalid Details"

  # Specify Headers
  # Note - Can only see collaborators if it is own repository
  headers = {'Authorization': "Token " + config.GITHUB_TOKEN}
  # API Request
  response = requests.post(
    config.BASE_URL,
    json={'query': config.getQuery()},
    headers=headers)
  
  json_data = json.loads(response.text)

  # Extract meaningful Information from json data
  # As per Query Structure
  num_collaborators = json_data['data']['repository']['collaborators']['totalCount']
  num_pullRequests = json_data['data']['repository']['pullRequests']['totalCount']
  num_stars = json_data['data']['repository']['stargazers']['totalCount']
  num_commits = json_data['data']['repository']['object']['history']['totalCount']

  return num_collaborators, num_pullRequests, num_stars, num_commits


if __name__ == '__main__':
  num_collaborators, num_pullRequests, num_stars, num_commits = getRepoDetails()

  # Pretty display 
  print("-" * 80)
  print(f"Stats for Repository {config.REPONAME} (Owner : {config.USERNAME})")
  print(f"Number of collaborators : {num_collaborators}")
  print(f"Number of Pull Requests : {num_pullRequests}")
  print(f"Number of Stars : {num_stars}")
  print(f"Number of Commits : {num_commits}")
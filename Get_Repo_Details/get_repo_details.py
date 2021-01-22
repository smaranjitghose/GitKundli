# Script to GET Repo details from user
# @Author - Sandip Dutta
# Email - duttasandip11100@gmail.com

# IMPORTS
import json
import requests
import config

def main():
  # Main function
  # Set names of Repo

  config.REPONAME = input("Enter Repo Name as it appears : ")
  config.USERNAME = input("Enter the owner of the repository as it appears : ")
  # Sanity check
  assert (config.REPONAME is not None and config.USERNAME is not None), "Invalid Details"

  # Specify Headers
  headers = {'Authorization': "Token " + config.GITHUB_TOKEN}
  # API Request
  response = requests.post(
    config.BASE_URL,
    json={'query': config.getQuery()},
    headers=headers)
  
  json_data = json.loads(response.text)

  print(json_data)


if __name__ == '__main__':
  main()
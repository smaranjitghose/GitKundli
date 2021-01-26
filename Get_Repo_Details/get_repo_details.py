# Script to GET Repo details from user
import json
import requests
import os
import pprint
import fire

# Global Constants
GH_API_ENDPOINT = "https://api.github.com/graphql" # Github base url
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']  # Github token environment variable

class GitKundli(object):
  '''
  Class to extract useful information about a user and repo.
  Accesses Github GraphQL API to extract information
  '''

  # Query to Obtain
  def repo_info(self, reponame, username):
    '''
    Gets Repository details from API and displays it.
    Shows num collaborators, num Stars, num Pull requests,
    and number of commits

    Args:
      reponame : The name of the repository about which we need to 
        get the info
      username : The user under whom the repo is present

    Returns:
      None
    '''

    # Query to get required details 
    repo_details_query = """query {{
      repository(name: \"{0}\", owner: \"{1}\") {{
        collaborators {{
          totalCount
        }}
        pullRequests {{
          totalCount
        }}
        stargazers {{
          totalCount
        }}
        object(expression: "master") {{
          ... on Commit {{
            history {{
              totalCount
            }}
          }}
        }}
      }}
    }}""".format(reponame, username)

    # Specify Headers
    # Note - Can only see collaborators if it is own repository
    headers = {'Authorization': "Token " + GITHUB_TOKEN}
    # Making our API Request
    response = requests.post(
      GH_API_ENDPOINT,
      json = {'query': repo_details_query},
      headers = headers)

    # Printing the Status Code to check for any error
    print(f"\nStatus Code : {response.status_code}")
    
    json_data = json.loads(response.text)
    # Display data
    pprint.pp(json_data['data']['repository'], compact=True)

if __name__ == '__main__':
  # Launch the CLI
  fire.Fire(GitKundli)
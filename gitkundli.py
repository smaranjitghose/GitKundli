# Getting our dependencies
import os
import requests
import json
import pandas as pd
from pprint import pprint


# Fetching our GitHub access token using Environment variables
access_token = os.environ.get('GITHUB_TOKEN')
# Our GraphQL Query to get the data about the pull requests on a particular repo with a particular label
query = """query{
	  repositoryOwner(login: "smaranjitghose") {
	    repository(name: "doc2pen") {
	      pullRequests(first: 100, labels: ["CH-20"]) {
	        edges {
	          node {
	            labels(first: 5) {
	              edges {
	                node {
	                  name
	                }
	              }
	            }
	            author {
	              login
	            }
	          }
	        }
	      }
	    }
	  }
	}"""

# GitHub's API endpoint for  GraphQL
url = 'https://api.github.com/graphql'
# Headers for Authentication
headers = {'Authorization': "Token " + access_token}
# Making our API request
r = requests.post(url, json={'query': query}, headers=headers)
# Printing the Status Code to check for any erros
print(r.status_code)
# The data fetched from GitHub server as per query
pprint(r.text)
json_data = json.loads(r.text)
# We remove some redundant details
df_data = json_data['data']['repositoryOwner']['repository']['pullRequests']['edges']
# Converting our data into a pandas data frame for further analysis
df = pd.DataFrame(df_data)
# Saving our data as CSV file
df.to_csv('.data/contributors.csv')

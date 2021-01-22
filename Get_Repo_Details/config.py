## Configuration constants
import os

BASE_URL = "https://api.github.com/graphql" # Github base url
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']  # Github token environment variable
REPONAME, USERNAME = None, None

def getQuery():
  # Reuturns the Query String
  query = """query {{
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
  }}""".format(REPONAME, USERNAME)   # GraphQL Query
  return query
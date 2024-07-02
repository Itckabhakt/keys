import requests
import json
from github import Github

# GitHub token and repo details
GITHUB_TOKEN = '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'
REPO_NAME = 'Itckabhakt/Keys'

# URL to fetch the new API key
api_url = 'https://livecrichdofficial.000webhostapp.com/livecrichd.php?id=24'

def fetch_new_api_key():
    response = requests.get(api_url)
    data = response.json()
    return data['channel_url']  # Assuming 'channel_url' is the new API key

def update_api_key_in_repo(api_key):
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    
    # Get the file contents
    contents = repo.get_contents("api_key.txt", ref="main")
    # Update the file contents
    repo.update_file(contents.path, "Update API key", api_key, contents.sha, branch="main")

if __name__ == "__main__":
    new_api_key = fetch_new_api_key()
    update_api_key_in_repo(new_api_key)
  

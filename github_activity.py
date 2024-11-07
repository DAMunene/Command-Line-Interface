import requests
import argparse

# Function to fetch GitHub user activity
def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        # Send a GET request to GitHub API
        response = requests.get(url)
        
        # Check if the response is successful (200 OK)
        if response.status_code == 200:
            events = response.json()
            if events:
                print(f"Recent activity for user {username}:")
                for event in events[:5]:  # Limiting to the 5 most recent events
                    event_type = event['type']
                    repo_name = event['repo']['name']
                    # Display activity type and repository name
                    if event_type == 'PushEvent':
                        commits = event['payload']['commits']
                        print(f"Pushed {len(commits)} commits to {repo_name}")
                    elif event_type == 'IssuesEvent' and event['payload']['action'] == 'opened':
                        print(f"Opened a new issue in {repo_name}")
                    elif event_type == 'WatchEvent' and event['payload']['action'] == 'star':
                        print(f"Starred {repo_name}")
                    else:
                        print(f"Other activity: {event_type} in {repo_name}")
            else:
                print(f"No activity found for {username}.")
        else:
            print(f"Error fetching data for {username}. HTTP Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Function to handle the command line arguments
def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Fetch recent GitHub activity for a user.")
    parser.add_argument("username", type=str, help="GitHub username to fetch activity for.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Fetch the activity for the provided username
    fetch_github_activity(args.username)

if __name__ == "__main__":
    main()

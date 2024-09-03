import subprocess
from datetime import datetime

def git_pull():
    try:
        # Pulling the latest changes from the remote repository
        subprocess.run(['git', 'pull'], check=True, capture_output=True)
        print("Successfully pulled updates from remote.")
    except subprocess.CalledProcessError as e:
        print("Warning: Pull operation failed. No changes made.")
        print(f"Error details: {e.stderr.decode().strip()}")

def git_commit_push():
    try:
        # Adding all changes in the git repository
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
        
        # Getting today's date in YYYY-MM-DD format
        today_date = datetime.now().strftime("%Y-%m-%d")
        
        # Committing the changes with a message
        commit_message = f"Daily model run {today_date}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True, capture_output=True)
        
        # Pushing the changes to the remote repository
        subprocess.run(['git', 'push'], check=True, capture_output=True)
        print("Successfully committed and pushed updates.")
    except subprocess.CalledProcessError as e:
        print("Warning: Commit/Push operation failed. No changes made.")
        print(f"Error details: {e.stderr.decode().strip()}")

if __name__ == "__main__":
    git_pull()  # Update local repository
    git_commit_push()  # Commit and push changes

import subprocess
from datetime import datetime

def git_pull(branch='main'):
    try:
        # Pulling the latest changes from the specified remote repository and branch
        subprocess.run(['git', 'pull', 'origin', branch], check=True, capture_output=True)
        print("Git: Successfully pulled updates from Git remote.")
    except subprocess.CalledProcessError as e:
        print("Git Warning: Git pull operation failed. No changes made.")
        print(f"Git Error details: {e.stderr.decode().strip()}")

def git_commit_push(branch='main', commit_message_prefix = "Daily Data Update"):
    try:
        # Adding all changes in the git repository
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
        
        # Getting today's date in YYYY-MM-DD format
        today_date = datetime.now().strftime("%Y-%m-%d")
        
        # Committing the changes with a message
        commit_message = f"{commit_message_prefix} ({today_date})"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True, capture_output=True)
        
        # Pushing the changes to the remote repository and specified branch
        subprocess.run(['git', 'push', 'origin', branch], check=True, capture_output=True)
        print("Git: Successfully committed and pushed updates.")
    except subprocess.CalledProcessError as e:
        print("Git Warning: Commit/Push operation failed. No changes made.")
        print(f"Git Error details: {e.stderr.decode().strip()}")

if __name__ == "__main__":
    git_pull()  # Update local repository
    git_commit_push()  # Commit and push changes

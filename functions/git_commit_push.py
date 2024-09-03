import subprocess
from datetime import datetime

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
        
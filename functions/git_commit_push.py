import subprocess
from datetime import datetime

def git_commit_push(branch='main', commit_message_prefix = "Daily Data Update"):
    """
    Commits and pushes changes to a Git repository.

    This function stages all changes in the current Git repository, commits them with a 
    message that includes a specified prefix and today's date, and then pushes the commit 
    to the specified branch on the remote repository.

    Args:
        branch (str): The name of the branch to push the changes to. Defaults to 'main'.
        commit_message_prefix (str): The prefix for the commit message. Defaults to "Daily Data Update".

    Returns:
        list: A list containing a boolean and a string message. The boolean indicates the 
        success (True) or failure (False) of the operation. The string provides details 
        on the outcome.

    Raises:
        subprocess.CalledProcessError: If the git commands fail during execution.
    """
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
        message = "Git: Successfully committed and pushed updates."
        print(message)

        return [True, message]

    except subprocess.CalledProcessError as e:
        message = "Git Warning: Commit/Push operation failed. No changes made.\n\n" + f"Git Error details: {e.stderr.decode().strip()}"
        print(message)
        
        return [False, message]

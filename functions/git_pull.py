import subprocess

def git_pull(branch='main'):
    """
    Pulls the latest changes from a specified branch of the remote Git repository.

    This function attempts to pull the latest updates from the specified branch of the 
    remote repository. If successful, it returns a success message; otherwise, it catches 
    any errors and returns a failure message with error details.

    Args:
        branch (str): The name of the branch to pull the changes from. Defaults to 'main'.

    Returns:
        list: A list containing a boolean and a string message. The boolean indicates the 
        success (True) or failure (False) of the operation. The string provides details 
        on the outcome.

    Raises:
        subprocess.CalledProcessError: If the git pull command fails during execution.
    """
    try:
        # Pulling the latest changes from the specified remote repository and branch
        subprocess.run(['git', 'pull', 'origin', branch], check=True, capture_output=True)
        message = "Git: Successfully pulled updates from Git remote."
        print(message)

        return [True, message]
    
    except subprocess.CalledProcessError as e:
        message = "Git Warning: Git pull operation failed. No changes made.\n" + f"Git Error details: {e.stderr.decode().strip()}"
        print(message)

        return [False, message]

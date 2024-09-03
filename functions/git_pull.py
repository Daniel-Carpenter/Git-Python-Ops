import subprocess

def git_pull(branch='main'):
    
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

import subprocess

def git_pull(branch='main'):
    
    try:
        # Pulling the latest changes from the specified remote repository and branch
        subprocess.run(['git', 'pull', 'origin', branch], check=True, capture_output=True)
        print("Git: Successfully pulled updates from Git remote.")
    
    except subprocess.CalledProcessError as e:
        print("Git Warning: Git pull operation failed. No changes made.")
        print(f"Git Error details: {e.stderr.decode().strip()}")

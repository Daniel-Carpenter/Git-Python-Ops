import functions.git_commit_push as gc
import functions.git_pull as gp

if __name__ == "__main__":
    gp.git_pull()  # Update local repository
    gc.git_commit_push(commit_message_prefix = 'Move sections')  # Commit and push changes

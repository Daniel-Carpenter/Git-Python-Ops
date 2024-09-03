import functions.git_commit_push as gc
import functions.git_pull as gp
import functions.send_email as msg
import functions.get_creds as pw

if __name__ == "__main__":
    """
    Main script for automating Git operations and sending email notifications.

    This script performs the following tasks:
    1. Retrieves email credentials.
    2. Pulls the latest changes from a Git repository.
    3. If the pull operation fails, sends an email notification.
    4. Commits and pushes changes to the Git repository.
    5. If the push operation fails, sends an email notification.

    The email notifications include the status of the Git operations (pull/push) and 
    any relevant error messages.
    """

    # --------------------------------------------------------
    # Credentials and Inputs
    # --------------------------------------------------------

    # Git Commit Message
    commit_message_prefix = 'Documentation'
    
    # Get Credentials for Emailing error codes
    smtp_server, port, sender_email, sender_password, recipients = pw.get_creds()



    # --------------------------------------------------------
    # Pull from Git 
    # --------------------------------------------------------

    pull_wasSuccess, pull_message = gp.git_pull()  # Update local repository
    
    # Send email with error message if failed
    if not pull_wasSuccess:
        msg.send_email(smtp_server, port, sender_email, sender_password, recipients, 
            subject = 'Git Pull Update (Automation)', 
            message = pull_message
            )
        
    

    # --------------------------------------------------------
    # Commit all changes and push to git
    # --------------------------------------------------------

    push_wasSuccess, push_message = gc.git_commit_push(commit_message_prefix=commit_message_prefix)  # Commit and push changes

    # Send email with error message if failed
    if not push_wasSuccess:
        msg.send_email(smtp_server, port, sender_email, sender_password, recipients, 
            subject = 'Git Push Update (Automation)', 
            message = push_message
            )

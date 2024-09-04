import automation.git.git_commit_push as gc
import automation.git.git_pull as gp
import automation.email.send_email as msg
import automation.email.get_creds as pw

def get_email_credentials():
    """
    Retrieves email credentials.
    Returns:
        tuple: smtp_server, port, sender_email, sender_password, recipients
    """
    return pw.get_creds()

def git_pull_notify(smtp_server, port, sender_email, sender_password, recipients):
    """
    Pulls the latest changes from a Git repository.
    Sends an email notification if the pull fails.
    """
    pull_wasSuccess, pull_message = gp.git_pull()  # Pull latest changes
    if not pull_wasSuccess:
        msg.send_email(smtp_server, port, sender_email, sender_password, recipients, 
            subject='Git Pull Update (Automation)', 
            message=pull_message)
    return pull_wasSuccess

def git_commit_push_notify(commit_message_prefix, smtp_server, port, sender_email, sender_password, recipients):
    """
    Commits and pushes changes to the Git repository.
    Sends an email notification if the push fails.
    """
    push_wasSuccess, push_message = gc.git_commit_push(commit_message_prefix=commit_message_prefix)
    if not push_wasSuccess:
        msg.send_email(smtp_server, port, sender_email, sender_password, recipients, 
            subject='Git Push Update (Automation)', 
            message=push_message)
    return push_wasSuccess

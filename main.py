import functions.git_commit_push as gc
import functions.git_pull as gp
import functions.send_email as msg
import functions.get_creds as pw

if __name__ == "__main__":

    # Example usage
    smtp_server, port, sender_email, sender_password, recipients = pw.get_creds()

    # Pull data
    pull_wasSuccess, pull_message = gp.git_pull()  # Update local repository
    
    if not pull_wasSuccess:
        msg.send_email(smtp_server, port, sender_email, sender_password, recipients, 
            subject = 'Git Pull Update (Automation)', 
            message = pull_message
            )
        
    
    # Push Data
    push_wasSuccess, push_message = gc.git_commit_push(commit_message_prefix = 'Testing Email Success')  # Commit and push changes

    if not push_wasSuccess:
        msg.send_email(smtp_server, port, sender_email, sender_password, recipients, 
            subject = 'Git Push Update (Automation)', 
            message = push_message
            )
    
    
    
    # push_wasSuccess = gc.git_commit_push(commit_message_prefix = 'Test Email')  # Commit and push changes

import automation.git_updates as gu

if __name__ == "__main__":
    
    # Inputs: git commit Message
    commit_message_prefix = 'Reorganize directory structure'

    # Retrieve email credentials
    smtp_server, port, sender_email, sender_password, recipients = gu.get_email_credentials()

    # Pull from Git and notify on failure
    gu.git_pull_notify(smtp_server, port, sender_email, sender_password, recipients)

    # Commit and push to Git and notify on failure
    gu.git_commit_push_notify(commit_message_prefix, smtp_server, port, sender_email, sender_password, recipients)
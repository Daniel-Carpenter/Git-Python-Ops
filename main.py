import automation.git_updates as gu

if __name__ == "__main__":
    """
    Main script for automating Git operations and sending email notifications.

    This script performs the following tasks:
    1. Retrieves email credentials.
    2. Pulls the latest changes from a Git repository.
    3. If the pull operation fails, sends an email notification.
    4. Commits and pushes changes to the Git repository.
    5. If the push operation fails, sends an email notification.

    The email notifications include the status of the Git operations (pull/push) and any relevant error messages.
    """

    # Inputs: git commit Message
    commit_message_prefix = 'Documentation'

    # Retrieve email credentials
    smtp_server, port, sender_email, sender_password, recipients = gu.get_email_credentials()

    # Pull from Git and email notify on failure
    gu.git_pull_notify(smtp_server, port, sender_email, sender_password, recipients)

    # Commit and push to Git and email notify on failure
    gu.git_commit_push_notify(commit_message_prefix, smtp_server, port, sender_email, sender_password, recipients)
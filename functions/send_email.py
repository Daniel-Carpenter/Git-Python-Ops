import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

def send_email(smtp_server: str, port: int, sender_email: str, sender_password: str, 
               recipients: List[str], subject: str, message: str, is_html: bool = False):
    """
    Sends an email to a list of recipients using the specified SMTP server.

    This function sets up an SMTP connection to the provided server, logs in with the 
    sender's credentials, and sends an email to each recipient in the provided list. 
    The email can be sent as plain text or HTML.

    Args:
        smtp_server (str): The SMTP server address.
        port (int): The port to use for the SMTP server (e.g., 587 for TLS).
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recipients (List[str]): A list of recipient email addresses.
        subject (str): The subject of the email.
        message (str): The body of the email.
        is_html (bool): Whether the email body is in HTML format. Defaults to False.

    Returns:
        None

    Raises:
        Exception: If there is an error during the email sending process.

    Example:
        smtp_server = "smtp-mail.outlook.com"
        port = 587
        sender_email = "example@example.com"
        sender_password = "password"
        recipients = ["recipient1@example.com", "recipient2@example.com"]
        subject = "Test Email"
        message = "<h2>This is a test email</h2>"
        send_email(smtp_server, port, sender_email, sender_password, recipients, subject, message, is_html=True)
    """
    try:
        # Set up the server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection

        # Login to the email account
        server.login(sender_email, sender_password)

        # Create the email
        for recipient in recipients:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the message
            if is_html:
                msg.attach(MIMEText(message, 'html'))
            else:
                msg.attach(MIMEText(message, 'plain'))

            # Send the email
            server.sendmail(sender_email, recipient, msg.as_string())

        # Quit the server
        server.quit()
        print("A log email has been sent successfully to the recipients.")

    except Exception as e:
        print(f"Failed to send email: {str(e)}")

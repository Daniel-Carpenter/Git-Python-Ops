import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

def send_email(smtp_server: str, port: int, sender_email: str, sender_password: str, 
               recipients: List[str], subject: str, message: str, is_html: bool = False):
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
        print("A log email has been sent successfully to the recepients.")

    except Exception as e:
        print(f"Failed to send email: {str(e)}")


# Example
# # Sample DataFrame
# df_sample = pd.DataFrame({
#     'y': ['a', 'b', 'c'],
#     'x': [10, 14, 12]
# }).to_html()

# # Example usage
# smtp_server = "smtp-mail.outlook.com"
# port = 587
# sender_email = ""
# sender_password = ""
# recipients = [""]
# subject = "Test Email"
# message = """
# <h2>This is a test email using Outlook as a email server.</h2>
# <p>Here is a sample DataFrame:</p>
# """ + df_sample

# send_email(smtp_server, port, sender_email, sender_password, recipients, subject, message, is_html=True)

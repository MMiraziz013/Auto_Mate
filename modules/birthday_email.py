import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Set up the server
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(sender_email, sender_password)

        # Build the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        smtp.sendmail(sender_email, recipient_email, msg.as_string())
        smtp.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {e}"

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(sender_email, sender_password)  # App Password here

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        smtp.sendmail(sender_email, recipient_email, msg.as_string())
        smtp.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
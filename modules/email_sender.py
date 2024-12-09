import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from modules.db_utils import update_email_status


def send_email(email_data):
    try:
        sender_email = email_data["sender_email"]
        sender_password = email_data["sender_password"]
        recipient_email = email_data["recipient_email"]
        subject = email_data["subject"]
        message = email_data["message"]
        scheduled_time = email_data["scheduled_time"]
        email_id = email_data["id"]  # Use 'id' consistently

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print(f"Email sent successfully to {recipient_email} at {scheduled_time}")
        update_email_status(email_id, "sent")
    except Exception as e:
        print(f"Error sending email: {e}")
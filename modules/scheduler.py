import threading
from datetime import datetime
from modules.db_utils import load_pending_emails, update_email_status
from modules.email_sender import send_email

active_timers = []

def process_emails():
    current_datetime = datetime.now()
    pending_emails = load_pending_emails()

    for email in pending_emails:
        email_id = email["id"]
        scheduled_time = email["scheduled_time"]

        try:
            if not isinstance(scheduled_time, str):
                scheduled_time_str = scheduled_time.strftime("%Y-%m-%d %H:%M:%S")
            else:
                scheduled_time_str = scheduled_time

            email_data = {
                "sender_email": email["sender_email"],
                "sender_password": email["sender_password"],
                "recipient_email": email["recipient_email"],
                "subject": email["subject"],
                "message": email["message"],
                "scheduled_time": scheduled_time_str,
                "id": email_id,  # Ensure correct field name
            }

            scheduled_datetime = datetime.strptime(scheduled_time_str, "%Y-%m-%d %H:%M:%S")

            if scheduled_datetime <= current_datetime:
                send_email(email_data)
                update_email_status(email_id, "sent")
            else:
                delay_seconds = (scheduled_datetime - current_datetime).total_seconds()
                timer = threading.Timer(delay_seconds, send_email, args=(email_data,))
                timer.start()
                active_timers.append(timer)  # Track the timer
        except ValueError:
            print(f"Error parsing scheduled time for email ID: {email_id}")
        except KeyError as e:
            print(f"Missing required field: {e}")


import schedule
import time
from threading import Thread
from modules.birthday_email import send_email

def schedule_email(sender_email, sender_password, recipient_email, subject, message, schedule_time):
    def job():
        send_email(sender_email, sender_password, recipient_email, subject, message)

    try:

        schedule.every().day.at(schedule_time).do(job)

        # Run the scheduler in a separate thread
        thread = Thread(target=run_scheduler)
        thread.daemon = True
        thread.start()

        return f"Email scheduled successfully for {schedule_time}."
    except Exception as e:
        return f"Failed to schedule email: {e}"

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

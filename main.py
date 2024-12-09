from gui.menu import main_menu
from modules.scheduler import process_emails

def start_email_scheduler():
    """
    Initialize the email scheduler to process pending emails when the app starts.
    """
    print("Initializing Email Scheduler...")
    process_emails()
    print("Email Scheduler is running.")

if __name__ == "__main__":
    start_email_scheduler()
    main_menu()
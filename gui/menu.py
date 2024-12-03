import tkinter as tk
from tkinter import messagebox, simpledialog
from modules.countdown import start_countdown, parse_time_input
from modules.birthday_email import send_email  # Import the function above
from tkcalendar import Calendar
from datetime import datetime
import threading

def open_email_automation():
    email_window = tk.Toplevel()
    email_window.title("Automated Birthday Email")

    tk.Label(email_window, text="Sender Email:").grid(row=0, column=0, padx=10, pady=5)
    sender_email_entry = tk.Entry(email_window, width=40)
    sender_email_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(email_window, text="Sender Password:").grid(row=1, column=0, padx=10, pady=5)
    sender_password_entry = tk.Entry(email_window, width=40, show="*")
    sender_password_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(email_window, text="Recipient Email:").grid(row=2, column=0, padx=10, pady=5)
    recipient_email_entry = tk.Entry(email_window, width=40)
    recipient_email_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(email_window, text="Subject:").grid(row=3, column=0, padx=10, pady=5)
    subject_entry = tk.Entry(email_window, width=40)
    subject_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(email_window, text="Message:").grid(row=4, column=0, padx=10, pady=5)
    message_entry = tk.Text(email_window, height=5, width=30)
    message_entry.grid(row=4, column=1, padx=10, pady=5)

    # Add a calendar widget for date selection
    tk.Label(email_window, text="Select Date:").grid(row=5, column=0, padx=10, pady=5)
    calendar = Calendar(email_window, selectmode='day', date_pattern='yyyy-mm-dd')
    calendar.grid(row=5, column=1, padx=10, pady=5)

    # Add a time input field for hh:mm:ss
    tk.Label(email_window, text="Enter Time (hh:mm:ss):").grid(row=6, column=0, padx=10, pady=5)
    time_entry = tk.Entry(email_window, width=20)
    time_entry.grid(row=6, column=1, padx=10, pady=5)

    def send_email_button():
        sender_email = sender_email_entry.get()
        sender_password = sender_password_entry.get()
        recipient_email = recipient_email_entry.get()
        subject = subject_entry.get()
        message = message_entry.get("1.0", tk.END)

        # Get the selected date and time
        selected_date = calendar.get_date()  # yyyy-mm-dd format
        selected_time = time_entry.get().strip()  # Remove whitespace

        try:
            # Default time to midnight if not specified
            if not selected_time:
                selected_time = "00:00:00"

            # Combine selected date and time
            schedule_datetime = datetime.strptime(f"{selected_date} {selected_time}", "%Y-%m-%d %H:%M:%S")
            current_datetime = datetime.now()

            # Calculate delay in seconds
            delay_seconds = (schedule_datetime - current_datetime).total_seconds()

            if delay_seconds > 0:
                # Schedule email using threading.Timer
                threading.Timer(delay_seconds, send_email, args=(sender_email, sender_password, recipient_email, subject, message)).start()
                messagebox.showinfo("Scheduled", f"Email scheduled for {schedule_datetime}")
            else:
                messagebox.showerror("Error", "Selected time is in the past!")

        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Use hh:mm:ss.")

    send_button = tk.Button(email_window, text="Schedule Email", command=send_email_button)
    send_button.grid(row=7, column=0, columnspan=2, pady=10)

def open_countdown():
    try:
        time_input = simpledialog.askstring(
            "Countdown Timer",
            "Enter time in 'hh:mm:ss' format (e.g., 01:05:30 for 1 hour, 5 minutes, and 30 seconds):"
        )
        if time_input:
            seconds = parse_time_input(time_input)
            start_countdown(seconds)
            messagebox.showinfo("Info", "Hey, your time is up!")
        else:
            messagebox.showwarning("Warning", "Please enter a valid time.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error",f"An error occurred: {e}")

def open_screen_recorder():
    messagebox.showinfo("Info", "Opening Screen Recorder...")

def open_video_downloader():
    messagebox.showinfo("Info", "Opening Video Downloader...")

def main_menu():
    root = tk.Tk()
    root.title("Auto-Mate")

    tk.Label(root, text="Welcome to Auto-Mate", font=("Times New Roman", 16)).pack(pady=10)
    tk.Button(root, text="Automated B-day Email", command=open_email_automation).pack(pady=5)
    tk.Button(root, text="Automated Countdown", command=open_countdown).pack(pady=5)
    tk.Button(root, text="Screen Recorder", command=open_screen_recorder).pack(pady=5)
    tk.Button(root, text="YouTube Video Downloader", command=open_video_downloader).pack(pady=5)

    tk.Button(root, text="Exit", command=root.quit).pack(pady=20)
    root.mainloop()
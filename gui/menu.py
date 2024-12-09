import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
from modules.countdown import parse_time_input, run_countdown_with_progress_bar
from modules.db_utils import save_email_to_db
from modules.email_sender import send_email
from modules.screen_recorder import record_screen
from tkcalendar import Calendar
from datetime import datetime
import threading
from modules.video_downloader import download_video
from ttkthemes import ThemedTk

FONT_HEADER = ("Times New Roman", 16, "bold")
FONT_LABEL = ("Arial", 12)
FONT_ENTRY = ("Arial", 11)
FONT_BUTTON = ("Arial", 12)
COLOR_PRIMARY = "#2B547E"
COLOR_SECONDARY = "#D1E8E2"
COLOR_BACKGROUND = "#F7F9F9"

root = None
active_timers = []

def on_exit():
    global active_timers
    global root

    for timer in active_timers:
        if timer.is_alive():
            timer.cancel()

    print("All timers canceled. Exiting application.")

    if root is not None:
        root.destroy()
    else:
        print("Root window is not initialized.")

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

    tk.Label(email_window, text="Select Date:").grid(row=5, column=0, padx=10, pady=5)
    calendar = Calendar(email_window, selectmode='day', date_pattern='yyyy-mm-dd')
    calendar.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(email_window, text="Enter Time (hh:mm:ss):").grid(row=6, column=0, padx=10, pady=5)
    time_entry = tk.Entry(email_window, width=20)
    time_entry.grid(row=6, column=1, padx=10, pady=5)

    def send_email_button():
        sender_email = sender_email_entry.get()
        sender_password = sender_password_entry.get()
        recipient_email = recipient_email_entry.get()
        subject = subject_entry.get()
        message = message_entry.get("1.0", tk.END)

        selected_date = calendar.get_date()
        selected_time = time_entry.get().strip()

        try:
            if not selected_time:
                selected_time = "00:00:00"

            schedule_datetime = datetime.strptime(f"{selected_date} {selected_time}", "%Y-%m-%d %H:%M:%S")
            current_datetime = datetime.now()

            delay_seconds = (schedule_datetime - current_datetime).total_seconds()

            if delay_seconds > 0:
                email_data = {
                    "sender_email": sender_email,
                    "sender_password": sender_password,
                    "recipient_email": recipient_email,
                    "subject": subject,
                    "message": message,
                    "scheduled_time": schedule_datetime,
                }
                email_id = save_email_to_db(email_data)
                email_data["id"] = email_id


                timer = threading.Timer(delay_seconds, send_email, args=(email_data,))
                timer.start()


                global active_timers
                active_timers.append(timer)

                messagebox.showinfo("Scheduled", f"Email scheduled for {schedule_datetime}")
            else:
                messagebox.showerror("Error", "Selected time is in the past!")

        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Use hh:mm:ss.")

    send_button = tk.Button(email_window, text="Schedule Email", command=send_email_button)
    send_button.grid(row=7, column=0, columnspan=2, pady=10)

def open_countdown():
    while True:
        time_input = simpledialog.askstring(
            "Countdown Timer",
            "Enter time in 'hh:mm:ss' format (e.g., 01:05:30 for 1 hour, 5 minutes, and 30 seconds):"
        )

        if time_input:
            try:
                seconds = parse_time_input(time_input)

                countdown_window = tk.Tk()
                countdown_window.title("Countdown")

                progress_bar = ttk.Progressbar(countdown_window, orient="horizontal", length=200, mode="determinate")
                progress_bar.pack()
                progress_bar['maximum'] = seconds
                progress_bar['value'] = 0

                run_countdown_with_progress_bar(seconds, countdown_window, progress_bar)
                countdown_window.mainloop()

                break
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            return


def open_screen_recorder():
    try:
        duration = simpledialog.askstring("Screen Recording Duration", "Enter recording duration in seconds:")
        if not duration or not duration.isdigit() or int(duration) <= 0:
            raise ValueError("Please enter a positive integer.")

        duration_seconds = int(duration)
        record_screen(duration_seconds)
        messagebox.showinfo("Info", "Screen recording finished!")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def open_video_downloader():
    def start_download():

        video_url = url_entry.get().strip()
        if not video_url:
            messagebox.showerror("Error", "Please enter a valid YouTube URL.")
            return

        save_path = filedialog.askdirectory(title="Select Save Directory")
        if not save_path:
            save_path = "."  # Defaults to current directory if path is not chosen!!!

        result = download_video(video_url, save_path)
        messagebox.showinfo("Download Status", result)

    downloader_window = tk.Toplevel()
    downloader_window.title("YouTube Video Downloader")
    downloader_window.geometry("400x200")

    tk.Label(downloader_window, text="Enter YouTube Video URL:", font=("Arial", 12)).pack(pady=10)
    url_entry = tk.Entry(downloader_window, width=50, font=("Arial", 12))
    url_entry.pack(pady=5)

    download_button = tk.Button(downloader_window, text="Download", font=("Arial", 12), command=start_download)
    download_button.pack(pady=20)


def main_menu():
    global root
    root = ThemedTk(theme="arc")
    root.title("Auto-Mate")

    root.geometry("400x400")

    style = ttk.Style(root)
    style.configure("TButton", font=FONT_BUTTON, padding=5, background=COLOR_SECONDARY)
    style.configure("TLabel", font=FONT_LABEL, background=COLOR_BACKGROUND, foreground=COLOR_PRIMARY)

    tk.Label(root, text="Welcome to Auto-Mate", font=("Times New Roman", 18, "bold"), fg="#2B547E").pack(pady=15)

    ttk.Button(root, text="Automated B-day Email", command=open_email_automation).pack(pady=5)
    ttk.Button(root, text="Automated Countdown", command=open_countdown).pack(pady=5)
    ttk.Button(root, text="Screen Recorder", command=open_screen_recorder).pack(pady=5)
    ttk.Button(root, text="YouTube Video Downloader", command=open_video_downloader).pack(pady=5)

    exit_button = ttk.Button(root, text="Exit", command=on_exit)
    exit_button.pack(pady=10)

    root.protocol("WM_DELETE_WINDOW", on_exit)
    root.mainloop()
import threading
from tkinter import messagebox


def parse_time_input(time_input):

    try:
        hours, minutes, seconds = map(int, time_input.split(":"))
        if minutes > 59:
            raise ValueError("Chosen minutes should be between 0-59! Please try again.")
        elif seconds > 59:
            raise ValueError("Chosen seconds should be between 0-59! Please try again.")
        return hours * 3600 + minutes * 60 + seconds
    except ValueError as e:
        raise ValueError(str(e))

def run_countdown_with_progress_bar(seconds, root, progress_bar):
    if seconds <= 0:
        root.destroy()
        messagebox.showinfo("Time's Up", "Hey, your time is up!")
        return

    progress_bar['value'] += 1
    progress_bar.update()

    hours, remainder = divmod(seconds, 3600)
    minutes, seconds_left = divmod(remainder, 60)
    time_display = f"{hours:02d}:{minutes:02d}:{seconds_left:02d}"
    print(time_display, end="\r")

    root.after(1000, run_countdown_with_progress_bar, seconds - 1, root, progress_bar)

def start_countdown(seconds):
    # Create and start a new thread for the countdown
    countdown_thread = threading.Thread(target=run_countdown_with_progress_bar, args=(seconds,))
    countdown_thread.start()
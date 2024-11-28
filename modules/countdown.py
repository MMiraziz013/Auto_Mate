import time

import time

def parse_time_input(time_input):
    """Parses input in 'hh:mm:ss' format and converts it to total seconds."""
    try:
        hours, minutes, seconds = map(int, time_input.split(":"))
        return hours * 3600 + minutes * 60 + seconds
    except ValueError:
        raise ValueError("Invalid time format! Use 'hh:mm:ss' format.")

def start_countdown(seconds):
    """Starts the countdown from the given total seconds."""
    print(f"Countdown started for {seconds} seconds...")
    while seconds > 0:
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds_left = divmod(remainder, 60)
        time_display = f"{hours:02d}:{minutes:02d}:{seconds_left:02d}"
        print(time_display, end="\r")  # Print the timer on the same line
        time.sleep(1)
        seconds -= 1
    print("\nCountdown finished!")


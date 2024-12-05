import time

import time

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

def start_countdown(seconds):

    print(f"Countdown started for {seconds} seconds...")
    while seconds > 0:
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds_left = divmod(remainder, 60)
        time_display = f"{hours:02d}:{minutes:02d}:{seconds_left:02d}"
        print(time_display, end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nCountdown finished!")
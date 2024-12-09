import pyautogui
import cv2
import time
import numpy

def record_screen(duration_seconds):


    width, height = pyautogui.size()

    # Type of the video and codec used
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("screen_recording.avi", fourcc, 10.0, (width, height))  # Target FPS: 10

    target_fps = 10
    frame_duration = 1 / target_fps


    start_time = time.time()
    elapsed_time = 0

    # Loop which works until the time set by a user is not up.
    while elapsed_time < duration_seconds:
        frame_start = time.time()

        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_BGR2RGB)

        # Write frame to the video file
        out.write(frame)

        # Calculate how long to sleep to maintain the target frame rate
        frame_end = time.time()
        processing_time = frame_end - frame_start
        sleep_time = max(0, frame_duration - processing_time)

        time.sleep(sleep_time)

        # Update elapsed time
        elapsed_time = time.time() - start_time

    # Release resources
    out.release()
    cv2.destroyAllWindows()

    print("Screen recording finished!")

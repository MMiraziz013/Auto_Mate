import yt_dlp
import os


def download_video(url, save_path="."):
    """
    Downloads a YouTube video using yt-dlp.

    Args:
        url (str): The YouTube video URL.
        save_path (str): The directory to save the downloaded video.
    Returns:
        str: Success or error message.
    """
    try:
        # Ensure the save path exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Set download options
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        }

        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return f"Video downloaded successfully to {save_path}!"
    except Exception as e:
        return f"An error occurred: {e}"
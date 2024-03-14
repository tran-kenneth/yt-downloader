from pytube import YouTube


def download_video(url, output_path):
    """
    Downloads a video from a given URL and saves it to the specified output path.

    Args:
        url (str): The URL of the video to be downloaded.
        output_path (str): The path where the downloaded video will be saved.
    """
    try:
        # Initialize a YouTube object with the given URL
        yt = YouTube(url)

        # Get the highest resolution stream of the video
        video = yt.streams.get_highest_resolution()

        # Download the video to the specified output path
        video.download(output_path)

        # Print a success message if download is successful
        print("Download successful!")
    except Exception as e:
        # Print the error message if an exception occurs during the download process
        print("Error:", e)

from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError


# def download_video(url, output_path="."):
#     """
#     Downloads a YouTube video from the given URL
#     and saves it to the specified output path.

#     Args:
#         url (str): The URL of the YouTube video to download.
#         output_path (str): The path to the directory where
#         the video will be saved. Default is the current directory.

#     Raises:
#         Exception: If there is an error downloading the video.
#     """
#     try:
#         yt = YouTube(url)
#         print(f"Downloading: {yt.title}")
#         yt.streams.filter(
#             progressive=True,
#             file_extension=
#             'mp4').get_highest_resolution().download(output_path)
#         print(f"Video downloaded to: {output_path}")
#     except VideoUnavailable:
#         print(f"Error: The video at {url} is unavailable.")
#     except RegexMatchError:
#         print("Error: Invalid URL format.")
#     except Exception as e:
#         print(f"Error downloading video: {e}")
        
def download_video(url, output_path="."):
    try:
        yt = YouTube(url)
        # Comment out the title fetching to avoid the error
        # print(f"Downloading: {yt.title}")
        yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(output_path)
        print(f"Video downloaded to: {output_path}")
    except VideoUnavailable:
        print(f"Error: The video at {url} is unavailable.")
    except RegexMatchError:
        print("Error: Invalid URL format.")
    except Exception as e:
        print(f"Error downloading video: {e}")



if __name__ == "__main__":
    video_url = input("Enter the URL of the YouTube video to download: ")
    output_directory = input("""Enter the output directory
                             (leave blank for current directory): """)
    if output_directory.strip() == "":
        output_directory = "."
    download_video(video_url, output_directory)

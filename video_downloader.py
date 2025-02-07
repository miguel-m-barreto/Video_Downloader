import os
import argparse
import yt_dlp
import datetime

from utils import get_timestamp_output_folder

DEFAULT_OUTPUT_FOLDER = "Video_download_Folder"

# Download a video from YouTube using yt-dlp
def download_video(url, output_path='downloads', format='mp4', resolution='1080', audio_quality='320', allow_playlist=False, timestamp_folder=False):
    output_path = os.path.abspath(DEFAULT_OUTPUT_FOLDER) if output_path is None else os.path.abspath(output_path)
    
    # Create the output folder if it does not exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    if timestamp_folder:
        output_path = get_timestamp_output_folder(output_path)
   
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': not allow_playlist  # Allow playlist download if specified
    }
    
    if format == 'mp4':
        ydl_opts['format'] = f'bestvideo[height<={resolution}]+bestaudio/best'
    elif format == 'mp3':
        ydl_opts['format'] = f'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': audio_quality
        }]
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")

# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download videos in various formats and qualities.")
    
    parser.add_argument("url", help='URL of the video to download')
    parser.add_argument("format", choices=['mp4', 'mp3'], help="Output format (mp4/mp3)")
    parser.add_argument("--output_folder", help="Path to the output folder", default=DEFAULT_OUTPUT_FOLDER)
    parser.add_argument("--resolution", help="Resolution of the video (e.g., 2160, 1080, 720, etc.)", default='1080')
    parser.add_argument("--audio_quality", help="Audio quality of the mp3 file (e.g., 320, 192, 128)", default='320')
    parser.add_argument("--allow_playlist", help="Download playlist", action='store_true')
    parser.add_argument("--timestamp_folder", help="Add timestamp to the output folder", action='store_true')

    args = parser.parse_args()
    
    download_video(args.url, args.output_folder, args.format, args.resolution, args.audio_quality, args.allow_playlist, args.timestamp_folder)

"""
usage:
python video_downloader.py --help
python video_downloader.py https://www.youtube.com/watch?v=video_id mp4 --output_folder downloads --resolution 1080 --audio_quality 320 --allow_playlist --timestamp_folder
"""
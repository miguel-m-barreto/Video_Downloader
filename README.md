# Video Downloader

## Description

This script allows users to download videos and audio from YouTube and other supported platforms using `yt-dlp`. Users can choose the output format (MP4 or MP3), specify resolution or audio quality, and save the files in a timestamped output folder.

---

## Features

- Download videos in **MP4** format with selectable resolution (e.g., 2160p, 1080p, 720p, etc.).

- Download audio in **MP3** format with customizable quality (320kbps, 192kbps, 128kbps).

- Automatically creates a unique **timestamped output folder** to prevent overwriting files.

- Option to download entire **playlists**.

- Works with **YouTube and other supported sites** via `yt-dlp`.

---

## Requirements

Ensure you have the following dependencies installed before running the script:
```bash
    pip install yt-dlp
```

---

## Usage

Run the script from the command line:
```bash
    python video_downloader.py <URL> <format> [options]
```

---

## Arguments

| Argument | Description |
| URL | The link to the video or playlist to download. |
| format | Choose output format: mp4 for video, mp3 for audio. |

---

## Options

| Option | Description |
|----------|------------|
| --output_folder | Path to save downloaded files (default: Video_download_Folder). |
| --resolution |Set video resolution (e.g., 2160, 1080, 720). Default is best. |
| --audio_quality | Set MP3 quality (e.g., 320, 192, 128). Default is 320. |
| --allow_playlist | Download entire playlists if provided. |
| --timestamp_folder | Create a unique timestamped folder for each download. |

---

## Example Commands

Download MP4 Video at 1080p
```bash
    python video_downloader.py "https://youtube.com/xyz" mp4 --resolution 1080
```

Download MP3 Audio at 320kbps
```bash
    python video_downloader.py "https://youtube.com/xyz" mp3 --audio_quality 320
```

Download Entire Playlist
```bash
python video_downloader.py "https://youtube.com/playlist?list=XYZ" mp4 --allow_playlist
```

---

## Notes

- The script creates an output folder automatically if it does not exist.

- If --timestamp_folder is enabled, a unique folder with the current timestamp is created.

- The script supports multiple sites via yt-dlp, not just YouTube.

---

## License
This software is licensed under a **Custom Source-Available License**:

- You **can use this software freely**, including for YouTube, content creation, and personal projects.

- You **can share it**, but **must credit the author**.

- **You cannot modify, sell, or redistribute it without permission.**

**For full terms, see the [LICENSE](LICENSE) file.**

Copyright (C) 2025 Miguel Matos Barreto

---

## **Contact**
For special permissions, support, or business inquiries, contact:  
**Email:** ***I'll add it later***
&nbsp;

**GitHub** ***I'll add it later***
&nbsp;

**Portfolio Link** ***I'll add it later***
&nbsp;

**WebSite** ***I'll add it later***

# Youtube-Playlist-Download
# YouTube Playlist Downloader

Scripts to download videos from YouTube playlists using `pytube` and `yt-dlp`.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Get Video URLs](#get-video-urls)
  - [Download Videos](#download-videos)

## Requirements

- Python 3.x
- `pytube`
- `yt-dlp`
- `os`

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/YOUR_USERNAME/youtube-playlist-downloader.git
    cd youtube-playlist-downloader
    ```

2. **Install dependencies**:
    ```bash
    pip install pytube yt-dlp
    ```

## Usage

### Get Video URLs

This script fetches video URLs from a YouTube playlist and saves them to a text file.

1. **Run the script**:
    ```bash
    python get_video_urls.py
    ```

2. **Follow the prompt** to enter the YouTube playlist URL.

### Download Videos

This script reads video URLs from a text file and downloads them using `yt-dlp`.

1. **Run the script**:
    ```bash
    python download_videos.py
    ```

2. **Follow the prompt** to enter the desired video quality (e.g., highest, lowest, 720p, 1080p).

3. **Downloaded videos** will be saved in the `downloaded_videos` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



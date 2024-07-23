import os
import yt_dlp

# Function to download a video from a URL using yt-dlp
def download_video(url, download_path, quality):
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s')
    }

    # Set the quality option based on user input
    if quality == "highest":
        ydl_opts['format'] = 'best'
    elif quality == "lowest":
        ydl_opts['format'] = 'worst'
    else:
        ydl_opts['format'] = f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]'

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")

# Function to read URLs from a text file
def read_urls_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Main function
def main():
    input_file = "youtube_playlist_urls.txt"
    download_path = "downloaded_videos"

    # Prompt user for desired quality
    quality = input("Enter desired quality (highest, lowest, 720p, 1080p, etc.): ")

    # Create the download directory if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    urls = read_urls_from_file(input_file)

    for url in urls:
        download_video(url, download_path, quality)

    print(f"All videos have been downloaded to {download_path}")

if __name__ == "__main__":
    main()

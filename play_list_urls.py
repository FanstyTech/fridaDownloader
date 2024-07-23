from pytube import Playlist

# Function to get video URLs from a playlist
def get_video_urls(playlist_url):
    playlist = Playlist(playlist_url)
    return [video.watch_url for video in playlist.videos]

# Function to save URLs to a text file
def save_urls_to_file(urls, filename):
    with open(filename, 'w') as file:
        for url in urls:
            file.write(f"{url}\n")

# Main function
def main():
    playlist_url = input("Enter the YouTube playlist URL: ")
    urls = get_video_urls(playlist_url)
    filename = "youtube_playlist_urls.txt"
    save_urls_to_file(urls, filename)
    print(f"Video URLs have been saved to {filename}")

if __name__ == "__main__":
    main()

from pytube import YouTube
from tqdm import tqdm

def download_video(url, path="."):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"\n🎬 Title: {yt.title}")
        print(f"📺 Channel: {yt.author}")
        print(f"⏱ Duration: {yt.length // 60} min {yt.length % 60} sec")

        # Get highest resolution stream
        stream = yt.streams.get_highest_resolution()

        print("\n📥 Downloading...")
        stream.download(output_path=path)
        print("\n✅ Download completed!")

    except Exception as e:
        print(f"❌ Error: {e}")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = bytes_downloaded / total_size * 100
    tqdm.write(f"Progress: {percent:.2f}%", end="\r")

if __name__ == "__main__":
    video_url = input("🔗 Enter YouTube video URL: ")
    save_path = input("💾 Enter download path (leave blank for current folder): ") or "."
    download_video(video_url, save_path)

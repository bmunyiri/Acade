import yt_dlp

# 👇 Paste your video URLs here
video_urls = [
    "https://www.youtube.com/watch?v=iXzcJyjZ-Qo",
    "https://www.youtube.com/watch?v=l4lEZ9rh9QE",
    "https://www.youtube.com/watch?v=ObQ6Rh3XM10",
]

# Options: save to "downloads" folder, best quality
ydl_opts = {
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "format": "bestvideo+bestaudio/best",
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for url in video_urls:
        try:
            print(f"⬇️  Downloading: {url}")
            ydl.download([url])
            print(f"✅ Done: {url}\n")
        except Exception as e:
            print(f"❌ Failed: {url} — {e}\n")

print("All finished!")
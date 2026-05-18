import csv
import yt_dlp
from pathlib import Path

def download_video(url):
    Path("videos").mkdir(exist_ok=True)
    ydl_options = {"outtmpl": "videos/%(title)s.%(ext)s"}
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])

def read_video_urls(csv_path):
    videos = []
    with open(csv_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Recreating as a dictionary with 'title' and 'url'
            videos.append({"title": row["title"], "url": row["url"]})
            return videos
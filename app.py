from fastapi import FastAPI, Query
from yt_dlp import YoutubeDL

app = FastAPI()

@app.get("/J_emmons_07/download")
def download(url: str = Query(...)):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "format": "bestvideo+bestaudio/best"
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return {
        "author": "J_emmons_07",
        "title": info.get("title"),
        "formats": info.get("formats", [])
    }

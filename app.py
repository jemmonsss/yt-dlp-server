from fastapi import FastAPI, Query
from yt_dlp import YoutubeDL
import os

app = FastAPI()

@app.get("/J_emmons_07/download")
def download(url: str = Query(...)):
    if not os.path.exists("cookies.txt"):
        return {"error": "cookies.txt not found in project root. Make sure it’s included and in Netscape format."}

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "format": "bestvideo+bestaudio/best",
        "cookiefile": "cookies.txt"
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return {"error": str(e)}

    return {
        "author": "J_emmons_07",
        "title": info.get("title"),
        "formats": info.get("formats", [])
    }

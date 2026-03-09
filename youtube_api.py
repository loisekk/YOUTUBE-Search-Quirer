from googleapiclient.discovery import build
import os
from dotenv import load_dotenv




API_KEY ="AIzaSyCHHHpPjptqoIhwSsjsdprf2t7VQy-nGtU"

youtube = build("youtube", "v3", developerKey=API_KEY)

# ---------------- SEARCH VIDEOS ----------------
def search_videos(query, max_results=20):
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=max_results
    )
    response = request.execute()

    videos = []
    for item in response["items"]:
        videos.append({
            "video_id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"]
        })

    return videos


# ---------------- SEARCH SHORTS ----------------
def search_shorts(query, max_results=12):
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        videoDuration="short",   # 🔥 THIS IS THE KEY
        maxResults=max_results
    )
    response = request.execute()

    shorts = []
    for item in response["items"]:
        shorts.append({
            "video_id": item["id"]["videoId"],
            "title": item["snippet"]["title"]
        })

    return shorts



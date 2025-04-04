from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter, TextFormatter

import yt_dlp
import re
from pytube import Playlist

def get_video_urls(channel_url):
    playlist = Playlist(channel_url)

    # this fixes the empty playlist.videos list
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    return playlist.video_urls

def get_youtube_video_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko'])
    return " ".join(line['text'] for line in transcript)

def get_youtube_video_info(video_url):
    ydl_opts = {
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        return {
            "video_url": video_url,
            "video_id": video_info['id'],
            "title": video_info['title'],
            "channel": video_info['channel'],
            "caption": get_youtube_video_transcript(video_info['id'])
        }
    


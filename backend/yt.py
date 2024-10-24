from yt_dlp import YoutubeDL
import json
from data import write

def extract_title(url):
    ydl_opts = {
            'quiet': True, 
        'force_generic_extractor': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info['title']

def download_video(url):
    ydl_opts = {'extract_flat': 'discard_in_playlist',
    'final_ext': 'mp3',
    'format': 'bestaudio/best',
    'fragment_retries': 10,
    'ignoreerrors': 'only_download',
    'outtmpl': {'default': 'title'},
    'postprocessors': [{'key': 'FFmpegExtractAudio',
                     'nopostoverwrites': False,
                     'preferredcodec': 'mp3',
                     'preferredquality': '0'},
                    {'key': 'FFmpegConcat',
                     'only_multi_video': True,
                     'when': 'playlist'}],
    'retries': 10}
    
    with YoutubeDL(ydl_opts) as ydl:

if __name__ == '__main__':
    url ="https://www.youtube.com/watch?v=QBFldAy7joo" 
    #title = extract_title(url)
    #print(title)
    download_video(url)
    

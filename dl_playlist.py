from datetime import datetime
from pathlib import Path

from pytube import YouTube
from pytube import Playlist

from utility import Utility


def download_playlist(url):
    d = Utility()
    d.connecting_to_youtube()
    playlist = Playlist(url)
    print()
    time_date_suffix = datetime.now().strftime("_%y%m%d_%H%M%S")
    
    folder_name = 'YT_Download' + time_date_suffix
    file_path = Path.home() / 'Downloads' / folder_name

    if not file_path.is_dir():
        Path.mkdir(Path.home() / 'Downloads' / folder_name)

    for vid_url in playlist:
        vid_size = YouTube(vid_url).streams.get_highest_resolution().filesize
        p = Utility(vid_size)
        video = YouTube(vid_url, on_progress_callback=p.progress_bar)
        print(f'\nDownloading {video.title}')
        video.streams.get_highest_resolution().download(file_path)
        print()

    print(f'\nDownload complete.\nSaved to [{file_path}].')


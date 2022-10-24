'''
• readme file
• validation or error trapping
'''
import sys
from pathlib import Path

from pytube import YouTube

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


def progress_check(chunk = None, file_handle = None, remaining = None):
    '''Display progress bar.'''
    current = ((file_size - remaining) / file_size)
    percent = ('{0:.1f}').format(current * 100)
    progress = int(50 * current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(f' ↳ |{status}| {percent}%\r')
    sys.stdout.flush()

def main():
    download_path = Path.home() / 'Downloads'

    video_url = input('Video URL: ')
    video = YouTube(video_url, on_progress_callback=progress_check)

    video_size = video.streams.get_highest_resolution().filesize
    global file_size
    file_size = video_size

    print(f'\nTitle: {video.title}')
    print('\nDownloading...')

    yt = video.streams.get_highest_resolution()
    yt.download(download_path)
    print(f'\n\nDownload complete.\nVideo saved to {download_path}.')

if __name__ == '__main__':
    main()

"""
To do:
    - refactor codes
    - readme.me file (instructions)
"""
import logging
import sys

from utility import Utility
import dl_video
import dl_playlist

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


def main():
    logging.basicConfig(level=logging.DEBUG, format=' %(name)s - %(levelname)s - %(message)s')
    logging.disable(logging.CRITICAL)

    yt_url = input('Enter YouTube URL: ')

    u = Utility(url=yt_url)
    url_type = u.yt_url_type()

    if url_type == 'video':
        # Call dl_video.
        logging.debug(f'Call dl_video.download_video')
        dl_video.download_video(yt_url)
    
    elif url_type == 'playlist':
        # Call dl_playlist.
        logging.debug('Call dl_playlist.download_playlist')
        dl_playlist.download_playlist(yt_url)

    else:
        logging.debug('Youtube URL is invalid.')
        print('Error: URL is invalid.')


if __name__ == '__main__':
    main()

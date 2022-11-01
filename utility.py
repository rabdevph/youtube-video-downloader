import re
from time import sleep


class Utility:
    """Class for utility functions/methods."""

    def __init__(self, file_size=None, url=None):
        self.file_size = file_size
        self.url = url

    def progress_bar(self, chunk = None, file_handle = None, remaining = None):
        """Display progress bar."""

        BAR = chr(9608) # Character 9608 is '█'
        current = ((self.file_size - remaining) / self.file_size)
        percent = (f'{(current * 100):.1f}')
        progress = int(50 * current)
        status = BAR * progress + '-' * (50 - progress)
        print(f' ↳ |{status}| {percent}%\r', end='', flush=True)

    def yt_url_type(self):
        """Check YouTube url format if valid."""
        yt_regex = re.compile(r'''(
            (https://|http://)
            (www.youtube.com/watch\?v=)
            (.*)
            )''', re.VERBOSE)
        mo = yt_regex.search(self.url)
        if mo:
            # Check if playlist or video.
            if 'list=PL' in mo.group():
                return 'playlist'
            return 'video'
        return 'invalid'

    def connecting_to_youtube(self):
        """Print message before video download."""
        sleep(1)
        print('Connecting to YouTube. Please wait\r', end='', flush=True)
        sleep(1)
        print('Connecting to YouTube. Please wait.\r', end='', flush=True)
        sleep(1)
        print('Connecting to YouTube. Please wait..\r', end='', flush=True)
        sleep(1)
        print('Connecting to YouTube. Please wait...\r', end='', flush=True)


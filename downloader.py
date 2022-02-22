from pytube import YouTube
import os

user_profile = os.environ['USERPROFILE']
dl_path = user_profile + '/downloads'


def mp4(links, path=dl_path):
    """Downloads mp4 files to specified path

    Args:
        links (list): List of YT videos
        path (str, optional): Download path. Defaults to dl_path.
    """
    for video in links:
        yt = YouTube(video)
        title = clean_title(yt.title)
        print(f'Downloading {title}')
        yt.streams.get_highest_resolution().download(filename=f'{title}.mp4', output_path=path)
        print(f'{title} has been downloaded.')


def mp3(links, path=dl_path):
    """Downloads mp3 files to specified path

    Args:
        links (list): List of YT videos
        path (str, optional): Download path. Defaults to dl_path.
    """
    for video in links:
        yt = YouTube(video)
        title = clean_title(yt.title)
        print(f'Downloading {title}')
        yt.streams.get_audio_only().download(filename=f'{title}.mp3', output_path=path)
        print(f'{title} has been downloaded')


def clean_title(title: str):
    """Reorganizes file names to conform to windows standards

    Args:
        title (str): Title

    Returns:
        str: Returns string without reserved characters
    """
    REMOVE = '|"?\/<>:*'

    for character in REMOVE:
        title = title.replace(character, '')

    return title

from pytube import YouTube
import os

user_profile = os.environ['USERPROFILE']
dl_path = user_profile + '/downloads'


def mp4(links):
    for video in links:
        yt = YouTube(video)
        title = yt.title
        print(f'Downloading {title}')
        yt.streams.get_highest_resolution().download(filename=f'{title}.mp4', output_path=dl_path)
        print(f'{title} has been downloaded.')


def mp3(links):
    for video in links:
        yt = YouTube(video)
        title = yt.title
        print(f'Downloading {title}')
        yt.streams.get_audio_only().download(filename=f'{title}.mp3', output_path=dl_path)
        print(f'{title} has been downloaded')

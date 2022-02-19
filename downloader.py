from pytube import YouTube


def mp4(links):
    for video in links:
        yt = YouTube(video)
        title = yt.title
        yt.streams.get_highest_resolution().download(filename=f'{title}.mp4')
        print(f'{title} has been downloaded.')


def mp3(links):
    for video in links:
        yt = YouTube(video)
        title = yt.title
        yt.streams.get_audio_only().download(filename=f'{title}.mp3')
        print(f'{title} has been downloaded')

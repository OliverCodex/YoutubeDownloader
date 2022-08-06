from pytube import YouTube
from pytube import Playlist
import re
import os

class Text():
    download_done = 'Download done.'
    best_audio = 'Downloading from best audio stream by default, change? (leave blank to skip):\n>>'
    def start(title, url, isPlaylist):
        if isPlaylist == True:
            text = 'playlist'
        else:
            text = 'video'
        print("Downloading " + text + " \"" + title + "\" from \"" + url + "\".....\n")
    def download_error(title):
        print('ERROR: failed to download \"' + title + '\". \n')
    def conversion_error(title):
        print('ERROR: failed to convert \"' + title + '\". ')
    def done(title, isPlaylist):
        if isPlaylist == True:
            text = 'playlist'
        else:
            text = 'video'
        print("Finished downloading " + text + " \"" + title + "\".\n")
    def main(default_path):
        url = input("Enter a YouTube URL:\n>>")
        path = input("\nEnter directory or leave blank for default, \"" + default_path + "\":\n>>") or default_path
        return url, path
    
def rename(dir):
    for filename in os.listdir(dir):
        base, ext = os.path.splitext(filename)
        name = input("Please enter a new name (leave blank to skip): \n" + base + "       " + ext + "\n>>") or base
        new_file = name + ext 
        os.rename(os.path.join(dir, filename), os.path.join(dir, new_file))

def isPlaylist(url, path):
    if 'playlist' in url:
        download_playlist(url, path)
    else:
        download_video(url, path)

def download_playlist(url, path):
    yt = Playlist(url)

    Text.start(yt.title, yt.playlist_url, True)

    # this fixes the empty playlist.videos list
    yt._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    for video in yt.videos:
        Text.start(video.title, video.watch_url, False)
        try:
            # audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
            audioStream = video.streams.get_audio_only()
            audioStream.download(output_path=path) 
            Text.done(video.title, False)
            # file = video.title + ".mp4"
            # convert(dir, ext, file)
        except:
            Text.download_error(video.title)
    Text.done(yt.title, True)


def download_video(url, path):
    yt = YouTube(url)

    Text.start(yt.title, yt.watch_url, False)

    # print(Text.best_audio)
    # show_streams = input() or False
    # if show_streams != False:
    #     for streams in yt.streams:
    #         print(streams)
    #     stream = yt.streams.get_by_itag(input("Enter your new stream itag:\n>>"))
    # else:
    #     stream = yt.streams.get_audio_only()
    stream = yt.streams.get_audio_only()
    try:
        stream.download(output_path=path)

        


        #file = video.title + ".mp4"
        #convert(dir, ext, file)
    except:
        Text.download_error(yt.title)

    Text.done(yt.title, False)
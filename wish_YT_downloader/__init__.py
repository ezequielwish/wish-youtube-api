import moviepy.editor as mp
from pytube import YouTube
import os

PATH = "./download"

class Video:
    def __init__(self, url):
        self.url = url
        self.yt = YouTube(url)

    @staticmethod
    def format_title(title, no_spaces=False):
        '''Turns the video title valid to Windows OS filenames'''
        new = []
        for char in title: # Separate only valid characters and put on the list
            if char == ' ':
                if no_spaces:
                    new.append('_')
                else:
                    new.append(char)
            elif char == '|':
                new.append('-')
            elif char.lower() in (r'aáàãâbcdeéèêfghiíìjklmnopqrstuvwxyz0987654321([{}])$&~#@!-".,?'):
                new.append(char)
        new = ''.join(new).strip() # Convert list into a string
        if len(new) <= 50: # 50 charactere is a good lenght to filenames
            return new
        else:
            return new[:45]+'...' # Return only the first 50 characteres to bypass Filename Lenght eror

    @staticmethod
    def convert_mp4_to_mp3(path, filename):
        print("Converting to MP3...")
        with mp.AudioFileClip(f'{path}\{filename}.mp4') as audioclip:
            audioclip.write_audiofile(f'{path}\{filename}.mp3')
        os.remove(f'{path}/{filename}.mp4') # Delete the .mp4
        print('Done!')

    def download(self, quality):
        '''Download the video in High Quality, Low Quality or MP3'''
        filename = self.format_title(self.yt.title[:])
        if quality == '-MP3-':
            '''The button pressed is Audio MP3, so download as audio .mp4 and convert to .mp3'''
            print('Downloading audio only...')
            video = self.yt.streams.get_audio_only()
            video.download(PATH, filename=f'{filename}.mp4') # Download in the specified folder (path)
            self.convert_mp4_to_mp3(PATH, filename)
            filename += '.mp3'
        elif quality == '-HQ-':
            '''Select the highest resolution and download them'''
            print('Downloading in the highest quality available...')
            filename += ' [HQ].mp4'
            video = self.yt.streams.get_highest_resolution()
            video.download(PATH, filename=f'{filename}')
        elif quality == '-LQ-':
            '''Select the lowest resolution and download them'''
            print('Downloading in the lowest quality available...')
            filename += ' [LQ].mp4'
            video = self.yt.streams.get_lowest_resolution()
            video.download(PATH, filename=f'{filename}')
        print('Download done!')
        return filename

    @staticmethod
    def delete_file(filename):
        os.remove(PATH+'/'+filename)

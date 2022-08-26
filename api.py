from flask import Flask, send_from_directory
from wish_YT_downloader import Video

path = './download/'
api = Flask(__name__)  

@api.route('/<video_id>/LQ')
def low_quality(video_id):
    video = Video(f'https://www.youtube.com/watch?v={video_id}')
    filename = video.download('-LQ-')
    return send_from_directory(path, filename, as_attachment=True)

@api.route('/<video_id>/HQ')
def high_quality(video_id):
    video = Video(f'https://www.youtube.com/watch?v={video_id}')
    filename = video.download('-HQ-')
    return send_from_directory(path, filename, as_attachment=True)

@api.route('/<video_id>/MP3')
def in_mp3(video_id):
    video = Video(f'https://www.youtube.com/watch?v={video_id}')
    filename = video.download('-MP3-')
    return send_from_directory(path, filename, as_attachment=True)


if __name__ == "__main__":
    api.run()

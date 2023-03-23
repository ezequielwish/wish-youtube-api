from flask import Flask, send_from_directory, request
from wish_YT_downloader import Video, PATH

path = PATH+'/'
api = Flask(__name__)

@api.route('/download', methods= ['POST'])
def download():
    videoID = request.args.get('v', '')
    quality = request.args.get('q', '')
    video = Video(f'https://www.youtube.com/watch?v={videoID}')
    filename = video.download(f'-{quality}-')
    return send_from_directory(path, filename, as_attachment=True)


if __name__ == "__main__":
    api.run(debug=True)

from common.util import ky_requests
from common.download import ky_ffmpeg, ky_constants
import os


def _download(path, url, file_name, check=True):
    if os.path.exists(path) and check:
        print('>--- 该文件已经存在，不进行下载操作 ---<')
        return

    if url is None or len(url) == 0:
        return
    response = ky_requests.get(url=url)
    with open(path, 'wb') as f:
        f.write(response.content)
    print(file_name + ' 已经下载完成 --------')


def download_audio(audio_lists, index):
    audio = audio_lists[index]
    audio_path = ky_constants.AUDIO_DIR + audio["title"] + ".mp3"
    audio_url = audio["audio_url"]

    _download(path=audio_path, url=audio_url, file_name=audio["title"])


def download_movie(movie_lists, index):
    movie = movie_lists[index]
    movie_path = ky_constants.MOVIE_DIR + movie["title"] + ".mp4"
    if os.path.exists(movie_path):
        print('>--- 该视频已经存在，不进行下载操作 ---<')
        return

    audio_url = movie["audio_url"]
    _download(path=ky_constants.TMP_FILE_MP3, url=audio_url, file_name="tmp.mp3", check=False)

    movie_url = movie["movie_url"]
    _download(path=ky_constants.TMP_FILE_MP4, url=movie_url, file_name="tmp.mp4", check=False)

    ky_ffmpeg.merge_audio_and_video(movie_path)
    print(movie["title"] + " 已经下载完成 --------")

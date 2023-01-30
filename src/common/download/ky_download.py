from common.util import ky_requests
from common.download import ky_ffmpeg, ky_constants
import os


def download_audio(audio_lists, index=0):
    audio = audio_lists[index]
    # 创建文件夹
    if not os.path.exists(ky_constants.AUDIO_DIR):
        os.makedirs(ky_constants.AUDIO_DIR)

    audio_path = ky_constants.AUDIO_DIR + audio["title"] + ".mp3"
    audio_url = audio["audio_url"]
    _download(path=audio_path, url=audio_url, file_name=audio["title"])


def download_movie(movie_lists, index=0):
    movie = movie_lists[index]
    # 创建文件夹
    if not os.path.exists(ky_constants.MOVIE_DIR):
        os.makedirs(ky_constants.MOVIE_DIR)
    # 避免重复下载
    movie_path = ky_constants.MOVIE_DIR + movie["title"] + ".mp4"
    if os.path.exists(movie_path):
        print('>--- 该视频已经存在，不进行下载操作 ---<')
        return

    # 音频下载
    audio_url = movie["audio_url"]
    _download(path=ky_constants.TMP_FILE_MP3, url=audio_url, file_name="tmp.mp3", check=False)
    # 视频下载
    movie_url = movie["movie_url"]
    _download(path=ky_constants.TMP_FILE_MP4, url=movie_url, file_name="tmp.mp4", check=False)
    # 音视频合并
    ky_ffmpeg.merge_audio_and_video(movie_path)

    # 下载完成提示
    print(movie["title"] + " 已经下载完成 --------")


def _download(path, url, file_name, check=True):
    # 避免重复下载
    if os.path.exists(path) and check:
        print('>--- 该文件已经存在，不进行下载操作 ---<')
        return
    # 判断url是否正确
    if url is None or len(url) == 0:
        return
    # 下载文件
    response = ky_requests.get(url=url)
    with open(path, 'wb') as f:
        f.write(response.content)
    # 下载完成提示
    print(file_name + ' 已经下载完成 --------')

from common.download import ky_constants
import subprocess
import os


# 合并音视频
def merge_audio_and_video(movie_path):
    # 合并音视频
    cmd = []
    cmd.extend(["ffmpeg -i ", ky_constants.TMP_FILE_MP3, " -i ", ky_constants.TMP_FILE_MP4, " -c:v copy -c:a aac -strict experimental ", ky_constants.OUTPUT_FILE_MP4])
    cmd = "".join(cmd)
    print(cmd)
    subprocess.call(cmd, shell=True)

    # 修改文件名
    os.rename(ky_constants.OUTPUT_FILE_MP4, movie_path)
    print('>--- 音视频合并成功 ---<')
    # 删除下载下来的临时文件
    os.remove(ky_constants.TMP_FILE_MP3)
    os.remove(ky_constants.TMP_FILE_MP4)

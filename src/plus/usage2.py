from common.download import ky_constants, ky_download
from common.lib import ky_bilibili
from plus import tool, usage1


# 指定多个收藏夹，将音频保存在不同的目录中
def get_all_audio_by_favorites(*favorites):
    result_map = {}

    # 获取不同的收藏夹的音频信息
    for favorite in favorites:
        result_map[favorite] = usage1.get_all_audio_by_favorite(favorite)

    return result_map


def download_all_songs_by_favorites_map(favorites_map):
    old_path = ky_constants.AUDIO_DIR

    for key in favorites_map:
        # 获取收藏夹名字
        favorite_name = ky_bilibili.get_favorite_name_by_favorite_id(key)
        # 修改下载路径
        ky_constants.AUDIO_DIR = old_path + ('{}_{}/'.format(key, favorite_name))

        favorite_audio = favorites_map[key]
        for index in range(0, len(favorite_audio)):
            tool.execute_function(lambda: ky_download.download_audio(favorite_audio, index))

    # 恢复下载路径
    ky_constants.AUDIO_DIR = old_path

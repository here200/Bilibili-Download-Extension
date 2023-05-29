from plus import usage1, tool, usage2
from common.download import ky_download


if __name__ == '__main__':
    # 第一种方法
    # all_songs = usage1.get_all_audio_by_favorite("1598050455")
    # for index in range(0, len(all_songs)):
    #     tool.execute_function(lambda: ky_download.download_audio(all_songs, index))

    # 第二种方法
    # all_movies = usage1.get_all_selections_by_one_movie("https://www.bilibili.com/video/BV1GE411R7sE")
    # for index in range(0, len(all_movies)):
    #     tool.execute_function(lambda: ky_download.download_movie(all_movies, index))

    # 第三种方法
    favorites_map = usage2.get_all_audio_by_favorites("1598050455")
    usage2.download_all_songs_by_favorites_map(favorites_map)

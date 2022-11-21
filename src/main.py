from plus import bilibili_plus
from common.download import ky_download
from common.util import ky_debugs


if __name__ == '__main__':
    # 第一种方法
    all_songs = bilibili_plus.get_all_audio_by_favorite("1598050455")
    ky_debugs.print_container_elements(all_songs)
    # for index in range(0, len(all_songs)):
    #     try:
    #         ky_download.download_audio(all_songs, index)
    #     except Exception:
    #         continue

    # 第二种方法
    # all_movies = bilibili_plus.get_all_selections_by_one_movie("https://www.bilibili.com/video/BV1GE411R7sE")
    # ky_debugs.print_container_elements(all_movies)
    # for index in range(0, len(all_movies)):
    #     try:
    #         ky_download.download_movie(all_movies, index)
    #     except Exception:
    #         continue

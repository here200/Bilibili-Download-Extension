from common.lib import ky_bilibili
from plus import tool


# 根据一个视频链接，获取该视频链接下，所有的选集
def get_all_selections_by_one_movie(url):
    ret_list = []
    # 获取所有的标题
    titles = ky_bilibili.get_all_titles_by_one_movie(url=url)
    for title in titles:
        params = {
            "p": title["index"]
        }
        try:
            ky_bilibili.get_title_href_by_one_movie(url=url, movie_lists=ret_list, params=params, need_title=False)
            ret_list[title['index'] - 1]["title"] = title["title"]
        except Exception:
            continue

    # 打印信息
    tool.print_container_elements(ret_list)

    return ret_list


# 获取单个收藏夹的所有音频信息
def get_all_audio_by_favorite(favorite):
    # 获取单个收藏夹里所有的视频信息
    favorite_lists = ky_bilibili.get_favorites_movie_lists(favorite)

    ret_lists = []
    for fl in favorite_lists:
        try:
            _url = ky_bilibili.get_url_by_av_id(fl["avid"])
            ky_bilibili.get_title_href_by_one_movie(url=_url, movie_lists=ret_lists, need_movie_url=False, need_title=False)
            ret_lists[len(ret_lists)-1]["title"] = fl["title"]
        except Exception:
            continue

    # 打印信息
    tool.print_container_elements(ret_lists)

    return ret_lists

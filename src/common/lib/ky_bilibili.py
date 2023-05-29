from common.util import ky_requests, ky_jsons, ky_res, ky_etrees


# 获取用户的所有收藏夹信息
def get_user_favorites(user_id):
    _url = 'https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid=' + user_id
    tmp = ky_requests.decode_response(ky_requests.get(url=_url))
    ky_jsons.cache = ky_jsons.json_string2python_object(tmp)
    favorites_data = ky_jsons.get_one_data("$.data.list")

    ret_list = []
    # 提取收藏夹的数据(名字，收藏夹id，收藏夹的视频个数)
    for index in range(0, len(favorites_data)):
        el = favorites_data[index]
        ret_list.append({
            'index': index,
            'fav_name': el['title'],
            'fav_id': el['id'],
            'media_count': el['media_count']
        })
    # 返回收藏夹列表
    return ret_list


# 获取单个收藏夹的所有视频信息
def get_favorites_movie_lists(favorites):
    ret_lists = []

    _url = 'https://api.bilibili.com/x/v3/fav/resource/list'
    # 是否还有视频数据
    has_more = True
    # 第n页，每页默认展示20个视频信息
    page = 1
    params = {
        'media_id': favorites,
        'ps': 20
    }
    while has_more:
        params["pn"] = page
        tmp = ky_requests.decode_response(ky_requests.get(url=_url, params=params))
        ky_jsons.cache = ky_jsons.json_string2python_object(tmp)
        media_lists = ky_jsons.get_one_data("$..data.medias")

        # 获取每条视频的标题、av号
        for index in range(0, len(media_lists)):
            el = media_lists[index]
            ret_lists.append({
                'index': len(ret_lists),
                'title': el['title'],
                'avid': el['id']
            })
        # 查询是否还有更多数据，如果有,让page++
        has_more = ky_jsons.get_one_data("$..has_more")
        if has_more is True:
            page += 1

    return ret_lists


# 获取单个收藏夹的名称
def get_favorite_name_by_favorite_id(favorite):
    _url = 'https://api.bilibili.com/x/v3/fav/resource/list'
    params = {
        'media_id': favorite,
        'ps': 20,
        'pn': 1
    }

    tmp = ky_requests.decode_response(ky_requests.get(url=_url, params=params))
    ky_jsons.cache = ky_jsons.json_string2python_object(tmp)
    favorite_title = ky_jsons.get_one_data("$..data.info.title")

    return favorite_title


# 根据b站的av号生成链接
def get_url_by_av_id(av_id):
    return "https://www.bilibili.com/video/av" + str(av_id)


# 根据b站的bv号生成链接
def get_url_by_bv_id(bv_id):
    return "https://www.bilibili.com/video/BV" + str(bv_id)


# 根据url获取每个视频的标题、音频链接、视频链接
def get_title_href_by_one_movie(url, movie_lists, params=None, need_movie_url=True, need_title=True):
    ky_res.cache = ky_requests.decode_response(ky_requests.get(url=url, params=params))
    res_data = ky_res.get_one_data(r'<script>window.__playinfo__=(.*?)</script>')

    # 1. 提取音频链接、视频链接
    ky_jsons.cache = ky_jsons.json_string2python_object(res_data)
    audio_url = ky_jsons.get_one_data("$.data.dash.audio..baseUrl")
    movie_url = None
    if need_movie_url:
        movie_url = ky_jsons.get_one_data("$.data.dash.video..baseUrl")

    # 2.提取标题(对标题中的不合理字符进行过滤)
    title = None
    if need_title:
        ky_etrees.html_cache = ky_etrees.generate_html_by_string(ky_res.cache)
        title = _remove_chars(ky_etrees.get_one_data_by_xpath('//title/text()'))

    movie_lists.append({
        "index": len(movie_lists),
        "title": title,
        "audio_url": audio_url,
        "movie_url": movie_url
    })


# 根据单个视频url，获取选集的所有标题
def get_all_titles_by_one_movie(url):
    ky_res.cache = ky_requests.decode_response(ky_requests.get(url=url))
    tmp = ky_res.get_one_data(r'<script>window.__INITIAL_STATE__=(.*?);\(function\(\).*?</script>')
    ky_jsons.cache = ky_jsons.json_string2python_object(tmp)
    titles = ky_jsons.get_data("$..pages..part")

    ret_lists = []
    for t in titles:
        ret_lists.append({
            'index': len(ret_lists) + 1,
            'title': _remove_chars(t)
        })
    return ret_lists


def _remove_chars(string):
    return string.replace('_哔哩哔哩_bilibili', ''). \
        replace('/', '_'). \
        replace('\\', '_')

def remove_chars(string):
    return string.replace('_哔哩哔哩_bilibili', ''). \
        replace('/', '_'). \
        replace('\\', '_')

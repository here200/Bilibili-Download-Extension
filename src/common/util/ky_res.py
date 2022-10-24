import re

cache = None


def get_data(pattern, string=None):
    if string is None:
        string = cache
    return re.findall(pattern=pattern, string=string)


def get_one_data(pattern, string=None):
    return get_data(pattern=pattern, string=string)[0]

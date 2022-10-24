from lxml import etree

html_cache = None


def generate_html_by_string(string):
    return etree.HTML(string)


def get_data_by_xpath(xpath, html=None):
    if html is None:
        html = html_cache
    return html.xpath(xpath)


def get_one_data_by_xpath(xpath, html=None):
    return get_data_by_xpath(xpath, html)[0]

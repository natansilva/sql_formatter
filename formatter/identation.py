import re


def remove_all_tabs(text_to_format):
    return re.sub('\t', '', text_to_format)

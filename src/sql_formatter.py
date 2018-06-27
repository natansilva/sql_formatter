import config as cfg
import re


def upper_sql_functions(text_to_format):
    for function_token in cfg.sql_functions:
        text_to_format = re.sub(function_token + '[\s]?\(', function_token + '(', text_to_format)

    return text_to_format

import re

newline_tokens = [
    'SELECT', 'FROM', 'WHERE', 'SET', 'ORDER BY', 'GROUP BY',  'DROP',
    'VALUES', 'UPDATE', 'HAVING', 'ADD', 'AFTER', 'ALTER TABLE', 'DELETE FROM',
    'UNION ALL', 'UNION'
    ]

same_line_tokens = [
    'LIMIT', 'LEFT OUTER JOIN', 'RIGHT OUTER JOIN', 'LEFT JOIN', 'RIGHT JOIN',
    'OUTER JOIN', 'INNER JOIN', 'JOIN', 'XOR', 'OR', 'AND'
    ]


def format_new_line_tokens(text_to_format):
    for token in newline_tokens:
        text_to_format = re.sub(
            token + '[\s\n\t]*',
            token + '\n',
            text_to_format,
            flags=re.IGNORECASE
        )
    return text_to_format


def format_same_line_tokens(text_to_format):
    for token in same_line_tokens:
        text_to_format = re.sub(
            token + '[\s]',
            token + ' ',
            text_to_format,
            flags=re.IGNORECASE
        )
    return text_to_format

import formatter.clauses as cl


def test_format_new_line_tokens():
    assert cl.format_new_line_tokens('SELECT') == 'SELECT\n\t  '


def test_format_new_line_tokens_with_space():
    assert cl.format_new_line_tokens('SELECT ') == 'SELECT\n\t  '


def test_format_new_line_tokens_with_break_line():
    assert cl.format_new_line_tokens('SELECT\n') == 'SELECT\n\t  '


def test_format_new_line_tokens_with_tab_token():
    assert cl.format_new_line_tokens('SELECT\t') == 'SELECT\n\t  '


def test_format_new_line_tokens_with_tab():
    assert cl.format_new_line_tokens('SELECT ') == 'SELECT\n\t  '


def test_format_new_line_tokens_with_break_line_and_tab_token():
    assert cl.format_new_line_tokens('SELECT\n\t') == 'SELECT\n\t  '


def test_format_new_line_tokens_with_break_line_and_tab():
    assert cl.format_new_line_tokens('SELECT\n   ') == 'SELECT\n\t  '


def test_format_same_line_tokens_with_space():
    assert cl.format_same_line_tokens('LIMIT ') == 'LIMIT '


def test_format_same_line_tokens_with_tab():
    assert cl.format_same_line_tokens('LIMIT ') == 'LIMIT '


def test_format_same_line_tokens_with_tab_token():
    assert cl.format_same_line_tokens('LIMIT\t') == 'LIMIT '


def test_format_same_line_tokens_with_break_line():
    assert cl.format_same_line_tokens('LIMIT\n') == 'LIMIT '

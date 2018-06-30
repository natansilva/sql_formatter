import formatter.clauses as cl


def test_formatter_new_line_tokens():
    assert cl.formatter_new_line_tokens('SELECT') == 'SELECT\n'


def test_formatter_new_line_tokens_with_space():
    assert cl.formatter_new_line_tokens('SELECT ') == 'SELECT\n'


def test_formatter_new_line_tokens_with_break_line():
    assert cl.formatter_new_line_tokens('SELECT\n') == 'SELECT\n'


def test_formatter_new_line_tokens_with_tab_token():
    assert cl.formatter_new_line_tokens('SELECT\t') == 'SELECT\n'


def test_formatter_new_line_tokens_with_tab():
    assert cl.formatter_new_line_tokens('SELECT ') == 'SELECT\n'


def test_formatter_new_line_tokens_with_break_line_and_tab_token():
    assert cl.formatter_new_line_tokens('SELECT\n\t') == 'SELECT\n'


def test_formatter_new_line_tokens_with_break_line_and_tab():
    assert cl.formatter_new_line_tokens('SELECT\n   ') == 'SELECT\n'


def test_formatter_same_line_tokens_with_space():
    assert cl.formatter_same_line_tokens('LIMIT ') == 'LIMIT '


def test_formatter_same_line_tokens_with_tab():
    assert cl.formatter_same_line_tokens('LIMIT ') == 'LIMIT '


def test_formatter_same_line_tokens_with_tab_token():
    assert cl.formatter_same_line_tokens('LIMIT\t') == 'LIMIT '


def test_formatter_same_line_tokens_with_break_line():
    assert cl.formatter_same_line_tokens('LIMIT\n') == 'LIMIT '

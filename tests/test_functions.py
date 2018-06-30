from formatter import formatter as sf


def test_upper_sql_functions_with_spaces():
    assert sf.format_sql_functions('round (') == 'ROUND('


def test_upper_sql_functions_without_spaces():
    assert sf.format_sql_functions('round(') == 'ROUND('


def test_upper_sql_functions_with_break_line():
    assert sf.format_sql_functions('round\n(') == 'ROUND('

import sql_formatter as sf

def test_upper_sql_functions():
    assert sf.upper_sql_functions('ROUND (') == 'ROUND('

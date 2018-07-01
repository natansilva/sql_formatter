import formatter.formatter as fm
import pytest
import os

dirname = os.path.dirname(__file__)


@pytest.mark.skip(reason='in development')
def test_format_file_simple():
    filename = os.path.join(dirname, 'simple_input_string.sql')
    simple_input_file = open(filename, 'r')
    simple_input_string = simple_input_file.read()
    simple_input_file.close()

    filename = os.path.join(dirname, 'simple_expected_string.sql')
    simple_expected_file = open(filename, 'r')
    simple_expected_string = simple_expected_file.read()
    simple_expected_file.close()

    assert fm.format_file(simple_input_string) == simple_expected_string

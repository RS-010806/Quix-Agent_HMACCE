import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from python_testcases.load_testdata import load_json_testcases

if pytest.use_correct:
    from correct_python_programs.is_valid_parenthesization import is_valid_parenthesization
else:
    from python_programs.is_valid_parenthesization import is_valid_parenthesization


testdata = load_json_testcases(is_valid_parenthesization.__name__)

 
@pytest.mark.parametrize("input_data,expected", testdata)
def test_is_valid_parenthesization(input_data, expected):
    assert is_valid_parenthesization(*input_data) == expected

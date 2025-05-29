import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from python_testcases.load_testdata import load_json_testcases

if pytest.use_correct:
    from correct_python_programs.lcs_length import lcs_length
else:
    from python_programs.lcs_length import lcs_length


testdata = load_json_testcases(lcs_length.__name__)
 

@pytest.mark.parametrize("input_data,expected", testdata)
def test_lcs_length(input_data, expected):
    assert lcs_length(*input_data) == expected

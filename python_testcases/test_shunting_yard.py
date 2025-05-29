import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from python_testcases.load_testdata import load_json_testcases

if pytest.use_correct:
    from correct_python_programs.shunting_yard import shunting_yard
else:
    from python_programs.shunting_yard import shunting_yard
 

testdata = load_json_testcases(shunting_yard.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_shunting_yard(input_data, expected):
    assert shunting_yard(*input_data) == expected

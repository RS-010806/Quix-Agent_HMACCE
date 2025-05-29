import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from python_testcases.load_testdata import load_json_testcases
from python_testcases.node import Node

if pytest.use_correct:
    from correct_python_programs.subsequences import subsequences
else:
    from python_programs.subsequences import subsequences


testdata = load_json_testcases(subsequences.__name__)

 
@pytest.mark.parametrize("input_data,expected", testdata)
def test_subsequences(input_data, expected):
    assert subsequences(*input_data) == expected

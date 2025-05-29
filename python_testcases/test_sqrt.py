import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from python_testcases.load_testdata import load_json_testcases
from python_testcases.node import Node

if pytest.use_correct:
    from correct_python_programs.sqrt import sqrt
else:
    from python_programs.sqrt import sqrt


testdata = load_json_testcases(sqrt.__name__)

 
@pytest.mark.parametrize("input_data,expected", testdata)
def test_sqrt(input_data, expected):
    assert sqrt(*input_data) == pytest.approx(expected, abs=input_data[-1])

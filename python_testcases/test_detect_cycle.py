import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from python_testcases.load_testdata import load_json_testcases
from python_programs.detect_cycle import detect_cycle
import pytest
testdata = load_json_testcases('detect_cycle')
@pytest.mark.parametrize("input_data,expected", testdata)
def test_detect_cycle(input_data, expected):
    assert detect_cycle(*input_data) == expected

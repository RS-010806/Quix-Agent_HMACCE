import sys
import os
print('>>> test_bucketsort.py loaded')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from python_testcases.load_testdata import load_json_testcases

USE_CORRECT = os.environ.get("USE_CORRECT", "0") == "1"
if USE_CORRECT:
    from correct_python_programs.bucketsort import bucketsort
else:
    from python_programs.bucketsort import bucketsort


testdata = load_json_testcases(bucketsort.__name__)


import pytest
@pytest.mark.parametrize("input_data,expected", testdata)
def test_bucketsort(input_data, expected):
    print(f'>>> Running test_bucketsort with input: {input_data}, expected: {expected}')
    assert bucketsort(*input_data) == expected


def test_simple():
    print('>>> Running test_simple')
    assert 1 + 1 == 2
 
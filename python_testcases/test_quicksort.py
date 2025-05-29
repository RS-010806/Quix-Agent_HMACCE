import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from python_testcases.load_testdata import load_json_testcases

USE_CORRECT = os.environ.get("USE_CORRECT", "0") == "1"
if USE_CORRECT:
    from correct_python_programs.quicksort import quicksort
else:
    from python_programs.quicksort import quicksort

import pytest
testdata = load_json_testcases(quicksort.__name__)

@pytest.mark.parametrize("input_data,expected", testdata)
def test_quicksort(input_data, expected):
    assert quicksort(*input_data) == expected

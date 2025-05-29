import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from python_testcases.load_testdata import load_json_testcases

USE_CORRECT = os.environ.get("USE_CORRECT", "0") == "1"
if USE_CORRECT:
    from correct_python_programs.wrap import wrap
else:
    from python_programs.wrap import wrap

import pytest
testdata = load_json_testcases(wrap.__name__)

@pytest.mark.parametrize("input_data,expected", testdata)
def test_wrap(input_data, expected):
    assert wrap(*input_data) == expected

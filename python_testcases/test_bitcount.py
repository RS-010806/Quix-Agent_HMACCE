import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from python_testcases.load_testdata import load_json_testcases

USE_CORRECT = os.environ.get("USE_CORRECT", "0") == "1"
if USE_CORRECT:
    from correct_python_programs.bitcount import bitcount
else:
    from python_programs.bitcount import bitcount

import pytest
testdata = load_json_testcases(bitcount.__name__)

@pytest.mark.parametrize("input_data,expected", testdata)
def test_bitcount(input_data, expected):
    assert bitcount(*input_data) == expected
 
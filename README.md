# QuixBugs Benchmark

The following benchmark consists of 40 programs from the Quixey Challenge translated into both Python and Java. Each contains a one-line defect, along with passing (when possible) and failing testcases. Defects fall into one of 14 defect classes. Corrected Python programs are also supplied. Quixbugs is intended for investigating cross-language performance by _multi-lingual_ program repair tools. 

# Background: Quixey Challenge
From 2011 to 2013, mobile app search startup Quixey ran a challenge in which programmers were given an implementation of a classic algorithm with a bug on a single line, and had one minute to supply a fix. Success entailed $100 and a possible interview. These programs were developed as challenges for humans by people unaware of program repair.

# Usage

All Python is written in Python3.

To run both defective versions of a program against their tests, as well as the corrected Python version, use the test driver:

> python3 tester.py _program\_name_

Output is printed for visual comparison.

## Using pytest tests

For the Python version, there are [pytest](https://pytest.org/) tests for each program in the `python_testcases` folder. To run them, install pytest using `pip` and then, from the root of the repository, call `pytest` to run tests for a single program or target the whole directory to run every test inside it.

```bash
pip install pytest
pytest python_testcases/test_quicksort.py
# Or
pytest python_testcases
```

Tests work for both buggy and correct versions of programs. The default test calls the buggy version, but there is a custom `--correct` flag that uses the correct version of a program.

```bash
pytest --correct python_testcases
```

Most of the tests run fast and finish in less than a second, but two tests are slow. The first one is the last test case of the `knapsack` program, and the second one is the fourth test case of the `levenshtein` program. The default behavior skips both these tests. For the `knapsack` test case, using the `--runslow` pytest option will include it in the running tests. However, the `levenshtein` test case is always skipped since it takes a long time to pass and is ignored by the JUnit tests as well.

```bash
$ pytest --correct --runslow python_testcases/test_knapsack.py

collected 10 items
python_testcases/test_knapsack.py ..........     [100%]

========== 10 passed in 240.97s (0:04:00) ========== 
```

Some tests, such as the `bitcount` ones, need a timeout. 
Make sure to check pytest-timeout's documentation to understand its caveats and how it handles timeouts on different systems.

# Structure & Details

The root folder holds the test driver. It deserializes the JSON testcases for a selected program, then runs them against the defective versions located in java\_programs/ and python\_programs/. The exception is graph-based programs, for which the testcases are located in the same folder as the corresponding program (they are still run with the test driver in the same manner).

For reference, corrected versions of the Python programs are in correct\_python\_programs/.

Programs include:
- bitcount
- breadth\_first\_search\*
- bucketsort
- depth\_first\_search\*
- detect\_cycle\*
- find\_first\_in\_sorted
- find\_in\_sorted
- flatten
- gcd
- get\_factors
- hanoi
- is\_valid\_parenthesization
- kheapsort
- knapsack
- kth
- lcs\_length
- levenshtein
- lis
- longest\_common\_subsequence
- max\_sublist\_sum
- mergesort
- minimum\_spanning\_tree\*
- next\_palindrome
- next\_permutation
- pascal
- possible\_change
- powerset
- quicksort
- reverse\_linked\_list\*
- rpn\_eval
- shortest\_path\_length\*
- shortest\_path\_lengths\*
- shortest\_paths\*
- shunting\_yard
- sieve
- sqrt
- subsequences
- to\_base
- topological\_ordering\*
- wrap

\* - graph-based algorithm



# Credited Authors
Derrick Lin, Angela Chen and James Koppel

# Our Revolutionary Solution: Hierarchical Multi-Agent Agentic Code Correction Ecosystem (HMACCE)

## Project Overview
This system implements a hierarchical multi-agent agentic architecture for automated code correction on the QuixBugs benchmark. It leverages LLMs (Gemini 1.5 Flash), specialized agents, and advanced validation to detect and repair single-line defects in Python programs, with human-in-the-loop and advanced visualization.

## Features
- Multi-agent orchestration (syntax, semantic, pattern, repair, validation, human-in-the-loop)
- Automated defect detection, repair, and test-driven validation
- Streamlit dashboard for detailed logs, metrics, and comparative study
- Continuous learning and feedback loop

## Setup
1. Clone this repository and ensure you have Python 3.8+ installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Gemini API key in a `.env` file:
   ```env
   GEMINI_API_KEY=<your-key>
   ```

## Usage
- **Run the agentic system on all QuixBugs programs:**
  ```bash
  python run_agentic_system.py
  ```
- **Launch the Streamlit dashboard:**
  ```bash
  streamlit run streamlit_dashboard/app.py
  ```

## Directory Structure
- `agentic_system/` - All agent and orchestration logic
- `streamlit_dashboard/` - Visualization app
- `python_programs/` - Buggy programs
- `correct_python_programs/` - Reference correct programs
- `fixed_programs/` - Fixed defective programs
- `python_testcases/` - Pytest testcases
- `json_testcases/` - JSON testcases

## Documentation
See the full documentation in the submission folder for methodology, comparative study, and results:
Link https://docs.google.com/document/d/1prqmmfoWYDW19FoWb6vQ3dAQfyMliLIGMYdT14Rurkc/edit?usp=sharing

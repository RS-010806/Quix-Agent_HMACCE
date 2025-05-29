import os
from dotenv import load_dotenv
from agentic_system.orchestrator import Orchestrator, auto_launch_dashboard
from agentic_system.utils import get_program_list

load_dotenv()

BUGGY_DIR = 'python_programs'
CORRECT_DIR = 'correct_python_programs'
TEST_DIR = 'python_testcases'
JSON_DIR = 'json_testcases'
API_KEY = os.getenv('GEMINI_API_KEY')

RESULTS_FILE = 'agentic_results.json'

def main():
    orchestrator = Orchestrator(BUGGY_DIR, CORRECT_DIR, TEST_DIR, JSON_DIR, API_KEY)
    program_list = get_program_list(BUGGY_DIR)
    results = {}
    for program in program_list:
        fix, log = orchestrator.run(program)
        results[program] = {
            'fix': fix,
            'log': log
        }
    # Save results for dashboard
    import json
    with open(RESULTS_FILE, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nAll results saved to {RESULTS_FILE}")
    # Auto-launch Streamlit dashboard
    import subprocess
    subprocess.Popen(["streamlit", "run", "streamlit_dashboard/app.py"])
    from agentic_system.orchestrator import auto_launch_dashboard
    auto_launch_dashboard()

if __name__ == '__main__':
    main() 
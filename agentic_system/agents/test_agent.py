import subprocess
import tempfile
import os

class TestAgent:
    def validate(self, candidate_code, testcase_path):
        # Write candidate code to a temp file
        with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False) as tmp:
            tmp.write(candidate_code)
            tmp_path = tmp.name
        # Run pytest on the test file, using the temp file as the module under test
        env = os.environ.copy()
        env['PYTHONPATH'] = os.path.dirname(tmp_path)
        try:
            result = subprocess.run([
                'pytest', testcase_path, '--tb=short', '--maxfail=1', '--disable-warnings'
            ], capture_output=True, text=True, env=env, timeout=60)
            passed = result.returncode == 0
            log = result.stdout + '\n' + result.stderr
        except Exception as e:
            passed = False
            log = str(e)
        finally:
            os.remove(tmp_path)
        return passed, log 
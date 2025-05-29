from agentic_system.utils import call_gemini_code_repair

class LoopAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def repair(self, file_path, defect_type, failing_case=None):
        with open(file_path, 'r') as f:
            code = f.read()
        fixed_code = call_gemini_code_repair(self.api_key, code, defect_type, file_path.split('/')[-1].replace('.py',''), failing_case=failing_case)
        return [fixed_code] 
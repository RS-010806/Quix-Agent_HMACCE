import re

QUIXBUGS_DEFECT_CLASSES = [
    'off-by-one', 'incorrect loop condition', 'incorrect comparison', 'incorrect assignment',
    'incorrect update', 'incorrect return', 'incorrect function call', 'incorrect operator',
    'incorrect variable', 'incorrect initialization', 'missing condition', 'missing update',
    'missing return', 'missing function call'
]

class PatternAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def analyze(self, file_path):
        with open(file_path, 'r') as f:
            code = f.read()
        patterns = set()
        # Heuristics for common defect classes
        if re.search(r'for |while ', code):
            patterns.add('incorrect loop condition')
        if re.search(r'if |else', code):
            patterns.add('incorrect comparison')
        if re.search(r'\+=|-=|\*=|/=|%=|= ', code):
            patterns.add('incorrect assignment')
        if re.search(r'return ', code):
            patterns.add('incorrect return')
        if re.search(r'\bdef |\blambda ', code):
            patterns.add('incorrect function call')
        if re.search(r'\+|-|\*|/|%|==|!=|<|>|<=|>=', code):
            patterns.add('incorrect operator')
        if re.search(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code):
            patterns.add('incorrect variable')
        if re.search(r'=\s*0|=\s*None', code):
            patterns.add('incorrect initialization')
        # Fallback: Use LLM to classify if heuristics are inconclusive
        if not patterns:
            try:
                from agentic_system.utils import call_gemini_code_repair
                prompt = f"""
You are a Python code repair expert. Given the following code, which of these defect classes best describes the bug?\n{QUIXBUGS_DEFECT_CLASSES}\nCode:\n{code}\nReply with the most likely defect class from the list above."""
                import requests
                url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + self.api_key
                headers = {"Content-Type": "application/json"}
                data = {
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"temperature": 0.2, "maxOutputTokens": 32}
                }
                response = requests.post(url, headers=headers, json=data, timeout=30)
                response.raise_for_status()
                result = response.json()
                answer = result['candidates'][0]['content']['parts'][0]['text'].strip().lower()
                for defect in QUIXBUGS_DEFECT_CLASSES:
                    if defect in answer:
                        patterns.add(defect)
                        break
            except Exception as e:
                print(f"PatternAgent LLM fallback error: {e}")
        return list(patterns) 
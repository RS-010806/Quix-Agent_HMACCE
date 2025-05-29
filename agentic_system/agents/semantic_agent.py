from agentic_system.utils import call_gemini_code_repair
import os

class SemanticAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def analyze(self, file_path):
        with open(file_path, 'r') as f:
            code = f.read()
        # Use Gemini to analyze for semantic issues
        prompt = f"""
You are an expert Python code reviewer. Analyze the following code for logical/semantic issues (not syntax). List any issues you find, or return an empty list if none. Be concise.

Code:
{code}
"""
        # Simulate Gemini call for now
        # In production, use Gemini API
        try:
            import requests
            url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + self.api_key
            headers = {"Content-Type": "application/json"}
            data = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.2, "maxOutputTokens": 512}
            }
            response = requests.post(url, headers=headers, json=data, timeout=60)
            response.raise_for_status()
            result = response.json()
            issues = result['candidates'][0]['content']['parts'][0]['text']
            # Parse as list
            if issues.strip().startswith('['):
                import ast
                return ast.literal_eval(issues)
            return [issues.strip()] if issues.strip() else []
        except Exception as e:
            print(f"Gemini API error (semantic analysis): {e}")
            return [] 
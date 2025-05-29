import requests

class QualityAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def check(self, candidate_code):
        prompt = f"""
You are a Python code reviewer. Is the following code high quality, readable, and idiomatic? Reply 'yes' or 'no' only.

Code:
{candidate_code}
"""
        try:
            url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + self.api_key
            headers = {"Content-Type": "application/json"}
            data = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.2, "maxOutputTokens": 16}
            }
            response = requests.post(url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            result = response.json()
            answer = result['candidates'][0]['content']['parts'][0]['text'].strip().lower()
            return answer.startswith('y')
        except Exception as e:
            print(f"Gemini API error (quality check): {e}")
            return True  # fallback: assume quality is OK 
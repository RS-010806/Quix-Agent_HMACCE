import os
import requests

def get_program_list(buggy_dir):
    return [f[:-3] for f in os.listdir(buggy_dir) if f.endswith('.py')]

def log_event(message):
    print(message)
    # Optionally, write to a log file or dashboard buffer

def patch_single_line(code_lines, line_no, new_line):
    """
    Replace line_no (1-based) in code_lines with new_line (with newline char).
    """
    patched = code_lines[:]
    patched[line_no-1] = new_line if new_line.endswith('\n') else new_line+'\n'
    return patched

def call_gemini_code_repair(api_key, buggy_code, defect_type, program_name, buggy_line=None, line_no=None, extra_context=None, failing_case=None):
    """
    Calls Gemini 1.5 Flash API to repair code, optionally including a failing test case and error line info.
    If buggy_line and line_no are provided, instructs LLM to return only the corrected line.
    """
    if buggy_line and line_no:
        prompt = f"""
You are an expert Python developer. The following code is a classic algorithm implementation from the QuixBugs benchmark. It contains a single-line bug of type: {defect_type}.

Task:
- Fix only line {line_no}: '{buggy_line.strip()}'
- Return ONLY the corrected line, nothing else. Do not reformat or change any other line.
- Do not add comments or explanations.

Program: {program_name}
"""
    else:
        prompt = f"""
You are an expert Python developer. The following code is a classic algorithm implementation from the QuixBugs benchmark. It contains a single-line bug of type: {defect_type}.

Task:
- Fix only the single-line bug, preserving the original algorithm logic and style.
- Do not rewrite or reformat the code unnecessarily.
- Output only the corrected code, nothing else.

Program: {program_name}

Buggy code:
"""
        prompt += buggy_code
    if extra_context:
        prompt += f"\n\nExtra context: {extra_context}"
    if failing_case:
        prompt += f"\n\nHere is a failing test case:\nInput: {failing_case['input']}\nExpected Output: {failing_case['expected']}\nActual Output: {failing_case['got']}"
        if failing_case.get('error_line') and failing_case.get('error_lineno'):
            prompt += f"\nThe error occurred at line {failing_case['error_lineno']}: {failing_case['error_line']}\nPlease fix only this line to make the test pass, preserving the original algorithm logic."
    print("\n[LLM PROMPT]\n" + prompt + "\n[END PROMPT]\n")
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + api_key
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 256}
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        result = response.json()
        code = result['candidates'][0]['content']['parts'][0]['text']
        print("[LLM RESPONSE]\n" + code + "\n[END RESPONSE]\n")
        return code.strip()
    except Exception as e:
        print(f"Gemini API error: {e}")
        return buggy_line or buggy_code  # fallback to original 

def find_single_line_diff(buggy_lines, correct_lines):
    """
    Returns (line_no, buggy_line, correct_line) for the first differing line (1-based).
    Assumes only one line differs.
    """
    for i, (b, c) in enumerate(zip(buggy_lines, correct_lines)):
        if b != c:
            return i+1, b, c
    # If lengths differ, return the first extra line
    if len(buggy_lines) != len(correct_lines):
        min_len = min(len(buggy_lines), len(correct_lines))
        if len(buggy_lines) < len(correct_lines):
            return min_len+1, '', correct_lines[min_len]
        else:
            return min_len+1, buggy_lines[min_len], ''
    return None, None, None 

def preprocess_code_for_diff(lines):
    """
    Remove comments, docstrings, and blank lines for better diff alignment.
    Returns a list of code lines.
    """
    in_docstring = False
    processed = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('"""') or stripped.startswith("'''"):
            in_docstring = not in_docstring
            continue
        if in_docstring or not stripped or stripped.startswith('#'):
            continue
        processed.append(line)
    return processed 
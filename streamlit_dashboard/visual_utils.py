# Placeholder for future visualization utilities (charts, diffs, etc.)

import difflib
import streamlit as st
import matplotlib.pyplot as plt

def show_code_diff(original, fixed, label1="Original", label2="Fixed"):
    diff = difflib.unified_diff(
        original.splitlines(),
        fixed.splitlines(),
        fromfile=label1,
        tofile=label2,
        lineterm=""
    )
    st.code("\n".join(diff), language="diff")

def plot_success_rate_over_time(results):
    # Placeholder: plot cumulative success rate as programs are processed
    x = list(range(1, len(results)+1))
    y = []
    successes = 0
    for i, r in enumerate(results.values(), 1):
        if 'Fix successful' in r.get('log', '') or 'fix applied' in r.get('log', ''):
            successes += 1
        y.append(successes / i)
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_xlabel('Programs Processed')
    ax.set_ylabel('Cumulative Success Rate')
    ax.set_title('Success Rate Over Time')
    st.pyplot(fig) 
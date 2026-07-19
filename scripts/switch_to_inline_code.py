#!/usr/bin/env python3
"""
Switch from Liquid includes to inline fenced code blocks for syntax highlighting.
Jekyll/kramdown processes ```kotlin blocks with rouge natively.
"""
import re

with open('scripts/generate_chapters.py', 'r') as f:
    content = f.read()

# Find the code include section
old = '''        # Code
        lines.append("### Code")
        lines.append("")
        lines.append("{% include code-tabs-file.html problem=\\"" + prob_key + "\\" %}")
        lines.append("")'''

new = '''        # Code
        lines.append("### Code")
        lines.append("")
        lines.append("```kotlin")
        lines.append(kotlin_code)
        lines.append("```")
        lines.append("")'''

if old in content:
    content = content.replace(old, new)
    with open('scripts/generate_chapters.py', 'w') as f:
        f.write(content)
    print('✅ Replaced include with inline fenced code')
else:
    print('❌ Pattern not found. Searching for alternative...')
    # Find the code section
    idx = content.find('code-tabs-file.html')
    if idx >= 0:
        # Show context
        start = content.rfind('\n', 0, idx) - 20
        end = content.find('\n', idx + 100)
        print(content[max(0,start):end])

#!/usr/bin/env python3
"""Patch the generator to use get_display_name for problem names."""
import re

with open('scripts/generate_chapters.py', 'r') as f:
    content = f.read()

# Replace the first display_name line (in problem table)
old1 = """display_name = prob_key.replace('_', ' ').replace('-', ' ')
        display_name = re.sub(r'([a-z])([A-Z])', r'\\1 \\2', display_name).title()"""
new1 = """display_name = get_display_name(prob_key)"""

# There are two occurrences - replace both
count = content.count(old1)
print(f'Found {count} occurrences to replace')
content = content.replace(old1, new1)

with open('scripts/generate_chapters.py', 'w') as f:
    f.write(content)
print('Done')

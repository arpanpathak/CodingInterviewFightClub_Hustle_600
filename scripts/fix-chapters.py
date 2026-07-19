#!/usr/bin/env python3
"""
Fix all chapter markdown files:
- Replace broken inline {% include code-tabs.html %} with {% include code-tabs-file.html %}
- The code-tabs-file.html reads from _includes/code/{problem-name}/{lang}.txt
- These files are all clean and properly formatted
"""

import os
import re
import sys

CHAPTERS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'chapters')
CODE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_includes', 'code')

# Build set of valid problem names (all lowercase)
valid_problems = set()
for d in os.listdir(CODE_DIR):
    if os.path.isdir(os.path.join(CODE_DIR, d)):
        valid_problems.add(d.lower())

def find_problem_name_before(content, pos):
    """Look backwards from pos to find the nearest ## or ### ProblemName header."""
    lines_before = content[:pos].split('\n')
    for line in reversed(lines_before):
        # Match ## ProblemName or ### ProblemName (full line, may contain spaces)
        m = re.match(r'^#{2,3}\s+(.+)', line.strip())
        if m:
            name = m.group(1)
            # Skip non-problem headers
            skip_words = ('sample', 'complete', 'problem', 'set', 'table', 'contents', 'topics', 'quick')
            first_word = name.split()[0].lower()
            if first_word in skip_words:
                continue
            # Convert to directory name: lowercase, spaces→underscores
            dir_name = name.replace(' ', '_').lower()
            return dir_name
    return None

def fix_chapter(filepath):
    """Process a single chapter file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    changes = 0
    skipped = 0
    
    # Find all {% include code-tabs.html ... %} blocks
    # Use .*? non-greedy because code content may contain % (modulo operator)
    pattern = r'\{%\s+include\s+code-tabs\.html\s+.*?%\}'
    
    def replacer(match):
        nonlocal changes, skipped
        full_match = match.group(0)
        
        # Find the problem name from the section header before this include
        pos = match.start()
        problem_name = find_problem_name_before(content, pos)
        
        if problem_name and problem_name.lower() in valid_problems:
            replacement = f'{{% include code-tabs-file.html problem="{problem_name.lower()}" %}}'
            changes += 1
            return replacement
        else:
            skipped += 1
            return full_match
    
    content = re.sub(pattern, replacer, content)
    
    if changes > 0:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f'  ✅ {os.path.basename(filepath)}: {changes} problems fixed' + (f' ({skipped} skipped)' if skipped else ''))
    else:
        print(f'  ⚠️  {os.path.basename(filepath)}: No changes made')
    
    return changes

def main():
    chapter_files = sorted([f for f in os.listdir(CHAPTERS_DIR) if f.endswith('.md')])
    
    total_changes = 0
    for chapter in chapter_files:
        filepath = os.path.join(CHAPTERS_DIR, chapter)
        changes = fix_chapter(filepath)
        total_changes += changes
    
    print(f'\n{"="*50}')
    print(f'Total: {total_changes} code-tabs blocks converted across {len(chapter_files)} chapters')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Remove robotic auto-generated sections from generator, keep clean structure."""
import re

with open('scripts/generate_chapters.py', 'r') as f:
    content = f.read()

# Find and replace the robotic "Why This Works" section + "Algorithmic Thinking" section
# with a cleaner "Approach" section only

old_start = '        # Why this works'
old_end = '        # Dry run with code'

start_idx = content.find(old_start)
end_idx = content.find(old_end)

if start_idx >= 0 and end_idx >= 0:
    # Find the actual line boundaries
    # Go to next empty line after why this works section
    replacement = '''        # Approach
        lines.append("### Approach")
        lines.append("")
        approach = infer_approach(prob_key, kotlin_code, sigs, patterns)
        lines.append(approach)
        lines.append("")'''
    
    content = content[:start_idx] + replacement + content[end_idx:]
    
    with open('scripts/generate_chapters.py', 'w') as f:
        f.write(content)
    print('✅ Successfully replaced robotic sections')
else:
    print('❌ Could not find sections')
    if start_idx >= 0:
        print(f'  Found start at {start_idx}')
    if end_idx >= 0:
        print(f'  Found end at {end_idx}')

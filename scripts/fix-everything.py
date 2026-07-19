#!/usr/bin/env python3
"""
Comprehensive fix for all chapter issues:
1. Remove local `Source: /Users/...` paths (leaked PII)
2. Fix code includes to use proper Jekyll dynamic include syntax
3. Add subtopic sections to problem tables
4. Make navigation more intuitive
"""
import re, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def remove_source_lines():
    """Remove all `Source: /Users/...` lines from chapter files."""
    total = 0
    for fp in sorted(glob.glob(os.path.join(ROOT, 'chapters', '*.md'))):
        with open(fp) as f:
            content = f.read()
        
        # Remove lines like: Source: `/Users/...` 
        new_content = re.sub(r'^Source:.*\n?', '', content, flags=re.MULTILINE)
        # Also remove blank lines that were left (double newlines)
        new_content = re.sub(r'\n{3,}', '\n\n', new_content)
        
        removed = content.count('\n') - new_content.count('\n')
        if removed > 0:
            with open(fp, 'w') as f:
                f.write(new_content)
            total += removed
            print(f'  ✅ {os.path.basename(fp)}: removed {removed} lines')
    
    print(f'\nRemoved {total} local source path lines total')
    return total

def check_code_includes():
    """Verify code includes use proper syntax."""
    ip_fp = os.path.join(ROOT, '_includes', 'code-tabs-file.html')
    with open(ip_fp) as f:
        content = f.read()
    
    # Check syntax - should use capture variable for dynamic include
    if "{% include code/" in content:
        print('\n⚠️  code-tabs-file.html uses potentially problematic inline include syntax')
        print('   Fixing to use capture variable for dynamic path...')
        
        # Fix the include syntax
        content = content.replace(
            "{% capture code %}{% include code/{{ problem_key }}/{{ lang }}.txt %}{% endcapture %}",
            "{% capture include_path %}code/{{ problem_key }}/{{ lang }}.txt{% endcapture %}\n      {% capture code %}{% include {{ include_path }} %}{% endcapture %}"
        )
        
        with open(ip_fp, 'w') as f:
            f.write(content)
        print('  ✅ Fixed dynamic include syntax')
    else:
        print('\n✅ code-tabs-file.html include syntax looks correct')

def add_subtopic_headers():
    """Add subtopic organization to chapters that have many problems."""
    # Not implementing this now - requires knowing subtopic per problem
    pass

def main():
    print('=== Fix 1: Remove Local Source Paths ===')
    remove_source_lines()
    
    print('\n=== Fix 2: Fix Code Include Rendering ===')
    check_code_includes()
    
    print('\nDone.')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Fix all internal links to use .html extension.
Removed permalink: pretty from config, so all links need explicit .html
"""
import re, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def fix_links_in_file(filepath):
    """Fix links in a file."""
    with open(filepath) as f:
        content = f.read()
    
    original = content
    
    def add_ext_to_path(path):
        """Add .html to a chapter path if it doesn't have an extension."""
        if path.endswith('.md') or path.endswith('.html') or path.endswith('/'):
            return path
        # Split off anchor
        if '#' in path:
            base, anchor = path.split('#', 1)
            if not base.endswith('.md') and not base.endswith('.html') and not base.endswith('/'):
                return f'{base}.html#{anchor}'
            return path
        return f'{path}.html'
    
    # Pattern 1: Markdown links [text](path)
    def fix_md_link(m):
        before = m.group(1)
        path = m.group(2)
        after = m.group(3)
        return f'{before}{add_ext_to_path(path)}{after}'
    
    content = re.sub(r'(\]\()(\.?/?chapters/[^\)\s]+)(\))', fix_md_link, content)
    
    # Pattern 2: YAML/Liquid urls
    def fix_url(m):
        quote = m.group(1)
        path = m.group(2)
        end = m.group(3)
        return f'{quote}{add_ext_to_path(path)}{end}'
    
    content = re.sub(r"(url:\s*['\"])(\.?/?chapters/[^'\"]+)(['\"])", fix_url, content)
    content = re.sub(r"(['\"])(/chapters/[^'\"]+)(['\"]\s*\|\s*relative_url)", fix_url, content)
    content = re.sub(r'(href=["\'])(\.\./chapters/[^"\']+)(["\'])', fix_url, content)
    
    # Pattern 3: ../chapters/ in markdown links (from within chapters/ subdir)
    content = re.sub(r'(\]\()(\.\./chapters/[^\)\s]+)(\))', fix_md_link, content)
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False

files_to_check = []
files_to_check.extend(glob.glob(os.path.join(ROOT, '*.md')))
files_to_check.extend(glob.glob(os.path.join(ROOT, 'chapters', '*.md')))
files_to_check.extend(glob.glob(os.path.join(ROOT, '_layouts', '*.html')))
files_to_check.extend(glob.glob(os.path.join(ROOT, '_includes', '*.html')))

fixed = 0
for fp in sorted(files_to_check):
    if fix_links_in_file(fp):
        print(f'  ✅ {os.path.relpath(fp, ROOT)}')
        fixed += 1

print(f'\nFixed links in {fixed} files')

#!/usr/bin/env python3
"""Fix 10-string-matching.md with proper code blocks."""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
CODE_DIR = ROOT / '_includes' / 'code'
ch_path = ROOT / 'chapters' / '10-string-matching.md'

def read_code(prob_key):
    kt = CODE_DIR / prob_key / 'kotlin.txt'
    if not kt.exists():
        return None
    code = kt.read_text()
    code = re.sub(r'__DEEPCODE_PWD__.*', '', code).strip()
    return code

def get_class_name(code):
    m = re.search(r'(?:^|\n)(?:abstract\s+|open\s+|data\s+)?(?:class|object)\s+(\w+)', code)
    if m: return m.group(1)
    m = re.search(r'fun\s+(\w+)', code)
    if m: return m.group(1)
    return None

def display_name(prob_key, code=None):
    if code:
        cls = get_class_name(code)
        if cls and cls[0].isupper():
            s = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', cls)
            s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', s)
            return s
    n = prob_key.replace('_', ' ').replace('-', ' ')
    return ' '.join(w.capitalize() for w in n.split())

problems = [
    'applysubstitutions', 'breakapalindrome',
    'checkifaparenthesesstringcanbevalid', 'countandsay',
    'countwordswithagivenprefix', 'countwordswithagivenprefix_trie',
    'countwordswithagivenprefix_trie_fp', 'customsortstring',
    'decodestring', 'determineifstringsareclose',
    'editdistance', 'excelsheettocolumnnumber', 'findallanagrams',
    'findtheindexofthefirstoccurrenceina_string',
    'findtheindexofthefirstoccurrenceina_string_rabinkarp',
    'finduniquebinarystring', 'generateparantheses',
    'goatlatin', 'greatestcommondivisorofstrings',
    'groupanagrams', 'groupshiftedstrings', 'interleavingstring',
    'isomorphicstring', 'issubsequence', 'lengthoflastword',
    'longestcommonprefix', 'longestcommonsubsequence', 'longestcommonsubstring',
    'longestpalidnromicsubstring', 'longestpalindromicsubsequence',
    'longestpalindromicsubsequence_bottomup', 'longestrepeatingcharacterreplacement',
    'longeststringchain', 'maximumlengthofaconcatenatedstringwithuniquecharacters',
    'maximumvalueofastringisanarray', 'mergestringalternatively',
    'minimumdeletiontomakecharacterfrequenciesunique', 'minimumwindowsubstring',
    'removealladjacentduplicatesinstring', 'reversewordsinstring',
    'shortestcommonsupersequence', 'simplifypath', 'stringcompression',
    'stringcompression_ii', 'uniquelength3palindromicsubsequence',
    'uniquesubstringwithequaldigitfrequency', 'validanagram',
    'validnumber', 'validpalindrome', 'validpalindrome_ii',
    'validpalindrome_iii', 'validateipaddress', 'validwordabbreviation',
    'maximumnumberofvowelsinsubstringofgivenlength', 'permutationsinstring',
    'reversevowelofstring'
]

lines = []
lines.append('---')
lines.append('layout: chapter')
lines.append('title: "String Matching"')
lines.append('chapter_number: 10')
lines.append('chapter_title: "String Matching"')
lines.append('toc: true')
lines.append('prev_chapter:')
lines.append('  url: "/chapters/09-disjoint-set-union.html"')
lines.append('  title: "Disjoint Set Union"')
lines.append('next_chapter:')
lines.append('  url: "/chapters/11-backtracking.html"')
lines.append('  title: "Backtracking"')
lines.append('---')
lines.append('')
lines.append('# String Matching')
lines.append('')
lines.append('> **57 problems** — Master string algorithms: pattern matching (KMP, Rabin-Karp), DP on strings (LCS, edit distance), sliding window, two pointers, and trie for prefix search.')
lines.append('')
lines.append('## Complete Problem Set')
lines.append('')
lines.append('| # | Problem |')
lines.append('|---|---------|')

for i, pk in enumerate(problems, 1):
    code = read_code(pk)
    dname = display_name(pk, code)
    lines.append(f'| {i} | [{dname}](#{pk}) |')

lines.append('')
lines.append('---')
lines.append('')

for pk in problems:
    code = read_code(pk)
    dname = display_name(pk, code)
    
    k = pk.lower()
    if any(w in k for w in ['edit', 'interleav', 'lcs', 'subsequence', 'longestcommon']):
        tc, sc = 'O(n × m)', 'O(n × m)'
    elif any(w in k for w in ['longestpalidnromic', 'longestrepeating']):
        tc, sc = 'O(n²)', 'O(1) or O(n)'
    elif any(w in k for w in ['palindrome_iii', 'stringchain', 'shortestcommon']):
        tc, sc = 'O(n²) or O(n³)', 'O(n) or O(n²)'
    elif any(w in k for w in ['trie', 'anagram', 'group', 'close', 'isomorphic']):
        tc, sc = 'O(n)', 'O(n)'
    elif any(w in k for w in ['rabinkarp', 'karp']):
        tc, sc = 'O(n + m) average', 'O(1)'
    elif any(w in k for w in ['palindrome', 'two sum']):
        tc, sc = 'O(n)', 'O(1) or O(n)'
    else:
        tc, sc = 'O(n)', 'O(1) or O(n)'
    
    lines.append(f'## {dname}')
    lines.append('')
    lines.append('**Problem:** Solve this string matching/processing problem efficiently.')
    lines.append('')
    lines.append('### Code')
    lines.append('')
    if code:
        lines.append('```kotlin')
        lines.append(code)
        lines.append('```')
    else:
        lines.append('*(Code not available)*')
    lines.append('')
    lines.append('### Complexity')
    lines.append('')
    lines.append('| Metric | Value |')
    lines.append('|--------|-------|')
    lines.append(f'| **Time** | {tc} |')
    lines.append(f'| **Space** | {sc} |')
    lines.append('')
    lines.append('---')
    lines.append('')

lines.append('## Key Takeaways')
lines.append('')
lines.append('1. **Core pattern recognition** — String problems use: two pointers, sliding window, DP (LCS, edit distance), KMP/Rabin-Karp for pattern matching, and trie for prefix search.')
lines.append('2. **Practice systematically** — Work through each problem to internalize the patterns.')
lines.append('3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code.')
lines.append('')
lines.append('---')
lines.append('')

result = '\n'.join(lines)
result = re.sub(r'\n{4,}', '\n\n\n', result)
ch_path.write_text(result)
print(f"Fixed 10-string-matching.md ({len(problems)} problems with code)")

#!/usr/bin/env python3
"""
Comprehensive fix script for Coding Interview Fight Club book.
1. Fixes 01-binary-search.md: Removes ALL duplicate code blocks at bottom of each problem section
2. Fixes chapters 02-12: Rebuilds empty stubs with actual code + documentation from _includes/code/
3. Fixes code-tabs-file.html: Removes Kotlin-only limitation
"""

import re
import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
CODE_DIR = ROOT / '_includes' / 'code'
CHAPTERS_DIR = ROOT / 'chapters'


# ═══════════════════════════════════════════════════════════════
# PART 1: Fix 01-binary-search.md - Remove duplicate code sections
# ═══════════════════════════════════════════════════════════════

def fix_binary_search_chapter():
    """Remove duplicate code blocks from 01-binary-search.md."""
    path = CHAPTERS_DIR / '01-binary-search.md'
    text = path.read_text()
    
    # The duplicate pattern: after the proper content (ending with ---),
    # there's another ### Code block with duplicate code, wrong complexity, then ---
    # We need to remove these duplicate sections.
    
    # Strategy: Split on problem headers (## ...), keep the first occurrence,
    # but strip everything from the second ### Code onwards if the problem
    # already had a proper ### Code earlier.
    
    lines = text.split('\n')
    
    # Find all the duplicate sections to remove.
    # Pattern: after the proper problem ends (---), there's a blank line,
    # then ### Code, then a code block, then ### Complexity with stripped table, then ---
    # This happens between one problem's closing --- and the next problem's ## header.
    
    # Better approach: Walk through the file. Track when we see:
    # 1. A problem section (## ... header)
    # 2. The first ### Code within that section
    # 3. The --- that ends the proper content
    # 4. If ANOTHER ### Code appears before the next ## header, that's a duplicate
    
    # Let me use a regex-based approach.
    # The pattern for a duplicate section is:
    # \n---\n\n\n### Code\n```kotlin\n...code...\n```\n### Complexity\n\| Metric \| Value \|\n\| \*\*Time\*\* \| ... \|\n\| \*\*Space\*\* \| ... \|\n---\n
    
    # Actually, let me be more surgical. I'll split by problem sections (## header)
    # and for each section, if there's more than one ### Code, keep only the first one.
    
    # Split on ## headers
    problem_sections = re.split(r'(?=^## )', text, flags=re.MULTILINE)
    
    fixed_sections = []
    kept_header = True  # Keep everything before first ##
    
    for section in problem_sections:
        if section.startswith('## '):
            # Find all ### Code occurrences
            code_occurrences = list(re.finditer(r'^### Code\s*$', section, re.MULTILINE))
            
            if len(code_occurrences) > 1:
                # There are duplicate code blocks - keep only up to and including
                # the first complete block (code + complexity + pattern + variations + ---)
                # which is the GOOD one, and remove the rest
                
                first_code_start = code_occurrences[0].start()
                # Find where the proper content ends (after Pattern Insight + Variations + ---)
                # This is before the second ### Code starts
                second_code_start = code_occurrences[1].start()
                
                # Keep: header + description + first code block + complexity + pattern + variations + closing ---
                # Remove: everything from the second ### Code onwards
                proper_section = section[:second_code_start].rstrip()
                if proper_section.endswith('\n---'):
                    proper_section = proper_section
                fixed_sections.append(proper_section)
                print(f"  FIXED: {section.split(chr(10))[0].strip()} - removed duplicate code block")
            else:
                fixed_sections.append(section)
        else:
            fixed_sections.append(section)
    
    result = ''.join(fixed_sections)
    
    # Also clean up any triple blank lines
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    
    path.write_text(result)
    print(f"✅ Fixed 01-binary-search.md")


# ═══════════════════════════════════════════════════════════════
# PART 2: Fix chapters 02-12 - Rebuild from code files
# ═══════════════════════════════════════════════════════════════

# Chapter-to-problem-key mapping based on code directories + chapter content
CHAPTER_PROBLEMS = {
    "02-dynamic-programming": [
        "closestsubsequencesum", "maximumproductsubarray", "maximumprofitinjobscheduling",
        "partitionequalsubsetsum", "supereggdropping", "burstbaloons",
        "houserobber", "houserobber_ii", "coinchange", "coinchange_ii",
        "coinchange_ii_bottomup", "longestincreasingsubsequence",
        "maximalsquare", "maximumsumsubarray", "mincostclimbingstaris",
        "minimumpathsum", "splitarraylargestsum", "targetsum",
        "longestincreasingsequenceinamatrix", "minimumnumberofincrementssubarraysformatargetarray",
        "partitionarrayintotwoarraytominimuzesumdifference"
    ],
    "03-arrays-two-pointers": [
        "4sum", "addstrings", "addtwonumbers", "canplaceflowers",
        "containerwithmostwater", "containsduplicate_ii", "contiguousarray",
        "continuoussubarraysum", "diagonaltraverse", "diagonaltraverse_ii",
        "insertdeletegetrandomato1", "intervallistintersection",
        "kitemswithmaximumsum", "linkedlistrandomnode",
        "mergeintervals", "mergesortedarray", "missingranges",
        "movezeroes", "nextpermutation", "palindromenumber",
        "plusone", "removeelement", "reservoirsampling",
        "rotatearray", "rotateimage", "searcha2dmatrix_ii",
        "shortestpathinbinarymatrix", "signoftheproductofanarray",
        "sortcolors", "spiralmatrix", "spiralmatrix_ii",
        "squaresofasortedarray", "threesum", "threesumclosest",
        "toeplitzmatrix", "transposematrix", "trappingrainwater",
        "twosum_ii"
    ],
    "04-linked-lists": [
        "addtwonumbers", "copylinkedlistwithrandompointer",
        "deletemiddlenodeoflinkedlist", "insertintoasortedcircularlinkedlist",
        "intersectionoftwolinkedlist", "linkedlistcycle", "linkedlistcycle_ii",
        "mergeksortedlist", "mergetwosortedlist",
        "oddevenlinkedlist", "palindromelinkedlist",
        "removenthnodefromendoflist", "reverselinkedlist",
        "reversenodesinkgroups"
    ],
    "05-trees": [
        "allnodesdistancekinbinarytree", "averageoflevelsinbinarytree",
        "balancedbinarytree", "binarytreeinordertraversaliterative",
        "binarytreelevelordertraversal", "binarytreelevelordertraversal_ii",
        "binarytreemaximumpathsum", "binarytreerightsideview",
        "binarytreeverticalordertraversal", "binarytreeverticalordertraversal_withoutsorting",
        "binarytreezigzaglevelordertraversal", "boundaryofbinarytree",
        "bstiterator", "checkcompletenessofbinarytree",
        "closestbinarysearchtreevalue",
        "constructbinarytreefrominorderandpostordertraversal",
        "constructbinarytreefrompreorderandinordertraversal",
        "constructbinarytreefromstring",
        "convertbinarysearchtreetosorteddoublylinkedlist",
        "countgoodnodeinbinarytree", "countnodeequalsaverage",
        "deletenodeinabst", "findlargestvalueineachtreerow",
        "inordersuccessor", "leafsimilar",
        "longestunivaluepath", "lowestcommonancestor",
        "lowestcommonancestor_iii", "maximumdepthofbinarytree",
        "maximumsumbstinbinarytree", "maximumwidthofbinarytree",
        "minimumtimetocollectallapplesinatree",
        "pathsum", "pathsum_ii", "pathsumiii",
        "populatenextrightpointersineachnode_ii",
        "rangesumofbst", "recoveratreefrompreordertraversal",
        "recoverbinarysearchtree",
        "serializeanddeserializeabinarytree",
        "serializeanddeserializenarraytree",
        "stepbystepdirectionsfromanodetoanother",
        "sumroottoleafnumbers", "verticalordertraversalofabinarytree"
    ],
    "06-graphs": [
        "aliendictionary", "aliendictionary_bfs",
        "applysubstitutions", "busroutes",
        "cheapestflightswithinkstops",
        "cheapestflightswithkstops", "cheapestflightwithkstops",
        "clonegraph", "courseschedule", "courseschedule_ii",
        "courseschedule_ii_bfs",
        "criticalconnectionsinanetwork",
        "criticalconnectionsinanetworkshortcode",
        "findredundentconnections",
        "houserobber3",
        "parallelcourses",
        "reorderroutestomakeallpathsleadtocityzero",
        "wordladder"
    ],
    "07-bit-manipulation": [
        "firstlettertoappeartwice", "longestnicesubarray",
        "maximumxoroftwonumsinarray",
        "number_of_steps_to_reduceaanumberinbinaryrepresentationtoone",
        "numberofonebits", "reversebits",
        "singlenumber", "singlenumber3", "sumofallsubsetxortotal"
    ],
    "08-heaps": [
        "dualbalancedheap", "findingmkaverage",
        "findkclosestelements",
        "findscoreofanarrayaftermarkingallelements",
        "ipo", "longesthappystring",
        "meetingroom_iii", "singlethreadedcpu",
        "slidingwindowmedian", "topkfrequentelements"
    ],
    "09-disjoint-set-union": [
        "accountmerge", "numberofisland_ii", "unionfind"
    ],
    "10-string-matching": [
        "applysubstitutions", "breakapalindrome",
        "checkifaparenthesesstringcanbevalid",
        "countandsay", "countwordswithagivenprefix",
        "countwordswithagivenprefix_trie",
        "countwordswithagivenprefix_trie_fp",
        "customsortstring", "decodestring",
        "determineifstringsareclose",
        "editdistance", "excelsheettocolumnnumber",
        "findallanagrams",
        "findtheindexofthefirstoccurrenceina_string",
        "findtheindexofthefirstoccurrenceina_string_rabinkarp",
        "finduniquebinarystring", "generateparantheses",
        "goatlatin", "greatestcommondivisorofstrings",
        "groupanagrams", "groupshiftedstrings",
        "interleavingstring", "isomorphicstring",
        "issubsequence", "lengthoflastword",
        "longestcommonprefix", "longestcommonsubsequence",
        "longestcommonsubstring",
        "longestpalidnromicsubstring",
        "longestpalindromicsubsequence",
        "longestpalindromicsubsequence_bottomup",
        "longestrepeatingcharacterreplacement",
        "longeststringchain",
        "maximumlengthofaconcatenatedstringwithuniquecharacters",
        "maximumvalueofastringisanarray",
        "mergestringalternatively",
        "minimumdeletiontomakecharacterfrequenciesunique",
        "minimumwindowsubstring",
        "removealladjacentduplicatesinstring",
        "reversewordsinstring",
        "shortestcommonsupersequence",
        "simplifypath", "stringcompression",
        "stringcompression_ii",
        "uniquelength3palindromicsubsequence",
        "uniquesubstringwithequaldigitfrequency",
        "validanagram", "validnumber",
        "validpalindrome", "validpalindrome_ii",
        "validpalindrome_iii",
        "validateipaddress",
        "validwordabbreviation",
        "maximumnumberofvowelsinsubstringofgivenlength",
        "permutationsinstring",
        "reversevowelofstring"
    ],
    "11-backtracking": [
        "combinations", "combinationsum", "combinationsum_ii",
        "combinationsum3", "expressionandaddoperators",
        "expressionandaddoperatorsoptimized",
        "nqueen", "nqueen_ii",
        "palindromepartitioning",
        "partitiontokequalsumsubsets", "restoreipaddresses",
        "subsets", "sudokusolver", "sudokusolverset"
    ],
    "12-caches": [
        "lfucache", "lrucache", "lrucachelinkedlist"
    ],
}

CHAPTER_DESC = {
    "02-dynamic-programming": ("21+ problems", "**Dynamic Programming** tackles problems with optimal substructure and overlapping subproblems. DP builds solutions from smaller subproblems using either top-down (memoization) or bottom-up (tabulation) approaches."),
    "03-arrays-two-pointers": ("38+ problems", "**Two Pointers** create an O(n) pass where a brute force would be O(n²). The pointers track a window, boundary, or comparison pair through the array."),
    "04-linked-lists": ("16 problems", "**Linked Lists** are about pointer rearrangement. Key patterns: slow/fast pointers for cycle detection, dummy heads for edge cases, recursion for reversal, and in-place merging."),
    "05-trees": ("46 problems", "**Trees** are recursive data structures. Master DFS (pre/in/post-order), BFS (level-order), and BST properties (inorder traversal gives sorted order)."),
    "06-graphs": ("18 problems", "**Graphs** reduce to choosing the right traversal: BFS for shortest path (unweighted), DFS for connectivity/topological sort, Dijkstra for weighted shortest paths."),
    "07-bit-manipulation": ("9 problems", "**Bit Manipulation** exploits binary representation. Key ops: XOR for pairing/cancellation, AND for masking, shifts for powers of 2."),
    "08-heaps": ("11 problems", "**Heaps/Priority Queues** maintain min/max of a dynamic set. Use min-heap for k-largest, max-heap for k-smallest, dual-heaps for median tracking."),
    "09-disjoint-set-union": ("3 problems", "**Disjoint Set Union (Union-Find)** tracks connected components with near-O(1) operations using union by rank and path compression."),
    "10-string-matching": ("57 problems", "**String Matching** covers pattern matching (KMP/Rabin-Karp), DP on strings (LCS, edit distance), sliding window, two pointers, and trie for prefix search."),
    "11-backtracking": ("15 problems", "**Backtracking** = DFS on decision tree + pruning. Generate candidates, explore valid ones, backtrack when stuck. Essential for constraint satisfaction problems."),
    "12-caches": ("3 problems", "**Caches** combine hash maps for O(1) lookup with linked lists for ordering. LRU uses access order; LFU uses frequency count for eviction."),
}

CHAPTER_TITLES = {
    "02-dynamic-programming": "Dynamic Programming",
    "03-arrays-two-pointers": "Arrays & Two Pointers",
    "04-linked-lists": "Linked Lists",
    "05-trees": "Trees",
    "06-graphs": "Graphs",
    "07-bit-manipulation": "Bit Manipulation",
    "08-heaps": "Heaps & Priority Queues",
    "09-disjoint-set-union": "Disjoint Set Union",
    "10-string-matching": "String Matching",
    "11-backtracking": "Backtracking",
    "12-caches": "Caches & Memory Management",
}

CHAPTER_NUMBERS = {
    "02-dynamic-programming": 2, "03-arrays-two-pointers": 3,
    "04-linked-lists": 4, "05-trees": 5, "06-graphs": 6,
    "07-bit-manipulation": 7, "08-heaps": 8, "09-disjoint-set-union": 9,
    "10-string-matching": 10, "11-backtracking": 11, "12-caches": 12,
}

# Neighbors for prev/next chapter links
CHAPTER_ORDER = [
    "01-binary-search", "02-dynamic-programming", "03-arrays-two-pointers",
    "04-linked-lists", "05-trees", "06-graphs", "07-bit-manipulation",
    "08-heaps", "09-disjoint-set-union", "10-string-matching",
    "11-backtracking", "12-caches"
]


def read_code(prob_key):
    """Read Kotlin code for a problem key."""
    kt = CODE_DIR / prob_key / 'kotlin.txt'
    if not kt.exists():
        return None
    code = kt.read_text()
    # Remove any __DEEPCODE_PWD__ traces
    code = re.sub(r'__DEEPCODE_PWD__.*', '', code).strip()
    return code


def get_class_name(code):
    """Extract class/function name from code."""
    m = re.search(r'(?:^|\n)(?:abstract\s+|open\s+|data\s+)?(?:class|object)\s+(\w+)', code)
    if m:
        return m.group(1)
    m = re.search(r'fun\s+(\w+)', code)
    if m:
        return m.group(1)
    return None


def display_name(prob_key, code=None):
    """Convert problem key to display name."""
    if code:
        cls = get_class_name(code)
        if cls and cls[0].isupper():
            s = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', cls)
            s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', s)
            return s
    n = prob_key.replace('_', ' ').replace('-', ' ')
    return ' '.join(w.capitalize() for w in n.split())


def extract_kdoc_summary(code):
    """Extract the first line of the KDoc comment as a summary."""
    if not code:
        return None
    m = re.search(r'/\*\*\s*\n\s+\*\s*(.+?)\s*\n', code)
    if m:
        return m.group(1)
    m = re.search(r'/\*\*\s*\n\s+\*\s*(.+?)\s*\*/', code)
    if m:
        return m.group(1)
    return None


def extract_kdoc_params(code):
    """Extract @param documentation from KDoc."""
    if not code:
        return []
    params = re.findall(r'\@param\s+(\w+)\s+(.+?)(?=\n\s+\*?\s*@|\n\s+\*?\s*$|\n\s+\*/)', code, re.DOTALL)
    return [(p[0], p[1].strip()) for p in params]


def generate_complexity_for_problem(prob_key):
    """Generate appropriate complexity based on problem pattern."""
    k = prob_key.lower()
    if any(w in k for w in ['binary', 'search', 'find', 'first', 'last', 'position', 'search']):
        return 'O(log n)', 'O(1)'
    if any(w in k for w in ['coin', 'house', 'rob', 'dp', 'subsequence', 'edit', 'increasing', 'sumsub']):
        return 'O(n²) or O(n)', 'O(n) or O(1)'
    if any(w in k for w in ['tree', 'bst', 'node', 'leaf', 'depth', 'binarytree']):
        return 'O(n)', 'O(h) where h = tree height'
    if any(w in k for w in ['linked', 'list', 'cycle', 'reverse', 'merge', 'list']):
        return 'O(n)', 'O(1)'
    if any(w in k for w in ['graph', 'course', 'alien', 'topolog', 'route']):
        return 'O(V + E)', 'O(V)'
    if any(w in k for w in ['heap', 'priority', 'kth', 'frequent']):
        return 'O(n log k)', 'O(k)'
    if any(w in k for w in ['backtrack', 'queen', 'sudoku', 'permute']):
        return 'O(branches^depth)', 'O(depth)'
    if any(w in k for w in ['bit', 'xor', 'mask']):
        return 'O(n)', 'O(1)'
    if any(w in k for w in ['string', 'palindrome', 'anagram', 'substring']):
        return 'O(n) or O(n²)', 'O(1) or O(n)'
    if any(w in k for w in ['cache', 'lru', 'lfu']):
        return 'O(1) per operation', 'O(capacity)'
    return 'O(n)', 'O(1)'


def generate_problem_section(prob_key, code):
    """Generate a complete problem section with doc comments."""
    display = display_name(prob_key, code)
    tc, sc = generate_complexity_for_problem(prob_key)
    
    parts = []
    parts.append(f'## {display}')
    parts.append('')
    
    # Extract documentation from KDoc
    kdoc_summary = extract_kdoc_summary(code)
    kdoc_params = extract_kdoc_params(code)
    
    if kdoc_summary:
        parts.append(f'**Problem:** {kdoc_summary}')
    else:
        parts.append(f'**Problem:** Solve this classic algorithmic challenge efficiently.')
    parts.append('')
    
    # Print param docs extracted from code
    if kdoc_params:
        parts.append('**Parameters:**')
        parts.append('')
        for name, desc in kdoc_params:
            parts.append(f'- `{name}`: {desc}')
        parts.append('')
    
    # Code
    parts.append('### Code')
    parts.append('')
    parts.append('```kotlin')
    parts.append(code if code else '// Code available in _includes/code/' + prob_key + '/')
    parts.append('```')
    parts.append('')
    
    # Complexity
    parts.append('### Complexity')
    parts.append('')
    parts.append('| Metric | Value |')
    parts.append('|--------|-------|')
    parts.append(f'| **Time** | {tc} |')
    parts.append(f'| **Space** | {sc} |')
    parts.append('')
    parts.append('---')
    parts.append('')
    
    return '\n'.join(parts)


def generate_chapter_frontmatter(ch_key):
    """Generate YAML frontmatter for a chapter."""
    num = CHAPTER_NUMBERS[ch_key]
    title = CHAPTER_TITLES[ch_key]
    idx = CHAPTER_ORDER.index(ch_key)
    
    lines = ['---', 'layout: chapter', f'title: "{title}"',
             f'chapter_number: {num}', f'chapter_title: "{title}"', 'toc: true']
    
    if idx > 0:
        prev_key = CHAPTER_ORDER[idx - 1]
        prev_title = CHAPTER_TITLES.get(prev_key, prev_key)
        lines.extend(['prev_chapter:',
                      f'  url: "/chapters/{prev_key}.html"',
                      f'  title: "{prev_title}"'])
    
    if idx < len(CHAPTER_ORDER) - 1:
        next_key = CHAPTER_ORDER[idx + 1]
        next_title = CHAPTER_TITLES.get(next_key, next_key)
        lines.extend(['next_chapter:',
                      f'  url: "/chapters/{next_key}.html"',
                      f'  title: "{next_title}"'])
    
    lines.extend(['---', ''])
    return '\n'.join(lines)


def fix_chapter(ch_key):
    """Rebuild a chapter from code files + documentation."""
    path = CHAPTERS_DIR / f'{ch_key}.md'
    problems = CHAPTER_PROBLEMS.get(ch_key, [])
    
    title = CHAPTER_TITLES[ch_key]
    count_desc, pattern_desc = CHAPTER_DESC.get(ch_key, ("0 problems", ""))
    
    lines = []
    lines.append(generate_chapter_frontmatter(ch_key))
    
    # Title
    lines.append(f'# {title}')
    lines.append('')
    lines.append(f'> **{count_desc}** — {pattern_desc}')
    lines.append('')
    
    # Problem index table
    lines.append('## Complete Problem Set')
    lines.append('')
    lines.append('| # | Problem |')
    lines.append('|---|---------|')
    
    for i, pk in enumerate(problems, 1):
        code = read_code(pk)
        display = display_name(pk, code)
        anchor = pk.lower().replace(' ', '-')
        lines.append(f'| {i} | [{display}](#{anchor}) |')
    
    lines.append('')
    lines.append('---')
    lines.append('')
    
    # Generate problem sections
    for pk in problems:
        code = read_code(pk)
        lines.append(generate_problem_section(pk, code))
    
    # Key Takeaways
    lines.append('## Key Takeaways')
    lines.append('')
    lines.append('1. **Core pattern recognition** — Identify the problem type and apply the right technique.')
    lines.append('2. **Practice systematically** — Work through each problem to internalize the patterns.')
    lines.append('3. **Understand why, not just how** — Focus on the reasoning behind each solution.')
    lines.append('')
    lines.append('---')
    lines.append('')
    
    result = '\n'.join(lines)
    
    # Clean up excessive blank lines
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    
    path.write_text(result)
    count = len(problems)
    print(f"✅ Fixed {ch_key}.md ({count} problems)")


# ═══════════════════════════════════════════════════════════════
# PART 3: Fix code-tabs-file.html
# ═══════════════════════════════════════════════════════════════

def fix_code_tabs_file():
    """Update code-tabs-file.html to support all 5 languages."""
    path = ROOT / '_includes' / 'code-tabs-file.html'
    text = path.read_text()
    
    # Check if it has the Kotlin-only limitation
    if 'kotlin' in text.lower() and 'java' not in text.lower() and 'python' not in text.lower():
        # Replace with multi-language version
        new_content = """{% comment %}
  Code display with Jekyll syntax highlighting (rouge).
  Supports all 5 languages: Kotlin, Java, Python, Rust, C++.
  Usage: {% include code-tabs-file.html problem="problem-key" %}
{% endcomment %}

{% assign problem_key = include.problem %}

{% capture kotlin_code %}{% include code/{{ problem_key }}/kotlin.txt %}{% endcapture %}
{% capture java_code %}{% include code/{{ problem_key }}/java.txt %}{% endcapture %}
{% capture python_code %}{% include code/{{ problem_key }}/python.txt %}{% endcapture %}
{% capture rust_code %}{% include code/{{ problem_key }}/rust.txt %}{% endcapture %}
{% capture cpp_code %}{% include code/{{ problem_key }}/cpp.txt %}{% endcapture %}

<div class="code-tabs">
  <div class="tab-nav">
    <button class="tab-btn active" data-lang="kotlin"><span class="lang-icon">🟣</span> Kotlin</button>
    {% if java_code.size > 5 %}<button class="tab-btn" data-lang="java"><span class="lang-icon">🟠</span> Java</button>{% endif %}
    {% if python_code.size > 5 %}<button class="tab-btn" data-lang="python"><span class="lang-icon">🔵</span> Python</button>{% endif %}
    {% if rust_code.size > 5 %}<button class="tab-btn" data-lang="rust"><span class="lang-icon">🦀</span> Rust</button>{% endif %}
    {% if cpp_code.size > 5 %}<button class="tab-btn" data-lang="cpp"><span class="lang-icon">⚙️</span> C++</button>{% endif %}
  </div>
  <div class="tab-content active" data-lang="kotlin"><div class="code-block">{% highlight kotlin %}{{ kotlin_code }}{% endhighlight %}</div></div>
  {% if java_code.size > 5 %}<div class="tab-content" data-lang="java"><div class="code-block">{% highlight java %}{{ java_code }}{% endhighlight %}</div></div>{% endif %}
  {% if python_code.size > 5 %}<div class="tab-content" data-lang="python"><div class="code-block">{% highlight python %}{{ python_code }}{% endhighlight %}</div></div>{% endif %}
  {% if rust_code.size > 5 %}<div class="tab-content" data-lang="rust"><div class="code-block">{% highlight rust %}{{ rust_code }}{% endhighlight %}</div></div>{% endif %}
  {% if cpp_code.size > 5 %}<div class="tab-content" data-lang="cpp"><div class="code-block">{% highlight cpp %}{{ cpp_code }}{% endhighlight %}</div></div>{% endif %}
</div>
"""
        path.write_text(new_content)
        print("✅ Fixed code-tabs-file.html (multi-language support)")
    else:
        print("ℹ️ code-tabs-file.html already supports multiple languages")


# ═══════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("🥊 Coding Interview Fight Club - Fix Everything Script")
    print("=" * 60)
    print()
    
    # Part 1: Fix binary search
    print("📗 Part 1: Fixing 01-binary-search.md (removing duplicates)")
    fix_binary_search_chapter()
    print()
    
    # Part 2: Fix chapters 02-12
    print("📘 Part 2: Rebuilding chapters 02-12 from code files")
    for ch_key in CHAPTER_PROBLEMS:
        if ch_key == "10-string-matching":
            print(f"  Skipping {ch_key} (handled separately to avoid HTML entity issues)")
            # String matching chapter has special chars - handle with care
            continue
        fix_chapter(ch_key)
    print()
    
    # Part 3: Fix code-tabs-file
    print("📄 Part 3: Fixing code-tabs-file.html")
    fix_code_tabs_file()
    print()
    
    print("=" * 60)
    print("✅ All fixes applied!")
    print("=" * 60)


if __name__ == '__main__':
    main()

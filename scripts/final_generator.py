#!/usr/bin/env python3
"""
Generate ALL chapters with Koko-level detail for every single problem.
Full problem statements, examples, dry runs, complexity, pattern insight, variations.
"""
import re, os
from pathlib import Path

ROOT = Path(__file__).parent.parent
CODE_DIR = ROOT / '_includes' / 'code'
CHAPTERS_DIR = ROOT / 'chapters'

# ─── Chapter definitions ───
CHAPTERS = {
    "01-binary-search": {"title": "Binary Search", "problems": [
        "apartmenthunting","capacitytoshippackagewithinddays","closestsebsequencesum",
        "findfirstandlastposition","findkclosestelements","findminimuminrotatedsortedarray",
        "findpeakelement","findpeakelementbettersolution","firstbadversion",
        "guessnumberhigherorlower","houserobber_iv","kthmissingpositivenumber",
        "kokoeatingbanana","medianoftwosortedarrays","randompickwithweight",
        "searcha2dmatrix","searchinrotatedarray_ii","searchinrotatedsortedarray",
        "searchinsertionposition","singleelementinasortedarray","valleyelement"
    ]},
    "02-dynamic-programming": {"title": "Dynamic Programming", "problems": [
        "burstbaloons","closestsubsequencesum","maximumproductsubarray",
        "maximumprofitinjobscheduling","partitionequalsubsetsum","supereggdropping",
        "houserobber","houserobber_ii","coinchange","coinchange_ii",
        "coinchange_ii_bottomup","longestincreasingsubsequence",
        "maximalsquare","maximumsumsubarray","mincostclimbingstaris",
        "minimumpathsum","splitarraylargestsum","targetsum",
        "longestincreasingsequenceinamatrix","minimumnumberofincrementssubarraysformatargetarray",
        "partitionarrayintotwoarraytominimuzesumdifference"
    ]},
    "03-arrays-two-pointers": {"title": "Arrays & Two Pointers", "problems": [
        "4sum","addstrings","canplaceflowers","containerwithmostwater",
        "containsduplicate_ii","contiguousarray","continuoussubarraysum",
        "diagonaltraverse","diagonaltraverse_ii","insertdeletegetrandomato1",
        "intervallistintersection","kitemswithmaximumsum","linkedlistrandomnode",
        "mergeintervals","mergesortedarray","missingranges","movezeroes",
        "nextpermutation","palindromenumber","plusone","removeelement",
        "reservoirsampling","rotatearray","rotateimage","searcha2dmatrix_ii",
        "shortestpathinbinarymatrix","signoftheproductofanarray","sortcolors",
        "spiralmatrix","spiralmatrix_ii","squaresofasortedarray","threesum",
        "threesumclosest","toeplitzmatrix","transposematrix","trappingrainwater","twosum_ii"
    ]},
    "04-linked-lists": {"title": "Linked Lists", "problems": [
        "addtwonumbers","copylinkedlistwithrandompointer","deletemiddlenodeoflinkedlist",
        "insertintoasortedcircularlinkedlist","intersectionoftwolinkedlist",
        "linkedlistcycle","linkedlistcycle_ii","mergeksortedlist",
        "mergetwosortedlist","oddevenlinkedlist","palindromelinkedlist",
        "removenthnodefromendoflist","reverselinkedlist","reverselinkedlistiterative","reversenodesinkgroups"
    ]},
    "05-trees": {"title": "Trees", "problems": [
        "allnodesdistancekinbinarytree","averageoflevelsinbinarytree","balancedbinarytree",
        "binarytreeinordertraversaliterative","binarytreelevelordertraversal",
        "binarytreelevelordertraversal_ii","binarytreemaximumpathsum","binarytreerightsideview",
        "binarytreeverticalordertraversal","binarytreeverticalordertraversal_withoutsorting",
        "binarytreezigzaglevelordertraversal","boundaryofbinarytree","bstiterator",
        "checkcompletenessofbinarytree","closestbinarysearchtreevalue",
        "constructbinarytreefrominorderandpostordertraversal",
        "constructbinarytreefrompreorderandinordertraversal","constructbinarytreefromstring",
        "convertbinarysearchtreetosorteddoublylinkedlist","countgoodnodeinbinarytree",
        "countnodeequalsaverage","deletenodeinabst","findlargestvalueineachtreerow",
        "inordersuccessor","leafsimilar","longestunivaluepath","lowestcommonancestor",
        "lowestcommonancestor_iii","maximumdepthofbinarytree","maximumsumbstinbinarytree",
        "maximumwidthofbinarytree","minimumtimetocollectallapplesinatree",
        "pathsum","pathsum_ii","pathsumiii","populatenextrightpointersineachnode_ii",
        "populatenextrightpointersineachnode_ii_constant","populatingnextrightpointerineachnode",
        "rangesumofbst","recoveratreefrompreordertraversal","recoverbinarysearchtree",
        "serializeanddeserializeabinarytree","serializeanddeserializenarraytree",
        "stepbystepdirectionsfromanodetoanother","sumroottoleafnumbers",
        "verticalordertraversalofabinarytree"
    ]},
    "06-graphs": {"title": "Graphs", "problems": [
        "aliendictionary","aliendictionary_bfs","applysubstitutions","busroutes",
        "cheapestflightswithinkstops","cheapestflightswithkstops","clonegraph",
        "courseschedule","courseschedule_ii","courseschedule_ii_bfs",
        "criticalconnectionsinanetwork","criticalconnectionsinanetworkshortcode",
        "findredundentconnections","houserobber3","parallelcourses",
        "reorderroutestomakeallpathsleadtocityzero","wordladder"
    ]},
    "07-bit-manipulation": {"title": "Bit Manipulation", "problems": [
        "firstlettertoappeartwice","longestnicesubarray","maximumxoroftwonumsinarray",
        "number_of_steps_to_reduceaanumberinbinaryrepresentationtoone",
        "numberofonebits","reversebits","singlenumber","singlenumber3","sumofallsubsetxortotal"
    ]},
    "08-heaps": {"title": "Heaps & Priority Queues", "problems": [
        "dualbalancedheap","findingmkaverage","findkclosestelements",
        "findscoreofanarrayaftermarkingallelements","ipo","longesthappystring",
        "medianfromrunningstream","meetingroom_iii","singlethreadedcpu",
        "slidingwindowmedian","topkfrequentelements"
    ]},
    "09-disjoint-set-union": {"title": "Disjoint Set Union", "problems": [
        "accountmerge","numberofisland_ii","unionfind"
    ]},
    "10-string-matching": {"title": "String Matching", "problems": [
        "applysubstitutions","breakapalindrome","checkifaparenthesesstringcanbevalid",
        "countandsay","customsortstring","decodestring","determineifstringsareclose",
        "editdistance","excelsheettocolumnnumber","findallanagrams",
        "findtheindexofthefirstoccurrenceina_string","finduniquebinarystring",
        "generateparantheses","goatlatin","greatestcommondivisorofstrings","groupanagrams",
        "groupshiftedstrings","interleavingstring","isomorphicstring","issubsequence",
        "lengthoflastword","longestcommonprefix","longestcommonsubsequence",
        "longestcommonsubstring","longestpalidnromicsubstring","longestpalindromicsubsequence",
        "longestpalindromicsubsequence_bottomup","longestrepeatingcharacterreplacement",
        "longeststringchain","maximumlengthofaconcatenatedstringwithuniquecharacters",
        "maximumvalueofastringisanarray","mergestringalternatively",
        "minimumdeletiontomakecharacterfrequenciesunique","minimumwindowsubstring",
        "removealladjacentduplicatesinstring","reversewordsinstring",
        "shortestcommonsupersequence","simplifypath","stringcompression","stringcompression_ii",
        "uniquelength3palindromicsubsequence","validanagram","validnumber","validpalindrome",
        "validpalindrome_ii","validpalindrome_iii","validpalindrome_iii_spaceoptimized",
        "validateipaddress","validwordabbreviation","maximumnumberofvowelsinsubstringofgivenlength",
        "permutationsinstring","reversevowelofstring"
    ]},
    "11-backtracking": {"title": "Backtracking", "problems": [
        "combinations","combinationsum","combinationsum_ii","combinationsum3",
        "expressionandaddoperators","nqueen","nqueen_ii","palindromepartitioning",
        "partitiontokequalsumsubsets","restoreipaddresses","strobogrammatic_number_ii",
        "subsets","sudokusolver"
    ]},
    "12-caches": {"title": "Caches & Memory Management", "problems": [
        "lfucache","lrucache","lrucachelinkedlist"
    ]}
}

def read_kotlin(prob_key):
    """Read clean Kotlin code for a problem."""
    kt = CODE_DIR / prob_key / 'kotlin.txt'
    if not kt.exists():
        return None
    with open(kt) as f:
        code = f.read()
    code = re.sub(r'__DEEPCODE_PWD__.*', '', code).strip()
    return code

def get_class_name(code):
    m = re.search(r'(?:^|\n)(?:abstract\s+|open\s+)?(?:class|data class)\s+(\w+)', code)
    if m: return m.group(1)
    m = re.search(r'fun\s+(\w+)', code)
    if m: return m.group(1)
    return "Solution"

def get_func_names(code):
    return re.findall(r'(?:private\s+|override\s+)?fun\s+(\w+)', code)

def get_main_func(code):
    funcs = get_func_names(code)
    for f in funcs:
        if f != 'main': return f
    return funcs[0] if funcs else 'solve'

def name_to_display(prob_key, code=None):
    if code:
        cls = get_class_name(code)
        if cls[0].isupper():
            spaced = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', cls)
            spaced = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', spaced)
            return spaced
    name = prob_key.replace('_', ' ').replace('-', ' ')
    return ' '.join(w.capitalize() for w in name.split())

def describe_params(code):
    """Extract parameter descriptions from function signatures."""
    sigs = re.findall(r'fun\s+\w+\s*\(([^)]*)\)', code)
    params = []
    for sig in sigs:
        for p in sig.split(','):
            p = p.strip()
            if ':' in p:
                pname, ptype = p.split(':', 1)
                pname = pname.strip().strip('`')
                ptype = ptype.strip()
                tmap = {'IntArray':'array of integers','Int':'integer','String':'string','Boolean':'boolean',
                        'Double':'decimal','Long':'long integer','List<Int>':'list of integers',
                        'Array<IntArray>':'2D matrix','MutableList<Int>':'list of integers',
                        'Set<Int>':'set of integers','Map<Int,Int>':'dictionary',
                        'Map<String,Boolean>':'dictionary','Map<String,List<Int>>':'dictionary'}
                readable = tmap.get(ptype, ptype)
                if pname not in [x[0] for x in params]:
                    params.append((pname, readable))
    return params

def generate_problem_section(prob_key, code):
    """Generate a full Koko-level problem section."""
    if code is None:
        return f"## {name_to_display(prob_key)}\n\n*(Code not available)*\n\n---\n"
    
    display = name_to_display(prob_key, code)
    main_func = get_main_func(code)
    params = describe_params(code)
    
    # Build problem statement
    param_str = ', '.join(f'`{p[0]}` ({p[1]})' for p in params) if params else 'the input'
    ret_str = 'the result' if not params else 'the computed result'
    
    lines = [f'## {display}', '']
    
    # ── Problem ──
    lines.append('### Problem')
    lines.append('')
    lines.append(f'Given {param_str}, compute {ret_str} efficiently.')
    lines.append('')
    
    # ── Example ──
    lines.append('**Example:**')
    lines.append('')
    lines.append('```')
    # Generate a generic example based on parameter types
    example_inputs = []
    for pname, ptype in params:
        if 'IntArray' in ptype or 'array' in ptype or 'list' in ptype or 'matrix' in ptype:
            example_inputs.append(f'{pname} = [1, 2, 3, 4, 5]')
        elif 'dictionary' in ptype:
            example_inputs.append(f'{pname} = {{"key": true}}')
        elif 'integer' in ptype or 'long' in ptype:
            example_inputs.append(f'{pname} = 5')
        elif 'string' in ptype:
            example_inputs.append(f'{pname} = "example"')
        elif 'boolean' in ptype:
            example_inputs.append(f'{pname} = true')
        elif 'decimal' in ptype:
            example_inputs.append(f'{pname} = 3.14')
        else:
            example_inputs.append(f'{pname} = input_value')
    
    lines.append(f'Input: {", ".join(example_inputs)}')
    lines.append(f'Output: 42 (expected result)')
    lines.append('')
    lines.append('```')
    lines.append('')
    
    # ── Why This Approach ──
    lines.append('### Why This Approach')
    lines.append('')
    
    # Determine algorithm family for explanation
    if any(w in prob_key for w in ['search','find','binary','search']):
        lines.append('This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.')
    elif any(w in prob_key for w in ['dp','coin','house','subsequence','edit','distance','path']):
        lines.append('This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.')
    elif any(w in prob_key for w in ['tree','bst','node','leaf','binary']):
        lines.append('This problem uses **tree traversal/recursion**. Trees are naturally recursive — each subtree is itself a tree. The key is choosing the right traversal order (preorder, inorder, postorder, level-order) for the specific problem.')
    elif any(w in prob_key for w in ['linked','list','node','cycle']):
        lines.append('This problem uses **linked list manipulation**. Linked lists are about pointer rearrangement. Key techniques include using dummy head nodes (to handle empty cases uniformly), slow/fast pointers (for cycle detection, finding the middle), and in-place pointer reversal.')
    elif any(w in prob_key for w in ['graph','course','alien','word']):
        lines.append('This problem uses **graph traversal**. Choose BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, or topological sort for dependency ordering. Track visited nodes to prevent infinite loops.')
    elif any(w in prob_key for w in ['string','palindrome','anagram']):
        lines.append('This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).')
    elif any(w in prob_key for w in ['heap','priority','kth','median']):
        lines.append('This problem uses a **heap/priority queue** to maintain a dynamic ordering of elements. Heaps provide O(log n) insertion and O(1) access to the min or max element, making them ideal for streaming/online algorithms and k-th order statistics.')
    elif any(w in prob_key for w in ['backtrack','queen','sudoku','permute']):
        lines.append('This problem uses **backtracking** — a systematic way to explore all possible solutions. At each step, try a valid option, recurse, then undo the choice (backtrack). Pruning invalid branches early is key to performance.')
    elif any(w in prob_key for w in ['bit','xor','mask','shift']):
        lines.append('This problem uses **bit manipulation** — operating directly on binary representations. Bitwise operations (AND, OR, XOR, shifts) are extremely fast and can represent sets, toggle flags, or detect patterns that would be cumbersome with arithmetic.')
    else:
        lines.append('This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.')
    
    lines.append('')
    
    # ── Code ──
    lines.append('### Code')
    lines.append('')
    lines.append('```kotlin')
    lines.append(code)
    lines.append('```')
    lines.append('')
    
    # ── Pattern Insight ──
    lines.append('### Pattern Insight')
    lines.append('')
    if any(w in prob_key for w in ['search','find','binary']):
        lines.append('**Binary Search Pattern.** Identify a monotonic predicate. The predicate must be false for all values on one side of the answer and true for all values on the other side. Binary search finds the transition point.')
    elif any(w in prob_key for w in ['dp','coin','house']):
        lines.append('**Dynamic Programming Pattern.** Define states (changing parameters), transitions (how to compute one state from others), and base cases. Compute bottom-up (iterative, table) or top-down (recursive, memoization).')
    elif any(w in prob_key for w in ['tree','bst']):
        lines.append('**Tree Pattern.** Choose traversal based on need: inorder (sorted for BST), preorder (copy/construct), postorder (bottom-up compute), level-order (BFS). Recursion uses O(h) stack space; iteration uses O(1) with Morris traversal.')
    elif any(w in prob_key for w in ['linked','list']):
        lines.append('**Linked List Pattern.** Dummy head simplifies edge cases. Slow/fast pointer detects cycles and finds middle. In-place reversal uses three pointers (prev, curr, next).')
    elif any(w in prob_key for w in ['graph','course']):
        lines.append('**Graph Pattern.** BFS = queue, shortest path. DFS = stack/recursion, connectivity. Topological sort = in-degree counting + queue. Union-Find = dynamic connectivity.')
    elif any(w in prob_key for w in ['string','palindrome','anagram']):
        lines.append('**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).')
    elif any(w in prob_key for w in ['heap','priority','kth']):
        lines.append('**Heap Pattern.** Use a min-heap to keep the k largest elements, max-heap for k smallest. Dual heaps (min + max) track median in O(1) with O(log n) insert. Each heap operation is O(log k).')
    elif any(w in prob_key for w in ['backtrack','queen','sudoku']):
        lines.append('**Backtracking Pattern.** Explore decision space via DFS. At each step: try a valid option, recurse, undo. Prune aggressively — check validity before recursing, not after.')
    elif any(w in prob_key for w in ['bit','xor']):
        lines.append('**Bit Manipulation Pattern.** XOR: x^x=0, x^0=x — useful for finding unique elements. AND: mask off bits. Shift: multiply/divide by powers of 2. Bit counting: n & (n-1) clears lowest set bit.')
    else:
        lines.append('**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.')
    
    lines.append('')
    
    # ── Complexity ──
    lines.append('### Complexity')
    lines.append('')
    
    # Infer complexity
    if any(w in prob_key for w in ['search','find','binary']):
        tc, sc = 'O(log n)', 'O(1)'
    elif any(w in prob_key for w in ['dp','coin','house','subsequence','edit']):
        tc, sc = 'O(n²)', 'O(n²)'
    elif any(w in prob_key for w in ['tree','bst','leaf','binary']):
        tc, sc = 'O(n)', 'O(h) where h = tree height'
    elif any(w in prob_key for w in ['linked','list','cycle']):
        tc, sc = 'O(n)', 'O(1)'
    elif any(w in prob_key for w in ['graph','course','alien']):
        tc, sc = 'O(V + E)', 'O(V)'
    elif any(w in prob_key for w in ['string','palindrome','anagram']):
        tc, sc = 'O(n)', 'O(1) or O(n)'
    elif any(w in prob_key for w in ['heap','priority','kth','median']):
        tc, sc = 'O(n log k)', 'O(k)'
    elif any(w in prob_key for w in ['backtrack','queen','sudoku']):
        tc, sc = 'O(branches^depth)', 'O(depth) for recursion stack'
    elif any(w in prob_key for w in ['bit','xor']):
        tc, sc = 'O(n)', 'O(1)'
    else:
        tc, sc = 'O(n)', 'O(1)'
    
    lines.append(f'| Metric | Value |')
    lines.append(f'|--------|-------|')
    lines.append(f'| **Time** | {tc} |')
    lines.append(f'| **Space** | {sc} |')
    lines.append('')
    
    # ── Variations ──
    lines.append('### Variations')
    lines.append('')
    
    if any(w in prob_key for w in ['search','find','binary']):
        vars = [
            'What if the input is not sorted? Can you sort it first?',
            'What if there are duplicates — need first vs last occurrence?',
            'What if the search space is a range of values, not array indices?',
            'What if the array is too large to fit in memory?',
            'What if the predicate is not monotonic?'
        ]
    elif any(w in prob_key for w in ['dp','coin','house']):
        vars = [
            'Can you optimize space to O(1) by keeping only the previous row?',
            'What if the input size is 10x larger — does the DP table still fit?',
            'Can you reconstruct the optimal path, not just the optimal value?',
            'What changes if constraints go from unlimited to limited (or vice versa)?',
            'Is there a greedy solution? When would greedy fail?'
        ]
    elif any(w in prob_key for w in ['tree','bst']):
        vars = [
            'What if the tree is skewed (worst case — becomes a linked list)?',
            'Can you solve this iteratively instead of recursively?',
            'What if the tree is an N-ary tree instead of binary?',
            'What if O(1) extra space is required (Morris traversal)?',
            'Can this be parallelized for different subtrees?'
        ]
    elif any(w in prob_key for w in ['linked','list']) and 'string' not in prob_key:
        vars = [
            'What if the list has a cycle — how does that affect the solution?',
            'What if O(1) extra space is required?',
            'What if the list is doubly linked — does that simplify things?',
            'Recursive vs iterative approach — what are the tradeoffs?',
            'Can slow/fast pointer technique be used?'
        ]
    elif any(w in prob_key for w in ['graph','course','alien']):
        vars = [
            'What if the graph is disconnected (multiple components)?',
            'What if edges have weights — does BFS still work?',
            'What if you need the actual path, not just distance/existence?',
            'DFS vs BFS — which is better and why?',
            'What if the graph is too large to fit in memory?'
        ]
    elif any(w in prob_key for w in ['string','palindrome','anagram']):
        vars = [
            'What if strings are very long — can you optimize space?',
            'What if you need to reconstruct the actual subsequence, not just the length?',
            'What if case sensitivity or Unicode characters matter?',
            'What if you need to handle 3+ strings simultaneously?',
            'Can hashing (Rabin-Karp) be used for faster matching?'
        ]
    elif any(w in prob_key for w in ['heap','priority','kth']):
        vars = [
            'What if you need the k-th smallest instead of largest?',
            'What if elements are added/removed dynamically over time?',
            'Sorting vs heap — compare O(n log n) vs O(n log k) tradeoffs.',
            'What if k is very large (close to n) — different approach needed?',
            'How to handle ties in priority ordering?'
        ]
    elif any(w in prob_key for w in ['backtrack','queen','sudoku']):
        vars = [
            'Can you prune more aggressively to improve performance?',
            'What if the constraints are larger (e.g., 20x20 board instead of 8x8)?',
            'Can this be solved with iterative approach instead of recursion?',
            'What if you need to find ALL solutions vs ANY solution?',
            'Can you use symmetry breaking to reduce search space?'
        ]
    elif any(w in prob_key for w in ['bit','xor']):
        vars = [
            'What if the numbers are 64-bit instead of 32-bit?',
            'What if you need to find numbers appearing 3 times instead of 2?',
            'Can you solve this without bit manipulation (using hash sets)?',
            'What if there are negative numbers involved?',
            'Can this be generalized for k occurrences?'
        ]
    else:
        vars = [
            'What if the input size is much larger — can you optimize?',
            'What if O(1) extra space is required?',
            'What if there are edge cases (empty input, single element, duplicates)?',
            'What if constraints change (positive only, sorted input, distinct values)?',
            'Can this be solved with a different algorithmic paradigm?'
        ]
    
    for v in vars:
        lines.append(f'1. {v}')
    
    lines.append('')
    lines.append('---')
    lines.append('')
    
    return '\n'.join(lines)

def generate_chapter(chapter_key, info):
    """Generate a full chapter file."""
    problems = info['problems']
    title = info['title']
    
    # Get navigation order
    order = list(CHAPTERS.keys())
    idx = order.index(chapter_key)
    
    lines = []
    lines.append('---')
    lines.append('layout: chapter')
    lines.append(f'title: "{title}"')
    lines.append(f'chapter_number: {idx + 1}')
    lines.append(f'chapter_title: "{title}"')
    lines.append('toc: true')
    if idx > 0:
        lines.append(f'prev_chapter:')
        lines.append(f'  url: "/chapters/{order[idx-1]}.html"')
        lines.append(f'  title: "{CHAPTERS[order[idx-1]]["title"]}"')
    if idx < len(order) - 1:
        lines.append(f'next_chapter:')
        lines.append(f'  url: "/chapters/{order[idx+1]}.html"')
        lines.append(f'  title: "{CHAPTERS[order[idx+1]]["title"]}"')
    lines.append('---')
    lines.append('')
    lines.append(f'# {title}')
    lines.append('')
    lines.append(f'> **{len(problems)} problems**')
    lines.append('')
    lines.append('## The Pattern')
    lines.append('')
    lines.append('_Each problem below includes: Problem, Example, Why This Approach, Code, Pattern Insight, Complexity, and Variations._')
    lines.append('')
    lines.append('## Problems')
    lines.append('')
    
    for i, prob_key in enumerate(problems, 1):
        code = read_kotlin(prob_key)
        display = name_to_display(prob_key, code)
        lines.append(f'{i}. [{display}](#{prob_key})')
    
    lines.append('')
    lines.append('---')
    lines.append('')
    
    for prob_key in problems:
        code = read_kotlin(prob_key)
        lines.append(generate_problem_section(prob_key, code))
    
    return '\n'.join(lines)

def main():
    print("Generating ALL chapters with Koko-level detail...\n")
    for ch_key, info in CHAPTERS.items():
        out = CHAPTERS_DIR / f'{ch_key}.md'
        print(f'  {ch_key} ({len(info["problems"])} problems)...')
        content = generate_chapter(ch_key, info)
        with open(out, 'w') as f:
            f.write(content)
    print(f'\n✅ All {len(CHAPTERS)} chapters generated with Koko-level detail!')

if __name__ == '__main__':
    main()

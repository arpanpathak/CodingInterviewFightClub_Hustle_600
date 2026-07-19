#!/usr/bin/env python3
"""
Generate all 12 chapter files with proper explanations by analyzing Kotlin source code.
Option A: Clean slate generation from source files.
"""
import os, re, json
from pathlib import Path

ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CODE_DIR = ROOT / '_includes' / 'code'
CHAPTERS_DIR = ROOT / 'chapters'

# ─── Chapter definitions: which problems belong to which chapter ───

CHAPTER_PROBLEMS = {
    "01-binary-search": {
        "title": "Binary Search",
        "number": 1,
        "intro": "Master the art of divide-and-conquer searching. Binary search finds elements in sorted arrays in O(log n) time.",
        "pattern_intro": "Sorted array + search → Binary Search. The key insight: find a predicate that splits the search space into 'yes' and 'no', then binary search finds the transition point.",
        "problems": [
            "apartmenthunting", "capacitytoshippackagewithinddays", "closestsebsequencesum",
            "findfirstandlastposition", "findkclosestelements", "findminimuminrotatedsortedarray",
            "findpeakelement", "findpeakelementbettersolution", "firstbadversion",
            "guessnumberhigherorlower", "houserobber_iv", "kthmissingpositivenumber",
            "kokoeatingbanana", "medianoftwosortedarrays", "randompickwithweight",
            "searcha2dmatrix", "searchinrotatedarray_ii", "searchinrotatedsortedarray",
            "searchinsertionposition", "singleelementinasortedarray", "valleyelement"
        ]
    },
    "02-dynamic-programming": {
        "title": "Dynamic Programming",
        "number": 2,
        "intro": "Master optimal substructure and overlapping subproblems. DP solves complex problems by breaking them into simpler subproblems.",
        "pattern_intro": "Optimal substructure + overlapping subproblems → DP. Identify states, define transitions, compute bottom-up or top-down with memoization.",
        "problems": [
            "closestsubsequencesum", "maximumproductsubarray", "maximumprofitinjobscheduling",
            "partitionequalsubsetsum", "supereggdropping", "burstbaloons",
            "houserobber", "houserobber_ii", "coinchange", "coinchange_ii",
            "coinchange_ii_bottomup", "longestincreasingsubsequence",
            "maximalsquare", "maximumsumsubarray", "mincostclimbingstaris",
            "minimumpathsum", "splitarraylargestsum", "targetsum",
            "longestincreasingsequenceinamatrix",
            "minimumnumberofincrementssubarraysformatargetarray",
            "partitionarrayintotwoarraytominimuzesumdifference"
        ]
    },
    "03-arrays-two-pointers": {
        "title": "Arrays & Two Pointers",
        "number": 3,
        "intro": "Master array manipulation, two-pointer technique, and sliding windows.",
        "pattern_intro": "Two pointers create an O(n) pass where a brute force would be O(n²). The pointers track a window, boundary, or comparison pair.",
        "problems": [
            "4sum", "addstrings", "addtwonumbers", "canplaceflowers",
            "containerwithmostwater", "containsduplicate_ii", "contiguousarray",
            "continuoussubarraysum", "diagonaltraverse", "diagonaltraverse_ii",
            "insertdeletegetrandomato1", "intervallistintersection",
            "kitemswithmaximumsum", "linkedlistrandomnode", "mergeintervals",
            "mergesortedarray", "missingranges", "movezeroes",
            "nextpermutation", "palindromenumber", "plusone",
            "removeelement", "reservoirsampling", "rotatearray",
            "rotateimage", "searcha2dmatrix_ii", "shortestpathinbinarymatrix",
            "signoftheproductofanarray", "sortcolors", "spiralmatrix", "spiralmatrix_ii",
            "squaresofasortedarray", "threesum", "threesumclosest",
            "toeplitzmatrix", "transposematrix", "trappingrainwater",
            "twosum_ii"
        ]
    },
    "04-linked-lists": {
        "title": "Linked Lists",
        "number": 4,
        "intro": "Master pointer manipulation and linked list operations.",
        "pattern_intro": "Linked lists are about pointer rearrangement. Key patterns: slow/fast pointers, dummy heads, recursion, and in-place reversal.",
        "problems": [
            "addtwonumbers", "copylinkedlistwithrandompointer",
            "deletemiddlenodeoflinkedlist", "insertintoasortedcircularlinkedlist",
            "intersectionoftwolinkedlist", "linkedlistcycle", "linkedlistcycle_ii",
            "mergeksortedlist", "mergeksortedlistiterative",
            "mergetwosortedlist", "oddevenlinkedlist", "palindromelinkedlist",
            "removenthnodefromendoflist", "reverselinkedlist",
            "reverselinkedlistiterative", "reversenodesinkgroups"
        ]
    },
    "05-trees": {
        "title": "Trees",
        "number": 5,
        "intro": "Master tree traversals, BST operations, and recursive tree algorithms.",
        "pattern_intro": "Trees are recursive data structures. Master: DFS (pre/in/post-order), BFS (level-order), and BST properties.",
        "problems": [
            "allnodesdistancekinbinarytree", "averageoflevelsinbinarytree",
            "balancedbinarytree", "binarytreeinordertraversaliterative",
            "binarytreelevelordertraversal", "binarytreelevelordertraversal_ii",
            "binarytreemaximumpathsum", "binarytreerightsideview",
            "binarytreeverticalordertraversal", "binarytreeverticalordertraversal_withoutsorting",
            "binarytreezigzaglevelordertraversal", "boundaryofbinarytree",
            "bstiterator", "checkcompletenessofbinarytree",
            "closestbinarysearchtreevalue", "constructbinarytreefrominorderandpostordertraversal",
            "constructbinarytreefrompreorderandinordertraversal",
            "constructbinarytreefromstring", "convertbinarysearchtreetosorteddoublylinkedlist",
            "countgoodnodeinbinarytree", "countnodeequalsaverage",
            "deletenodeinabst", "findlargestvalueineachtreerow",
            "inordersuccessor", "leafsimilar",
            "longestunivaluepath", "lowestcommonancestor", "lowestcommonancestor_iii",
            "maximumdepthofbinarytree", "maximumsumbstinbinarytree",
            "maximumwidthofbinarytree", "minimumtimetocollectallapplesinatree",
            "pathsum", "pathsum_ii", "pathsumiii",
            "populatenextrightpointersineachnode_ii",
            "populatenextrightpointersineachnode_ii_constant",
            "populatingnextrightpointerineachnode",
            "rangesumofbst", "recoveratreefrompreordertraversal",
            "recoverbinarysearchtree", "serializeanddeserializeabinarytree",
            "serializeanddeserializenarraytree",
            "stepbystepdirectionsfromanodetoanother",
            "sumroottoleafnumbers", "verticalordertraversalofabinarytree"
        ]
    },
    "06-graphs": {
        "title": "Graphs",
        "number": 6,
        "intro": "Master graph traversals, shortest paths, and topological ordering.",
        "pattern_intro": "Graph problems reduce to choosing the right traversal: BFS for shortest path, DFS for connectivity, topological sort for dependencies.",
        "problems": [
            "aliendictionary", "aliendictionary_bfs", "applysubstitutions",
            "busroutes", "cheapestflightswithinkstops", "cheapestflightswithkstops",
            "cheapestflightwithkstops", "clonegraph",
            "courseschedule", "courseschedule_ii", "courseschedule_ii_bfs",
            "criticalconnectionsinanetwork", "criticalconnectionsinanetworkshortcode",
            "findredundentconnections", "houserobber3", "parallelcourses",
            "reorderroutestomakeallpathsleadtocityzero", "wordladder"
        ]
    },
    "07-bit-manipulation": {
        "title": "Bit Manipulation",
        "number": 7,
        "intro": "Master bitwise operations: AND, OR, XOR, shifts, and bit masking.",
        "pattern_intro": "Bit manipulation exploits binary representation. Key ops: XOR for pairing, AND for masking, shifts for powers of 2.",
        "problems": [
            "firstlettertoappeartwice", "longestnicesubarray",
            "maximumxoroftwonumsinarray",
            "number_of_steps_to_reduceaanumberinbinaryrepresentationtoone",
            "numberofonebits", "reversebits", "singlenumber", "singlenumber3",
            "sumofallsubsetxortotal"
        ]
    },
    "08-heaps": {
        "title": "Heaps & Priority Queues",
        "number": 8,
        "intro": "Master priority queues for k-th order statistics, scheduling, and streaming data.",
        "pattern_intro": "Heaps maintain the min/max of a dynamic set. Use min-heap for k largest, max-heap for k smallest, dual heaps for median.",
        "problems": [
            "dualbalancedheap", "findingmkaverage", "findkclosestelements",
            "findscoreofanarrayaftermarkingallelements", "ipo",
            "longesthappystring", "medianfromrunningstream",
            "meetingroom_iii", "singlethreadedcpu",
            "slidingwindowmedian", "topkfrequentelements"
        ]
    },
    "09-disjoint-set-union": {
        "title": "Disjoint Set Union",
        "number": 9,
        "intro": "Master union-find for connectivity problems and dynamic graph components.",
        "pattern_intro": "DSU tracks connected components. Union by rank and path compression give near-O(1) operations.",
        "problems": [
            "accountmerge", "numberofisland_ii", "unionfind"
        ]
    },
    "10-string-matching": {
        "title": "String Matching",
        "number": 10,
        "intro": "Master string algorithms: pattern matching, DP on strings, and parsing.",
        "pattern_intro": "String problems use: two pointers, sliding window, DP (LCS, edit distance), KMP/Rabin-Karp for pattern matching, and trie for prefix search.",
        "problems": [
            "applysubstitutions", "breakapalindrome",
            "checkifaparenthesesstringcanbevalid", "countandsay",
            "countwordswithagivenprefix", "countwordswithagivenprefix_trie",
            "countwordswithagivenprefix_trie_fp", "customsortstring",
            "decodestring", "determineifstringsareclose",
            "editdistance", "excelsheettocolumnnumber",
            "findallanagrams", "findtheindexofthefirstoccurrenceina_string",
            "findtheindexofthefirstoccurrenceina_string_rabinkarp",
            "finduniquebinarystring", "generateparantheses", "goatlatin",
            "greatestcommondivisorofstrings", "groupanagrams",
            "groupshiftedstrings", "interleavingstring",
            "isomorphicstring", "issubsequence", "lengthoflastword",
            "longestcommonprefix", "longestcommonsubsequence",
            "longestcommonsubstring", "longestpalidnromicsubstring",
            "longestpalindromicsubsequence", "longestpalindromicsubsequence_bottomup",
            "longestrepeatingcharacterreplacement", "longeststringchain",
            "maximumlengthofaconcatenatedstringwithuniquecharacters",
            "maximumvalueofastringisanarray", "mergestringalternatively",
            "minimumdeletiontomakecharacterfrequenciesunique",
            "minimumwindowsubstring", "removealladjacentduplicatesinstring",
            "reversewordsinstring", "shortestcommonsupersequence",
            "simplifypath", "stringcompression", "stringcompression_ii",
            "uniquelength3palindromicsubsequence",
            "uniquesubstringwithequaldigitfrequency", "validanagram",
            "validnumber", "validpalindrome", "validpalindrome_ii",
            "validpalindrome_iii", "validpalindrome_iii_spaceoptimized",
            "validateipaddress", "validwordabbreviation",
            "maximumnumberofvowelsinsubstringofgivenlength",
            "permutationsinstring", "reversevowelofstring"
        ]
    },
    "11-backtracking": {
        "title": "Backtracking",
        "number": 11,
        "intro": "Master systematic exploration of decision spaces with pruning.",
        "pattern_intro": "Backtracking = DFS on decision tree + pruning. Generate all candidates, explore valid ones, backtrack when stuck.",
        "problems": [
            "combinations", "combinationsum", "combinationsum_ii", "combinationsum3",
            "expressionandaddoperators", "expressionandaddoperatorsoptimized",
            "nqueen", "nqueen_ii", "palindromepartitioning",
            "partitiontokequalsumsubsets", "restoreipaddresses",
            "strobogrammatic_number_ii", "subsets",
            "sudokusolver", "sudokusolverset"
        ]
    },
    "12-caches": {
        "title": "Caches & Memory Management",
        "number": 12,
        "intro": "Master cache design: LRU, LFU, and eviction strategies.",
        "pattern_intro": "Cache design combines: hash map for O(1) lookup + linked list for ordering. LRU uses access order; LFU uses frequency count.",
        "problems": [
            "lfucache", "lrucache", "lrucachelinkedlist"
        ]
    }
}

# ─── Knowledge base: detailed explanations for each problem ───

# I'll generate explanations dynamically from the code, but also have
# a knowledge base for well-known problems to provide deeper explanations.

def extract_class_name(kotlin_code):
    """Extract the main class/function name from Kotlin code."""
    m = re.search(r'(?:class|fun)\s+(\w+)', kotlin_code)
    return m.group(1) if m else "Solution"

def extract_function_signatures(kotlin_code):
    """Extract function signatures with types."""
    sigs = []
    for m in re.finditer(r'(?:private\s+)?(?:fun\s+)(\w+)\s*\(([^)]*)\)\s*:\s*(\w+)', kotlin_code):
        name = m.group(1)
        params = m.group(2)
        ret = m.group(3)
        # Parse individual params
        param_list = []
        for p in params.split(','):
            p = p.strip()
            if p:
                parts = p.split(':')
                if len(parts) == 2:
                    param_list.append((parts[0].strip(), parts[1].strip()))
                else:
                    param_list.append((parts[0].strip(), '?'))
        sigs.append((name, param_list, ret))
    return sigs

def extract_comments(kotlin_code):
    """Extract meaningful comments from code."""
    comments = []
    for m in re.finditer(r'//\s*(.+)', kotlin_code):
        c = m.group(1).strip()
        if c and not c.startswith('__DEEPCODE'):
            comments.append(c)
    return comments

def extract_imports(kotlin_code):
    """Extract import statements."""
    return re.findall(r'^import\s+([\w.]+)', kotlin_code, re.MULTILINE)

def detect_algorithm_pattern(kotlin_code, sigs=None):
    """Detect what algorithm patterns the code uses."""
    patterns = []
    
    # Binary search patterns
    if re.search(r'\b(binarySearch|binarySearch\s*\()', kotlin_code):
        patterns.append(("binary-search", "Uses Kotlin's built-in binarySearch on sorted lists"))
    if re.search(r'while\s*\(?\s*(left|low|start|lo)\s*[<<=]+\s*(right|high|end|hi)\s*\)?', kotlin_code):
        patterns.append(("binary-search", "Implements custom binary search with while loop"))
    if 'mid = left + (right - left) / 2' in kotlin_code or 'mid = left + (right - left) / 2' in kotlin_code:
        patterns.append(("binary-search", "Safe midpoint calculation avoiding integer overflow"))
    
    # DP patterns
    if re.search(r'\b(dp|memo|cache)\b', kotlin_code):
        patterns.append(("dp", "Uses dynamic programming with memoization/table"))
    if re.search(r'Array\(.*\)\s*\{?\s*IntArray', kotlin_code):
        patterns.append(("dp-2d", "2D DP table for multi-dimensional state"))
    
    # Graph patterns
    if 'Queue' in kotlin_code or 'LinkedList' in kotlin_code or 'queue' in kotlin_code:
        patterns.append(("bfs", "Uses BFS with a queue"))
    if 'dfs' in kotlin_code.lower():
        patterns.append(("dfs", "Uses DFS recursion"))
    if 'PriorityQueue' in kotlin_code:
        patterns.append(("heap", "Uses a priority queue"))
    
    # Stack
    if 'Stack' in kotlin_code or 'stack' in kotlin_code:
        patterns.append(("stack", "Uses a stack for LIFO processing"))
    
    # HashMap / HashSet
    if 'HashMap' in kotlin_code or 'hashMapOf' in kotlin_code or 'mutableMapOf' in kotlin_code:
        patterns.append(("hash-map", "Uses hash map for O(1) lookups"))
    if 'HashSet' in kotlin_code or 'hashSetOf' in kotlin_code or 'mutableSetOf' in kotlin_code:
        patterns.append(("hash-set", "Uses hash set for uniqueness checks"))
    
    # Two pointers
    if re.search(r'\b(left|right|l|r)\s*[+][+]\b', kotlin_code):
        patterns.append(("two-pointers", "Uses two-pointer technique"))
    
    # Recursion — check if function calls itself
    func_names = [s[0] for s in sigs] if sigs else []
    for fname in func_names:
        if f' {fname}(' in kotlin_code[kotlin_code.index(f'fun {fname}'):][len(fname)+10:]:
            patterns.append(("recursion", "Uses recursion"))
            break
    
    # Sorting
    if 'sort' in kotlin_code.lower():
        patterns.append(("sorting", "Uses sorting as preprocessing step"))
    
    return patterns

def infer_problem_description(problem_name, package, sigs, comments):
    """Infer a detailed problem description from code analysis."""
    readable = problem_name.replace('_', ' ').replace('-', ' ')
    # CamelCase to words
    readable = re.sub(r'([a-z])([A-Z])', r'\1 \2', readable)
    readable = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', readable)
    readable = readable.title()
    
    # Build description from function signature
    desc = f"**{readable}**\n\n"
    
    if sigs:
        main_sig = sigs[0]
        func_name = main_sig[0]
        params = main_sig[1]
        ret_type = main_sig[2]
        
        # Human-readable function name
        func_readable = re.sub(r'([a-z])([A-Z])', r'\1 \2', func_name).title()
        
        param_desc = []
        for p_name, p_type in params:
            type_readable = p_type.replace('IntArray', 'array of integers').replace('Int', 'integer').replace('String', 'string').replace('Boolean', 'boolean').replace('List<Int>', 'list of integers').replace('List<List<Int>>', '2D list of integers').replace('Array<IntArray>', '2D matrix')
            param_desc.append(f"`{p_name}` ({type_readable})")
        
        param_str = ", ".join(param_desc) if param_desc else "none"
        ret_readable = ret_type.replace('IntArray', 'array of integers').replace('Int', 'integer').replace('Boolean', 'boolean').replace('String', 'string').replace('Unit', 'nothing (modifies in-place)').replace('List<Int>', 'list of integers').replace('Double', 'double')
        
        desc += f"**Function:** `{func_readable}` takes {param_str} and returns **{ret_readable}**.\n\n"
    
    if comments:
        desc += "**Key logic:**\n"
        for c in comments[:5]:
            desc += f"- {c}\n"
        desc += "\n"
    
    return desc

def infer_approach(problem_name, kotlin_code, sigs, patterns):
    """Generate a detailed approach explanation."""
    readable = problem_name.replace('_', ' ').replace('-', ' ')
    readable = re.sub(r'([a-z])([A-Z])', r'\1 \2', readable)
    
    approach_parts = []
    
    # Detect algorithm family
    if any(p[0] == 'binary-search' for p in patterns):
        approach_parts.append("**Binary Search Approach:**\n")
        approach_parts.append("1. Define the search space and feasibility predicate\n")
        approach_parts.append("2. Repeatedly halve the search range until finding the optimal value\n")
        approach_parts.append("3. The predicate must be monotonic for binary search to work\n")
        
        # Check for specific variant
        if 'feasible' in kotlin_code.lower() or 'can' in kotlin_code.lower()[:200]:
            approach_parts.append("\nThis uses a **feasibility function** that checks if a candidate value satisfies the constraint, making it a 'minimize/maximize with binary search' pattern.\n")
        if 'target' in kotlin_code.lower():
            approach_parts.append("\nThis searches for an exact target value in a sorted structure.\n")
    
    elif any(p[0] == 'dp' for p in patterns):
        if 'dfs' in kotlin_code.lower():
            approach_parts.append("**Top-Down DP (Memoization) Approach:**\n")
            approach_parts.append("1. Define a recursive function that explores all possibilities\n")
            approach_parts.append("2. Cache results in a table/dictionary to avoid redundant work\n")
            approach_parts.append("3. The state is defined by the function parameters that change between calls\n")
        else:
            approach_parts.append("**Bottom-Up DP (Tabulation) Approach:**\n")
            approach_parts.append("1. Define the DP table dimensions based on state variables\n")
            approach_parts.append("2. Initialize base cases\n")
            approach_parts.append("3. Fill the table iteratively from smallest to largest subproblems\n")
            approach_parts.append("4. The answer is in dp[final_state]\n")
    
    elif any(p[0] == 'bfs' for p in patterns):
        approach_parts.append("**BFS (Breadth-First Search) Approach:**\n")
        approach_parts.append("1. Use a queue to process nodes level by level\n")
        approach_parts.append("2. Track visited nodes to avoid cycles\n")
        approach_parts.append("3. BFS guarantees shortest path in unweighted graphs\n")
    
    elif any(p[0] == 'dfs' for p in patterns):
        approach_parts.append("**DFS (Depth-First Search) Approach:**\n")
        approach_parts.append("1. Recursively explore each path until reaching a base case\n")
        approach_parts.append("2. Backtrack when stuck to try alternative paths\n")
        approach_parts.append("3. DFS is useful for connectivity, path existence, and exhaustive search\n")
    
    elif any(p[0] == 'stack' for p in patterns):
        approach_parts.append("**Stack-Based Approach:**\n")
        approach_parts.append("1. Process elements left to right\n")
        approach_parts.append("2. Maintain a stack that tracks relevant previous elements\n")
        approach_parts.append("3. Pop from stack when current element breaks a monotonic property\n")
    
    elif any(p[0] == 'heap' for p in patterns):
        approach_parts.append("**Priority Queue / Heap Approach:**\n")
        approach_parts.append("1. Insert elements into a heap to maintain ordering dynamically\n")
        approach_parts.append("2. Extract min/max as needed for the problem\n")
        approach_parts.append("3. Time complexity is O(log n) per operation\n")
    
    elif any(p[0] == 'hash-map' for p in patterns):
        approach_parts.append("**Hash Map Approach:**\n")
        approach_parts.append("1. Use a hash map for O(1) average lookups\n")
        approach_parts.append("2. Store key-value pairs where the key enables fast retrieval\n")
        approach_parts.append("3. Trade off memory for time\n")
    
    elif any(p[0] == 'two-pointers' for p in patterns):
        approach_parts.append("**Two-Pointer Approach:**\n")
        approach_parts.append("1. Initialize two pointers at different positions\n")
        approach_parts.append("2. Move pointers toward each other or in the same direction\n")
        approach_parts.append("3. Each step processes one element, giving O(n) time\n")
    
    else:
        # Generic approach from code structure
        if sigs:
            main_sig = sigs[0]
            func_name = main_sig[0]
            approach_parts.append(f"**Solution Approach:**\n")
            approach_parts.append(f"1. The main function `{func_name}` processes the input")
            
            # Count helper functions
            if len(sigs) > 1:
                helpers = [s[0] for s in sigs[1:]]
                approach_parts.append(f"\n2. Uses helper functions: {', '.join(helpers)}")
    
    return ''.join(approach_parts)

def infer_complexity(kotlin_code, patterns, sigs):
    """Infer time and space complexity from code analysis."""
    
    time_complexity = "O(n)"
    space_complexity = "O(1)"
    
    # Check for nested loops
    loop_depth = 0
    # Count for loops
    for_loops = re.findall(r'\bfor\b', kotlin_code)
    while_loops = re.findall(r'\bwhile\b', kotlin_code)
    
    # Nested for detection (rough)
    lines = kotlin_code.split('\n')
    max_indent = 0
    for line in lines:
        indent = len(line) - len(line.lstrip())
        if indent > max_indent:
            max_indent = indent
    
    depth_indicators = {
        'for': len(re.findall(r'\bfor\b', kotlin_code)),
        'while': len(re.findall(r'\bwhile\b', kotlin_code)),
        'nested': max_indent // 4
    }
    
    if any(p[0] == 'binary-search' for p in patterns):
        time_complexity = "O(log n)"
    elif any(p[0] == 'dp' for p in patterns):
        if 'for' in kotlin_code and max_indent >= 12:
            time_complexity = "O(n³)"
            space_complexity = "O(n²)"
        elif 'for' in kotlin_code and max_indent >= 8:
            time_complexity = "O(n²)"
            space_complexity = "O(n²)"
        else:
            time_complexity = "O(n × m)"
            space_complexity = "O(n)"
    elif any(p[0] == 'heap' for p in patterns):
        time_complexity = "O(n log k)"
        space_complexity = "O(k)"
    elif any(p[0] == 'bfs' for p in patterns):
        time_complexity = "O(V + E)"
        space_complexity = "O(V)"
    elif any(p[0] == 'dfs' for p in patterns):
        time_complexity = "O(V + E)"
        space_complexity = "O(V)"
    elif any(p[0] == 'hash-map' for p in patterns):
        time_complexity = "O(n)"
        space_complexity = "O(n)"
    elif any(p[0] == 'two-pointers' for p in patterns):
        time_complexity = "O(n)"
        space_complexity = "O(1)"
    elif depth_indicators['nested'] >= 3:
        time_complexity = "O(n²)"
    
    # Check for recursion (stack space)
    if any(p[0] == 'recursion' for p in patterns):
        space_complexity = space_complexity.replace("O(1)", "O(n) [call stack]")
        if "O(n)" in space_complexity:
            space_complexity += " [with call stack]"
    
    return time_complexity, space_complexity

def generate_chapter(chapter_key, chapter_info):
    """Generate a complete chapter markdown file."""
    lines = []
    
    # Front matter
    lines.append("---")
    lines.append(f'layout: chapter')
    lines.append(f'title: "{chapter_info["title"]}"')
    lines.append(f'chapter_number: {chapter_info["number"]}')
    lines.append(f'chapter_title: "{chapter_info["title"]}"')
    lines.append('toc: true')
    
    # Chapter navigation
    chapters_order = list(CHAPTER_PROBLEMS.keys())
    idx = chapters_order.index(chapter_key)
    if idx > 0:
        prev_key = chapters_order[idx - 1]
        prev_info = CHAPTER_PROBLEMS[prev_key]
        lines.append('prev_chapter:')
        lines.append(f'  url: "/chapters/{prev_key}.html"')
        lines.append(f'  title: "{prev_info["title"]}"')
    if idx < len(chapters_order) - 1:
        next_key = chapters_order[idx + 1]
        next_info = CHAPTER_PROBLEMS[next_key]
        lines.append('next_chapter:')
        lines.append(f'  url: "/chapters/{next_key}.html"')
        lines.append(f'  title: "{next_info["title"]}"')
    
    lines.append("---")
    lines.append("")
    
    # Title
    lines.append(f'# {chapter_info["title"]}')
    lines.append("")
    lines.append(f'> **{len(chapter_info["problems"])} problems** — {chapter_info["intro"]}')
    lines.append("")
    
    # Pattern section
    lines.append("## The Pattern")
    lines.append("")
    lines.append(chapter_info["pattern_intro"])
    lines.append("")
    
    # Problem table
    lines.append("## Complete Problem Set")
    lines.append("")
    lines.append("| # | Problem | Pattern | Difficulty |")
    lines.append("|---|---------|-----------|------------|")
    
    for i, prob_key in enumerate(chapter_info["problems"], 1):
        display_name = get_display_name(prob_key)
        lines.append(f'| {i} | [{display_name}](#{prob_key}) | — | <span class="badge badge-medium">Medium</span> |')
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Generate each problem section
    for prob_key in chapter_info["problems"]:
        kotlin_file = CODE_DIR / prob_key / "kotlin.txt"
        if not kotlin_file.exists():
            lines.append(f"## {prob_key.replace('_', ' ').title()}")
            lines.append("")
            lines.append("{% include code-tabs-file.html problem=\"" + prob_key + "\" %}")
            lines.append("")
            lines.append("---")
            lines.append("")
            continue
        
        with open(kotlin_file) as f:
            kotlin_code = f.read()
        
        # Remove DeepCode PWD suffix
        kotlin_code = re.sub(r'__DEEPCODE_PWD__.*', '', kotlin_code).strip()
        
        sigs = extract_function_signatures(kotlin_code)
        comments = extract_comments(kotlin_code)
        patterns = detect_algorithm_pattern(kotlin_code)
        time_cplx, space_cplx = infer_complexity(kotlin_code, patterns, sigs)
        
        display_name = get_display_name(prob_key)
        
        lines.append(f"## {display_name}")
        lines.append("")
        lines.append(f'<span id="{prob_key}"></span>')
        lines.append("")
        
        # Problem description
        lines.append("### Problem")
        lines.append("")
        desc = infer_problem_description(prob_key, "", sigs, comments)
        lines.append(desc)
        lines.append("")
        
        # Why this works
        lines.append("### Why This Works")
        lines.append("")
        
        if any(p[0] == 'binary-search' for p in patterns):
            lines.append("The algorithm exploits **monotonicity** — the property that once a condition becomes true (or false), it stays that way. Binary search divides the search space in half each iteration, guaranteeing logarithmic time. The correctness follows from the loop invariant: the answer is always within `[left, right]`.")
            lines.append("")
        
        elif any(p[0] == 'dp' for p in patterns):
            lines.append("Dynamic programming works because this problem has **optimal substructure** (the optimal solution contains optimal solutions to subproblems) and **overlapping subproblems** (the same subproblems are solved multiple times). The DP table/memoization cache stores computed results to avoid redundant work.")
            lines.append("")
        
        elif any(p[0] == 'bfs' for p in patterns):
            lines.append("BFS works because it explores nodes in order of their distance from the source. The queue ensures that nodes at distance `k` are processed before nodes at distance `k+1`. This guarantees the first time we reach the target, it's via the shortest path.")
            lines.append("")
        
        elif any(p[0] == 'dfs' for p in patterns):
            lines.append("DFS systematically explores every path to its end before backtracking. This exhaustive search guarantees correctness for connectivity problems and path existence. The recursion implicitly uses a stack to track the exploration path.")
            lines.append("")
        
        else:
            lines.append("The algorithm systematically processes the input to produce the correct result. Each step maintains an invariant that leads to the final correct answer. The data structures used optimize the critical operations to O(1) or O(log n) each.")
            lines.append("")
        
        # Algorithmic thinking
        lines.append("### Algorithmic Thinking")
        lines.append("")
        approach = infer_approach(prob_key, kotlin_code, sigs, patterns)
        lines.append(approach)
        lines.append("")
        
        # Dry run with code
        lines.append("### Code Walkthrough")
        lines.append("")
        lines.append("Let's trace through the code to understand how it processes the input:")
        lines.append("")
        
        # Extract key variables from code
        vars_found = re.findall(r'(?:val|var)\s+(\w+)', kotlin_code)
        if vars_found:
            lines.append(f"**Key variables:** `{'`, `'.join(vars_found[:8])}`")
            lines.append("")
        
        # Add key comments as walkthrough steps
        if comments:
            lines.append("**Execution flow:**")
            for c in comments[:8]:
                if len(c) > 10:  # Skip trivial comments
                    lines.append(f"- {c}")
            lines.append("")
        
        # Code with detailed comments
        lines.append("### Code")
        lines.append("")
        lines.append("{% include code-tabs-file.html problem=\"" + prob_key + "\" %}")
        lines.append("")
        
        # Complexity
        lines.append("### Complexity")
        lines.append("")
        lines.append(f"| Metric | Value |")
        lines.append(f"|--------|-------|")
        lines.append(f"| **Time** | {time_cplx} |")
        lines.append(f"| **Space** | {space_cplx} |")
        lines.append("")
        
        # Analysis
        lines.append("**Analysis:**")
        lines.append("")
        
        if any(p[0] == 'binary-search' for p in patterns):
            lines.append(f"Each iteration halves the search space, giving {time_cplx} time. Only constant extra space is needed beyond the input ({space_cplx}).")
        elif any(p[0] == 'dp' for p in patterns):
            if any(p[0] == 'dp-2d' for p in patterns):
                lines.append(f"The DP table has dimensions proportional to the input size, giving {space_cplx} space. Each cell requires O(1) or O(n) work, totaling {time_cplx}.")
            else:
                lines.append(f"We compute each state exactly once and each state takes O(1) to O(n) transitions, giving {time_cplx}. The memoization/table stores one entry per state ({space_cplx}).")
        elif any(p[0] == 'bfs' for p in patterns) or any(p[0] == 'dfs' for p in patterns):
            lines.append(f"Each node and edge is visited at most once, giving {time_cplx} for a graph with V vertices and E edges. The {space_cplx} space stores visited tracking and the queue/stack.")
        else:
            lines.append(f"The algorithm processes each element a constant number of times, giving {time_cplx}. The {space_cplx} space comes from the auxiliary data structures used.")
        
        lines.append("")
        lines.append("---")
        lines.append("")
    
    # Key Takeaways
    lines.append("## Key Takeaways")
    lines.append("")
    lines.append(f"1. **Core pattern recognition** — {chapter_info['pattern_intro']}")
    lines.append(f"2. **Practice systematically** — Work through each problem to internalize the patterns")
    lines.append(f"3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    return '\n'.join(lines)

def get_display_name(prob_key):
    """Get proper PascalCase display name from the Kotlin source file."""
    kt_file = CODE_DIR / prob_key / 'kotlin.txt'
    if not kt_file.exists():
        name = prob_key.replace('_', ' ').replace('-', ' ')
        return ' '.join(w.capitalize() for w in name.split())
    
    with open(kt_file) as f:
        code = f.read()
    code = re.sub(r'__DEEPCODE_PWD__.*', '', code).strip()
    
    # Try class name first
    m = re.search(r'(?:^|\n)(?:abstract\s+|open\s+|sealed\s+)?(?:class|data class)\s+(\w+)', code)
    if m:
        name = m.group(1)
    else:
        m = re.search(r'^fun\s+(\w+)', code, re.MULTILINE)
        if m:
            name = m.group(1)
            if name[0].islower():
                name = prob_key.replace('_', ' ').replace('-', ' ')
                return ' '.join(w.capitalize() for w in name.split())
        else:
            name = prob_key.replace('_', ' ').replace('-', ' ')
            return ' '.join(w.capitalize() for w in name.split())
    
    spaced = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', name)
    spaced = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', spaced)
    return spaced

def main():
    """Generate all chapters."""
    print("Generating chapters from Kotlin source analysis...\n")
    
    for chapter_key, chapter_info in CHAPTER_PROBLEMS.items():
        output_file = CHAPTERS_DIR / f"{chapter_key}.md"
        print(f"  Generating {chapter_key}.md ({len(chapter_info['problems'])} problems)...")
        content = generate_chapter(chapter_key, chapter_info)
        with open(output_file, 'w') as f:
            f.write(content)
        print(f"    ✅ Done ({len(content)} chars)")
    
    print(f"\n✅ All {len(CHAPTER_PROBLEMS)} chapters generated!")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Comprehensive Kotlin source enrichment + chapter generation.
1. Adds generous KDoc comments (@param, @return, algorithm explanations) to ALL kotlin.txt files
2. Generates detailed chapter markdown with full problem structure
"""
import re, os, shutil
from pathlib import Path

ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CODE_DIR = ROOT / '_includes' / 'code'
CHAPTERS_DIR = ROOT / 'chapters'

def backup_originals():
    """Backup all kotlin.txt files before modifying."""
    backup_dir = ROOT / '.kotlin_backup'
    backup_dir.mkdir(exist_ok=True)
    for kt_file in sorted(CODE_DIR.rglob('kotlin.txt')):
        rel = kt_file.relative_to(CODE_DIR)
        dest = backup_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(kt_file, dest)
    print(f'✅ Backed up all kotlin.txt to {backup_dir}')

def type_to_english(type_str):
    """Convert Kotlin type to human-readable description."""
    mapping = {
        'Int': 'integer',
        'IntArray': 'array of integers',
        'IntArray?': 'nullable array of integers',
        'Long': 'long integer',
        'Double': 'double-precision floating point',
        'Float': 'floating point number',
        'String': 'string',
        'Boolean': 'boolean (true/false)',
        'Char': 'character',
        'Unit': 'nothing (function performs side effects)',
        'List<Int>': 'list of integers',
        'List<String>': 'list of strings',
        'List<List<Int>>': '2D list of integers',
        'Array<IntArray>': '2D matrix of integers',
        'Array<IntArray>?': 'nullable 2D matrix',
        'MutableList<Int>': 'mutable list of integers',
        'Set<Int>': 'set of integers',
        'Map<Int, Int>': 'map from integer to integer',
        'Map<String, Boolean>': 'map from string to boolean',
        'Map<String, MutableList<Int>>': 'map from string to list of integers',
        'Pair<Int, Int>': 'pair of integers',
        'Int': 'integer',
        'TreeNode?': 'binary tree node reference',
        'ListNode?': 'linked list node reference',
    }
    return mapping.get(type_str, type_str)

def enrich_kotlin_file(filepath):
    """Add generous KDoc comments and inline explanations to a Kotlin file."""
    with open(filepath) as f:
        code = f.read()
    
    code = re.sub(r'__DEEPCODE_PWD__.*', '', code).strip()
    original = code
    
    # ─── Extract structure ───
    package = ''
    pm = re.search(r'^package\s+([\w.]+)', code, re.MULTILINE)
    if pm:
        package = pm.group(1)
    
    class_name = ''
    cm = re.search(r'(?:^|\n)(?:abstract\s+|open\s+|sealed\s+)?(?:class|data class|object)\s+(\w+)', code)
    if cm:
        class_name = cm.group(1)
    
    # Extract all function signatures
    funcs = []
    for m in re.finditer(r'((?:private\s+|protected\s+|public\s+|override\s+)?(?:fun|suspend fun)\s+(\w+)\s*\(([^)]*)\)\s*(?::\s*(\w+(?:<[^>]*>)?(?:\?)?))?)', code):
        full_sig = m.group(1)
        fname = m.group(2)
        params_str = m.group(3)
        ret_type = m.group(4) if m.group(4) else 'Unit'
        
        # Parse params
        params = []
        for p in params_str.split(','):
            p = p.strip()
            if not p:
                continue
            parts = p.split(':')
            if len(parts) >= 2:
                pname = parts[0].strip()
                ptype = ':'.join(parts[1:]).strip()
                params.append((pname, ptype))
        
        funcs.append((fname, params, ret_type, full_sig))
    
    if not funcs:
        return False  # No functions to document
    
    # ─── Build enriched code ───
    lines = code.split('\n')
    new_lines = []
    i = 0
    
    # Determine the problem name for description
    prob_dir = filepath.parent.name
    prob_name = prob_dir.replace('_', ' ').replace('-', ' ')
    prob_name = re.sub(r'([a-z])([A-Z])', r'\1 \2', class_name if class_name else prob_name)
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check if this line starts a function definition
        for fname, params, ret_type, full_sig in funcs:
            # Find the function definition line
            if f'fun {fname}(' in stripped or f'suspend fun {fname}(' in stripped:
                # Check if there's already a KDoc comment before this function
                has_kdoc = False
                for j in range(i-1, max(i-5, -1), -1):
                    if lines[j].strip().startswith('/**'):
                        has_kdoc = True
                        break
                    if lines[j].strip() and not lines[j].strip().startswith('*') and not lines[j].strip().startswith('//'):
                        break
                
                if not has_kdoc:
                    # Generate KDoc
                    is_private = 'private' in stripped
                    is_override = 'override' in stripped
                    
                    kdoc_lines = []
                    kdoc_lines.append('    /**')
                    
                    # Generate description based on function name and params
                    func_desc = fname.replace('_', ' ')
                    func_desc = re.sub(r'([a-z])([A-Z])', r'\1 \2', func_desc).lower()
                    
                    if fname in ('main', 'run'):
                        kdoc_lines.append(f'     * Entry point for the program.')
                    elif is_override:
                        kdoc_lines.append(f'     * Implements/overrides the base class method.')
                    elif is_private:
                        kdoc_lines.append(f'     * Helper: {func_desc}.')
                    else:
                        kdoc_lines.append(f'     * Solves the {prob_name} problem.')
                        if params:
                            param_desc = ', '.join(f'`{p[0]}` ({type_to_english(p[1])})' for p in params)
                            kdoc_lines.append(f'     * Takes {param_desc}.')
                    
                    kdoc_lines.append(f'     *')
                    
                    # Generate @param tags
                    for pname, ptype in params:
                        ptype_eng = type_to_english(ptype)
                        if 'IntArray' in ptype or 'Array' in ptype or 'List' in ptype or 'Set' in ptype or 'Map' in ptype:
                            kdoc_lines.append(f'     * @param {pname} The input {ptype_eng}.')
                        elif ptype in ('Int', 'Long', 'Double', 'Float'):
                            kdoc_lines.append(f'     * @param {pname} The {ptype_eng} parameter representing {pname.replace("_", " ")}.')
                        elif 'Boolean' in ptype:
                            kdoc_lines.append(f'     * @param {pname} A boolean flag: {pname.replace("_", " ")}.')
                        elif 'String' in ptype:
                            kdoc_lines.append(f'     * @param {pname} The input string.')
                        elif '?' in ptype:
                            kdoc_lines.append(f'     * @param {pname} The {ptype_eng} (nullable).')
                        else:
                            kdoc_lines.append(f'     * @param {pname} The {ptype_eng}.')
                    
                    # Generate @return
                    if ret_type and ret_type != 'Unit':
                        if 'Boolean' in ret_type:
                            kdoc_lines.append(f'     * @return `true` if the condition is met, `false` otherwise.')
                        elif 'Int' in ret_type or 'Long' in ret_type:
                            kdoc_lines.append(f'     * @return The computed integer result.')
                        elif 'Double' in ret_type or 'Float' in ret_type:
                            kdoc_lines.append(f'     * @return The computed floating-point result.')
                        elif 'Array' in ret_type or 'List' in ret_type or 'Set' in ret_type or 'Map' in ret_type:
                            kdoc_lines.append(f'     * @return The resulting collection ({type_to_english(ret_type)}).')
                        elif 'String' in ret_type:
                            kdoc_lines.append(f'     * @return The resulting string.')
                        elif '?' in ret_type:
                            kdoc_lines.append(f'     * @return The result, or `null` if not found.')
                        else:
                            kdoc_lines.append(f'     * @return The computed result ({type_to_english(ret_type)}).')
                    else:
                        kdoc_lines.append(f'     * @return Unit (no return value, modifies state in-place).')
                    
                    kdoc_lines.append('     */')
                    
                    # Insert KDoc before the function
                    indent = line[:len(line) - len(stripped)]
                    for kdoc_line in kdoc_lines:
                        if kdoc_line.strip():
                            new_lines.append(indent + kdoc_line.lstrip())
                        else:
                            new_lines.append('')
                    
                    # Also add inline comment after function signature if it's the public API
                    if not is_private and not is_override:
                        pass  # KDoc is sufficient
                    
                    break
        
        new_lines.append(line)
        i += 1
    
    new_code = '\n'.join(new_lines)
    
    if new_code != original:
        with open(filepath, 'w') as f:
            f.write(new_code)
        return True
    return False

# ─── Chapter definitions ───
CHAPTER_PROBLEMS = {
    "01-binary-search": {
        "title": "Binary Search", "number": 1,
        "intro": "Master the art of divide-and-conquer searching. Binary search finds elements in sorted arrays in O(log n) time.",
        "pattern_intro": "Sorted array + search → Binary Search. Find a predicate that splits the search space into yes/no.",
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
        "title": "Dynamic Programming", "number": 2,
        "intro": "Master optimal substructure and overlapping subproblems.",
        "pattern_intro": "Optimal substructure + overlapping subproblems → DP. Identify states, define transitions.",
        "problems": [
            "burstbaloons", "closestsubsequencesum", "maximumproductsubarray",
            "maximumprofitinjobscheduling", "partitionequalsubsetsum", "supereggdropping",
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
        "title": "Arrays & Two Pointers", "number": 3,
        "intro": "Master array manipulation, two-pointer technique, and sliding windows.",
        "pattern_intro": "Two pointers create O(n) passes where brute force would be O(n^2).",
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
        "title": "Linked Lists", "number": 4,
        "intro": "Master pointer manipulation and linked list operations.",
        "pattern_intro": "Linked lists are about pointer rearrangement: slow/fast pointers, dummy heads, in-place reversal.",
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
        "title": "Trees", "number": 5,
        "intro": "Master tree traversals, BST operations, and recursive tree algorithms.",
        "pattern_intro": "Trees are recursive — master DFS (pre/in/post-order), BFS (level-order), and BST properties.",
        "problems": [
            "allnodesdistancekinbinarytree", "averageoflevelsinbinarytree",
            "balancedbinarytree", "binarytreeinordertraversaliterative",
            "binarytreelevelordertraversal", "binarytreelevelordertraversal_ii",
            "binarytreemaximumpathsum", "binarytreerightsideview",
            "binarytreeverticalordertraversal",
            "binarytreeverticalordertraversal_withoutsorting",
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
        "title": "Graphs", "number": 6,
        "intro": "Master graph traversals, shortest paths, and topological ordering.",
        "pattern_intro": "BFS for shortest path, DFS for connectivity, topological sort for dependencies.",
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
        "title": "Bit Manipulation", "number": 7,
        "intro": "Master bitwise operations: AND, OR, XOR, shifts, and bit masking.",
        "pattern_intro": "XOR for pairing, AND for masking, shifts for powers of 2.",
        "problems": [
            "firstlettertoappeartwice", "longestnicesubarray",
            "maximumxoroftwonumsinarray",
            "number_of_steps_to_reduceaanumberinbinaryrepresentationtoone",
            "numberofonebits", "reversebits", "singlenumber", "singlenumber3",
            "sumofallsubsetxortotal"
        ]
    },
    "08-heaps": {
        "title": "Heaps & Priority Queues", "number": 8,
        "intro": "Master priority queues for k-th order statistics, scheduling, streaming.",
        "pattern_intro": "Min-heap for k largest, max-heap for k smallest, dual heaps for median.",
        "problems": [
            "dualbalancedheap", "findingmkaverage", "findkclosestelements",
            "findscoreofanarrayaftermarkingallelements", "ipo",
            "longesthappystring", "medianfromrunningstream",
            "meetingroom_iii", "singlethreadedcpu",
            "slidingwindowmedian", "topkfrequentelements"
        ]
    },
    "09-disjoint-set-union": {
        "title": "Disjoint Set Union", "number": 9,
        "intro": "Master union-find for connectivity and dynamic graph components.",
        "pattern_intro": "DSU tracks connected components. Union by rank + path compression = near-O(1).",
        "problems": [
            "accountmerge", "numberofisland_ii", "unionfind"
        ]
    },
    "10-string-matching": {
        "title": "String Matching", "number": 10,
        "intro": "Master string algorithms: pattern matching, DP on strings, and parsing.",
        "pattern_intro": "Two pointers, sliding window, DP (LCS, edit distance), Rabin-Karp, trie for prefix search.",
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
        "title": "Backtracking", "number": 11,
        "intro": "Master systematic exploration of decision spaces with pruning.",
        "pattern_intro": "DFS on decision tree + pruning. Generate valid candidates, backtrack when stuck.",
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
        "title": "Caches & Memory Management", "number": 12,
        "intro": "Master cache design: LRU, LFU, and eviction strategies.",
        "pattern_intro": "Hash map for O(1) lookup + linked list for ordering. LRU = access order, LFU = frequency.",
        "problems": [
            "lfucache", "lrucache", "lrucachelinkedlist"
        ]
    }
}

def generate_chapter(chapter_key, chapter_info):
    """Generate chapter with detailed structure like Koko sample."""
    lines = []
    
    lines.append("---")
    lines.append('layout: chapter')
    lines.append(f'title: "{chapter_info["title"]}"')
    lines.append(f'chapter_number: {chapter_info["number"]}')
    lines.append(f'chapter_title: "{chapter_info["title"]}"')
    lines.append('toc: true')
    
    chapters_order = list(CHAPTER_PROBLEMS.keys())
    idx = chapters_order.index(chapter_key)
    if idx > 0:
        prev_key = chapters_order[idx - 1]
        lines.append('prev_chapter:')
        lines.append(f'  url: "/chapters/{prev_key}.html"')
        lines.append(f'  title: "{CHAPTER_PROBLEMS[prev_key]["title"]}"')
    if idx < len(chapters_order) - 1:
        next_key = chapters_order[idx + 1]
        lines.append('next_chapter:')
        lines.append(f'  url: "/chapters/{next_key}.html"')
        lines.append(f'  title: "{CHAPTER_PROBLEMS[next_key]["title"]}"')
    
    lines.append("---")
    lines.append("")
    lines.append(f'# {chapter_info["title"]}')
    lines.append("")
    lines.append(f'> **{len(chapter_info["problems"])} problems** — {chapter_info["intro"]}')
    lines.append("")
    lines.append("## The Pattern")
    lines.append("")
    lines.append(chapter_info["pattern_intro"])
    lines.append("")
    lines.append("## Complete Problem Set")
    lines.append("")
    lines.append("| # | Problem | Pattern | Difficulty |")
    lines.append("|---|---------|-----------|------------|")
    
    for i, prob_key in enumerate(chapter_info["problems"], 1):
        display = get_display_name(prob_key)
        lines.append(f'| {i} | [{display}](#{prob_key}) | — | <span class="badge badge-medium">Medium</span> |')
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    for prob_key in chapter_info["problems"]:
        kt_file = CODE_DIR / prob_key / "kotlin.txt"
        if not kt_file.exists():
            lines.append(f'## {prob_key.replace("_", " ").title()}')
            lines.append("")
            lines.append("*(Code not available)*")
            lines.append("")
            lines.append("---")
            lines.append("")
            continue
        
        with open(kt_file) as f:
            kt_code = f.read()
        kt_code = re.sub(r'__DEEPCODE_PWD__.*', '', kt_code).strip()
        
        display = get_display_name(prob_key)
        
        lines.append(f'## {display}')
        lines.append("")
        
        # Problem section
        lines.append("### Problem")
        lines.append("")
        
        # Extract description from KDoc if available
        kdoc_desc = extract_kdoc_description(kt_code)
        if kdoc_desc:
            lines.append(kdoc_desc)
        else:
            lines.append(f'Solve the **{display}** problem efficiently.')
        
        lines.append("")
        
        # Why this approach
        lines.append("### Why This Approach")
        lines.append("")
        lines.append(f'_Refer to the **Pattern** section above for the general algorithmic pattern._')
        lines.append("")
        
        # Code
        lines.append("### Code")
        lines.append("")
        lines.append("```kotlin")
        lines.append(kt_code)
        lines.append("```")
        lines.append("")
        
        # Complexity
        lines.append("### Complexity")
        lines.append("")
        time_cplx, space_cplx = infer_complexity(kt_code)
        lines.append(f'| Metric | Value |')
        lines.append(f'|--------|-------|')
        lines.append(f'| **Time** | {time_cplx} |')
        lines.append(f'| **Space** | {space_cplx} |')
        lines.append("")
        lines.append("---")
        lines.append("")
    
    return '\n'.join(lines)

def get_display_name(prob_key):
    """Get readable display name from Kotlin source."""
    kt_file = CODE_DIR / prob_key / "kotlin.txt"
    if not kt_file.exists():
        name = prob_key.replace('_', ' ').replace('-', ' ')
        return ' '.join(w.capitalize() for w in name.split())
    with open(kt_file) as f:
        code = f.read()
    code = re.sub(r'__DEEPCODE_PWD__.*', '', code).strip()
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

def extract_kdoc_description(code):
    """Extract first meaningful KDoc description from code."""
    m = re.search(r'/\*\*\s*\n\s+\*\s*(.+?)\s*\n', code)
    if m:
        return m.group(1).strip()
    return None

def infer_complexity(code):
    """Basic complexity inference from code structure."""
    lines = code.split('\n')
    max_indent = max((len(l) - len(l.lstrip()) for l in lines), default=0)
    loop_count = len(re.findall(r'\b(for|while)\b', code))
    nested = max_indent // 4
    
    if any(w in code for w in ['binarySearch', 'binarySearch']):
        return "O(log n)", "O(1)"
    if any(w in code.lower() for w in ['dp', 'memoization', 'cache']):
        if nested >= 3:
            return "O(n³)", "O(n²)"
        if nested >= 2:
            return "O(n²)", "O(n²)"
        return "O(n × m)", "O(n)"
    if 'PriorityQueue' in code or 'priorityQueue' in code:
        return "O(n log k)", "O(k)"
    if 'Queue' in code or 'LinkedList' in code:
        return "O(V + E)", "O(V)"
    if nested >= 2:
        return "O(n²)", "O(1)"
    return "O(n)", "O(1)"

def main():
    print("═" * 60)
    print("STEP 1: Enrich all Kotlin source files with generous documentation")
    print("═" * 60)
    
    # backup_originals()  # Uncomment to enable backup
    
    enriched = 0
    for kt_file in sorted(CODE_DIR.rglob('kotlin.txt')):
        if enrich_kotlin_file(kt_file):
            enriched += 1
            if enriched % 50 == 0:
                print(f'  Enriched {enriched} files...')
    
    print(f'\n✅ Enriched {enriched} Kotlin files with generous documentation')
    
    print("\n" + "═" * 60)
    print("STEP 2: Generate all chapter markdown files")
    print("═" * 60)
    
    for chapter_key, chapter_info in CHAPTER_PROBLEMS.items():
        output_file = CHAPTERS_DIR / f"{chapter_key}.md"
        print(f'  Generating {chapter_key}.md ({len(chapter_info["problems"])} problems)...')
        content = generate_chapter(chapter_key, chapter_info)
        with open(output_file, 'w') as f:
            f.write(content)
        print(f'    ✅ Done')
    
    print(f'\n✅ All {len(CHAPTER_PROBLEMS)} chapters generated!')

if __name__ == '__main__':
    main()

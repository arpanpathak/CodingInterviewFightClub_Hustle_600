#!/usr/bin/env python3
"""
Upgrade all auto-generated chapters to Koko-level format:
- Detailed problem statements from enriched KDoc
- Pattern insights per algorithm type
- Variations & follow-ups
- Consistent structure across all 465 problems
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = ROOT / 'chapters'
CODE_DIR = ROOT / '_includes' / 'code'

def get_kdoc_description(prob_key):
    """Extract the first KDoc line as problem description."""
    kt_file = CODE_DIR / prob_key / 'kotlin.txt'
    if not kt_file.exists():
        return None
    with open(kt_file) as f:
        code = f.read()
    code = re.sub(r'__DEEPCODE_PWD__.*', '', code).strip()
    m = re.search(r'/\*\*\s*\n\s+\*\s*(.+?)\s*\n', code)
    return m.group(1).strip() if m else None

def get_variations(prob_key):
    """Return variations for common problem patterns."""
    kt_file = CODE_DIR / prob_key / 'kotlin.txt'
    if not kt_file.exists():
        return []
    
    with open(kt_file) as f:
        code = f.read()
    
    # Detect algorithm type and return relevant variations
    if any(w in code for w in ['binarySearch', 'binarySearch', 'while.*<.*right', 'while.*<.*end']):
        return [
            "What if the array is not sorted? Can you sort first?",
            "What if there are duplicates? How does that affect the search?",
            "What if the search space is a range of values rather than array indices?",
            "What if you need to find the FIRST vs LAST occurrence?",
            "What if the input is too large to fit in memory (external search)?"
        ]
    if any(w in code for w in ['dp', 'memo', 'cache']):
        return [
            "Can you optimize space by using only the previous row?",
            "What if the input size is too large for 2D DP? Can you reduce dimensions?",
            "Can this be solved greedily instead? When does greedy fail?",
            "What if you need to reconstruct the path, not just the optimal value?",
            "What changes if you can make unlimited vs limited moves/choices?"
        ]
    if any(w in code for w in ['Queue', 'LinkedList', 'queue']):
        return [
            "What if the graph is disconnected?",
            "What if edges have weights (non-uniform cost)?",
            "Can this be solved with DFS instead? What's the tradeoff?",
            "What if you need the path, not just the distance/existence?",
            "What if the graph is too large for BFS? Iterative deepening?"
        ]
    if any(w in code for w in ['PriorityQueue', 'priorityQueue', 'heap']):
        return [
            "What if you need the k-th smallest instead of largest?",
            "What if elements are added/removed dynamically?",
            "Can this be solved with sorting instead? What's the tradeoff?",
            "What if k is very large (close to n)? Different approach?",
            "What if there are ties? How does your comparator handle them?"
        ]
    if 'ListNode' in code or 'linked' in code.lower():
        return [
            "What if the list is circular? How does detection change?",
            "What if you can't use extra memory (O(1) space constraint)?",
            "What if the list is doubly linked? Any simplifications?",
            "What if you need to do this recursively vs iteratively?",
            "What if multiple operations need to be supported (LRU cache pattern)?"
        ]
    if 'TreeNode' in code or 'treeNode' in code or 'bst' in code.lower():
        return [
            "What if the tree is not balanced (skewed)? Worst-case complexity?",
            "What if you need to do this iteratively (no recursion)?",
            "What if the tree is an N-ary tree instead of binary?",
            "What if you need to handle both BST and non-BST trees?",
            "Can this be solved with Morris traversal (O(1) space)?"
        ]
    if 'dp' in code.lower() and ('string' in code.lower() or 'subsequence' in code.lower() or 'edit' in code.lower()):
        return [
            "What if you need to reconstruct the actual subsequence/path?",
            "What if the strings are very long? Can you optimize space?",
            "What if case sensitivity or character encoding matters?",
            "What if you need to handle multiple strings (3+)?",
            "What if there are wildcards or regex patterns involved?"
        ]
    
    return [
        "What if the input size is much larger? Can you optimize?",
        "What if you need O(1) extra space instead of O(n)?",
        "What if there are duplicates or edge cases to handle?",
        "What if the problem constraints change (positive only, sorted, etc.)?",
        "Can this solution be parallelized?"
    ]

def get_pattern_insight(prob_key):
    """Return pattern insight based on algorithm type."""
    kt_file = CODE_DIR / prob_key / 'kotlin.txt'
    if not kt_file.exists():
        return "Study the code and identify the algorithmic pattern."
    
    with open(kt_file) as f:
        code = f.read()
    
    if any(w in code for w in ['binarySearch', 'binarySearch']):
        return "**Pattern:** Binary search on sorted data. Key insight: the predicate must be monotonic — once it becomes true, it stays true for all larger values."
    if any(w in code for w in ['dp', 'memo', 'cache', 'dp[']):
        if 'dfs' in code.lower():
            return "**Pattern:** Top-down DP with memoization. Cache results of recursive calls to avoid recomputing overlapping subproblems."
        return "**Pattern:** Bottom-up DP. Build solutions from smallest subproblems upward using a table."
    if any(w in code for w in ['Queue', 'LinkedList']):
        if 'Priority' in code:
            return "**Pattern:** Dijkstra / priority-queue BFS. Use a min-heap to always expand the cheapest node first."
        return "**Pattern:** BFS (Breadth-First Search). Use a queue to explore nodes level by level, guaranteeing shortest path in unweighted graphs."
    if 'PriorityQueue' in code or 'priorityQueue' in code:
        return "**Pattern:** Heap-based processing. Use a priority queue to maintain a dynamic ordering of elements."
    if 'ListNode' in code or 'linked' in code.lower():
        return "**Pattern:** Linked list manipulation. Use pointer rearrangement to achieve O(1) space solutions."
    if 'TreeNode' in code or 'treeNode' in code:
        if 'bst' in code.lower() or 'binarySearchTree' in code or 'search' in code.lower():
            return "**Pattern:** BST property exploitation. Inorder traversal of a BST gives sorted order."
        return "**Pattern:** Tree traversal. Choose DFS for depth exploration, BFS for level-order processing."
    if 'backtrack' in code.lower() or 'dfs' in code.lower():
        return "**Pattern:** Backtracking / DFS. Explore all possibilities, pruning when constraints are violated."
    if 'trie' in code.lower():
        return "**Pattern:** Trie (prefix tree). Store strings in a tree structure for O(L) prefix lookups."
    if 'union' in code.lower() or 'find' in code.lower():
        return "**Pattern:** Disjoint Set Union (Union-Find). Track connected components with near-O(1) operations."
    if '|' in code or '&' in code or 'xor' in code.lower() or 'shl' in code or 'shr' in code:
        return "**Pattern:** Bit manipulation. Use bitwise operations for fast computation and compact state tracking."
    
    return "**Pattern:** Study the code's approach — identify the core data structure and traversal method."

def upgrade_chapter(filepath):
    """Upgrade a chapter to Koko-level format."""
    with open(filepath) as f:
        content = f.read()
    
    original = content
    changes = 0
    
    # Find each problem section
    problem_sections = list(re.finditer(r'^##\s+(.+?)\n', content, re.MULTILINE))
    
    for i, section_match in enumerate(problem_sections):
        section_start = section_match.start()
        section_name = section_match.group(1).strip()
        
        # Skip non-problem sections (The Pattern, Complete Problem Set, Key Takeaways)
        if section_name in ['The Pattern', 'Complete Problem Set', 'Key Takeaways']:
            continue
        
        # Get the section content start (skip the ## header line)
        section_content_start = section_match.end()
        
        # Determine section end (next ## or end of file)
        if i + 1 < len(problem_sections):
            section_end = problem_sections[i + 1].start()
        else:
            section_end = len(content)
        
        section_content = content[section_content_start:section_end]
        
        # Check if this problem already has a detailed Problem section
        if '### Problem' not in section_content[:500]:
            continue  # Skip if no Problem section
        
        # Get problem key (lowercase directory name)
        prob_key = section_name.lower().replace(' ', '')
        # Try to find the actual directory name
        prob_dir = prob_key.replace(' ', '')
        
        # Build enhanced problem section
        kdoc = get_kdoc_description(prob_dir)
        variations = get_variations(prob_dir)
        pattern_insight = get_pattern_insight(prob_dir)
        
        # Check what's currently in the section
        has_variations = '### Variations' in section_content
        has_pattern = '### Pattern Insight' in section_content
        
        # Insert Pattern Insight before Complexity
        if not has_pattern:
            complexity_match = re.search(r'### Complexity', section_content)
            if complexity_match:
                pos = complexity_match.start()
                insight_block = f'\n### Pattern Insight\n\n{pattern_insight}\n\n### Complexity'
                section_content = section_content[:pos] + insight_block + section_content[pos + len('### Complexity'):]
                changes += 1
        
        # Insert Variations at the end
        if not has_variations:
            var_block = '\n### Variations\n\n'
            for v in variations:
                var_block += f'1. {v}\n'
            var_block += '\n---\n'
            
            # Find the end marker
            end_marker = section_content.rfind('\n---')
            if end_marker >= 0:
                section_content = section_content[:end_marker] + var_block
                changes += 1
        
        # Replace section content
        content = content[:section_content_start] + section_content + content[section_end:]
    
    if changes > 0:
        with open(filepath, 'w') as f:
            f.write(content)
        return changes
    return 0

def main():
    print("Upgrading all chapters to Koko-level format...\n")
    total = 0
    for ch_file in sorted(CHAPTERS_DIR.glob('*.md')):
        if ch_file.name == '14-problem-index.md':
            continue
        changes = upgrade_chapter(ch_file)
        if changes > 0:
            print(f'  ✅ {ch_file.name}: {changes} enhancements applied')
            total += changes
        else:
            print(f'  ⚠️  {ch_file.name}: no changes needed')
    print(f'\n✅ Total: {total} enhancements across all chapters')

if __name__ == '__main__':
    main()

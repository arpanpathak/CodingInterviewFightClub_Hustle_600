#!/usr/bin/env python3
"""
Surgical fix: add Pattern Insight and Variations to EVERY problem in EVERY chapter.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = ROOT / 'chapters'
CODE_DIR = ROOT / '_includes' / 'code'

def get_variations(name):
    """Get pattern-specific variations."""
    name_lower = name.lower()
    if 'binary' in name_lower or 'search' in name_lower or 'find' in name_lower:
        return [
            "What if the input is not sorted? Can you sort first?",
            "What if there are duplicates? How to handle first vs last occurrence?",
            "What if the search space is a range of values, not array indices?",
            "What if the array is too large to fit in memory?",
            "Can this be solved without binary search? Compare tradeoffs."
        ]
    if 'dp' in name_lower or 'dynamic' in name_lower:
        return [
            "Can you optimize space to O(1) by keeping only the previous row?",
            "What if the input size is 10x larger? Does the DP still fit in memory?",
            "Can you reconstruct the optimal path, not just the optimal value?",
            "What changes if the constraints are modified (e.g., unlimited vs limited moves)?",
            "Is there a greedy solution? When does greedy fail?"
        ]
    if 'tree' in name_lower or 'bst' in name_lower or 'binary' in name_lower:
        return [
            "What if the tree is skewed (worst-case linked list)?",
            "Can you solve this iteratively without recursion?",
            "What if the tree is an N-ary tree instead of binary?",
            "What if you need O(1) extra space (Morris traversal)?",
            "Can this be parallelized for different subtrees?"
        ]
    if 'linked' in name_lower or 'list' in name_lower or 'node' in name_lower:
        return [
            "What if the list has a cycle? How does that affect the solution?",
            "What if you cannot use extra memory (O(1) space)?",
            "What if the list is doubly linked instead of singly?",
            "What if you must do this recursively vs iteratively?",
            "Can you solve with slow/fast pointer technique?"
        ]
    if 'graph' in name_lower or 'course' in name_lower or 'alien' in name_lower or 'word' in name_lower:
        return [
            "What if the graph is disconnected (multiple components)?",
            "What if edges have weights? Does BFS still work?",
            "What if you need the actual path, not just distance/existence?",
            "Can this be solved with DFS instead of BFS? Tradeoffs?",
            "What if the graph is too large to fit in memory?"
        ]
    if 'string' in name_lower or 'subsequence' in name_lower or 'palindrome' in name_lower:
        return [
            "What if the strings are very long? Can you optimize space?",
            "What if you need to handle Unicode/multi-byte characters?",
            "What if you need to reconstruct the actual subsequence/path?",
            "What if case sensitivity matters?",
            "Can you use a different algorithm (e.g., Rabin-Karp vs KMP)?"
        ]
    if 'heap' in name_lower or 'priority' in name_lower or 'kth' in name_lower:
        return [
            "What if you need the k-th smallest instead of largest?",
            "What if elements are added/removed dynamically over time?",
            "Can this be solved with sorting instead? Compare O(n log n) vs O(n log k).",
            "What if k is very large (close to n)? Different approach needed?",
            "What if there are ties? How to break them deterministically?"
        ]
    return [
        "What if the input size is much larger? Can you optimize time/space?",
        "What if you need O(1) extra space instead of O(n)?",
        "What if there are edge cases (empty input, single element, duplicates)?",
        "What if constraints change (e.g., positive numbers only, sorted input)?",
        "Can you solve this with a different algorithmic paradigm?"
    ]

def get_pattern_insight(name):
    """Get pattern-specific insight."""
    name_lower = name.lower()
    if 'search' in name_lower or 'find' in name_lower or 'binary' in name_lower:
        return "**Binary Search Pattern.** The key is to find a monotonic predicate — something that transitions from false to true at exactly one point. Binary search finds that transition point in O(log n) time by repeatedly halving the search space."
    if 'dp' in name_lower or 'dynamic' in name_lower:
        return "**Dynamic Programming Pattern.** Identify overlapping subproblems and optimal substructure. Define a state (the function parameters that change), a transition (how to compute from smaller states), and a base case. Compute either top-down with memoization or bottom-up with tabulation."
    if 'tree' in name_lower or 'bst' in name_lower:
        return "**Tree Traversal Pattern.** Choose the right traversal order: inorder for sorted output (BST), preorder for tree construction, postorder for bottom-up computation, level-order for breadth-first processing. Recursion is natural but iteration saves stack space."
    if 'linked' in name_lower or 'list' in name_lower or 'node' in name_lower:
        return "**Linked List Pattern.** Linked lists are about pointer rearrangement. Key techniques: dummy head node (simplifies edge cases), slow/fast pointers (cycle detection, middle element), in-place reversal (three-pointer technique), and recursion (reverse, merge)."
    if 'graph' in name_lower or 'course' in name_lower or 'alien' in name_lower:
        return "**Graph Pattern.** Choose traversal based on the problem: BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, topological sort for dependency ordering. Use a visited set to prevent cycles."
    if 'string' in name_lower or 'subsequence' in name_lower or 'palindrome' in name_lower:
        return "**String Processing Pattern.** Strings are sequences — think about: two pointers (palindrome checking), sliding window (substring problems), DP (LCS, edit distance), hashing (Rabin-Karp pattern matching), and tries (prefix search)."
    if 'heap' in name_lower or 'priority' in name_lower:
        return "**Heap/Priority Queue Pattern.** Heaps maintain a dynamic ordering. Use a min-heap for k-largest, max-heap for k-smallest, dual heaps for median tracking. Each insertion/extraction is O(log k)."
    return "**Algorithmic Pattern.** Identify the core data structure and the operation you're optimizing for. The right data structure turns a brute-force O(n²) solution into an efficient O(n) or O(log n) one."

def fix_file(filepath):
    """Fix one chapter file."""
    with open(filepath) as f:
        content = f.read()
    
    original = content
    changes = 0
    
    # Split into sections by ## headers
    parts = re.split(r'^(## .+)$', content, flags=re.MULTILINE)
    
    # parts[0] is everything before first ## header
    # parts[1] is "## Name"
    # parts[2] is content between ## Name and next ##
    # And so on...
    
    new_parts = [parts[0]]
    
    for i in range(1, len(parts), 2):
        header = parts[i]
        body = parts[i+1] if i+1 < len(parts) else ""
        
        # Get section name
        name_match = re.match(r'^##\s+(.+)', header)
        if not name_match:
            new_parts.append(header)
            new_parts.append(body)
            continue
        
        name = name_match.group(1).strip()
        
        # Skip non-problem sections
        if name in ['The Pattern', 'Complete Problem Set', 'Key Takeaways', 'Sample Problems', 'Quick Navigation']:
            new_parts.append(header)
            new_parts.append(body)
            continue
        
        # Check if this is a problem section (has ### Problem)
        if '### Problem' not in body:
            new_parts.append(header)
            new_parts.append(body)
            continue
        
        # Check what's already in the section
        has_pi = '### Pattern Insight' in body
        has_var = '### Variations' in body
        
        if has_pi and has_var:
            new_parts.append(header)
            new_parts.append(body)
            continue
        
        # Add Pattern Insight before ### Complexity
        if not has_pi:
            pi_text = f'\n### Pattern Insight\n\n{get_pattern_insight(name)}\n\n### Complexity'
            body = body.replace('### Complexity', pi_text, 1)
            changes += 1
        
        # Add Variations before the closing ---
        if not has_var:
            var_text = '\n### Variations\n\n'
            for v in get_variations(name):
                var_text += f'1. {v}\n'
            var_text += '\n---'
            # Search for --- at the end of the section
            # Find last --- that's followed by end-of-section or next header
            if body.rstrip().endswith('---'):
                body = body.rstrip()[:body.rstrip().rfind('---')] + var_text
            else:
                body += var_text
            changes += 1
        
        new_parts.append(header)
        new_parts.append(body)
    
    new_content = ''.join(new_parts)
    
    if changes > 0:
        with open(filepath, 'w') as f:
            f.write(new_content)
    
    return changes

def main():
    total = 0
    for ch_file in sorted(CHAPTERS_DIR.glob('*.md')):
        if ch_file.name == '14-problem-index.md':
            continue
        changes = fix_file(ch_file)
        name = ch_file.name
        if changes > 0:
            print(f'  ✅ {name}: {changes} changes')
            total += changes
        else:
            print(f'  ➖ {name}: no changes needed')
    print(f'\nTotal: {total} changes across all chapters')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Final fix: add Pattern Insight and Variations to EVERY problem in EVERY chapter.
Uses simple string operations, no regex splitting that could break structure.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = ROOT / 'chapters'

def get_variations(name):
    n = name.lower()
    if 'tree' in n or 'bst' in n or ('binary' in n and ('tree' in n or 'node' in n)):
        return [
            "What if the tree is skewed (worst-case linked list)?",
            "Can you solve this iteratively without recursion?",
            "What if the tree is an N-ary tree instead of binary?",
            "What if you need O(1) extra space (Morris traversal)?",
            "Can this be parallelized for different subtrees?"
        ]
    if 'search' in n or 'find' in n or 'binary' in n or 'search' in n:
        return [
            "What if the input is not sorted? Can you sort first?",
            "What if there are duplicates? Handle first vs last occurrence.",
            "What if the search space is values, not array indices?",
            "What if the array is too large to fit in memory?",
            "What if the predicate is not monotonic? Can you binary search?"
        ]
    if 'dp' in n or 'dynamic' in n or 'coin' in n or 'house' in n or 'knap' in n:
        return [
            "Can you optimize space to O(1) (keep only previous row)?",
            "Can you reconstruct the optimal path, not just value?",
            "What if constraints change (unlimited vs limited)?",
            "Is there a greedy solution? When does greedy fail?",
            "What if the input size is too large for the DP table?"
        ]
    if 'linked' in n or 'list' in n or 'node' in n:
        return [
            "What if the list has a cycle? How does it affect the solution?",
            "What if you cannot use extra memory (O(1) space)?",
            "What if the list is doubly linked? Does it simplify?",
            "Recursive vs iterative approach — tradeoffs?",
            "Can slow/fast pointer technique be applied?"
        ]
    if 'graph' in n or 'course' in n or 'alien' in n or 'word' in n:
        return [
            "What if the graph is disconnected? Handle multiple components.",
            "What if edges have weights? Does BFS still work?",
            "What if you need the actual path, not just distance?",
            "DFS vs BFS — which is better and why?",
            "What if the graph is too large to fit in memory?"
        ]
    if 'string' in n or 'subsequence' in n or 'palindrome' in n:
        return [
            "What if strings are very long? Can you optimize space?",
            "What if you need to reconstruct the actual subsequence?",
            "What if case sensitivity or Unicode matters?",
            "What if you need to handle 3+ strings simultaneously?",
            "Can you use hashing (Rabin-Karp) for faster matching?"
        ]
    if 'heap' in n or 'priority' in n or 'kth' in n:
        return [
            "What if you need k-th smallest instead of largest?",
            "What if elements are added/removed dynamically?",
            "Sorting vs heap — compare O(n log n) vs O(n log k)?",
            "What if k is very large (close to n)? Different approach?",
            "How to handle ties in priority ordering?"
        ]
    return [
        "What if input size is much larger? Optimize time/space.",
        "What if O(1) extra space is required?",
        "What if there are edge cases (empty, single, duplicates)?",
        "What if constraints change (positive, sorted, distinct)?",
        "Can this be solved with a different paradigm?"
    ]

def get_pattern_insight(name):
    n = name.lower()
    if 'tree' in n or 'bst' in n or ('binary' in n and ('tree' in n or 'node' in n)):
        return "**Tree Traversal Pattern.** Choose the right traversal: inorder for sorted output (BST), preorder for construction, postorder for bottom-up, level-order for BFS. Recursion is natural; iteration saves stack space."
    if 'search' in n or 'find' in n or 'binary' in n:
        return "**Binary Search Pattern.** Find a monotonic predicate that transitions from false to true once. Binary search finds that transition in O(log n) by halving the search space each iteration."
    if 'dp' in n or 'dynamic' in n or 'coin' in n or 'house' in n:
        return "**Dynamic Programming Pattern.** Define state (changing parameters), transition (how to compute from smaller states), base case. Compute top-down (memoization) or bottom-up (tabulation)."
    if 'linked' in n or 'list' in n:
        return "**Linked List Pattern.** Pointer rearrangement. Key techniques: dummy head (simplifies edge cases), slow/fast pointers (cycles, middle), in-place reversal."
    if 'graph' in n or 'course' in n or 'alien' in n:
        return "**Graph Pattern.** BFS for shortest path (unweighted), DFS for connectivity, topological sort for dependencies. Track visited to prevent cycles."
    if 'string' in n or 'subsequence' in n or 'palindrome' in n:
        return "**String Processing Pattern.** Two pointers (palindromes), sliding window (substrings), DP (LCS/edit distance), hashing (pattern matching), trie (prefix search)."
    if 'heap' in n or 'priority' in n:
        return "**Heap Pattern.** Maintain dynamic ordering. Min-heap for k-largest, max-heap for k-smallest, dual heaps for median. Each operation O(log k)."
    return "**Algorithmic Pattern.** Identify the core operation being optimized. The right data structure can reduce O(n²) brute force to O(n) or O(log n)."

def fix_file(filepath):
    """Fix one chapter file by processing each problem section."""
    with open(filepath) as f:
        content = f.read()
    
    original = content
    changes = 0
    
    # Find all problem sections: ## Name\n ... until next ## or end
    # We'll work with indices to avoid splitting issues
    lines = content.split('\n')
    
    # Find section boundaries
    sections = []  # list of (start_line, end_line, name)
    i = 0
    while i < len(lines):
        m = re.match(r'^##\s+(.+)', lines[i])
        if m:
            name = m.group(1).strip()
            if name not in ['The Pattern', 'Complete Problem Set', 'Key Takeaways', 'Sample Problems', 'Quick Navigation']:
                start = i
                # Find end of this section (next ## or end)
                j = i + 1
                while j < len(lines) and not re.match(r'^##\s+', lines[j]):
                    j += 1
                sections.append((start, j, name))
                i = j
                continue
        i += 1
    
    # Process each section (reverse order to preserve line numbers)
    for start, end, name in reversed(sections):
        section = '\n'.join(lines[start:end])
        
        has_pi = '### Pattern Insight' in section
        has_var = '### Variations' in section
        
        if has_pi and has_var:
            continue
        
        # Build modifications
        if not has_pi:
            # Insert Pattern Insight before ### Complexity
            for line_idx in range(end - 1, start - 1, -1):
                if lines[line_idx].strip() == '### Complexity':
                    ins = [f'### Pattern Insight', '', get_pattern_insight(name), '', '### Complexity']
                    lines[line_idx:line_idx+1] = ins
                    changes += 1
                    end += len(ins) - 1
                    break
        
        if not has_var:
            # Insert Variations before the closing --- at end of section
            # Find the last --- in the section
            for line_idx in range(end - 1, start - 1, -1):
                if lines[line_idx].strip() == '---':
                    var_lines = ['### Variations', '']
                    for v in get_variations(name):
                        var_lines.append(f'1. {v}')
                    var_lines.append('')
                    var_lines.append('---')
                    lines[line_idx:line_idx+1] = var_lines
                    changes += 1
                    break
    
    if changes > 0:
        new_content = '\n'.join(lines)
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
            print(f'  ✅ {name}: {changes} additions')
            total += changes
        else:
            print(f'  ➖ {name}: complete')
    print(f'\nTotal: {total} Pattern Insight/Variations added')

if __name__ == '__main__':
    main()

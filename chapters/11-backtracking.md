---
layout: chapter
title: "Backtracking - Exhaustive Search Mastery"
chapter_number: 11
chapter_title: "Backtracking"
toc: true
prev_chapter:
  url: "/chapters/10-string-matching"
  title: "String Matching - KMP, Rabin-Karp & More"
next_chapter:
  url: "/chapters/12-caches"
  title: "Caches - LRU, LFU & Memory Management"
---

# Backtracking: Exhaustive Search Mastery

## Core Pattern

```kotlin
fun backtrack(candidate, state) {
    if (isSolution(candidate)) { result.add(candidate.copy()); return }
    for (choice in choices) {
        makeChoice(choice); backtrack(candidate, state); undoChoice(choice)
    }
}
```

## Complete Problem Set (13+ problems)

| # | Problem | Pattern | File |
|---|---------|---------|------|
| 1 | Subsets | Powerset | array/Combinatorics/Subsets.kt |
| 2 | Permutations | All arrangements | array/Combinatorics/Permutations.kt |
| 3 | Permutations II (dups) | With pruning | array/Combinatorics/Permutation_II.kt |
| 4 | Combinations | Choose k | array/Combinatorics/Combinations.kt |
| 5 | Combination Sum | Unbounded choices | array/backtracking/CombinationSum.kt |
| 6 | Combination Sum II (no reuse) | With frequency | array/backtracking/CombinationSum_II.kt |
| 7 | Combination Sum III | Fixed size k | array/backtracking/CombinationSum3.kt |
| 8 | Next Permutation | In-place | array/Combinatorics/NextPermutation.kt |
| 9 | Next Greater Element III | Permutation | array/Combinatorics/NextGreaterElement_III.kt |
| 10 | N-Queens | Classic | backtracking/NQueen.kt |
| 11 | N-Queens II | Count solutions | backtracking/NQueen_II.kt |
| 12 | Sudoku Solver | Board fill | backtracking/SudokuSolver.kt |
| 13 | Expression Add Operators | Expression eval | backtracking/ExpressionAndAddOperators.kt |
| 14 | Palindrome Partitioning | String splits | backtracking/PalindromePartitioning.kt |
| 15 | Partition to K Equal Sum | Subset sum | backtracking/PartitionToKEqualSumSubsets.kt |
| 16 | Strobogrammatic Number II | Recursive build | backtracking/Strobogrammatic_Number_II.kt |
| 17 | Word Search | Grid DFS | grid/search/WordSearch_II.kt |

### Subsets
```kotlin
fun subsets(nums: IntArray): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    fun backtrack(start: Int, current: MutableList<Int>) {
        result.add(current.toList())
        for (i in start until nums.size) {
            current.add(nums[i]); backtrack(i + 1, current); current.removeAt(current.lastIndex)
        }
    }
    backtrack(0, mutableListOf()); return result
}
```

### Permutations
```kotlin
fun permute(nums: IntArray): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    fun backtrack(current: MutableList<Int>) {
        if (current.size == nums.size) { result.add(current.toList()); return }
        for (num in nums) {
            if (num in current) continue
            current.add(num); backtrack(current); current.removeAt(current.lastIndex)
        }
    }
    backtrack(mutableListOf()); return result
}
```

### N-Queens
```kotlin
fun solveNQueens(n: Int): List<List<String>> {
    val result = mutableListOf<List<String>>()
    val board = Array(n) { CharArray(n) { '.' } }
    val cols = BooleanArray(n); val diag1 = BooleanArray(2*n-1); val diag2 = BooleanArray(2*n-1)
    
    fun backtrack(row: Int) {
        if (row == n) { result.add(board.map { String(it) }); return }
        for (col in 0 until n) {
            if (cols[col] || diag1[row+col] || diag2[row-col+n-1]) continue
            board[row][col] = 'Q'; cols[col] = true; diag1[row+col] = true; diag2[row-col+n-1] = true
            backtrack(row + 1)
            board[row][col] = '.'; cols[col] = false; diag1[row+col] = false; diag2[row-col+n-1] = false
        }
    }
    backtrack(0); return result
}
```

---

> **Next up: [Caches ->](./12-caches.md)**

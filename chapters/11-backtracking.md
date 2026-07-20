---
layout: chapter
title: "Backtracking"
chapter_number: 11
chapter_title: "Backtracking"
toc: true
prev_chapter:
  url: "/chapters/10-string-matching.html"
  title: "String Matching"
next_chapter:
  url: "/chapters/12-caches.html"
  title: "Caches & Memory Management"
---

# Backtracking

> **14 problems** — **Backtracking** = DFS on decision tree + pruning. Generate candidates, explore valid ones, backtrack when stuck. Essential for constraint satisfaction problems.

## Complete Problem Set

| # | Problem |
|---|---------|
| 1 | [Combinations](#combinations) |
| 2 | [Combination Sum](#combinationsum) |
| 3 | [Combination Sum_II](#combinationsum_ii) |
| 4 | [Combination Sum3](#combinationsum3) |
| 5 | [Expression And Add Operators](#expressionandaddoperators) |
| 6 | [Expression And Add Operators Optimized](#expressionandaddoperatorsoptimized) |
| 7 | [N Queen](#nqueen) |
| 8 | [N Queen_II](#nqueen_ii) |
| 9 | [Palindrome Partitioning](#palindromepartitioning) |
| 10 | [Partition To K Equal Sum Subsets](#partitiontokequalsumsubsets) |
| 11 | [Restore IP Addresses](#restoreipaddresses) |
| 12 | [Subsets](#subsets) |
| 13 | [Sudoku Solver](#sudokusolver) |
| 14 | [Sudoku Solver Set](#sudokusolverset) |

---

## Combinations

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.Combinatorics

class Combinations {

/**
 * combine — executes the core logic of this algorithm on the provided input.
 *
 * @param n the size/dimension parameter for the algorithm
 * @param k the number of elements/operations to consider (k parameter)
 * @return a list/collection of result elements
 */
    fun combine(n: Int, k: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()

/**
 * combine — executes the core logic of this algorithm on the provided input.
 *
 * @param start the left/starting boundary of the search range (inclusive)
 * @param n the size/dimension parameter for the algorithm
 * @param k the number of elements/operations to consider (k parameter)
 * @param current the current parameter — a list of integers used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
        fun combine(start: Int, n: Int, k: Int, current: MutableList<Int> = mutableListOf()) {
            if (current.size == k) {
                result.add(current.toList())
                return
            }

            for(i in start..n) {
                current.add(i)
                combine(i + 1, n, k, current)

                current.removeLast()

            }
        }

        combine(1, n,k)
        return result
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) |

---

## Combination Sum

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.backtracking

class CombinationSum {

/**
 * combination Sum — executes the core logic of this algorithm on the provided input.
 *
 * @param candidates the candidates parameter — a array of integers used in the computation
 * @param target the target value to search for or match against
 * @return a list/collection of result elements
 */
    fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()

/**
 * Searches for and returns the target element/position using an efficient algorithm.
 *
 * @param current the current parameter — a list of integers used in the computation
 * @param start the left/starting boundary of the search range (inclusive)
 * @param remaining the remaining parameter — a integer value used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
        fun findCombinations(current: MutableList<Int>, start: Int, remaining: Int) {
            when {
                remaining == 0 -> result.add(ArrayList(current))
                remaining > 0 && start < candidates.size -> {
                    current.add(candidates[start])
                    findCombinations(current, start, remaining - candidates[start]) // Include current candidate
                    current.removeLast();
                    findCombinations(current, start + 1, remaining) // Exclude and move to next
                }
            }
        }

        findCombinations(mutableListOf(), 0, target)
        return result
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) |

---

## Combination Sum_II

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.backtracking

class CombinationSum_II {

/**
 * combination Sum2 — executes the core logic of this algorithm on the provided input.
 *
 * @param candidates the candidates parameter — a array of integers used in the computation
 * @param target the target value to search for or match against
 * @return a list/collection of result elements
 */
    fun combinationSum2(candidates: IntArray, target: Int): List<List<Int>> {
        val results = mutableListOf<List<Int>>()
        candidates.sort()

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param index the index position in the collection
 * @param target the target value to search for or match against
 * @param curr the curr parameter — a list of integers used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
        fun dfs(index: Int, target: Int, curr: MutableList<Int>) {
            if (target == 0) {
                results.add(ArrayList(curr))
                return
            }

            for (i in index until candidates.size) {
                if (i > index && candidates[i] == candidates[i - 1]) continue // Skip duplicates
                if (candidates[i] > target) break // Prune the search

                curr.add(candidates[i])
                dfs(i + 1, target - candidates[i], curr)
                curr.removeAt(curr.size - 1)
            }
        }

        dfs(0, target, mutableListOf())
        return results
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) |

---

## Combination Sum3

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.backtracking

class CombinationSum3 {

/**
 * combination Sum3 — executes the core logic of this algorithm on the provided input.
 *
 * @param k the number of elements/operations to consider (k parameter)
 * @param n the size/dimension parameter for the algorithm
 * @return a list/collection of result elements
 */
    fun combinationSum3(k: Int, n: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        dfs(k,n, 1, result)
        return result
    }

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param k the number of elements/operations to consider (k parameter)
 * @param remaining the remaining parameter — a integer value used in the computation
 * @param start the left/starting boundary of the search range (inclusive)
 * @param result the result parameter — a list of integers used in the computation
 * @param curr the curr parameter — a list of integers used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
    fun dfs(
        k: Int,
        remaining: Int,
        start: Int,
        result: MutableList<List<Int>>,
        curr: MutableList<Int> = mutableListOf(),
    ) {

        if (curr.size == k && remaining == 0) {
            result.add(curr.toList())
            return
        }

        if  (remaining <=0 || curr.size == k)
            return

        for (i in start..9) {
            curr.add(i)

            dfs(k, remaining - i, i + 1, result, curr)

            curr.remove(i)
        }

    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) |

---

## Expression And Add Operators

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package backtracking

class ExpressionAndAddOperators {

/**
 * Inserts the specified element into the data structure.
 *
 * @param num the num parameter — a string value used in the computation
 * @param target the target value to search for or match against
 * @return a list/collection of result elements
 */
    fun addOperators(num: String, target: Int): List<String> {
        val result = mutableListOf<String>()

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param index the index position in the collection
 * @param prevOperand the prevOperand parameter — a input parameter of type Long used in the computation
 * @param currentOperand the currentOperand parameter — a input parameter of type Long used in the computation
 * @param value the target value to search for or match against
 * @param expression the expression parameter — a string value used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
        fun dfs(index: Int, prevOperand: Long, currentOperand: Long, value: Long, expression: String) {
            if (index == num.length) {
                if (value == target.toLong() && currentOperand == 0L) {
                    result.add(expression)
                }
                return
            }

            // Extending the current operand by one digit
            val currentDigit = num[index].toString().toLong()
            val newOperand = currentOperand * 10 + currentDigit

            // Avoid cases where numbers start with '0'
            if (newOperand > 0) {
                // No operator added, just extend the current operand
                dfs(index + 1, prevOperand, newOperand, value, expression)
            }

            // Add '+'
            dfs(index + 1, newOperand, 0, value + newOperand, "$expression+$newOperand")

            // Add '-'
            dfs(index + 1, -newOperand, 0, value - newOperand, "$expression-$newOperand")

            // Add '*'
            dfs(index + 1, prevOperand * newOperand, 0, value - prevOperand + (prevOperand * newOperand), "$expression*$newOperand")
        }

        for (i in 1..num.length) {
            val currentOperand = num.substring(0, i).toLong()
            if (currentOperand.toString().length != i) continue // Skip numbers with leading zeros

            dfs(i, currentOperand, 0, currentOperand, currentOperand.toString())
        }

        return result
    }

    // ANother leetcode solution https://leetcode.com/problems/expression-add-operators/discuss/951147/Kotlin-C%2B%2B%3A-O(n4n)-time-and-O(n)-time-with-backtracking

/**
 * Inserts the specified element into the data structure.
 *
 * @param num the num parameter — a string value used in the computation
 * @param target the target value to search for or match against
 * @return a list/collection of result elements
 */
    fun addOperators2(num: String, target: Int): List<String> {
        val res = ArrayList<String>()

/**
 * partition — executes the core logic of this algorithm on the provided input.
 *
 * @param start the left/starting boundary of the search range (inclusive)
 * @param path the path parameter — a string value used in the computation
 * @param sum the target amount/sum to achieve
 * @param prev the prev parameter — a input parameter of type Long used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
        fun partition(start: Int, path: String, sum: Long, prev: Long) {
            if (start == num.length) {
                if (sum == target.toLong()) {
                    res.add(path)
                }
                return
            }

            // 1|23
            // 12|3
            // 123|
            for (i in start..num.length - 1) {
                val s = num.substring(start..i)
                val current = s.toLong()
                // invalid case: 1 + 05
                if (s.length > 1 && s[0] == '0')
                    break

                if (path.isEmpty()) {
                    partition(i + 1, s, current, current)
                } else {
                    partition(i + 1, "$path+$s", sum + current, current)
                    partition(i + 1, "$path-$s", sum - current, -current)
                    // 1 + 2 - 4 * 12 --> -1 - (-4) + (-4 * 12) --> 3 + (-48) --> -45
                    partition(i + 1, "$path*$s", sum - prev + prev * current, prev * current)
                }
            }
        }

        partition(0, "", 0L, 0L)
        return res.toList()
    }

}


/**
 * main — executes the core logic of this algorithm on the provided input.
 *
 * @param args the args parameter — a array of elements used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
fun main(args: Array<String>) {
    val test = ExpressionAndAddOperators()

    println(test.addOperators("1310", 130))
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) |

---

## Expression And Add Operators Optimized

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package backtracking

class ExpressionAndAddOperatorsOptimized {

/**
 * Inserts the specified element into the data structure.
 *
 * @param num the num parameter — a string value used in the computation
 * @param target the target value to search for or match against
 * @return a list/collection of result elements
 */
    fun addOperators(num: String, target: Int): List<String> {
        val res = ArrayList<String>()

/**
 * partition — executes the core logic of this algorithm on the provided input.
 *
 * @param start the left/starting boundary of the search range (inclusive)
 * @param path the path parameter — a input parameter of type StringBuilder used in the computation
 * @param sum the target amount/sum to achieve
 * @param prev the prev parameter — a input parameter of type Long used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
        fun partition(start: Int, path: StringBuilder, sum: Long, prev: Long) {
            if (start == num.length) {
                if (sum == target.toLong()) {
                    res.add(path.toString())
                }
                return
            }

            for (i in start until num.length) {
                val s = num.substring(start..i)
                val current = s.toLong()

                // Skip invalid numbers with leading zeros
                if (s.length > 1 && s[0] == '0') break

                val len = path.length // Remember the length of the path before modification

                if (path.isEmpty()) {
                    path.append(s)
                    partition(i + 1, path, current, current)
                    path.setLength(len) // Revert the path to its previous state
                } else {
                    // Try adding '+' operator
                    path.append("+").append(s)
                    partition(i + 1, path, sum + current, current)
                    path.setLength(len)

                    // Try adding '-' operator
                    path.append("-").append(s)
                    partition(i + 1, path, sum - current, -current)
                    path.setLength(len)

                    // Try adding '*' operator
                    path.append("*").append(s)
                    partition(i + 1, path, sum - prev + prev * current, prev * current)
                    path.setLength(len)
                }
            }
        }

        partition(0, StringBuilder(), 0L, 0L)
        return res
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) |

---

## N Queen

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package backtracking

import javax.swing.text.html.HTML.Attribute.N

class NQueen {
    private lateinit var placed: IntArray

/**
 * Performs the core computation/algorithm and returns the result.
 *
 * @param n the size/dimension parameter for the algorithm
 * @return a list/collection of result elements
 */
    fun solveNQueens(n: Int): List<List<String>> {
        val results = mutableListOf<List<String>>()
        placed = IntArray(n) { -1 } // Initialize with -1 indicating no queens are placed

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param row the row parameter — a integer value used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
        fun dfs(row: Int) {
            if (row == n) {
                // Convert the board configuration to the required output format
                val board = List(n) { CharArray(n) { '.' } }
                for (r in placed.indices) {
                    board[r][placed[r]] = 'Q'
                }
                results.add(board.map { it.joinToString("") })
                return
            }

            for (col in 0 until n) {
                if (isSafe(row, col)) {
                    placed[row] = col
                    dfs(row + 1)
                    placed[row] = -1 // Remove the queen (backtrack)
                }
            }
        }

        dfs(0)
        return results
    }

/**
 * is Safe — executes the core logic of this algorithm on the provided input.
 *
 * @param row the row parameter — a integer value used in the computation
 * @param col the col parameter — a integer value used in the computation
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
 */
    private fun isSafe(row: Int, col: Int): Boolean {
        for (prevRow in 0 until row) {
            val prevCol = placed[prevRow]
            if (prevCol == col || Math.abs(prevRow - row) == Math.abs(prevCol - col)) {
                return false
            }
        }
        return true
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) |

---

## N Queen_II

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package backtracking

class NQueen_II {
    private lateinit var placed: IntArray

/**
 * Converts/transforms the input from one representation to another.
 *
 * @param n the size/dimension parameter for the algorithm
 * @return the computed sum/total value
 */
    fun totalNQueens(n: Int): Int {
        placed = IntArray(n) { -1 } // Initialize with -1 indicating no queens are placed
        var solutionCount = 0

/**
 * backtrack — executes the core logic of this algorithm on the provided input.
 *
 * @param row the row parameter — a integer value used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
        fun backtrack(row: Int) {
            if (row == n) {
                // Found a valid solution, increment the count
                solutionCount++
                return
            }

            for (col in 0 until n) {
                if (isSafe(row, col)) {
                    placed[row] = col
                    backtrack(row + 1)
                    placed[row] = -1 // Remove the queen (backtrack)
                }
            }
        }

        backtrack(0)
        return solutionCount
    }

/**
 * is Safe — executes the core logic of this algorithm on the provided input.
 *
 * @param row the row parameter — a integer value used in the computation
 * @param col the col parameter — a integer value used in the computation
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
 */
    private fun isSafe(row: Int, col: Int): Boolean {
        for (prevRow in 0 until row) {
            val prevCol = placed[prevRow]
            if (prevCol == col || Math.abs(prevRow - row) == Math.abs(prevCol - col)) {
                return false
            }
        }
        return true
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) |

---

## Palindrome Partitioning

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package backtracking

class PalindromePartitioning {

/**
 * partition — executes the core logic of this algorithm on the provided input.
 *
 * @param s the input string to process
 * @return a list/collection of result elements
 */
    fun partition(s: String): List<List<String>> {
        val result = mutableListOf<List<String>>()

/**
 * is Palindrome — executes the core logic of this algorithm on the provided input.
 *
 * @param s the input string to process
 * @param left the left/starting boundary of the search range (inclusive)
 * @param right the right/ending boundary of the search range (inclusive)
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
 */
        fun isPalindrome(s: String, left: Int, right: Int): Boolean {
            var (l, r) = left to right
            while (l < r) {
                if (s[l++] != s[r--]) return false
            }
            return true
        }

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param start the left/starting boundary of the search range (inclusive)
 * @param path the path parameter — a list of strings used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
        fun dfs(start: Int, path: MutableList<String>) {
            if (start == s.length) {
                result.add(ArrayList(path))
                return
            }
            for (end in start until s.length) {
                if (isPalindrome(s, start, end)) {
                    path.add(s.substring(start, end + 1))
                    dfs(end + 1, path)
                    path.removeAt(path.size - 1)
                }
            }
        }

        dfs(0, mutableListOf())
        return result
    }
}

```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) or O(n²) |
| **Space** | O(1) or O(n) |

---

## Partition To K Equal Sum Subsets

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package backtracking

class PartitionToKEqualSumSubsets {

/**
 * Checks whether the specified condition holds true for the given input.
 *
 * @param nums the input array of numbers to process
 * @param k the number of elements/operations to consider (k parameter)
 * @return `true` if the condition/constraint is satisfied, `false` otherwise
 */
    fun canPartitionKSubsets(nums: IntArray, k: Int): Boolean {
        val totalSum = nums.sum()
        if (totalSum % k !=0) return false

        val targetSum = totalSum / k
        val used = BooleanArray(nums.size)

/**
 * backtrack — executes the core logic of this algorithm on the provided input.
 *
 * @param start the left/starting boundary of the search range (inclusive)
 * @param currentSum the currentSum parameter — a integer value used in the computation
 * @param remainingSubsets the remainingSubsets parameter — a integer value used in the computation
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
 */
        fun backtrack(start: Int, currentSum: Int, remainingSubsets: Int): Boolean {
            if (remainingSubsets == 0)
                return true
            if (currentSum == targetSum)
                return backtrack(0, 0, remainingSubsets - 1)

            for(i in start until nums.size) {
                if (!used[i] && currentSum + nums[i] <= targetSum) {
                    used[i] = true
                    if (backtrack(i + 1, currentSum + nums[i], remainingSubsets))
                        return true
                    // backtracking
                    used[i] = false
                }
            }

            return false
        }

        return backtrack(0, 0, k)
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) |

---

## Restore IP Addresses

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package backtracking

class RestoreIPAddresses {

/**
 * Inserts the specified element into the data structure.
 *
 * @param s the input string to process
 * @return a list/collection of result elements
 */
    fun restoreIpAddresses(s: String): List<String> {
        val result = mutableListOf<String>()

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param i the index position in the collection
 * @param path the path parameter — a list of strings used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
        fun dfs(i: Int, path: MutableList<String>) {
            if (path.size == 4) {
                if (i == s.length) {
                    result.add(path.joinToString("."))
                }
                return
            }

            for (len in 1..3) {
                if (i + len <= s.length) {
                    val segment = s.substring(i, i + len)
                    // Skip invalid segments
                    if ((segment.length > 1 && segment[0] == '0') || segment.toInt() > 255) continue
                    path.add(segment)
                    dfs(i + len, path)
                    path.removeAt(path.size - 1)
                }
            }
        }

        dfs(0, mutableListOf())
        return result
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Subsets

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.Combinatorics

class Subsets {

/**
 * Updates the data structure with the provided value at the specified location.
 *
 * @param nums the input array of numbers to process
 * @return a list/collection of result elements
 */
    fun subsets(nums: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val currentSubset = mutableListOf<Int>()

        // Backtracking helper function

/**
 * backtrack — executes the core logic of this algorithm on the provided input.
 *
 * @param start the left/starting boundary of the search range (inclusive)
 * @return Unit (nothing) — this function operates via side effects
 */
        fun backtrack(start: Int) {
            result.add(ArrayList(currentSubset))  // Add the current subset to the result

            for (i in start until nums.size) {
                currentSubset.add(nums[i])         // Include nums[i] in the current subset
                backtrack(i + 1)                   // Recurse for the next elements
                currentSubset.removeAt(currentSubset.size - 1)  // Backtrack: remove last added element
            }
        }

        // Start the backtracking process from index 0
        backtrack(0)

        return result
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) |

---

## Sudoku Solver

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package backtracking

class SudokuSolver {

/**
 * Performs the core computation/algorithm and returns the result.
 *
 * @param board the 2D matrix/grid to traverse or process
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
 */
    fun solveSudoku(board: Array<CharArray>) {
        solve(board)
    }

/**
 * Performs the core computation/algorithm and returns the result.
 *
 * @param board the 2D matrix/grid to traverse or process
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
 */
    private fun solve(board: Array<CharArray>): Boolean {
        for (row in 0..8) {
            for (col in 0..8) {
                if (board[row][col] == '.') {
                    for (ch in '1'..'9') {
                        if (isValid(board, row, col, ch)) {
                            board[row][col] = ch
                            if (solve(board)) return true
                            board[row][col] = '.' // backtrack
                        }
                    }
                    return false // no valid number found
                }
            }
        }
        return true // board solved
    }

/**
 * Checks whether the specified condition holds true for the given input.
 *
 * @param board the 2D matrix/grid to traverse or process
 * @param row the row parameter — a integer value used in the computation
 * @param col the col parameter — a integer value used in the computation
 * @param ch the ch parameter — a input parameter of type Char used in the computation
 * @return `true` if the condition/constraint is satisfied, `false` otherwise
 */
    private fun isValid(board: Array<CharArray>, row: Int, col: Int, ch: Char): Boolean {
        for (i in 0..8) {
            if (board[row][i] == ch || board[i][col] == ch) return false
            val boxRow = 3 * (row / 3) + i / 3
            val boxCol = 3 * (col / 3) + i % 3
            if (board[boxRow][boxCol] == ch) return false
        }
        return true
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) |

---

## Sudoku Solver Set

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package backtracking

class SudokuSolverSet {

/**
 * Performs the core computation/algorithm and returns the result.
 *
 * @param board the 2D matrix/grid to traverse or process
 * @return Unit (nothing) — this function operates via side effects
 */
    fun solveSudoku(board: Array<CharArray>) {
        val seen = mutableSetOf<String>()

        // Add initial values to the seen set
        for (i in 0..8) {
            for (j in 0..8) {
                val ch = board[i][j]
                if (ch != '.') {
                    addToSet(i, j, ch, seen)
                }
            }
        }

/**
 * is Safe — executes the core logic of this algorithm on the provided input.
 *
 * @param i the index position in the collection
 * @param j the index position in the collection
 * @param c the c parameter — a input parameter of type Char used in the computation
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
 */
        fun isSafe(i: Int, j: Int, c: Char): Boolean {
            return "$c row $i" !in seen &&
                    "$c col $j" !in seen &&
                    "$c block ${i / 3}${j / 3}" !in seen
        }

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
 */
        fun dfs(): Boolean {
            for (i in 0..8) {
                for (j in 0..8) {
                    if (board[i][j] != '.') continue
                    for (c in '1'..'9') {
                        if (!isSafe(i, j, c)) continue
                        board[i][j] = c
                        addToSet(i, j, c, seen)
                        if (dfs()) return true
                        board[i][j] = '.'
                        removeFromSet(i, j, c, seen)
                    }
                    return false
                }
            }
            return true
        }

        dfs()
    }

/**
 * Inserts the specified element into the data structure.
 *
 * @param i the index position in the collection
 * @param j the index position in the collection
 * @param c the c parameter — a input parameter of type Char used in the computation
 * @param seen the seen parameter — a set of elements used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
    fun addToSet(i: Int, j: Int, c: Char, seen: MutableSet<String>) {
        seen.add("$c row $i")
        seen.add("$c col $j")
        seen.add("$c block ${i / 3}${j / 3}")
    }

/**
 * Removes specified elements from the collection and returns the result.
 *
 * @param i the index position in the collection
 * @param j the index position in the collection
 * @param c the c parameter — a input parameter of type Char used in the computation
 * @param seen the seen parameter — a set of elements used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
    fun removeFromSet(i: Int, j: Int, c: Char, seen: MutableSet<String>) {
        seen.remove("$c row $i")
        seen.remove("$c col $j")
        seen.remove("$c block ${i / 3}${j / 3}")
    }
}

```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) |

---

## Key Takeaways

1. **Core pattern recognition** — Identify the problem type and apply the right algorithmic technique.
2. **Practice systematically** — Work through each problem to internalize the patterns.
3. **Understand why, not just how** — Focus on the reasoning behind each solution.

---

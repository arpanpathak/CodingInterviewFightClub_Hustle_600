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

> **13 problems**

## The Pattern

_Each problem below includes: Problem, Example, Why This Approach, Code, Pattern Insight, Complexity, and Variations._

## Problems

1. [Combinations](#combinations)
2. [Combination Sum](#combinationsum)
3. [Combination Sum_II](#combinationsum_ii)
4. [Combination Sum3](#combinationsum3)
5. [Expression And Add Operators](#expressionandaddoperators)
6. [N Queen](#nqueen)
7. [N Queen_II](#nqueen_ii)
8. [Palindrome Partitioning](#palindromepartitioning)
9. [Partition To K Equal Sum Subsets](#partitiontokequalsumsubsets)
10. [Restore IP Addresses](#restoreipaddresses)
11. [Strobogrammatic_Number_II](#strobogrammatic_number_ii)
12. [Subsets](#subsets)
13. [Sudoku Solver](#sudokusolver)

---

## Combinations

### Problem

Given `n` (integer), `k` (integer), `start` (integer), `current` (MutableList<Int> = mutableListOf(), compute the computed result efficiently.

**Example:**

```
Input: n = 5, k = 5, start = 5, current = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package array.Combinatorics

class Combinations {
    /**
    * Solves the Combinations problem.
    * Takes `n` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Combinations problem.
    * Takes `n` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Combinations problem.
    * Takes `n` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Combinations problem.
    * Takes `n` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    fun combine(n: Int, k: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()

        /**
        * Solves the Combinations problem.
        * Takes `n` (integer), `k` (integer).
        *
        * @param n The integer parameter representing n.
        * @param k The integer parameter representing k.
        * @return The computed integer result.
        */
        /**
        * Solves the Combinations problem.
        * Takes `n` (integer), `k` (integer).
        *
        * @param n The integer parameter representing n.
        * @param k The integer parameter representing k.
        * @return The computed integer result.
        */
        /**
        * Solves the Combinations problem.
        * Takes `n` (integer), `k` (integer).
        *
        * @param n The integer parameter representing n.
        * @param k The integer parameter representing k.
        * @return The computed integer result.
        */
        /**
        * Solves the Combinations problem.
        * Takes `n` (integer), `k` (integer).
        *
        * @param n The integer parameter representing n.
        * @param k The integer parameter representing k.
        * @return The computed integer result.
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

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Combination Sum

### Problem

Given `candidates` (array of integers), `target` (integer), `current` (list of integers), `start` (integer), `remaining` (integer), compute the computed result efficiently.

**Example:**

```
Input: candidates = [1, 2, 3, 4, 5], target = 5, current = [1, 2, 3, 4, 5], start = 5, remaining = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package array.backtracking

class CombinationSum {
    /**
    * Solves the Combination Sum problem.
    * Takes `candidates` (array of integers), `target` (integer).
    *
    * @param candidates The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Combination Sum problem.
    * Takes `candidates` (array of integers), `target` (integer).
    *
    * @param candidates The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Combination Sum problem.
    * Takes `candidates` (array of integers), `target` (integer).
    *
    * @param candidates The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Combination Sum problem.
    * Takes `candidates` (array of integers), `target` (integer).
    *
    * @param candidates The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()

        /**
        * Solves the Combination Sum problem.
        * Takes `current` (mutable list of integers), `start` (integer), `remaining` (integer).
        *
        * @param current The input mutable list of integers.
        * @param start The integer parameter representing start.
        * @param remaining The integer parameter representing remaining.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Combination Sum problem.
        * Takes `current` (mutable list of integers), `start` (integer), `remaining` (integer).
        *
        * @param current The input mutable list of integers.
        * @param start The integer parameter representing start.
        * @param remaining The integer parameter representing remaining.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Combination Sum problem.
        * Takes `current` (mutable list of integers), `start` (integer), `remaining` (integer).
        *
        * @param current The input mutable list of integers.
        * @param start The integer parameter representing start.
        * @param remaining The integer parameter representing remaining.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Combination Sum problem.
        * Takes `current` (mutable list of integers), `start` (integer), `remaining` (integer).
        *
        * @param current The input mutable list of integers.
        * @param start The integer parameter representing start.
        * @param remaining The integer parameter representing remaining.
        * @return Unit (no return value, modifies state in-place).
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

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Combination Sum_II

### Problem

Given `candidates` (array of integers), `target` (integer), `index` (integer), `curr` (list of integers), compute the computed result efficiently.

**Example:**

```
Input: candidates = [1, 2, 3, 4, 5], target = 5, index = 5, curr = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package array.backtracking

class CombinationSum_II {
    /**
    * Solves the Combination Sum_II problem.
    * Takes `candidates` (array of integers), `target` (integer).
    *
    * @param candidates The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Combination Sum_II problem.
    * Takes `candidates` (array of integers), `target` (integer).
    *
    * @param candidates The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Combination Sum_II problem.
    * Takes `candidates` (array of integers), `target` (integer).
    *
    * @param candidates The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Combination Sum_II problem.
    * Takes `candidates` (array of integers), `target` (integer).
    *
    * @param candidates The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    fun combinationSum2(candidates: IntArray, target: Int): List<List<Int>> {
        val results = mutableListOf<List<Int>>()
        candidates.sort()

        /**
        * Solves the Combination Sum_II problem.
        * Takes `index` (integer), `target` (integer), `curr` (mutable list of integers).
        *
        * @param index The integer parameter representing index.
        * @param target The integer parameter representing target.
        * @param curr The input mutable list of integers.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Combination Sum_II problem.
        * Takes `index` (integer), `target` (integer), `curr` (mutable list of integers).
        *
        * @param index The integer parameter representing index.
        * @param target The integer parameter representing target.
        * @param curr The input mutable list of integers.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Combination Sum_II problem.
        * Takes `index` (integer), `target` (integer), `curr` (mutable list of integers).
        *
        * @param index The integer parameter representing index.
        * @param target The integer parameter representing target.
        * @param curr The input mutable list of integers.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Combination Sum_II problem.
        * Takes `index` (integer), `target` (integer), `curr` (mutable list of integers).
        *
        * @param index The integer parameter representing index.
        * @param target The integer parameter representing target.
        * @param curr The input mutable list of integers.
        * @return Unit (no return value, modifies state in-place).
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

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Combination Sum3

### Problem

Given `k` (integer), `n` (integer), `remaining` (integer), `start` (integer), `result` (MutableList<List<Int>>), `curr` (MutableList<Int> = mutableListOf(), compute the computed result efficiently.

**Example:**

```
Input: k = 5, n = 5, remaining = 5, start = 5, result = input_value, curr = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package array.backtracking

class CombinationSum3 {
    /**
    * Solves the Combination Sum3 problem.
    * Takes `k` (integer), `n` (integer).
    *
    * @param k The integer parameter representing k.
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Combination Sum3 problem.
    * Takes `k` (integer), `n` (integer).
    *
    * @param k The integer parameter representing k.
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Combination Sum3 problem.
    * Takes `k` (integer), `n` (integer).
    *
    * @param k The integer parameter representing k.
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Combination Sum3 problem.
    * Takes `k` (integer), `n` (integer).
    *
    * @param k The integer parameter representing k.
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    fun combinationSum3(k: Int, n: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        dfs(k,n, 1, result)
        return result
    }

    /**
    * Solves the Combination Sum3 problem.
    * Takes `k` (integer), `remaining` (integer), `start` (integer), `result` (MutableList<List<Int>>), `curr` (MutableList<Int> = mutableListOf().
    *
    * @param k The integer parameter representing k.
    * @param remaining The integer parameter representing remaining.
    * @param start The integer parameter representing start.
    * @param result The input MutableList<List<Int>>.
    * @param curr The input MutableList<Int> = mutableListOf(.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Combination Sum3 problem.
    * Takes `k` (integer), `remaining` (integer), `start` (integer), `result` (MutableList<List<Int>>), `curr` (MutableList<Int> = mutableListOf().
    *
    * @param k The integer parameter representing k.
    * @param remaining The integer parameter representing remaining.
    * @param start The integer parameter representing start.
    * @param result The input MutableList<List<Int>>.
    * @param curr The input MutableList<Int> = mutableListOf(.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Combination Sum3 problem.
    * Takes `k` (integer), `remaining` (integer), `start` (integer), `result` (MutableList<List<Int>>), `curr` (MutableList<Int> = mutableListOf().
    *
    * @param k The integer parameter representing k.
    * @param remaining The integer parameter representing remaining.
    * @param start The integer parameter representing start.
    * @param result The input MutableList<List<Int>>.
    * @param curr The input MutableList<Int> = mutableListOf(.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Combination Sum3 problem.
    * Takes `k` (integer), `remaining` (integer), `start` (integer), `result` (MutableList<List<Int>>), `curr` (MutableList<Int> = mutableListOf().
    *
    * @param k The integer parameter representing k.
    * @param remaining The integer parameter representing remaining.
    * @param start The integer parameter representing start.
    * @param result The input MutableList<List<Int>>.
    * @param curr The input MutableList<Int> = mutableListOf(.
    * @return Unit (no return value, modifies state in-place).
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

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Expression And Add Operators

### Problem

Given `num` (string), `target` (integer), `index` (integer), `prevOperand` (long integer), `currentOperand` (long integer), `value` (long integer), `expression` (string), `start` (integer), `path` (string), `sum` (long integer), `prev` (long integer), `args` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: num = "example", target = 5, index = 5, prevOperand = 5, currentOperand = 5, value = 5, expression = "example", start = 5, path = "example", sum = 5, prev = 5, args = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package backtracking

class ExpressionAndAddOperators {
    /**
    * Solves the Expression And Add Operators problem.
    * Takes `num` (string), `target` (integer).
    *
    * @param num The input string.
    * @param target The integer parameter representing target.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Expression And Add Operators problem.
    * Takes `num` (string), `target` (integer).
    *
    * @param num The input string.
    * @param target The integer parameter representing target.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Expression And Add Operators problem.
    * Takes `num` (string), `target` (integer).
    *
    * @param num The input string.
    * @param target The integer parameter representing target.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Expression And Add Operators problem.
    * Takes `num` (string), `target` (integer).
    *
    * @param num The input string.
    * @param target The integer parameter representing target.
    * @return The resulting collection (list of strings).
    */
    fun addOperators(num: String, target: Int): List<String> {
        val result = mutableListOf<String>()

        /**
        * Solves the Expression And Add Operators problem.
        * Takes `index` (integer), `prevOperand` (long integer), `currentOperand` (long integer), `value` (long integer), `expression` (string).
        *
        * @param index The integer parameter representing index.
        * @param prevOperand The long integer parameter representing prevOperand.
        * @param currentOperand The long integer parameter representing currentOperand.
        * @param value The long integer parameter representing value.
        * @param expression The input string.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Expression And Add Operators problem.
        * Takes `index` (integer), `prevOperand` (long integer), `currentOperand` (long integer), `value` (long integer), `expression` (string).
        *
        * @param index The integer parameter representing index.
        * @param prevOperand The long integer parameter representing prevOperand.
        * @param currentOperand The long integer parameter representing currentOperand.
        * @param value The long integer parameter representing value.
        * @param expression The input string.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Expression And Add Operators problem.
        * Takes `index` (integer), `prevOperand` (long integer), `currentOperand` (long integer), `value` (long integer), `expression` (string).
        *
        * @param index The integer parameter representing index.
        * @param prevOperand The long integer parameter representing prevOperand.
        * @param currentOperand The long integer parameter representing currentOperand.
        * @param value The long integer parameter representing value.
        * @param expression The input string.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Expression And Add Operators problem.
        * Takes `index` (integer), `prevOperand` (long integer), `currentOperand` (long integer), `value` (long integer), `expression` (string).
        *
        * @param index The integer parameter representing index.
        * @param prevOperand The long integer parameter representing prevOperand.
        * @param currentOperand The long integer parameter representing currentOperand.
        * @param value The long integer parameter representing value.
        * @param expression The input string.
        * @return Unit (no return value, modifies state in-place).
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
    * Solves the Expression And Add Operators problem.
    * Takes `num` (string), `target` (integer).
    *
    * @param num The input string.
    * @param target The integer parameter representing target.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Expression And Add Operators problem.
    * Takes `num` (string), `target` (integer).
    *
    * @param num The input string.
    * @param target The integer parameter representing target.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Expression And Add Operators problem.
    * Takes `num` (string), `target` (integer).
    *
    * @param num The input string.
    * @param target The integer parameter representing target.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Expression And Add Operators problem.
    * Takes `num` (string), `target` (integer).
    *
    * @param num The input string.
    * @param target The integer parameter representing target.
    * @return The resulting collection (list of strings).
    */
    fun addOperators2(num: String, target: Int): List<String> {
        val res = ArrayList<String>()

        /**
        * Solves the Expression And Add Operators problem.
        * Takes `start` (integer), `path` (string), `sum` (long integer), `prev` (long integer).
        *
        * @param start The integer parameter representing start.
        * @param path The input string.
        * @param sum The long integer parameter representing sum.
        * @param prev The long integer parameter representing prev.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Expression And Add Operators problem.
        * Takes `start` (integer), `path` (string), `sum` (long integer), `prev` (long integer).
        *
        * @param start The integer parameter representing start.
        * @param path The input string.
        * @param sum The long integer parameter representing sum.
        * @param prev The long integer parameter representing prev.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Expression And Add Operators problem.
        * Takes `start` (integer), `path` (string), `sum` (long integer), `prev` (long integer).
        *
        * @param start The integer parameter representing start.
        * @param path The input string.
        * @param sum The long integer parameter representing sum.
        * @param prev The long integer parameter representing prev.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Expression And Add Operators problem.
        * Takes `start` (integer), `path` (string), `sum` (long integer), `prev` (long integer).
        *
        * @param start The integer parameter representing start.
        * @param path The input string.
        * @param sum The long integer parameter representing sum.
        * @param prev The long integer parameter representing prev.
        * @return Unit (no return value, modifies state in-place).
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
* Entry point for the program.
*
* @param args The input Array<String>.
* @return Unit (no return value, modifies state in-place).
*/
/**
* Entry point for the program.
*
* @param args The input Array<String>.
* @return Unit (no return value, modifies state in-place).
*/
/**
* Entry point for the program.
*
* @param args The input Array<String>.
* @return Unit (no return value, modifies state in-place).
*/
/**
* Entry point for the program.
*
* @param args The input Array<String>.
* @return Unit (no return value, modifies state in-place).
*/
fun main(args: Array<String>) {
    val test = ExpressionAndAddOperators()

    println(test.addOperators("1310", 130))
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## N Queen

### Problem

Given `n` (integer), `row` (integer), `col` (integer), compute the computed result efficiently.

**Example:**

```
Input: n = 5, row = 5, col = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **backtracking** — a systematic way to explore all possible solutions. At each step, try a valid option, recurse, then undo the choice (backtrack). Pruning invalid branches early is key to performance.

### Code

```kotlin
package backtracking

import javax.swing.text.html.HTML.Attribute.N

class NQueen {
    private lateinit var placed: IntArray

    /**
    * Solves the NQueen problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting collection (List<List<String>).
    */
    /**
    * Solves the NQueen problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting collection (List<List<String>).
    */
    /**
    * Solves the NQueen problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting collection (List<List<String>).
    */
    /**
    * Solves the NQueen problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting collection (List<List<String>).
    */
    fun solveNQueens(n: Int): List<List<String>> {
        val results = mutableListOf<List<String>>()
        placed = IntArray(n) { -1 } // Initialize with -1 indicating no queens are placed

        /**
        * Solves the NQueen problem.
        * Takes `row` (integer).
        *
        * @param row The integer parameter representing row.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the NQueen problem.
        * Takes `row` (integer).
        *
        * @param row The integer parameter representing row.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the NQueen problem.
        * Takes `row` (integer).
        *
        * @param row The integer parameter representing row.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the NQueen problem.
        * Takes `row` (integer).
        *
        * @param row The integer parameter representing row.
        * @return Unit (no return value, modifies state in-place).
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
    * Helper: is safe.
    *
    * @param row The integer parameter representing row.
    * @param col The integer parameter representing col.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is safe.
    *
    * @param row The integer parameter representing row.
    * @param col The integer parameter representing col.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is safe.
    *
    * @param row The integer parameter representing row.
    * @param col The integer parameter representing col.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is safe.
    *
    * @param row The integer parameter representing row.
    * @param col The integer parameter representing col.
    * @return `true` if the condition is met, `false` otherwise.
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

### Pattern Insight

**Backtracking Pattern.** Explore decision space via DFS. At each step: try a valid option, recurse, undo. Prune aggressively — check validity before recursing, not after.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) for recursion stack |

### Variations

1. Can you prune more aggressively to improve performance?
1. What if the constraints are larger (e.g., 20x20 board instead of 8x8)?
1. Can this be solved with iterative approach instead of recursion?
1. What if you need to find ALL solutions vs ANY solution?
1. Can you use symmetry breaking to reduce search space?

---

## N Queen_II

### Problem

Given `n` (integer), `row` (integer), `col` (integer), compute the computed result efficiently.

**Example:**

```
Input: n = 5, row = 5, col = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **backtracking** — a systematic way to explore all possible solutions. At each step, try a valid option, recurse, then undo the choice (backtrack). Pruning invalid branches early is key to performance.

### Code

```kotlin
package backtracking

class NQueen_II {
    private lateinit var placed: IntArray

    /**
    * Solves the NQueen_II problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the NQueen_II problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the NQueen_II problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the NQueen_II problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    fun totalNQueens(n: Int): Int {
        placed = IntArray(n) { -1 } // Initialize with -1 indicating no queens are placed
        var solutionCount = 0

        /**
        * Solves the NQueen_II problem.
        * Takes `row` (integer).
        *
        * @param row The integer parameter representing row.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the NQueen_II problem.
        * Takes `row` (integer).
        *
        * @param row The integer parameter representing row.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the NQueen_II problem.
        * Takes `row` (integer).
        *
        * @param row The integer parameter representing row.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the NQueen_II problem.
        * Takes `row` (integer).
        *
        * @param row The integer parameter representing row.
        * @return Unit (no return value, modifies state in-place).
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
    * Helper: is safe.
    *
    * @param row The integer parameter representing row.
    * @param col The integer parameter representing col.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is safe.
    *
    * @param row The integer parameter representing row.
    * @param col The integer parameter representing col.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is safe.
    *
    * @param row The integer parameter representing row.
    * @param col The integer parameter representing col.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is safe.
    *
    * @param row The integer parameter representing row.
    * @param col The integer parameter representing col.
    * @return `true` if the condition is met, `false` otherwise.
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

### Pattern Insight

**Backtracking Pattern.** Explore decision space via DFS. At each step: try a valid option, recurse, undo. Prune aggressively — check validity before recursing, not after.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) for recursion stack |

### Variations

1. Can you prune more aggressively to improve performance?
1. What if the constraints are larger (e.g., 20x20 board instead of 8x8)?
1. Can this be solved with iterative approach instead of recursion?
1. What if you need to find ALL solutions vs ANY solution?
1. Can you use symmetry breaking to reduce search space?

---

## Palindrome Partitioning

### Problem

Given `s` (string), `left` (integer), `right` (integer), `start` (integer), `path` (MutableList<String>), compute the computed result efficiently.

**Example:**

```
Input: s = "example", left = 5, right = 5, start = 5, path = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package backtracking

class PalindromePartitioning {
    /**
    * Solves the Palindrome Partitioning problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting collection (List<List<String>).
    */
    /**
    * Solves the Palindrome Partitioning problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting collection (List<List<String>).
    */
    /**
    * Solves the Palindrome Partitioning problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting collection (List<List<String>).
    */
    /**
    * Solves the Palindrome Partitioning problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting collection (List<List<String>).
    */
    fun partition(s: String): List<List<String>> {
        val result = mutableListOf<List<String>>()

        /**
        * Solves the Palindrome Partitioning problem.
        * Takes `s` (string), `left` (integer), `right` (integer).
        *
        * @param s The input string.
        * @param left The integer parameter representing left.
        * @param right The integer parameter representing right.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Palindrome Partitioning problem.
        * Takes `s` (string), `left` (integer), `right` (integer).
        *
        * @param s The input string.
        * @param left The integer parameter representing left.
        * @param right The integer parameter representing right.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Palindrome Partitioning problem.
        * Takes `s` (string), `left` (integer), `right` (integer).
        *
        * @param s The input string.
        * @param left The integer parameter representing left.
        * @param right The integer parameter representing right.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Palindrome Partitioning problem.
        * Takes `s` (string), `left` (integer), `right` (integer).
        *
        * @param s The input string.
        * @param left The integer parameter representing left.
        * @param right The integer parameter representing right.
        * @return `true` if the condition is met, `false` otherwise.
        */
        fun isPalindrome(s: String, left: Int, right: Int): Boolean {
            var (l, r) = left to right
            while (l < r) {
                if (s[l++] != s[r--]) return false
            }
            return true
        }

        /**
        * Solves the Palindrome Partitioning problem.
        * Takes `start` (integer), `path` (MutableList<String>).
        *
        * @param start The integer parameter representing start.
        * @param path The input MutableList<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Palindrome Partitioning problem.
        * Takes `start` (integer), `path` (MutableList<String>).
        *
        * @param start The integer parameter representing start.
        * @param path The input MutableList<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Palindrome Partitioning problem.
        * Takes `start` (integer), `path` (MutableList<String>).
        *
        * @param start The integer parameter representing start.
        * @param path The input MutableList<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Palindrome Partitioning problem.
        * Takes `start` (integer), `path` (MutableList<String>).
        *
        * @param start The integer parameter representing start.
        * @param path The input MutableList<String>.
        * @return Unit (no return value, modifies state in-place).
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

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Partition To K Equal Sum Subsets

### Problem

Given `nums` (array of integers), `k` (integer), `start` (integer), `currentSum` (integer), `remainingSubsets` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], k = 5, start = 5, currentSum = 5, remainingSubsets = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package backtracking

class PartitionToKEqualSumSubsets {
    /**
    * Solves the Partition To KEqual Sum Subsets problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Partition To KEqual Sum Subsets problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Partition To KEqual Sum Subsets problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Partition To KEqual Sum Subsets problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun canPartitionKSubsets(nums: IntArray, k: Int): Boolean {
        val totalSum = nums.sum()
        if (totalSum % k !=0) return false

        val targetSum = totalSum / k
        val used = BooleanArray(nums.size)

        /**
        * Solves the Partition To KEqual Sum Subsets problem.
        * Takes `start` (integer), `currentSum` (integer), `remainingSubsets` (integer).
        *
        * @param start The integer parameter representing start.
        * @param currentSum The integer parameter representing currentSum.
        * @param remainingSubsets The integer parameter representing remainingSubsets.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Partition To KEqual Sum Subsets problem.
        * Takes `start` (integer), `currentSum` (integer), `remainingSubsets` (integer).
        *
        * @param start The integer parameter representing start.
        * @param currentSum The integer parameter representing currentSum.
        * @param remainingSubsets The integer parameter representing remainingSubsets.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Partition To KEqual Sum Subsets problem.
        * Takes `start` (integer), `currentSum` (integer), `remainingSubsets` (integer).
        *
        * @param start The integer parameter representing start.
        * @param currentSum The integer parameter representing currentSum.
        * @param remainingSubsets The integer parameter representing remainingSubsets.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Partition To KEqual Sum Subsets problem.
        * Takes `start` (integer), `currentSum` (integer), `remainingSubsets` (integer).
        *
        * @param start The integer parameter representing start.
        * @param currentSum The integer parameter representing currentSum.
        * @param remainingSubsets The integer parameter representing remainingSubsets.
        * @return `true` if the condition is met, `false` otherwise.
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

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Restore IP Addresses

### Problem

Given `s` (string), `i` (integer), `path` (MutableList<String>), compute the computed result efficiently.

**Example:**

```
Input: s = "example", i = 5, path = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package backtracking

class RestoreIPAddresses {
    /**
    * Solves the Restore IPAddresses problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Restore IPAddresses problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Restore IPAddresses problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Restore IPAddresses problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting collection (list of strings).
    */
    fun restoreIpAddresses(s: String): List<String> {
        val result = mutableListOf<String>()

        /**
        * Solves the Restore IPAddresses problem.
        * Takes `i` (integer), `path` (MutableList<String>).
        *
        * @param i The integer parameter representing i.
        * @param path The input MutableList<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Restore IPAddresses problem.
        * Takes `i` (integer), `path` (MutableList<String>).
        *
        * @param i The integer parameter representing i.
        * @param path The input MutableList<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Restore IPAddresses problem.
        * Takes `i` (integer), `path` (MutableList<String>).
        *
        * @param i The integer parameter representing i.
        * @param path The input MutableList<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Restore IPAddresses problem.
        * Takes `i` (integer), `path` (MutableList<String>).
        *
        * @param i The integer parameter representing i.
        * @param path The input MutableList<String>.
        * @return Unit (no return value, modifies state in-place).
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

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Strobogrammatic_Number_II

### Problem

Given `n` (integer), `currentLength` (integer), compute the computed result efficiently.

**Example:**

```
Input: n = 5, currentLength = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package backtracking

class Strobogrammatic_Number_II {
    /**
    * Solves the Strobogrammatic_Number_II problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Strobogrammatic_Number_II problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Strobogrammatic_Number_II problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Strobogrammatic_Number_II problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting collection (list of strings).
    */
    fun findStrobogrammatic(n: Int): List<String> {
        val pairs = listOf("0" to "0", "1" to "1", "6" to "9", "8" to "8", "9" to "6")
        /**
        * Solves the Strobogrammatic_Number_II problem.
        * Takes `currentLength` (integer).
        *
        * @param currentLength The integer parameter representing currentLength.
        * @return The resulting collection (list of strings).
        */
        /**
        * Solves the Strobogrammatic_Number_II problem.
        * Takes `currentLength` (integer).
        *
        * @param currentLength The integer parameter representing currentLength.
        * @return The resulting collection (list of strings).
        */
        /**
        * Solves the Strobogrammatic_Number_II problem.
        * Takes `currentLength` (integer).
        *
        * @param currentLength The integer parameter representing currentLength.
        * @return The resulting collection (list of strings).
        */
        /**
        * Solves the Strobogrammatic_Number_II problem.
        * Takes `currentLength` (integer).
        *
        * @param currentLength The integer parameter representing currentLength.
        * @return The resulting collection (list of strings).
        */
        fun generateStrobogrammatic(currentLength: Int): List<String> {
            if (currentLength == 0) return listOf("")
            if (currentLength == 1) return listOf("0", "1", "8")

            val result = mutableListOf<String>()

            for ((left, right) in pairs) {
                // Avoid leading zeros
                if (currentLength == n && left == "0") continue

                // Generate the inner strobogrammatic numbers
                val innerNumbers = generateStrobogrammatic(currentLength - 2)

                // Append the current pair to the inner numbers
                for (inner in innerNumbers) {
                    result.add(left + inner + right)
                }
            }

            return result
        }

        return generateStrobogrammatic(n)
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Subsets

### Problem

Given `nums` (array of integers), `start` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], start = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package array.Combinatorics

class Subsets {
    /**
    * Solves the Subsets problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Subsets problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Subsets problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Subsets problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun subsets(nums: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val currentSubset = mutableListOf<Int>()

        // Backtracking helper function
        /**
        * Solves the Subsets problem.
        * Takes `start` (integer).
        *
        * @param start The integer parameter representing start.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Subsets problem.
        * Takes `start` (integer).
        *
        * @param start The integer parameter representing start.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Subsets problem.
        * Takes `start` (integer).
        *
        * @param start The integer parameter representing start.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Subsets problem.
        * Takes `start` (integer).
        *
        * @param start The integer parameter representing start.
        * @return Unit (no return value, modifies state in-place).
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

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Sudoku Solver

### Problem

Given `board` (Array<CharArray>), `row` (integer), `col` (integer), `ch` (Char), compute the computed result efficiently.

**Example:**

```
Input: board = input_value, row = 5, col = 5, ch = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses **backtracking** — a systematic way to explore all possible solutions. At each step, try a valid option, recurse, then undo the choice (backtrack). Pruning invalid branches early is key to performance.

### Code

```kotlin
package backtracking

class SudokuSolver {
    /**
    * Solves the Sudoku Solver problem.
    * Takes `board` (Array<CharArray>).
    *
    * @param board The input Array<CharArray>.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Sudoku Solver problem.
    * Takes `board` (Array<CharArray>).
    *
    * @param board The input Array<CharArray>.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Sudoku Solver problem.
    * Takes `board` (Array<CharArray>).
    *
    * @param board The input Array<CharArray>.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Sudoku Solver problem.
    * Takes `board` (Array<CharArray>).
    *
    * @param board The input Array<CharArray>.
    * @return Unit (no return value, modifies state in-place).
    */
    fun solveSudoku(board: Array<CharArray>) {
        solve(board)
    }

    /**
    * Helper: solve.
    *
    * @param board The input Array<CharArray>.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: solve.
    *
    * @param board The input Array<CharArray>.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: solve.
    *
    * @param board The input Array<CharArray>.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: solve.
    *
    * @param board The input Array<CharArray>.
    * @return `true` if the condition is met, `false` otherwise.
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
    * Helper: is valid.
    *
    * @param board The input Array<CharArray>.
    * @param row The integer parameter representing row.
    * @param col The integer parameter representing col.
    * @param ch The character.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is valid.
    *
    * @param board The input Array<CharArray>.
    * @param row The integer parameter representing row.
    * @param col The integer parameter representing col.
    * @param ch The character.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is valid.
    *
    * @param board The input Array<CharArray>.
    * @param row The integer parameter representing row.
    * @param col The integer parameter representing col.
    * @param ch The character.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is valid.
    *
    * @param board The input Array<CharArray>.
    * @param row The integer parameter representing row.
    * @param col The integer parameter representing col.
    * @param ch The character.
    * @return `true` if the condition is met, `false` otherwise.
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

### Pattern Insight

**Backtracking Pattern.** Explore decision space via DFS. At each step: try a valid option, recurse, undo. Prune aggressively — check validity before recursing, not after.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(branches^depth) |
| **Space** | O(depth) for recursion stack |

### Variations

1. Can you prune more aggressively to improve performance?
1. What if the constraints are larger (e.g., 20x20 board instead of 8x8)?
1. Can this be solved with iterative approach instead of recursion?
1. What if you need to find ALL solutions vs ANY solution?
1. Can you use symmetry breaking to reduce search space?

---

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

> **15 problems** — Master systematic exploration of decision spaces with pruning.

## The Pattern

Backtracking = DFS on decision tree + pruning. Generate all candidates, explore valid ones, backtrack when stuck.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [Combinations](#combinations) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Combination Sum](#combinationsum) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Combination Sum_II](#combinationsum_ii) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Combination Sum3](#combinationsum3) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [Expression And Add Operators](#expressionandaddoperators) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Expression And Add Operators Optimized](#expressionandaddoperatorsoptimized) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [N Queen](#nqueen) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [N Queen_II](#nqueen_ii) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Palindrome Partitioning](#palindromepartitioning) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Partition To K Equal Sum Subsets](#partitiontokequalsumsubsets) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [Restore IP Addresses](#restoreipaddresses) | — | <span class="badge badge-medium">Medium</span> |
| 12 | [Strobogrammatic_Number_II](#strobogrammatic_number_ii) | — | <span class="badge badge-medium">Medium</span> |
| 13 | [Subsets](#subsets) | — | <span class="badge badge-medium">Medium</span> |
| 14 | [Sudoku Solver](#sudokusolver) | — | <span class="badge badge-medium">Medium</span> |
| 15 | [Sudoku Solver Set](#sudokusolverset) | — | <span class="badge badge-medium">Medium</span> |

---

## Combinations

<span id="combinations"></span>

### Problem

**Combinations**

**Function:** `Combine` takes `n` (integer), `k` (integer) and returns **List**.



### Approach

**Solution Approach:**
1. The main function `combine` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`

### Code

{% include code-tabs-file.html problem="combinations" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Combination Sum

<span id="combinationsum"></span>

### Problem

**Combinationsum**

**Function:** `Combination Sum` takes `candidates` (array of integers), `target` (integer) and returns **List**.

**Key logic:**
- Include current candidate
- Exclude and move to next



### Approach

**Solution Approach:**
1. The main function `combinationSum` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`

**Execution flow:**
- Include current candidate
- Exclude and move to next

### Code

{% include code-tabs-file.html problem="combinationsum" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Combination Sum_II

<span id="combinationsum_ii"></span>

### Problem

**Combinationsum Ii**

**Function:** `Combination Sum2` takes `candidates` (array of integers), `target` (integer) and returns **List**.

**Key logic:**
- Skip duplicates
- Prune the search



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `results`

**Execution flow:**
- Skip duplicates
- Prune the search

### Code

{% include code-tabs-file.html problem="combinationsum_ii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Combination Sum3

<span id="combinationsum3"></span>

### Problem

**Combinationsum3**

**Function:** `Combination Sum3` takes `k` (integer), `n` (integer) and returns **List**.



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`

### Code

{% include code-tabs-file.html problem="combinationsum3" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Expression And Add Operators

<span id="expressionandaddoperators"></span>

### Problem

**Expressionandaddoperators**

**Function:** `Add Operators` takes `num` (string), `target` (integer) and returns **List**.

**Key logic:**
- Extending the current operand by one digit
- Avoid cases where numbers start with '0'
- No operator added, just extend the current operand
- Add '+'
- Add '-'



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `currentDigit`, `newOperand`, `currentOperand`, `res`, `s`, `current`, `test`

**Execution flow:**
- Extending the current operand by one digit
- Avoid cases where numbers start with '0'
- No operator added, just extend the current operand
- Skip numbers with leading zeros
- ANother leetcode solution https://leetcode.com/problems/expression-add-operators/discuss/951147/Kotlin-C%2B%2B%3A-O(n4n)-time-and-O(n)-time-with-backtracking

### Code

{% include code-tabs-file.html problem="expressionandaddoperators" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Expression And Add Operators Optimized

<span id="expressionandaddoperatorsoptimized"></span>

### Problem

**Expressionandaddoperatorsoptimized**

**Function:** `Add Operators` takes `num` (string), `target` (integer) and returns **List**.

**Key logic:**
- Skip invalid numbers with leading zeros
- Remember the length of the path before modification
- Revert the path to its previous state
- Try adding '+' operator
- Try adding '-' operator



### Approach

**Solution Approach:**
1. The main function `addOperators` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `res`, `s`, `current`, `len`

**Execution flow:**
- Skip invalid numbers with leading zeros
- Remember the length of the path before modification
- Revert the path to its previous state
- Try adding '+' operator
- Try adding '-' operator
- Try adding '*' operator

### Code

{% include code-tabs-file.html problem="expressionandaddoperatorsoptimized" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## N Queen

<span id="nqueen"></span>

### Problem

**Nqueen**

**Function:** `Solve Nqueens` takes `n` (integer) and returns **List**.

**Key logic:**
- Initialize with -1 indicating no queens are placed
- Convert the board configuration to the required output format
- Remove the queen (backtrack)



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `placed`, `results`, `board`, `prevCol`

**Execution flow:**
- Initialize with -1 indicating no queens are placed
- Convert the board configuration to the required output format
- Remove the queen (backtrack)

### Code

{% include code-tabs-file.html problem="nqueen" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## N Queen_II

<span id="nqueen_ii"></span>

### Problem

**Nqueen Ii**

**Function:** `Total Nqueens` takes `n` (integer) and returns **integer**.

**Key logic:**
- Initialize with -1 indicating no queens are placed
- Found a valid solution, increment the count
- Remove the queen (backtrack)



### Approach

**Solution Approach:**
1. The main function `totalNQueens` processes the input
2. Uses helper functions: isSafe

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `placed`, `solutionCount`, `prevCol`

**Execution flow:**
- Initialize with -1 indicating no queens are placed
- Found a valid solution, increment the count
- Remove the queen (backtrack)

### Code

{% include code-tabs-file.html problem="nqueen_ii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Palindrome Partitioning

<span id="palindromepartitioning"></span>

### Problem

**Palindromepartitioning**

**Function:** `Partition` takes `s` (string) and returns **List**.



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`

### Code

{% include code-tabs-file.html problem="palindromepartitioning" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Partition To K Equal Sum Subsets

<span id="partitiontokequalsumsubsets"></span>

### Problem

**Partitiontokequalsumsubsets**

**Function:** `Can Partition Ksubsets` takes `nums` (array of integers), `k` (integer) and returns **boolean**.

**Key logic:**
- backtracking



### Approach

**Solution Approach:**
1. The main function `canPartitionKSubsets` processes the input
2. Uses helper functions: backtrack

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `totalSum`, `targetSum`, `used`

**Execution flow:**
- backtracking

### Code

{% include code-tabs-file.html problem="partitiontokequalsumsubsets" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Restore IP Addresses

<span id="restoreipaddresses"></span>

### Problem

**Restoreipaddresses**

**Function:** `Restore Ip Addresses` takes `s` (string) and returns **List**.

**Key logic:**
- Skip invalid segments



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `segment`

**Execution flow:**
- Skip invalid segments

### Code

{% include code-tabs-file.html problem="restoreipaddresses" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Strobogrammatic_Number_II

<span id="strobogrammatic_number_ii"></span>

### Problem

**Strobogrammatic Number Ii**

**Function:** `Find Strobogrammatic` takes `n` (integer) and returns **List**.

**Key logic:**
- Avoid leading zeros
- Generate the inner strobogrammatic numbers
- Append the current pair to the inner numbers



### Approach

**Solution Approach:**
1. The main function `findStrobogrammatic` processes the input
2. Uses helper functions: generateStrobogrammatic

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `pairs`, `result`, `innerNumbers`

**Execution flow:**
- Avoid leading zeros
- Generate the inner strobogrammatic numbers
- Append the current pair to the inner numbers

### Code

{% include code-tabs-file.html problem="strobogrammatic_number_ii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Subsets

<span id="subsets"></span>

### Problem

**Subsets**

**Function:** `Subsets` takes `nums` (array of integers) and returns **List**.

**Key logic:**
- Backtracking helper function
- Add the current subset to the result
- Include nums[i] in the current subset
- Recurse for the next elements
- Backtrack: remove last added element



### Approach

**Solution Approach:**
1. The main function `subsets` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `currentSubset`

**Execution flow:**
- Backtracking helper function
- Add the current subset to the result
- Include nums[i] in the current subset
- Recurse for the next elements
- Backtrack: remove last added element
- Start the backtracking process from index 0

### Code

{% include code-tabs-file.html problem="subsets" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Sudoku Solver

<span id="sudokusolver"></span>

### Problem

**Sudokusolver**

**Function:** `Solve` takes `board` (Array<CharArray>) and returns **boolean**.

**Key logic:**
- backtrack
- no valid number found
- board solved



### Approach

**Solution Approach:**
1. The main function `solve` processes the input
2. Uses helper functions: isValid

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `boxRow`, `boxCol`

**Execution flow:**
- no valid number found
- board solved

### Code

{% include code-tabs-file.html problem="sudokusolver" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Sudoku Solver Set

<span id="sudokusolverset"></span>

### Problem

**Sudokusolverset**

**Function:** `Is Safe` takes `i` (integer), `j` (integer), `c` (Char) and returns **boolean**.

**Key logic:**
- Add initial values to the seen set



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `seen`, `ch`

**Execution flow:**
- Add initial values to the seen set

### Code

{% include code-tabs-file.html problem="sudokusolverset" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Key Takeaways

1. **Core pattern recognition** — Backtracking = DFS on decision tree + pruning. Generate all candidates, explore valid ones, backtrack when stuck.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

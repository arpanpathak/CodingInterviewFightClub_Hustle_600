---
layout: chapter
title: "Dynamic Programming"
chapter_number: 2
chapter_title: "Dynamic Programming"
toc: true
prev_chapter:
  url: "/chapters/01-binary-search.html"
  title: "Binary Search"
next_chapter:
  url: "/chapters/03-arrays-two-pointers.html"
  title: "Arrays & Two Pointers"
---

# Dynamic Programming

> **21 problems** — Master optimal substructure and overlapping subproblems. DP solves complex problems by breaking them into simpler subproblems.

## The Pattern

Optimal substructure + overlapping subproblems → DP. Identify states, define transitions, compute bottom-up or top-down with memoization.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [Closest Subsequence Sum](#closestsubsequencesum) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Maximumproductsubarray](#maximumproductsubarray) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Maximum Profit In Job Scheduling](#maximumprofitinjobscheduling) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Partition Equal Subset Sum](#partitionequalsubsetsum) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [Super Egg Dropping](#supereggdropping) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Burst Baloons](#burstbaloons) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [House Robber](#houserobber) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [House Robber_II](#houserobber_ii) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Coin Change](#coinchange) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Coin Change_II](#coinchange_ii) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [Coin Change_II_Bottom Up](#coinchange_ii_bottomup) | — | <span class="badge badge-medium">Medium</span> |
| 12 | [Longest Increasing Subsequence](#longestincreasingsubsequence) | — | <span class="badge badge-medium">Medium</span> |
| 13 | [Maximal Square](#maximalsquare) | — | <span class="badge badge-medium">Medium</span> |
| 14 | [Maximum Sum Sub Array](#maximumsumsubarray) | — | <span class="badge badge-medium">Medium</span> |
| 15 | [Min Cost Climbing Staris](#mincostclimbingstaris) | — | <span class="badge badge-medium">Medium</span> |
| 16 | [Minimum Path Sum](#minimumpathsum) | — | <span class="badge badge-medium">Medium</span> |
| 17 | [Split Array Largest Sum](#splitarraylargestsum) | — | <span class="badge badge-medium">Medium</span> |
| 18 | [Target Sum](#targetsum) | — | <span class="badge badge-medium">Medium</span> |
| 19 | [Longest Increasing Sequence In A Matrix](#longestincreasingsequenceinamatrix) | — | <span class="badge badge-medium">Medium</span> |
| 20 | [Minimum Numberof Increments Subarrays Forma Target Array](#minimumnumberofincrementssubarraysformatargetarray) | — | <span class="badge badge-medium">Medium</span> |
| 21 | [Partition Array Into Two Array To Minimuze Sum Difference](#partitionarrayintotwoarraytominimuzesumdifference) | — | <span class="badge badge-medium">Medium</span> |

---

## Closest Subsequence Sum

<span id="closestsubsequencesum"></span>

### Problem

**Closestsubsequencesum**

**Function:** `Min Abs Difference` takes `nums` (array of integers), `goal` (integer) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `minAbsDifference` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `possibleSums`, `newSums`, `minDiff`

### Code

{% include code-tabs-file.html problem="closestsubsequencesum" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Maximumproductsubarray

<span id="maximumproductsubarray"></span>

### Problem

**Maximumproductsubarray**

**Function:** `Max Product` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Edge case: empty array
- Initialize trackers with first element
- Tracks maximum product ending at current position
- Tracks minimum product ending at current position (for negative numbers)
- Stores the overall maximum product found



### Approach

**Solution Approach:**
1. The main function `maxProduct` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `m`, `maxSoFar`, `minSoFar`, `result`, `currentNum`, `tempMax`, `tests`, `output`

**Execution flow:**
- Edge case: empty array
- Initialize trackers with first element
- Tracks maximum product ending at current position
- Tracks minimum product ending at current position (for negative numbers)
- Stores the overall maximum product found
- Calculate new maximum product ending at current position:
- 1. currentNum alone (start new subarray)
- 2. currentNum * previous max (extend positive product)

### Code

{% include code-tabs-file.html problem="maximumproductsubarray" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Maximum Profit In Job Scheduling

<span id="maximumprofitinjobscheduling"></span>

### Problem

**Maximumprofitinjobscheduling**

**Function:** `Job Scheduling` takes `startTime` (array of integers), `endTime` (array of integers), `profit` (array of integers) and returns **integer**.

**Key logic:**
- Create a list of jobs and sort them by end time
- Initialize dp array
- Profit if the current job is not included
- Find the last non-overlapping job
- Profit if the current job is included



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `start`, `end`, `profit`, `jobs`, `dp`, `prevJobIndex`, `currentProfit`, `currentJob`

**Execution flow:**
- Create a list of jobs and sort them by end time
- Initialize dp array
- Profit if the current job is not included
- Find the last non-overlapping job
- Profit if the current job is included
- Take the maximum profit between including and excluding the current job
- Search in the right half
- Search in the left half

### Code

{% include code-tabs-file.html problem="maximumprofitinjobscheduling" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Partition Equal Subset Sum

<span id="partitionequalsubsetsum"></span>

### Problem

**Partitionequalsubsetsum**

**Function:** `Can Partition` takes `nums` (array of integers) and returns **boolean**.



### Approach

**Top-Down DP (Memoization) Approach:**
1. Define a recursive function that explores all possibilities
2. Cache results in a table/dictionary to avoid redundant work
3. The state is defined by the function parameters that change between calls


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `sum`, `target`, `dp`, `sum`, `target`, `dp`

### Code

{% include code-tabs-file.html problem="partitionequalsubsetsum" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

The DP table has dimensions proportional to the input size, giving O(n²) space. Each cell requires O(1) or O(n) work, totaling O(n³).

---

## Super Egg Dropping

<span id="supereggdropping"></span>

### Problem

**Supereggdropping**

**Function:** `Super Egg Drop` takes `k` (integer), `n` (integer) and returns **integer**.



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`, `m`

### Code

{% include code-tabs-file.html problem="supereggdropping" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

The DP table has dimensions proportional to the input size, giving O(n²) space. Each cell requires O(1) or O(n) work, totaling O(n³).

---

## Burst Baloons

<span id="burstbaloons"></span>

### Problem

**Burstbaloons**

**Function:** `Max Coins` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Time COmplexity O(N^3) Space O(N^2)
- Calculate the maximum coins for this partition



### Approach

**Top-Down DP (Memoization) Approach:**
1. Define a recursive function that explores all possibilities
2. Cache results in a table/dictionary to avoid redundant work
3. The state is defined by the function parameters that change between calls


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`, `res`, `left`, `right`

**Execution flow:**
- Time COmplexity O(N^3) Space O(N^2)
- Calculate the maximum coins for this partition

### Code

{% include code-tabs-file.html problem="burstbaloons" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

The DP table has dimensions proportional to the input size, giving O(n²) space. Each cell requires O(1) or O(n) work, totaling O(n³).

---

## House Robber

<span id="houserobber"></span>

### Problem

**Houserobber**

**Function:** `Rob` takes `nums` (array of integers) and returns **integer**.



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`, `include`, `exclude`, `temp`

### Code

{% include code-tabs-file.html problem="houserobber" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n³). The memoization/table stores one entry per state (O(n²)).

---

## House Robber_II

<span id="houserobber_ii"></span>

### Problem

**Houserobber Ii**

**Function:** `Rob` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Initialize an array to store the maximum amount that can be robbed up to each house
- Base cases
- Fill the dp array from start + 2 to end
- The last element of dp array contains the maximum amount that can be robbed



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`

**Execution flow:**
- Initialize an array to store the maximum amount that can be robbed up to each house
- Fill the dp array from start + 2 to end
- The last element of dp array contains the maximum amount that can be robbed

### Code

{% include code-tabs-file.html problem="houserobber_ii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n³). The memoization/table stores one entry per state (O(n²)).

---

## Coin Change

<span id="coinchange"></span>

### Problem

**Coinchange**

**Function:** `Coin Change` takes `coins` (array of integers), `amount` (integer) and returns **integer**.



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`, `minCoins`, `result`

### Code

{% include code-tabs-file.html problem="coinchange" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n³). The memoization/table stores one entry per state (O(n²)).

---

## Coin Change_II

<span id="coinchange_ii"></span>

### Problem

**Coinchange Ii**

**Function:** `Change` takes `amount` (integer), `coins` (array of integers) and returns **integer**.



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`

### Code

{% include code-tabs-file.html problem="coinchange_ii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n × m) |
| **Space** | O(n) |

**Analysis:**

The DP table has dimensions proportional to the input size, giving O(n) space. Each cell requires O(1) or O(n) work, totaling O(n × m).

---

## Coin Change_II_Bottom Up

<span id="coinchange_ii_bottomup"></span>

### Problem

**Coinchange Ii Bottomup**

**Function:** `Change` takes `amount` (integer), `coins` (array of integers) and returns **integer**.

**Key logic:**
- Base case: 1 way to make amount 0 (using no coins)



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`

**Execution flow:**
- Base case: 1 way to make amount 0 (using no coins)

### Code

{% include code-tabs-file.html problem="coinchange_ii_bottomup" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n³). The memoization/table stores one entry per state (O(n²)).

---

## Longest Increasing Subsequence

<span id="longestincreasingsubsequence"></span>

### Problem

**Longestincreasingsubsequence**

**Function:** `Length Of Lis` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Patience sorting algorithm
- Find the smallest element in the tree which is greater than or equal to num
- If such an element is found, it means num can replace it to potentially
- form a new valid increasing subsequence or extend the current one
- Add num to the tree. If num is not replacing any element,



### Approach

**Solution Approach:**
1. The main function `lengthOfLIS` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `tree`

**Execution flow:**
- Patience sorting algorithm
- Find the smallest element in the tree which is greater than or equal to num
- If such an element is found, it means num can replace it to potentially
- form a new valid increasing subsequence or extend the current one
- Add num to the tree. If num is not replacing any element,
- it is extending the subsequence with a new larger element.
- The size of the tree at the end will represent the length of the longest
- increasing subsequence

### Code

{% include code-tabs-file.html problem="longestincreasingsubsequence" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Maximal Square

<span id="maximalsquare"></span>

### Problem

**Maximalsquare**

**Function:** `Maximal Square` takes `matrix` (Array<CharArray>) and returns **integer**.



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `m`, `n`, `dp`, `maxSize`

### Code

{% include code-tabs-file.html problem="maximalsquare" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

The DP table has dimensions proportional to the input size, giving O(n²) space. Each cell requires O(1) or O(n) work, totaling O(n³).

---

## Maximum Sum Sub Array

<span id="maximumsumsubarray"></span>

### Problem

**Maximumsumsubarray**

**Function:** `Max Sub Array` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Kaden's Algorithm Dynamic Programming



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Execution flow:**
- Kaden's Algorithm Dynamic Programming

### Code

{% include code-tabs-file.html problem="maximumsumsubarray" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n³). The memoization/table stores one entry per state (O(n²)).

---

## Min Cost Climbing Staris

<span id="mincostclimbingstaris"></span>

### Problem

**Mincostclimbingstaris**

**Function:** `Min Cost Climbing Stairs_Iterative` takes `cost` (array of integers) and returns **integer**.

**Key logic:**
- Handle base cases
- Initialize the dp array with the size of the cost array
- Base cases
- Fill the dp array
- The result is the minimum cost to reach the last or the second-to-last step



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`, `dp`, `prev2`, `prev1`, `cur`, `memo`, `n`

**Execution flow:**
- Handle base cases
- Initialize the dp array with the size of the cost array
- Fill the dp array
- The result is the minimum cost to reach the last or the second-to-last step
- Handle base cases
- Initialize the dp array with the size of the cost array

### Code

{% include code-tabs-file.html problem="mincostclimbingstaris" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n³). The memoization/table stores one entry per state (O(n²)).

---

## Minimum Path Sum

<span id="minimumpathsum"></span>

### Problem

**Minimumpathsum**

**Function:** `Min Path Sum` takes `grid` (Array<array of integers>?) and returns **integer**.



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`

### Code

{% include code-tabs-file.html problem="minimumpathsum" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

The DP table has dimensions proportional to the input size, giving O(n²) space. Each cell requires O(1) or O(n) work, totaling O(n³).

---

## Split Array Largest Sum

<span id="splitarraylargestsum"></span>

### Problem

**Splitarraylargestsum**

**Function:** `Split Array` takes `nums` (array of integers), `k` (integer) and returns **integer**.

**Key logic:**
- Last split takes remaining sum
- Prune unnecessary recursion



### Approach

**Top-Down DP (Memoization) Approach:**
1. Define a recursive function that explores all possibilities
2. Cache results in a table/dictionary to avoid redundant work
3. The state is defined by the function parameters that change between calls


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `n`, `prefixSum`, `memo`, `minLargestSum`, `currentSum`, `largestInRemainingSplits`, `maxSplitSum`

**Execution flow:**
- Last split takes remaining sum
- Prune unnecessary recursion

### Code

{% include code-tabs-file.html problem="splitarraylargestsum" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n³). The memoization/table stores one entry per state (O(n²)).

---

## Target Sum

<span id="targetsum"></span>

### Problem

**Targetsum**

**Function:** `Find Target Sum Ways` takes `nums` (array of integers), `target` (integer) and returns **integer**.

**Key logic:**
- If the target sum is not reachable, return 0
- If the sumAll + target is not non-negative or even, it's impossible to partition
- DP array to store the number of ways to reach each sum



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`, `state`, `count`, `sumAll`, `newTarget`, `dp`

**Execution flow:**
- If the target sum is not reachable, return 0
- If the sumAll + target is not non-negative or even, it's impossible to partition
- DP array to store the number of ways to reach each sum

### Code

{% include code-tabs-file.html problem="targetsum" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n³). The memoization/table stores one entry per state (O(n²)).

---

## Longest Increasing Sequence In A Matrix

<span id="longestincreasingsequenceinamatrix"></span>

### Problem

**Longestincreasingsequenceinamatrix**

**Function:** `Longest Increasing Path` takes `matrix` (Array<array of integers>) and returns **integer**.



### Approach

**Top-Down DP (Memoization) Approach:**
1. Define a recursive function that explores all possibilities
2. Cache results in a table/dictionary to avoid redundant work
3. The state is defined by the function parameters that change between calls


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dirs`, `cache`, `max`

### Code

{% include code-tabs-file.html problem="longestincreasingsequenceinamatrix" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

The DP table has dimensions proportional to the input size, giving O(n²) space. Each cell requires O(1) or O(n) work, totaling O(n³).

---

## Minimum Numberof Increments Subarrays Forma Target Array

<span id="minimumnumberofincrementssubarraysformatargetarray"></span>

### Problem

**Minimumnumberofincrementssubarraysformatargetarray**

**Function:** `Min Number Operations` takes `target` (array of integers) and returns **integer**.



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `operations`

### Code

{% include code-tabs-file.html problem="minimumnumberofincrementssubarraysformatargetarray" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n³). The memoization/table stores one entry per state (O(n²)).

---

## Partition Array Into Two Array To Minimuze Sum Difference

<span id="partitionarrayintotwoarraytominimuzesumdifference"></span>

### Problem

**Partitionarrayintotwoarraytominimuzesumdifference**

**Function:** `Minimum Difference` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Early exit if perfect match found
- Exact match
- Remove duplicates if adjacent values are equal



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `n`, `totalSum`, `halfSize`, `leftSubsets`, `rightSubsets`, `minDiff`, `leftSums`, `rightSums`

**Execution flow:**
- Early exit if perfect match found
- Exact match
- Remove duplicates if adjacent values are equal

### Code

{% include code-tabs-file.html problem="partitionarrayintotwoarraytominimuzesumdifference" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Key Takeaways

1. **Core pattern recognition** — Optimal substructure + overlapping subproblems → DP. Identify states, define transitions, compute bottom-up or top-down with memoization.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

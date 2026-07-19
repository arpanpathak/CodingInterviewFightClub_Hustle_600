---
layout: chapter
title: "Binary Search"
chapter_number: 1
chapter_title: "Binary Search"
toc: true
next_chapter:
  url: "/chapters/02-dynamic-programming.html"
  title: "Dynamic Programming"
---

# Binary Search

> **21 problems** — Master the art of divide-and-conquer searching. Binary search finds elements in sorted arrays in O(log n) time.

## The Pattern

Sorted array + search → Binary Search. The key insight: find a predicate that splits the search space into 'yes' and 'no', then binary search finds the transition point.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [Apartmenthunting](#apartmenthunting) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Capacity To Ship Package Within D Days](#capacitytoshippackagewithinddays) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Closest Sebsequence Sum](#closestsebsequencesum) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Find First And Last Position](#findfirstandlastposition) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [Find K Closest Elements](#findkclosestelements) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Find Minimum In Rotated Sorted Array](#findminimuminrotatedsortedarray) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [Find Peak Element](#findpeakelement) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [Find Peak Element Better Solution](#findpeakelementbettersolution) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Version Control](#firstbadversion) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Solution](#guessnumberhigherorlower) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [House Robber_IV](#houserobber_iv) | — | <span class="badge badge-medium">Medium</span> |
| 12 | [K Th Missing Positive Number](#kthmissingpositivenumber) | — | <span class="badge badge-medium">Medium</span> |
| 13 | [Koko Eating Banana](#kokoeatingbanana) | — | <span class="badge badge-medium">Medium</span> |
| 14 | [Median Of Two Sorted A Rrays](#medianoftwosortedarrays) | — | <span class="badge badge-medium">Medium</span> |
| 15 | [Random Pick With Weight](#randompickwithweight) | — | <span class="badge badge-medium">Medium</span> |
| 16 | [Search A2d Matrix](#searcha2dmatrix) | — | <span class="badge badge-medium">Medium</span> |
| 17 | [Search In Rotated Array_II](#searchinrotatedarray_ii) | — | <span class="badge badge-medium">Medium</span> |
| 18 | [Search In Rotated Sorted Array](#searchinrotatedsortedarray) | — | <span class="badge badge-medium">Medium</span> |
| 19 | [Search Insertion Position](#searchinsertionposition) | — | <span class="badge badge-medium">Medium</span> |
| 20 | [Single Element In A Sorted Array](#singleelementinasortedarray) | — | <span class="badge badge-medium">Medium</span> |
| 21 | [Valley Element](#valleyelement) | — | <span class="badge badge-medium">Medium</span> |

---

## Apartmenthunting

<span id="apartmenthunting"></span>

### Problem

**Apartmenthunting**

**Function:** `Find Best Block` takes `blocks` (List<Map<string), `Boolean>>` (?), `requirements` (List<string>) and returns **integer**.

**Key logic:**
- Step 1: Create a HashMap where each key is an amenity and each value is a sorted list of blocks where the amenity is present
- Ensure all required amenities are present
- Return -1 if any required amenity is not present in any block
- Step 2: Determine the optimal block
- N * R * Log(K) , K = number of unique amininties present across all the blocks



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `amenityMap`, `bestBlock`, `bestMaxDistance`, `maxDistance`, `pos`, `insertPoint`, `leftDistance`, `rightDistance`

**Execution flow:**
- Step 1: Create a HashMap where each key is an amenity and each value is a sorted list of blocks where the amenity is present
- Ensure all required amenities are present
- Return -1 if any required amenity is not present in any block
- Step 2: Determine the optimal block
- N * R * Log(K) , K = number of unique amininties present across all the blocks
- Check if the current block has the smallest maximum distance
- Function to find the minimum distance to the closest block with the given amenity
- Custom Binary Search implementation

### Code

{% include code-tabs-file.html problem="apartmenthunting" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Capacity To Ship Package Within D Days

<span id="capacitytoshippackagewithinddays"></span>

### Problem

**Capacitytoshippackagewithinddays**

**Function:** `Feasible` takes `weights` (array of integers), `mid` (integer), `days` (integer) and returns **boolean**.



### Approach

**Solution Approach:**
1. The main function `feasible` processes the input
2. Uses helper functions: shipWithinDays

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`

### Code

{% include code-tabs-file.html problem="capacitytoshippackagewithinddays" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Closest Sebsequence Sum

<span id="closestsebsequencesum"></span>

### Problem

**Closestsebsequencesum**

**Function:** `Min Abs Difference` takes `nums` (array of integers), `goal` (integer) and returns **integer**.

**Key logic:**
- exclude
- include
- exact match found



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `leftSums`, `rightSums`, `n`, `mid`, `minDiff`, `target`, `idx`, `insertPoint`

**Execution flow:**
- exact match found

### Code

{% include code-tabs-file.html problem="closestsebsequencesum" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Find First And Last Position

<span id="findfirstandlastposition"></span>

### Problem

**Findfirstandlastposition**

**Function:** `Search Range` takes `nums` (array of integers), `target` (integer) and returns **array of integers**.

**Key logic:**
- Find the first occurrence
- If the first occurrence is not found, return [-1, -1]
- Find the last occurrence
- Adjust the search range based on whether we are looking for the first or last occurrence
- Move left to find the first occurrence



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `left`, `right`, `result`, `mid`

**Execution flow:**
- Find the first occurrence
- If the first occurrence is not found, return [-1, -1]
- Find the last occurrence
- Adjust the search range based on whether we are looking for the first or last occurrence
- Move left to find the first occurrence
- Move right to find the last occurrence

### Code

{% include code-tabs-file.html problem="findfirstandlastposition" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Find K Closest Elements

<span id="findkclosestelements"></span>

### Problem

**Findkclosestelements**

**Function:** `Find Closest Elements` takes `arr` (Array<integer>), `k` (integer), `x` (integer) and returns **List**.

**Key logic:**
- Remove the farthest element
- We could also do



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `priorityQueue`, `diffA`, `diffB`, `result`, `testClass`

**Execution flow:**
- Remove the farthest element
- We could also do

### Code

{% include code-tabs-file.html problem="findkclosestelements" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

---

## Find Minimum In Rotated Sorted Array

<span id="findminimuminrotatedsortedarray"></span>

### Problem

**Findminimuminrotatedsortedarray**

**Function:** `Find Min` takes `nums` (array of integers) and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`

### Code

{% include code-tabs-file.html problem="findminimuminrotatedsortedarray" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Find Peak Element

<span id="findpeakelement"></span>

### Problem

**Findpeakelement**

**Function:** `Find Peak Element` takes `nums` (array of integers) and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `mid`

### Code

{% include code-tabs-file.html problem="findpeakelement" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Find Peak Element Better Solution

<span id="findpeakelementbettersolution"></span>

### Problem

**Findpeakelementbettersolution**

**Function:** `Find Peak Element` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Safely handle boundaries
- Found peak
- Move to the right
- Move to the left
- Single peak element when the range narrows down



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`, `leftNeighbor`, `rightNeighbor`

**Execution flow:**
- Safely handle boundaries
- Move to the right
- Move to the left
- Single peak element when the range narrows down

### Code

{% include code-tabs-file.html problem="findpeakelementbettersolution" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Version Control

<span id="firstbadversion"></span>

### Problem

**Firstbadversion**

**Function:** `Is Bad Version` takes `mid` (integer) and returns **boolean**.

**Key logic:**
- Return dummy value



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `start`, `end`, `mid`

**Execution flow:**
- Return dummy value

### Code

{% include code-tabs-file.html problem="firstbadversion" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Solution

<span id="guessnumberhigherorlower"></span>

### Problem

**Guessnumberhigherorlower**

**Function:** `Guess` takes `num` (integer) and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `start`, `end`, `mid`, `distance`

### Code

{% include code-tabs-file.html problem="guessnumberhigherorlower" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## House Robber_IV

<span id="houserobber_iv"></span>

### Problem

**Houserobber Iv**

**Function:** `Min Capability` takes `nums` (array of integers), `k` (integer) and returns **integer**.

**Key logic:**
- skip adjacent



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This uses a **feasibility function** that checks if a candidate value satisfies the constraint, making it a 'minimize/maximize with binary search' pattern.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `robbed`, `i`, `mid`

**Execution flow:**
- skip adjacent

### Code

{% include code-tabs-file.html problem="houserobber_iv" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## K Th Missing Positive Number

<span id="kthmissingpositivenumber"></span>

### Problem

**Kthmissingpositivenumber**

**Function:** `Find Kth Positive` takes `arr` (array of integers), `k` (integer) and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`, `missingCount`

### Code

{% include code-tabs-file.html problem="kthmissingpositivenumber" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Koko Eating Banana

<span id="kokoeatingbanana"></span>

### Problem

**Kokoeatingbanana**

**Function:** `Min Eating Speed` takes `piles` (array of integers), `h` (integer) and returns **integer**.

**Key logic:**
- Left is the slowest speed, right is the fastest speed
- Binary search to find the minimum valid eating speed
- If Koko can eat all bananas at speed `mid`, try slower speeds
- Otherwise, try faster speeds
- Helper function to check if Koko can finish all bananas in `h` hours at speed `k`



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `mid`, `totalHours`

**Execution flow:**
- Left is the slowest speed, right is the fastest speed
- Binary search to find the minimum valid eating speed
- If Koko can eat all bananas at speed `mid`, try slower speeds
- Otherwise, try faster speeds
- Helper function to check if Koko can finish all bananas in `h` hours at speed `k`
- Add the number of hours it takes to finish this pile at speed `k`
- Same as Math.ceil(pile / k)

### Code

{% include code-tabs-file.html problem="kokoeatingbanana" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Median Of Two Sorted A Rrays

<span id="medianoftwosortedarrays"></span>

### Problem

**Medianoftwosortedarrays**

**Function:** `Find Median Sorted Arrays` takes `nums1` (array of integers), `nums2` (array of integers) and returns **double**.

**Key logic:**
- These are the challenges that I need to somewhoe solve to get
- Use getOrNull with the Elvis operator to handle boundaries
- Check if we have found the correct partition



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `m`, `n`, `start`, `end`, `partitionX`, `partitionY`, `leftX`, `rightX`

**Execution flow:**
- These are the challenges that I need to somewhoe solve to get
- Use getOrNull with the Elvis operator to handle boundaries
- Check if we have found the correct partition

### Code

{% include code-tabs-file.html problem="medianoftwosortedarrays" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Random Pick With Weight

<span id="randompickwithweight"></span>

### Problem

**Randompickwithweight**

**Function:** `Pick Index` takes none and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `prefixSum`, `totalSum`, `w`, `randomPick`, `mid`

### Code

{% include code-tabs-file.html problem="randompickwithweight" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Search A2d Matrix

<span id="searcha2dmatrix"></span>

### Problem

**Searcha2Dmatrix**

**Function:** `Search Matrix` takes `matrix` (Array<array of integers>), `target` (integer) and returns **boolean**.

**Key logic:**
- Convert 1D index to 2D



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`, `midValue`

**Execution flow:**
- Convert 1D index to 2D

### Code

{% include code-tabs-file.html problem="searcha2dmatrix" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Search In Rotated Array_II

<span id="searchinrotatedarray_ii"></span>

### Problem

**Searchinrotatedarray Ii**

**Function:** `Search` takes `nums` (array of integers), `target` (integer) and returns **boolean**.

**Key logic:**
- Handle duplicates: skip the duplicates
- Left portion is sorted
- Target in left portion
- Target in right portion
- Right portion is sorted



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `mid`

**Execution flow:**
- Handle duplicates: skip the duplicates
- Left portion is sorted
- Target in left portion
- Target in right portion
- Right portion is sorted
- Target in right portion
- Target in left portion

### Code

{% include code-tabs-file.html problem="searchinrotatedarray_ii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Search In Rotated Sorted Array

<span id="searchinrotatedsortedarray"></span>

### Problem

**Searchinrotatedsortedarray**

**Function:** `Search` takes `nums` (array of integers), `target` (integer) and returns **integer**.

**Key logic:**
- Determine if Left half is sorted
- Right half is sorted



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`

**Execution flow:**
- Determine if Left half is sorted
- Right half is sorted

### Code

{% include code-tabs-file.html problem="searchinrotatedsortedarray" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Search Insertion Position

<span id="searchinsertionposition"></span>

### Problem

**Searchinsertionposition**

**Function:** `Search Insert` takes `nums` (array of integers), `target` (integer) and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `start`, `end`, `mid`

### Code

{% include code-tabs-file.html problem="searchinsertionposition" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Single Element In A Sorted Array

<span id="singleelementinasortedarray"></span>

### Problem

**Singleelementinasortedarray**

**Function:** `Single Non Duplicate` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Ensure mid is even for checking pair with the next element
- Check if the pair is valid
- Move to the right half
- Move to the left half
- low == high will give the unique element



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `low`, `high`, `mid`

**Execution flow:**
- Ensure mid is even for checking pair with the next element
- Check if the pair is valid
- Move to the right half
- Move to the left half
- low == high will give the unique element

### Code

{% include code-tabs-file.html problem="singleelementinasortedarray" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Valley Element

<span id="valleyelement"></span>

### Problem

**Valleyelement**

**Function:** `Find Valley Element Binary` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Safely handle boundaries
- Found valley
- Move to the right
- Move to the left
- No valley found (unlikely for a valid array)



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`, `leftNeighbor`, `rightNeighbor`

**Execution flow:**
- Safely handle boundaries
- Found valley
- Move to the right
- Move to the left
- No valley found (unlikely for a valid array)

### Code

{% include code-tabs-file.html problem="valleyelement" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Key Takeaways

1. **Core pattern recognition** — Sorted array + search → Binary Search. The key insight: find a predicate that splits the search space into 'yes' and 'no', then binary search finds the transition point.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

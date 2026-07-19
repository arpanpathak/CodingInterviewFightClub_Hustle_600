---
layout: chapter
title: "Heaps & Priority Queues"
chapter_number: 8
chapter_title: "Heaps & Priority Queues"
toc: true
prev_chapter:
  url: "/chapters/07-bit-manipulation.html"
  title: "Bit Manipulation"
next_chapter:
  url: "/chapters/09-disjoint-set-union.html"
  title: "Disjoint Set Union"
---

# Heaps & Priority Queues

> **11 problems** — Master priority queues for k-th order statistics, scheduling, and streaming data.

## The Pattern

Heaps maintain the min/max of a dynamic set. Use min-heap for k largest, max-heap for k smallest, dual heaps for median.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [Dual Balanced Heap](#dualbalancedheap) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [MK Average](#findingmkaverage) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Find K Closest Elements](#findkclosestelements) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Find Score Of An Array After Marking All Elements](#findscoreofanarrayaftermarkingallelements) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [IPO](#ipo) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Longest Happy String](#longesthappystring) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [Median From Running Stream](#medianfromrunningstream) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [Meeting Room_III](#meetingroom_iii) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Single Threaded CPU](#singlethreadedcpu) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Sliding Window Median](#slidingwindowmedian) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [Top K Frequent Elements](#topkfrequentelements) | — | <span class="badge badge-medium">Medium</span> |

---

## Dual Balanced Heap

<span id="dualbalancedheap"></span>

### Problem

**Dualbalancedheap**

**Function:** `Get Median` takes none and returns **T**.

**Key logic:**
- Min-heap for the larger half
- Max-heap for the smaller half
- Handling generic types requires a custom approach for averaging or choosing one of the elements.
- Simplification: you may need to define how to combine two elements for real applications.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `minHeap`, `maxHeap`

**Execution flow:**
- Min-heap for the larger half
- Max-heap for the smaller half
- Handling generic types requires a custom approach for averaging or choosing one of the elements.
- Simplification: you may need to define how to combine two elements for real applications.

### Code

{% include code-tabs-file.html problem="dualbalancedheap" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

---

## MK Average

<span id="findingmkaverage"></span>

### Problem

**Findingmkaverage**

**Function:** `Calculate Mkaverage` takes none and returns **integer**.

**Key logic:**
- max heap (for k smallest elements)
- min heap (for k largest elements)
- Sum of the middle elements
- Add to deque
- Add to one of the heaps



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `m`, `k`, `deque`, `lowHeap`, `highHeap`, `sum`, `oldest`, `middleCount`

**Execution flow:**
- max heap (for k smallest elements)
- min heap (for k largest elements)
- Sum of the middle elements
- Add to deque
- Add to one of the heaps
- Add to lowHeap (max heap)
- Add to highHeap (min heap)
- Maintain the window size of m

### Code

{% include code-tabs-file.html problem="findingmkaverage" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

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

## Find Score Of An Array After Marking All Elements

<span id="findscoreofanarrayaftermarkingallelements"></span>

### Problem

**Findscoreofanarrayaftermarkingallelements**

**Function:** `Find Score` takes `nums` (array of integers) and returns **Long**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `n`, `marked`, `minHeap`, `score`

### Code

{% include code-tabs-file.html problem="findscoreofanarrayaftermarkingallelements" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

---

## IPO

<span id="ipo"></span>

### Problem

**Ipo**

**Function:** `Find Maximized Capital` takes `k` (integer), `w` (integer), `profits` (array of integers), `capital` (array of integers) and returns **integer**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `capital`, `profit`, `projects`, `maxHeap`, `currentCapital`, `i`

### Code

{% include code-tabs-file.html problem="ipo" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

---

## Longest Happy String

<span id="longesthappystring"></span>

### Problem

**Longesthappystring**

**Function:** `Longest Diverse String` takes `a` (integer), `b` (integer), `c` (integer) and returns **string**.

**Key logic:**
- Use a priority queue to always get the character with highest remaining count
- Add non-zero counts to the queue
- Build the result
- Get the character with highest remaining count
- If we already have two consecutive of the same character,



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `pq`, `lastChar`, `lastCount`

**Execution flow:**
- Use a priority queue to always get the character with highest remaining count
- Add non-zero counts to the queue
- Build the result
- Get the character with highest remaining count
- If we already have two consecutive of the same character,
- we need to use the second highest count character
- Put the character back with reduced count
- Put the original highest character back

### Code

{% include code-tabs-file.html problem="longesthappystring" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

---

## Median From Running Stream

<span id="medianfromrunningstream"></span>

### Problem

**Medianfromrunningstream**

**Function:** `Find Median` takes none and returns **double**.

**Key logic:**
- Min-heap for the larger half
- Max-heap for the smaller half



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `minHeap`, `maxHeap`

**Execution flow:**
- Min-heap for the larger half
- Max-heap for the smaller half

### Code

{% include code-tabs-file.html problem="medianfromrunningstream" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

---

## Meeting Room_III

<span id="meetingroom_iii"></span>

### Problem

**Meetingroom Iii**

**Function:** `Most Booked` takes `n` (integer), `meetings` (Array<array of integers>) and returns **integer**.

**Key logic:**
- Sort meetings by start time
- Initialize available rooms
- Free up any rooms that are now available
- If a room is available, use it
- If all rooms are busy, use the one that will become available first



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `endTime`, `index`, `roomUsage`, `busyRooms`, `availableRooms`, `duration`, `room`, `earliestRoom`

**Execution flow:**
- Sort meetings by start time
- Initialize available rooms
- Free up any rooms that are now available
- If a room is available, use it
- If all rooms are busy, use the one that will become available first
- The new end time is the earliest available time plus the duration
- Find the room with maximum usage (if tied, return the smallest index)

### Code

{% include code-tabs-file.html problem="meetingroom_iii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

---

## Single Threaded CPU

<span id="singlethreadedcpu"></span>

### Problem

**Singlethreadedcpu**

**Function:** `Get Order` takes `tasks` (Array<array of integers>) and returns **array of integers**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `enqueueTime`, `processingTime`, `index`, `allTasks`, `pq`, `result`, `time`, `i`

### Code

{% include code-tabs-file.html problem="singlethreadedcpu" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

---

## Sliding Window Median

<span id="slidingwindowmedian"></span>

### Problem

**Slidingwindowmedian**

**Function:** `Get Median` takes none and returns **double**.

**Key logic:**
- Min-heap for the larger half
- Max-heap for the smaller half
- TreeMap to track delayed removals



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `minHeap`, `maxHeap`, `delayedRemoval`, `result`

**Execution flow:**
- Min-heap for the larger half
- Max-heap for the smaller half
- TreeMap to track delayed removals

### Code

{% include code-tabs-file.html problem="slidingwindowmedian" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

---

## Top K Frequent Elements

<span id="topkfrequentelements"></span>

### Problem

**Topkfrequentelements**

**Function:** `Top Kfrequent` takes `nums` (array of integers), `k` (integer) and returns **array of integers**.

**Key logic:**
- Randomized Quick Partition...
- Swap pivot with the end
- Swap back the pivot to the correct position



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `map`, `uniqueNums`, `start`, `end`, `partitionIndex`, `randomIndex`, `pivot`, `partitionIndex`

**Execution flow:**
- Randomized Quick Partition...
- Swap pivot with the end
- Swap back the pivot to the correct position

### Code

{% include code-tabs-file.html problem="topkfrequentelements" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Key Takeaways

1. **Core pattern recognition** — Heaps maintain the min/max of a dynamic set. Use min-heap for k largest, max-heap for k smallest, dual heaps for median.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

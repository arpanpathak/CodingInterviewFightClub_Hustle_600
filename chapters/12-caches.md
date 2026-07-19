---
layout: chapter
title: "Caches & Memory Management"
chapter_number: 12
chapter_title: "Caches & Memory Management"
toc: true
prev_chapter:
  url: "/chapters/11-backtracking.html"
  title: "Backtracking"
---

# Caches & Memory Management

> **3 problems** — Master cache design: LRU, LFU, and eviction strategies.

## The Pattern

Cache design combines: hash map for O(1) lookup + linked list for ordering. LRU uses access order; LFU uses frequency count.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [LFU Cache](#lfucache) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [LRU Cache](#lrucache) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [LRU Cache Linked List](#lrucachelinkedlist) | — | <span class="badge badge-medium">Medium</span> |

---

## LFU Cache

<span id="lfucache"></span>

### Problem

**Lfucache**

**Function:** `Get` takes `key` (integer) and returns **integer**.



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `vals`, `freq`, `lists`, `MAX_SIZE`, `min`, `count`, `evict`

### Code

{% include code-tabs-file.html problem="lfucache" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n × m) |
| **Space** | O(n) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n × m). The memoization/table stores one entry per state (O(n)).

---

## LRU Cache

<span id="lrucache"></span>

### Problem

**Lrucache**

**Function:** `Get` takes `key` (integer) and returns **integer**.

**Key logic:**
- cache[key] = data // Move accessed element to the end to mark it as recently used
- Eviction policy
- Remove the least recently used element
- Insert the new element



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `capacity`, `cache`, `data`

**Execution flow:**
- cache[key] = data // Move accessed element to the end to mark it as recently used
- Eviction policy
- Remove the least recently used element
- Insert the new element

### Code

{% include code-tabs-file.html problem="lrucache" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n × m) |
| **Space** | O(n) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n × m). The memoization/table stores one entry per state (O(n)).

---

## LRU Cache Linked List

<span id="lrucachelinkedlist"></span>

### Problem

**Lrucachelinkedlist**

**Function:** `Get` takes `key` (integer) and returns **integer**.

**Key logic:**
- Hash map for O(1) access
- Dummy head
- Dummy tail
- Key not found
- Move the node to the head (most recently used)



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `capacity`, `key`, `value`, `prev`, `next`, `cache`, `head`, `tail`

**Execution flow:**
- Hash map for O(1) access
- Key not found
- Move the node to the head (most recently used)
- Update the value and move to head
- Create a new node and add to head
- If capacity is exceeded, remove the tail node (least recently used)

### Code

{% include code-tabs-file.html problem="lrucachelinkedlist" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n³). The memoization/table stores one entry per state (O(n²)).

---

## Key Takeaways

1. **Core pattern recognition** — Cache design combines: hash map for O(1) lookup + linked list for ordering. LRU uses access order; LFU uses frequency count.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

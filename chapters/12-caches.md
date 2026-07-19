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
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n × m) |
| **Space** | O(n) |
---
## LRU Cache
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n × m) |
| **Space** | O(n) |
---
## LRU Cache Linked List
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n³) |
| **Space** | O(n²) |
---
## Key Takeaways

1. **Core pattern recognition** — Cache design combines: hash map for O(1) lookup + linked list for ordering. LRU uses access order; LFU uses frequency count.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

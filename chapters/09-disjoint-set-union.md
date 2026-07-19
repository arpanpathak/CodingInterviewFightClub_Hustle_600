---
layout: chapter
title: "Disjoint Set Union"
chapter_number: 9
chapter_title: "Disjoint Set Union"
toc: true
prev_chapter:
  url: "/chapters/08-heaps.html"
  title: "Heaps & Priority Queues"
next_chapter:
  url: "/chapters/10-string-matching.html"
  title: "String Matching"
---

# Disjoint Set Union

> **3 problems** — Master union-find for connectivity problems and dynamic graph components.

## The Pattern

DSU tracks connected components. Union by rank and path compression give near-O(1) operations.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [Account Merge](#accountmerge) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Number Of Island_II](#numberofisland_ii) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Union Find](#unionfind) | — | <span class="badge badge-medium">Medium</span> |

---

## Account Merge

<span id="accountmerge"></span>

### Problem

**Accountmerge**

**Function:** `Find` takes `x` (T) and returns **T**.

**Key logic:**
- Add emails to Union-Find, map them to their owner's name, and union them in one pass
- Group emails by their root parent
- Construct the result



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `parent`, `rank`, `nodes`, `node`, `rootX`, `rootY`, `nodeX`, `nodeY`

**Execution flow:**
- Add emails to Union-Find, map them to their owner's name, and union them in one pass
- Group emails by their root parent
- Construct the result

### Code

{% include code-tabs-file.html problem="accountmerge" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Number Of Island_II

<span id="numberofisland_ii"></span>

### Problem

**Numberofisland Ii**

**Function:** `Find` takes `x` (Pair<integer), `Int>` (?) and returns **Pair**.

**Key logic:**
- Path compression



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `parent`, `rank`, `count`, `rootX`, `rootY`, `uf`, `result`, `directions`

**Execution flow:**
- Path compression

### Code

{% include code-tabs-file.html problem="numberofisland_ii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Union Find

<span id="unionfind"></span>

### Problem

**Unionfind**

**Function:** `Find` takes `x` (T) and returns **T**.



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `parent`, `rank`, `nodes`, `node`, `rootX`, `rootY`, `nodeX`, `nodeY`

### Code

{% include code-tabs-file.html problem="unionfind" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Key Takeaways

1. **Core pattern recognition** — DSU tracks connected components. Union by rank and path compression give near-O(1) operations.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

---
layout: chapter
title: "Linked Lists"
chapter_number: 4
chapter_title: "Linked Lists"
toc: true
prev_chapter:
  url: "/chapters/03-arrays-two-pointers.html"
  title: "Arrays & Two Pointers"
next_chapter:
  url: "/chapters/05-trees.html"
  title: "Trees"
---

# Linked Lists

> **16 problems** — Master pointer manipulation and linked list operations.

## The Pattern

Linked lists are about pointer rearrangement. Key patterns: slow/fast pointers, dummy heads, recursion, and in-place reversal.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [List Node](#addtwonumbers) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Copy Linked List With Random Pointer](#copylinkedlistwithrandompointer) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Delete Middle Node Of Linked List](#deletemiddlenodeoflinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Node](#insertintoasortedcircularlinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [Intersection Of Two Linked List](#intersectionoftwolinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Linked List Cycle](#linkedlistcycle) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [Linked List Cycle_II](#linkedlistcycle_ii) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [Merge K Sorted List](#mergeksortedlist) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Merge K Sorted List Iterative](#mergeksortedlistiterative) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Merge Two Sorted L Ist](#mergetwosortedlist) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [Odd Even Linked List](#oddevenlinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 12 | [Palindrome Linked List](#palindromelinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 13 | [Remove Nth Node From End Of List](#removenthnodefromendoflist) | — | <span class="badge badge-medium">Medium</span> |
| 14 | [Reverse Linked List](#reverselinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 15 | [Reverse Linked List Iterative](#reverselinkedlistiterative) | — | <span class="badge badge-medium">Medium</span> |
| 16 | [Reverse Nodes In K Groups](#reversenodesinkgroups) | — | <span class="badge badge-medium">Medium</span> |

---

## List Node

<span id="addtwonumbers"></span>

### Problem

**Addtwonumbers**

**Function:** `Add Two Numbers` takes `l1` (ListNode?), `l2` (ListNode?) and returns **ListNode**.



### Approach

**Solution Approach:**
1. The main function `addTwoNumbers` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `next`, `carry`, `head`, `ptr`, `sum`

### Code

{% include code-tabs-file.html problem="addtwonumbers" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Copy Linked List With Random Pointer

<span id="copylinkedlistwithrandompointer"></span>

### Problem

**Copylinkedlistwithrandompointer**

**Function:** `Copy Random List` takes `node` (Node?) and returns **Node**.

**Key logic:**
- Step 1: Create deep copies of all nodes and store the mapping
- Step 2: Set the next and random pointers for the copied nodes
- Return the head of the new copied list



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `ti`, `v`, `next`, `random`, `next`, `random`, `nodeMap`, `ptr`

**Execution flow:**
- Step 1: Create deep copies of all nodes and store the mapping
- Step 2: Set the next and random pointers for the copied nodes
- Return the head of the new copied list

### Code

{% include code-tabs-file.html problem="copylinkedlistwithrandompointer" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Delete Middle Node Of Linked List

<span id="deletemiddlenodeoflinkedlist"></span>

### Problem

**Deletemiddlenodeoflinkedlist**

**Function:** `Delete Middle` takes `head` (ListNode?) and returns **ListNode**.

**Key logic:**
- Two Pass Approach



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `currentNode`, `prevNode`, `index`, `n`

**Execution flow:**
- Two Pass Approach

### Code

{% include code-tabs-file.html problem="deletemiddlenodeoflinkedlist" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Node

<span id="insertintoasortedcircularlinkedlist"></span>

### Problem

**Insertintoasortedcircularlinkedlist**

**Function:** `Insert` takes `head` (Node?), `insertVal` (integer) and returns **Node**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `next`, `newNode`, `current`

### Code

{% include code-tabs-file.html problem="insertintoasortedcircularlinkedlist" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Intersection Of Two Linked List

<span id="intersectionoftwolinkedlist"></span>

### Problem

**Intersectionoftwolinkedlist**

**Function:** `Get Intersection Node` takes `headA` (ListNode?), `headB` (ListNode?) and returns **ListNode**.

**Key logic:**
- Traverse both lists. When one pointer reaches the end, redirect it to the head of the other list.
- This will return the intersection node, or null if no intersection.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `pA`, `pB`

**Execution flow:**
- Traverse both lists. When one pointer reaches the end, redirect it to the head of the other list.
- This will return the intersection node, or null if no intersection.

### Code

{% include code-tabs-file.html problem="intersectionoftwolinkedlist" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Linked List Cycle

<span id="linkedlistcycle"></span>

### Problem

**Linkedlistcycle**

**Function:** `Has Cycle` takes `head` (ListNode?) and returns **boolean**.

**Key logic:**
- Better version



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `slow`, `fast`, `slow`, `fast`

**Execution flow:**
- Better version

### Code

{% include code-tabs-file.html problem="linkedlistcycle" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Linked List Cycle_II

<span id="linkedlistcycle_ii"></span>

### Problem

**Linkedlistcycle Ii**

**Function:** `Detect Cycle` takes `head` (ListNode?) and returns **ListNode**.

**Key logic:**
- Phase 1: Detect if a cycle exists
- Cycle detected
- Phase 2: Find the start of the cycle
- No cycle



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `slow`, `fast`, `entry`

**Execution flow:**
- Phase 1: Detect if a cycle exists
- Cycle detected
- Phase 2: Find the start of the cycle

### Code

{% include code-tabs-file.html problem="linkedlistcycle_ii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Merge K Sorted List

<span id="mergeksortedlist"></span>

### Problem

**Mergeksortedlist**

**Function:** `Merge Two Lists` takes `list1` (ListNode?), `list2` (ListNode?) and returns **ListNode**.

**Key logic:**
- dummy node



### Approach

**Solution Approach:**
1. The main function `mergeTwoLists` processes the input
2. Uses helper functions: mergeKLists, merge

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `head`, `ptr`, `ptr1`, `ptr2`, `mid`, `left`, `right`

**Execution flow:**

### Code

{% include code-tabs-file.html problem="mergeksortedlist" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Merge K Sorted List Iterative

<span id="mergeksortedlistiterative"></span>

### Problem

**Mergeksortedlistiterative**

**Function:** `Merge Klists` takes `lists` (Array<ListNode?>) and returns **ListNode**.

**Key logic:**
- Dummy node



### Approach

**Solution Approach:**
1. The main function `mergeKLists` processes the input
2. Uses helper functions: mergeTwoLists

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `interval`, `n`, `step`, `head`, `ptr`, `ptr1`, `ptr2`

**Execution flow:**

### Code

{% include code-tabs-file.html problem="mergeksortedlistiterative" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Merge Two Sorted L Ist

<span id="mergetwosortedlist"></span>

### Problem

**Mergetwosortedlist**

**Function:** `Merge Two Lists` takes `list1` (ListNode?), `list2` (ListNode?) and returns **ListNode**.

**Key logic:**
- dummy node



### Approach

**Solution Approach:**
1. The main function `mergeTwoLists` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `head`, `ptr`, `ptr1`, `ptr2`

**Execution flow:**

### Code

{% include code-tabs-file.html problem="mergetwosortedlist" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Odd Even Linked List

<span id="oddevenlinkedlist"></span>

### Problem

**Oddevenlinkedlist**

**Function:** `Odd Even List` takes `head` (ListNode?) and returns **ListNode**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `odd`, `even`, `evenHead`

### Code

{% include code-tabs-file.html problem="oddevenlinkedlist" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Palindrome Linked List

<span id="palindromelinkedlist"></span>

### Problem

**Palindromelinkedlist**

**Function:** `Is Palindrome` takes `head` (ListNode?) and returns **boolean**.

**Key logic:**
- Edge case: empty or single node
- Step 1: Find the middle
- Step 2: Reverse second half
- Step 3: Compare both halves
- Step 4: Restore original list (optional)



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `slow`, `fast`, `secondHalf`, `firstHalf`, `temp`, `prev`, `curr`, `next`

**Execution flow:**
- Edge case: empty or single node
- Step 1: Find the middle
- Step 2: Reverse second half
- Step 3: Compare both halves
- Step 4: Restore original list (optional)

### Code

{% include code-tabs-file.html problem="palindromelinkedlist" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Remove Nth Node From End Of List

<span id="removenthnodefromendoflist"></span>

### Problem

**Removenthnodefromendoflist**

**Function:** `Remove Nth From End` takes `head` (ListNode?), `n` (integer) and returns **ListNode**.

**Key logic:**
- Move first n + 1 steps ahead
- Move first to the end, maintaining the gap of size n
- Remove the nth node from the end



### Approach

**Solution Approach:**
1. The main function `removeNthFromEnd` processes the input
2. Uses helper functions: removeNthFromFront, removeNthFromEndTwoPointer

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `size`, `ptr`, `indexToRemove`, `ptr`, `prev`, `dummy`, `first`, `second`

**Execution flow:**
- Move first n + 1 steps ahead
- Move first to the end, maintaining the gap of size n
- Remove the nth node from the end

### Code

{% include code-tabs-file.html problem="removenthnodefromendoflist" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Reverse Linked List

<span id="reverselinkedlist"></span>

### Problem

**Reverselinkedlist**

**Function:** `Reverse List` takes `head` (ListNode?) and returns **ListNode**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `reversedHead`

### Code

{% include code-tabs-file.html problem="reverselinkedlist" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Reverse Linked List Iterative

<span id="reverselinkedlistiterative"></span>

### Problem

**Reverselinkedlistiterative**

**Function:** `Reverse List` takes `head` (ListNode?) and returns **ListNode**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `prev`, `current`, `nextTemp`

### Code

{% include code-tabs-file.html problem="reverselinkedlistiterative" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Reverse Nodes In K Groups

<span id="reversenodesinkgroups"></span>

### Problem

**Reversenodesinkgroups**

**Function:** `Reverse Kgroup` takes `head` (ListNode?), `k` (integer) and returns **ListNode**.

**Key logic:**
- Move `end` k steps forward
- Not enough nodes to reverse
- Store the next group start
- Reverse the current group
- Connect the reversed group back to the list



### Approach

**Solution Approach:**
1. The main function `reverseKGroup` processes the input
2. Uses helper functions: reverse

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dummy`, `start`, `end`, `nextGroupStart`, `prev`, `current`, `stop`, `next`

**Execution flow:**
- Move `end` k steps forward
- Not enough nodes to reverse
- Store the next group start
- Reverse the current group
- Connect the reversed group back to the list
- Move `start` to `newEnd` (which was the original `start` before reversing)
- Set `end` back to `start` for the next iteration
- `end` is the new start and `start` is the new end after reversing

### Code

{% include code-tabs-file.html problem="reversenodesinkgroups" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Key Takeaways

1. **Core pattern recognition** — Linked lists are about pointer rearrangement. Key patterns: slow/fast pointers, dummy heads, recursion, and in-place reversal.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

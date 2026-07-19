---
layout: chapter
title: "Trees"
chapter_number: 5
chapter_title: "Trees"
toc: true
prev_chapter:
  url: "/chapters/04-linked-lists.html"
  title: "Linked Lists"
next_chapter:
  url: "/chapters/06-graphs.html"
  title: "Graphs"
---

# Trees

> **46 problems** — Master tree traversals, BST operations, and recursive tree algorithms.

## The Pattern

Trees are recursive data structures. Master: DFS (pre/in/post-order), BFS (level-order), and BST properties.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [All Nodes Distance Kin Binary Tree](#allnodesdistancekinbinarytree) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Average Of Levels In Binary Tree](#averageoflevelsinbinarytree) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Balanced Binary Tree](#balancedbinarytree) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [B Inary Tree In Order Traversal Iterative](#binarytreeinordertraversaliterative) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [Binary Tree Level Order Traversal](#binarytreelevelordertraversal) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Binary Tree Level Order Traversal_II](#binarytreelevelordertraversal_ii) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [Binary Tree Maximum Path Sum](#binarytreemaximumpathsum) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [Binary Tree Right Side View](#binarytreerightsideview) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Binary Tree Vertical Order Traversal](#binarytreeverticalordertraversal) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Binary Tree Vertical Order Traversal_Without Sorting](#binarytreeverticalordertraversal_withoutsorting) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [Binary Tree Zig Zag Level Order Traversal](#binarytreezigzaglevelordertraversal) | — | <span class="badge badge-medium">Medium</span> |
| 12 | [Boundary Of Binary Tree](#boundaryofbinarytree) | — | <span class="badge badge-medium">Medium</span> |
| 13 | [BST Iterator](#bstiterator) | — | <span class="badge badge-medium">Medium</span> |
| 14 | [Check Completeness Of Binary Tree](#checkcompletenessofbinarytree) | — | <span class="badge badge-medium">Medium</span> |
| 15 | [Closest Binary Search Tree Value](#closestbinarysearchtreevalue) | — | <span class="badge badge-medium">Medium</span> |
| 16 | [Construct Binary Tree From Inorder And Post Order Traversal](#constructbinarytreefrominorderandpostordertraversal) | — | <span class="badge badge-medium">Medium</span> |
| 17 | [Construct Binary Tree From Preorder And In Order Traversal](#constructbinarytreefrompreorderandinordertraversal) | — | <span class="badge badge-medium">Medium</span> |
| 18 | [Construct Binary Tree From String](#constructbinarytreefromstring) | — | <span class="badge badge-medium">Medium</span> |
| 19 | [Convert B Inary Search Tree To Sorted Doubly Linked List](#convertbinarysearchtreetosorteddoublylinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 20 | [Count Good Node In B Inary Tree](#countgoodnodeinbinarytree) | — | <span class="badge badge-medium">Medium</span> |
| 21 | [Tree Node](#countnodeequalsaverage) | — | <span class="badge badge-medium">Medium</span> |
| 22 | [Tree Node](#deletenodeinabst) | — | <span class="badge badge-medium">Medium</span> |
| 23 | [Find Largest Value In Each Tree Row](#findlargestvalueineachtreerow) | — | <span class="badge badge-medium">Medium</span> |
| 24 | [Inorder Successor](#inordersuccessor) | — | <span class="badge badge-medium">Medium</span> |
| 25 | [Leaf Similar](#leafsimilar) | — | <span class="badge badge-medium">Medium</span> |
| 26 | [Longest Univalue Path](#longestunivaluepath) | — | <span class="badge badge-medium">Medium</span> |
| 27 | [Lowest Common Ancestor](#lowestcommonancestor) | — | <span class="badge badge-medium">Medium</span> |
| 28 | [Lowest Common Ancestor_III](#lowestcommonancestor_iii) | — | <span class="badge badge-medium">Medium</span> |
| 29 | [Maximum Depth Of Binary Tree](#maximumdepthofbinarytree) | — | <span class="badge badge-medium">Medium</span> |
| 30 | [Maximum Sum BST In Binary Tree](#maximumsumbstinbinarytree) | — | <span class="badge badge-medium">Medium</span> |
| 31 | [Maximum Width Of Binary Tree](#maximumwidthofbinarytree) | — | <span class="badge badge-medium">Medium</span> |
| 32 | [Minimum Time To Collect All Apples In A Tree](#minimumtimetocollectallapplesinatree) | — | <span class="badge badge-medium">Medium</span> |
| 33 | [Path Sum](#pathsum) | — | <span class="badge badge-medium">Medium</span> |
| 34 | [Path Sum_II](#pathsum_ii) | — | <span class="badge badge-medium">Medium</span> |
| 35 | [Path Sum III](#pathsumiii) | — | <span class="badge badge-medium">Medium</span> |
| 36 | [Populate Next Right Pointers In Each Node_II](#populatenextrightpointersineachnode_ii) | — | <span class="badge badge-medium">Medium</span> |
| 37 | [Populate Next Right Pointers In Each Node_II_Constant](#populatenextrightpointersineachnode_ii_constant) | — | <span class="badge badge-medium">Medium</span> |
| 38 | [Node](#populatingnextrightpointerineachnode) | — | <span class="badge badge-medium">Medium</span> |
| 39 | [Range Sum Of BST](#rangesumofbst) | — | <span class="badge badge-medium">Medium</span> |
| 40 | [Recover A Tree From Pre Order Traversal](#recoveratreefrompreordertraversal) | — | <span class="badge badge-medium">Medium</span> |
| 41 | [Recover Binary Search Tree](#recoverbinarysearchtree) | — | <span class="badge badge-medium">Medium</span> |
| 42 | [Codec](#serializeanddeserializeabinarytree) | — | <span class="badge badge-medium">Medium</span> |
| 43 | [Serialize And Deserialize N Array Tree](#serializeanddeserializenarraytree) | — | <span class="badge badge-medium">Medium</span> |
| 44 | [Step By Step Directions From A Node To Another](#stepbystepdirectionsfromanodetoanother) | — | <span class="badge badge-medium">Medium</span> |
| 45 | [Sum Root To Leaf Numbers](#sumroottoleafnumbers) | — | <span class="badge badge-medium">Medium</span> |
| 46 | [Vertical Order Traversal Of A Binary Tree](#verticalordertraversalofabinarytree) | — | <span class="badge badge-medium">Medium</span> |

---

## All Nodes Distance Kin Binary Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Average Of Levels In Binary Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Balanced Binary Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## B Inary Tree In Order Traversal Iterative
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Binary Tree Level Order Traversal
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Binary Tree Level Order Traversal_II
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Binary Tree Maximum Path Sum
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Binary Tree Right Side View
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Binary Tree Vertical Order Traversal
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Binary Tree Vertical Order Traversal_Without Sorting
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Binary Tree Zig Zag Level Order Traversal
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Boundary Of Binary Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## BST Iterator
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Check Completeness Of Binary Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Closest Binary Search Tree Value
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Construct Binary Tree From Inorder And Post Order Traversal
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(n) |
---
## Construct Binary Tree From Preorder And In Order Traversal
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(n) |
---
## Construct Binary Tree From String
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Convert B Inary Search Tree To Sorted Doubly Linked List
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Count Good Node In B Inary Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Tree Node
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Tree Node
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Find Largest Value In Each Tree Row
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Inorder Successor
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Leaf Similar
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Longest Univalue Path
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Lowest Common Ancestor
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(1) |
---
## Lowest Common Ancestor_III
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Maximum Depth Of Binary Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Maximum Sum BST In Binary Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Maximum Width Of Binary Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Minimum Time To Collect All Apples In A Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Path Sum
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Path Sum_II
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Path Sum III
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Populate Next Right Pointers In Each Node_II
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Populate Next Right Pointers In Each Node_II_Constant
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Node
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Range Sum Of BST
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Recover A Tree From Pre Order Traversal
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Recover Binary Search Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Codec
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Serialize And Deserialize N Array Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Step By Step Directions From A Node To Another
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Sum Root To Leaf Numbers
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Vertical Order Traversal Of A Binary Tree
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(V + E) |
| **Space** | O(V) |
---
## Key Takeaways

1. **Core pattern recognition** — Trees are recursive data structures. Master: DFS (pre/in/post-order), BFS (level-order), and BST properties.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

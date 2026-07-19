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

<span id="allnodesdistancekinbinarytree"></span>

### Problem

**Allnodesdistancekinbinarytree**

**Function:** `Distance K` takes `root` (TreeNode?), `target` (TreeNode?), `k` (integer) and returns **List**.

**Key logic:**
- To store parent references
- Helper function to perform DFS and populate parent map, then find target
- Start DFS from the root to populate parentMap and find the target
- Function to collect nodes at distance K from the target node
- If distance is 0, add node's value to result



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `parentMap`, `result`

**Execution flow:**
- To store parent references
- Helper function to perform DFS and populate parent map, then find target
- Start DFS from the root to populate parentMap and find the target
- Function to collect nodes at distance K from the target node
- If distance is 0, add node's value to result
- Explore parent node

### Code

{% include code-tabs-file.html problem="allnodesdistancekinbinarytree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Average Of Levels In Binary Tree

<span id="averageoflevelsinbinarytree"></span>

### Problem

**Averageoflevelsinbinarytree**

**Function:** `Average Of Levels` takes `root` (TreeNode?) and returns **doubleArray**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `queue`, `sum`, `size`, `node`

### Code

{% include code-tabs-file.html problem="averageoflevelsinbinarytree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Balanced Binary Tree

<span id="balancedbinarytree"></span>

### Problem

**Balancedbinarytree**

**Function:** `Is Balanced` takes `root` (TreeNode?) and returns **boolean**.

**Key logic:**
- If subtree is unbalanced, return -1 to signal it
- Return the height of the tree rooted at this node



### Approach

**Solution Approach:**
1. The main function `isBalanced` processes the input
2. Uses helper functions: checkHeight

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `leftHeight`, `rightHeight`

**Execution flow:**
- If subtree is unbalanced, return -1 to signal it
- Return the height of the tree rooted at this node

### Code

{% include code-tabs-file.html problem="balancedbinarytree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## B Inary Tree In Order Traversal Iterative

<span id="binarytreeinordertraversaliterative"></span>

### Problem

**Binarytreeinordertraversaliterative**

**Function:** `Inorder Traversal` takes `root` (TreeNode?) and returns **List**.

**Key logic:**
- Traverse to the leftmost node
- Visit the node
- Move to the right subtree



### Approach

**Stack-Based Approach:**
1. Process elements left to right
2. Maintain a stack that tracks relevant previous elements
3. Pop from stack when current element breaks a monotonic property


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `stack`, `result`, `current`

**Execution flow:**
- Traverse to the leftmost node
- Visit the node
- Move to the right subtree

### Code

{% include code-tabs-file.html problem="binarytreeinordertraversaliterative" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Binary Tree Level Order Traversal

<span id="binarytreelevelordertraversal"></span>

### Problem

**Binarytreelevelordertraversal**

**Function:** `Level Order` takes `root` (TreeNode?) and returns **List**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `queue`, `lst`, `size`, `temp`

### Code

{% include code-tabs-file.html problem="binarytreelevelordertraversal" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Binary Tree Level Order Traversal_II

<span id="binarytreelevelordertraversal_ii"></span>

### Problem

**Binarytreelevelordertraversal Ii**

**Function:** `Level Order Bottom` takes `root` (TreeNode?) and returns **List**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `queue`, `size`, `currentLevel`, `node`

### Code

{% include code-tabs-file.html problem="binarytreelevelordertraversal_ii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Binary Tree Maximum Path Sum

<span id="binarytreemaximumpathsum"></span>

### Problem

**Binarytreemaximumpathsum**

**Function:** `Max Path Sum` takes `root` (TreeNode?) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `maxPathSum` processes the input
2. Uses helper functions: getMaxPathSum

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `ans`, `left`, `right`, `currentMax`, `maxSoFar`

### Code

{% include code-tabs-file.html problem="binarytreemaximumpathsum" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Binary Tree Right Side View

<span id="binarytreerightsideview"></span>

### Problem

**Binarytreerightsideview**

**Function:** `Right Side View` takes `root` (TreeNode?) and returns **List**.



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `rightSide`

### Code

{% include code-tabs-file.html problem="binarytreerightsideview" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Binary Tree Vertical Order Traversal

<span id="binarytreeverticalordertraversal"></span>

### Problem

**Binarytreeverticalordertraversal**

**Function:** `Vertical Order` takes `root` (TreeNode?) and returns **List**.

**Key logic:**
- fun verticalOrder(root: TreeNode?): List<List<Int>> {
- val result = TreeMap<Int, LinkedList<Int>>()
- //        fun dfs(node: TreeNode?, verticalIndex: Int = 0) {
- if (node == null)
- return



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `bucket`, `node`, `verticalIndex`, `result`, `queue`

**Execution flow:**
- fun verticalOrder(root: TreeNode?): List<List<Int>> {
- val result = TreeMap<Int, LinkedList<Int>>()
- //        fun dfs(node: TreeNode?, verticalIndex: Int = 0) {
- if (node == null)
- val bucket = result.getOrPut(verticalIndex) { LinkedList() }
- //            bucket.add(node.`val`)
- dfs(node.left, verticalIndex - 1)

### Code

{% include code-tabs-file.html problem="binarytreeverticalordertraversal" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Binary Tree Vertical Order Traversal_Without Sorting

<span id="binarytreeverticalordertraversal_withoutsorting"></span>

### Problem

**Binarytreeverticalordertraversal Withoutsorting**

**Function:** `Vertical Order` takes `root` (TreeNode?) and returns **List**.

**Key logic:**
- Update min and max column indices



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `node`, `verticalIndex`, `columnTable`, `minColumn`, `maxColumn`, `queue`, `result`

**Execution flow:**
- Update min and max column indices

### Code

{% include code-tabs-file.html problem="binarytreeverticalordertraversal_withoutsorting" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Binary Tree Zig Zag Level Order Traversal

<span id="binarytreezigzaglevelordertraversal"></span>

### Problem

**Binarytreezigzaglevelordertraversal**

**Function:** `Zigzag Level Order` takes `root` (TreeNode?) and returns **List**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `node`, `index`, `result`, `queue`, `level`, `levelSize`, `currentLevel`

### Code

{% include code-tabs-file.html problem="binarytreezigzaglevelordertraversal" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Boundary Of Binary Tree

<span id="boundaryofbinarytree"></span>

### Problem

**Boundaryofbinarytree**

**Function:** `Boundary Of Binary Tree` takes `root` (TreeNode?) and returns **List**.

**Key logic:**
- Step 1: Add the root node
- Step 2: Add the left boundary (excluding leaves)
- Step 3: Add all leaf nodes (excluding root if it is a leaf)
- Step 4: Add the right boundary (excluding leaves, in reverse order)
- Don't add leaf nodes to the left boundary



### Approach

**Solution Approach:**
1. The main function `boundaryOfBinaryTree` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `rightBoundary`, `current`, `current`

**Execution flow:**
- Step 1: Add the root node
- Step 2: Add the left boundary (excluding leaves)
- Step 3: Add all leaf nodes (excluding root if it is a leaf)
- Step 4: Add the right boundary (excluding leaves, in reverse order)
- Don't add leaf nodes to the left boundary
- Move down the left child, or the right if left is null
- If it's a leaf node and it's not the root, add it to the result
- Otherwise, continue the traversal for both subtrees

### Code

{% include code-tabs-file.html problem="boundaryofbinarytree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## BST Iterator

<span id="bstiterator"></span>

### Problem

**Bstiterator**

**Function:** `Next` takes none and returns **integer**.

**Key logic:**
- Initialize the stack by adding all the leftmost nodes
- Push all the left nodes of a given node to the stack
- Returns the next smallest number
- Pop the node from the stack
- Push the leftmost nodes of the right child, if any



### Approach

**Stack-Based Approach:**
1. Process elements left to right
2. Maintain a stack that tracks relevant previous elements
3. Pop from stack when current element breaks a monotonic property


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `stack`, `current`, `node`, `obj`, `param_1`, `param_2`

**Execution flow:**
- Initialize the stack by adding all the leftmost nodes
- Push all the left nodes of a given node to the stack
- Returns the next smallest number
- Pop the node from the stack
- Push the leftmost nodes of the right child, if any
- Returns whether we have a next smallest number
- If the stack is not empty, there are more nodes to visit

### Code

{% include code-tabs-file.html problem="bstiterator" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Check Completeness Of Binary Tree

<span id="checkcompletenessofbinarytree"></span>

### Problem

**Checkcompletenessofbinarytree**

**Function:** `Is Complete Tree` takes `root` (TreeNode?) and returns **boolean**.

**Key logic:**
- Edge case: An empty tree is considered complete
- A flag to indicate if a null node has been encountered
- If we have already seen a null node, we shouldn't encounter any non-null nodes after that.
- If we encounter a non-null node after a null node, it's not complete



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `queue`, `foundNull`, `current`

**Execution flow:**
- Edge case: An empty tree is considered complete
- A flag to indicate if a null node has been encountered
- If we have already seen a null node, we shouldn't encounter any non-null nodes after that.
- If we encounter a non-null node after a null node, it's not complete

### Code

{% include code-tabs-file.html problem="checkcompletenessofbinarytree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Closest Binary Search Tree Value

<span id="closestbinarysearchtreevalue"></span>

### Problem

**Closestbinarysearchtreevalue**

**Function:** `Closest Value` takes `root` (TreeNode?), `target` (Double) and returns **integer**.

**Key logic:**
- Update closest based on the given conditions:
- Move to the left or right subtree based on the target



### Approach

**Solution Approach:**
1. The main function `closestValue` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `closest`, `current`, `currentValue`

**Execution flow:**
- Update closest based on the given conditions:
- Move to the left or right subtree based on the target

### Code

{% include code-tabs-file.html problem="closestbinarysearchtreevalue" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Construct Binary Tree From Inorder And Post Order Traversal

<span id="constructbinarytreefrominorderandpostordertraversal"></span>

### Problem

**Constructbinarytreefrominorderandpostordertraversal**

**Function:** `Build Tree` takes `inorder` (array of integers), `postorder` (array of integers) and returns **TreeNode**.

**Key logic:**
- Build Inverted InOrder Index Map
- Build right subtree first
- Build left subtree



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `rootIndices`, `postIndex`, `rootVal`

**Execution flow:**
- Build Inverted InOrder Index Map
- Build right subtree first
- Build left subtree

### Code

{% include code-tabs-file.html problem="constructbinarytreefrominorderandpostordertraversal" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Construct Binary Tree From Preorder And In Order Traversal

<span id="constructbinarytreefrompreorderandinordertraversal"></span>

### Problem

**Constructbinarytreefrompreorderandinordertraversal**

**Function:** `Build Tree` takes `preorder` (array of integers), `inorder` (array of integers) and returns **TreeNode**.

**Key logic:**
- Build Inverted InOrder Index Map



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `rootIndices`, `rootIndex`, `rootVal`

**Execution flow:**
- Build Inverted InOrder Index Map

### Code

{% include code-tabs-file.html problem="constructbinarytreefrompreorderandinordertraversal" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Construct Binary Tree From String

<span id="constructbinarytreefromstring"></span>

### Problem

**Constructbinarytreefromstring**

**Function:** `Str2Tree` takes `s` (string) and returns **TreeNode**.

**Key logic:**
- We are only interested in the tree root, not the index
- Handle negative numbers
- Skip over digits
- Check for left child (subtree)
- Skip '('



### Approach

**Solution Approach:**
1. The main function `str2tree` processes the input
2. Uses helper functions: buildTree

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `currentIndex`, `start`, `valStr`, `root`, `leftResult`, `rightResult`

**Execution flow:**
- We are only interested in the tree root, not the index
- Handle negative numbers
- Skip over digits
- Check for left child (subtree)
- Update index after processing left subtree
- Check for right child (subtree)

### Code

{% include code-tabs-file.html problem="constructbinarytreefromstring" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Convert B Inary Search Tree To Sorted Doubly Linked List

<span id="convertbinarysearchtreetosorteddoublylinkedlist"></span>

### Problem

**Convertbinarysearchtreetosorteddoublylinkedlist**

**Function:** `Tree To Doubly List` takes `root` (Node?) and returns **Node**.

**Key logic:**
- Perform in-order traversal and link nodes
- Complete the doubly linked list by linking head and tail
- Traverse left subtree
- Link the current node with the previous node (tail)
- This is the first node (head of the doubly linked list)



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `left`, `right`, `head`, `tail`

**Execution flow:**
- Perform in-order traversal and link nodes
- Complete the doubly linked list by linking head and tail
- Traverse left subtree
- Link the current node with the previous node (tail)
- This is the first node (head of the doubly linked list)
- Update the tail to the current node
- Traverse right subtree

### Code

{% include code-tabs-file.html problem="convertbinarysearchtreetosorteddoublylinkedlist" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Count Good Node In B Inary Tree

<span id="countgoodnodeinbinarytree"></span>

### Problem

**Countgoodnodeinbinarytree**

**Function:** `Good Nodes` takes `root` (TreeNode?) and returns **integer**.



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `newMax`, `good`

### Code

{% include code-tabs-file.html problem="countgoodnodeinbinarytree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Tree Node

<span id="countnodeequalsaverage"></span>

### Problem

**Countnodeequalsaverage**

**Function:** `Average Of Subtree` takes `root` (TreeNode?) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `averageOfSubtree` processes the input
2. Uses helper functions: postOrder

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `sum`, `count`, `count`, `left`, `right`, `nodeSum`

### Code

{% include code-tabs-file.html problem="countnodeequalsaverage" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Tree Node

<span id="deletenodeinabst"></span>

### Problem

**Deletenodeinabst**

**Function:** `Delete Node` takes `root` (TreeNode?), `key` (integer) and returns **TreeNode**.



### Approach

**Solution Approach:**
1. The main function `deleteNode` processes the input
2. Uses helper functions: minValue

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `current`

### Code

{% include code-tabs-file.html problem="deletenodeinabst" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Find Largest Value In Each Tree Row

<span id="findlargestvalueineachtreerow"></span>

### Problem

**Findlargestvalueineachtreerow**

**Function:** `Largest Values` takes `root` (TreeNode?) and returns **List**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `queue`, `size`, `max`, `current`

### Code

{% include code-tabs-file.html problem="findlargestvalueineachtreerow" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Inorder Successor

<span id="inordersuccessor"></span>

### Problem

**Inordersuccessor**

**Function:** `Inorder Successor` takes `root` (TreeNode?), `p` (TreeNode?) and returns **TreeNode**.

**Key logic:**
- If p's value is less than current, the successor is possibly current
- If p's value is greater or equal to current, move to the right subtree



### Approach

**Solution Approach:**
1. The main function `inorderSuccessor` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `successor`, `current`

**Execution flow:**
- If p's value is less than current, the successor is possibly current
- If p's value is greater or equal to current, move to the right subtree

### Code

{% include code-tabs-file.html problem="inordersuccessor" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Leaf Similar

<span id="leafsimilar"></span>

### Problem

**Leafsimilar**

**Function:** `Leaf Similar` takes `root1` (TreeNode?), `root2` (TreeNode?) and returns **boolean**.



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `leaves1`, `leaves2`

### Code

{% include code-tabs-file.html problem="leafsimilar" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Longest Univalue Path

<span id="longestunivaluepath"></span>

### Problem

**Longestunivaluepath**

**Function:** `Longest Univalue Path` takes `root` (TreeNode?) and returns **integer**.

**Key logic:**
- Get the maximum univalue chain from both left and right
- Compute the branch lengthes if
- Take maximum of max found so far , OD
- We can only propagate the maximum branch chain b/w left and right



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `maxLength`, `left`, `right`, `currentLeft`, `currentRight`

**Execution flow:**
- Get the maximum univalue chain from both left and right
- Compute the branch lengthes if
- Take maximum of max found so far , OD
- We can only propagate the maximum branch chain b/w left and right

### Code

{% include code-tabs-file.html problem="longestunivaluepath" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Lowest Common Ancestor

<span id="lowestcommonancestor"></span>

### Problem

**Lowestcommonancestor**

**Function:** `Lowest Common Ancestor` takes `root` (TreeNode?), `p` (TreeNode?), `q` (TreeNode?) and returns **TreeNode**.



### Approach

**Solution Approach:**
1. The main function `lowestCommonAncestor` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`

### Code

{% include code-tabs-file.html problem="lowestcommonancestor" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(1) space comes from the auxiliary data structures used.

---

## Lowest Common Ancestor_III

<span id="lowestcommonancestor_iii"></span>

### Problem

**Lowestcommonancestor Iii**

**Function:** `Lowest Common Ancestor` takes `p` (Node?), `q` (Node?) and returns **Node**.

**Key logic:**
- Move parent1 upwards, or switch to q if it becomes null
- Move parent2 upwards, or switch to p if it becomes null
- parent1 and parent2 are now pointing to the same node, which is the LCA



### Approach

**Solution Approach:**
1. The main function `lowestCommonAncestor` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `parent`, `parent1`, `parent2`

**Execution flow:**
- Move parent1 upwards, or switch to q if it becomes null
- Move parent2 upwards, or switch to p if it becomes null
- parent1 and parent2 are now pointing to the same node, which is the LCA

### Code

{% include code-tabs-file.html problem="lowestcommonancestor_iii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Maximum Depth Of Binary Tree

<span id="maximumdepthofbinarytree"></span>

### Problem

**Maximumdepthofbinarytree**

**Function:** `Max Depth` takes `root` (TreeNode?) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `maxDepth` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

### Code

{% include code-tabs-file.html problem="maximumdepthofbinarytree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Maximum Sum BST In Binary Tree

<span id="maximumsumbstinbinarytree"></span>

### Problem

**Maximumsumbstinbinarytree**

**Function:** `Max Sum Bst` takes `root` (TreeNode?) and returns **integer**.

**Key logic:**
- Base case: if the node is null, it's trivially a BST with sum = 0
- Recursively traverse the left and right subtrees
- Check if the current node is a valid BST
- Current node is part of a valid BST
- Update the global max sum if needed



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `isBST`, `sum`, `min`, `max`, `maxSum`, `left`, `right`, `sum`

**Execution flow:**
- Base case: if the node is null, it's trivially a BST with sum = 0
- Recursively traverse the left and right subtrees
- Check if the current node is a valid BST
- Current node is part of a valid BST
- Update the global max sum if needed
- Return the result for this subtree
- If it's not a valid BST, return invalid information

### Code

{% include code-tabs-file.html problem="maximumsumbstinbinarytree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Maximum Width Of Binary Tree

<span id="maximumwidthofbinarytree"></span>

### Problem

**Maximumwidthofbinarytree**

**Function:** `Width Of Binary Tree` takes `root` (TreeNode?) and returns **integer**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `node`, `index`, `queue`, `max`, `size`, `left`, `right`, `current`

### Code

{% include code-tabs-file.html problem="maximumwidthofbinarytree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Minimum Time To Collect All Apples In A Tree

<span id="minimumtimetocollectallapplesinatree"></span>

### Problem

**Minimumtimetocollectallapplesinatree**

**Function:** `Min Time` takes `n` (integer), `edges` (Array<array of integers>), `hasApple` (List<boolean>) and returns **integer**.

**Key logic:**
- Build the graph as a list of lists (adjacency list representation)
- DFS function to calculate the total time
- Use forEach to iterate over each neighbor
- If the time is greater than 0 or the neighbor has an apple, add the time and return time (2)
- Start DFS from node 0 with no parent (-1)



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `graph`, `totalTime`, `time`

**Execution flow:**
- Build the graph as a list of lists (adjacency list representation)
- DFS function to calculate the total time
- Use forEach to iterate over each neighbor
- If the time is greater than 0 or the neighbor has an apple, add the time and return time (2)
- Start DFS from node 0 with no parent (-1)

### Code

{% include code-tabs-file.html problem="minimumtimetocollectallapplesinatree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Path Sum

<span id="pathsum"></span>

### Problem

**Pathsum**

**Function:** `Has Path Sum` takes `root` (TreeNode?), `targetSum` (integer) and returns **boolean**.



### Approach

**Solution Approach:**
1. The main function `hasPathSum` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

### Code

{% include code-tabs-file.html problem="pathsum" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Path Sum_II

<span id="pathsum_ii"></span>

### Problem

**Pathsum Ii**

**Function:** `Path Sum` takes `root` (TreeNode?), `targetSum` (integer) and returns **List**.

**Key logic:**
- Add the current node's value to the path
- If the node is a leaf and the path sum equals targetSum, add the path to the result
- copy the current path list and add
- Continue the search on the left and right subtree
- Backtrack: remove the current node from the path



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`

**Execution flow:**
- Add the current node's value to the path
- If the node is a leaf and the path sum equals targetSum, add the path to the result
- copy the current path list and add
- Continue the search on the left and right subtree
- Backtrack: remove the current node from the path

### Code

{% include code-tabs-file.html problem="pathsum_ii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Path Sum III

<span id="pathsumiii"></span>

### Problem

**Pathsumiii**

**Function:** `Path Sum` takes `root` (TreeNode?), `targetSum` (integer) and returns **integer**.

**Key logic:**
- O(N^2) solution
- Count paths with targetSum starting from the current node
- Start counting paths from the root
- Revisit I didn't understand
- HashMap to store prefix sums and their frequencies



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `newSum`, `count`, `prefixSumCount`, `newSum`, `pathCount`

**Execution flow:**
- O(N^2) solution
- Count paths with targetSum starting from the current node
- Start counting paths from the root
- Revisit I didn't understand
- HashMap to store prefix sums and their frequencies
- Initialize with a prefix sum of 0 having occurred once (considering no node)
- Helper function to perform DFS
- Calculate the current sum at the current node

### Code

{% include code-tabs-file.html problem="pathsumiii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Populate Next Right Pointers In Each Node_II

<span id="populatenextrightpointersineachnode_ii"></span>

### Problem

**Populatenextrightpointersineachnode Ii**

**Function:** `Connect` takes `root` (Node?) and returns **Node**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `queue`, `prev`, `node`

### Code

{% include code-tabs-file.html problem="populatenextrightpointersineachnode_ii" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Populate Next Right Pointers In Each Node_II_Constant

<span id="populatenextrightpointersineachnode_ii_constant"></span>

### Problem

**Populatenextrightpointersineachnode Ii Constant**

**Function:** `Connect` takes `root` (Node?) and returns **Node**.

**Key logic:**
- Traverse the current level
- Connect left child
- Connect right child
- Move to the next level



### Approach

**Solution Approach:**
1. The main function `connect` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `current`, `nextLevelStart`, `prev`, `node`

**Execution flow:**
- Traverse the current level
- Connect left child
- Connect right child
- Move to the next level

### Code

{% include code-tabs-file.html problem="populatenextrightpointersineachnode_ii_constant" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Node

<span id="populatingnextrightpointerineachnode"></span>

### Problem

**Populatingnextrightpointerineachnode**

**Function:** `Connect` takes `root` (Node?) and returns **Node**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `next`, `q`, `levelSize`, `prev`

### Code

{% include code-tabs-file.html problem="populatingnextrightpointerineachnode" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Range Sum Of BST

<span id="rangesumofbst"></span>

### Problem

**Rangesumofbst**

**Function:** `Range Sum Bst` takes `root` (TreeNode?), `low` (integer), `high` (integer) and returns **integer**.



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `sum`

### Code

{% include code-tabs-file.html problem="rangesumofbst" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Recover A Tree From Pre Order Traversal

<span id="recoveratreefrompreordertraversal"></span>

### Problem

**Recoveratreefrompreordertraversal**

**Function:** `Recover From Preorder` takes `traversal` (string) and returns **TreeNode**.

**Key logic:**
- Global index to track position in the string
- Recursive function to build the tree
- Base case: end of string
- Read the depth of the current node
- If the current depth doesn't match the expected depth, backtrack



### Approach

**Solution Approach:**
1. The main function `recoverFromPreorder` processes the input
2. Uses helper functions: buildTree

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `index`, `currentDepth`, `value`, `node`

**Execution flow:**
- Global index to track position in the string
- Recursive function to build the tree
- Base case: end of string
- Read the depth of the current node
- If the current depth doesn't match the expected depth, backtrack
- Rewind the index
- Read the value of the current node
- Create the current node

### Code

{% include code-tabs-file.html problem="recoveratreefrompreordertraversal" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Recover Binary Search Tree

<span id="recoverbinarysearchtree"></span>

### Problem

**Recoverbinarysearchtree**

**Key logic:**
- Helper function to perform in-order traversal
- Traverse left subtree
- Identify swapped nodes
- First out-of-order node
- Second out-of-order node



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `first`, `second`, `prev`, `temp`

**Execution flow:**
- Helper function to perform in-order traversal
- Traverse left subtree
- Identify swapped nodes
- First out-of-order node
- Second out-of-order node
- Update previous node
- Traverse right subtree
- Step 1: In-order traversal to find the swapped nodes

### Code

{% include code-tabs-file.html problem="recoverbinarysearchtree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Codec

<span id="serializeanddeserializeabinarytree"></span>

### Problem

**Serializeanddeserializeabinarytree**

**Function:** `Serialize` takes `root` (TreeNode?) and returns **string**.

**Key logic:**
- Encodes a URL to a shortened URL.
- Decodes the encoded string to tree using a recursive approach.



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `serializedTree`, `nodes`, `value`, `node`, `ser`, `deser`

**Execution flow:**
- Encodes a URL to a shortened URL.
- Decodes the encoded string to tree using a recursive approach.

### Code

{% include code-tabs-file.html problem="serializeanddeserializeabinarytree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Serialize And Deserialize N Array Tree

<span id="serializeanddeserializenarraytree"></span>

### Problem

**Serializeanddeserializenarraytree**

**Function:** `Serialize` takes `root` (Node?) and returns **string**.

**Key logic:**
- Encodes a tree to a single string.
- Deserialize with internal DFS
- Use destructuring declaration
- Create children using functional approach



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `children`, `tokens`, `index`, `node`

**Execution flow:**
- Encodes a tree to a single string.
- Deserialize with internal DFS
- Use destructuring declaration
- Create children using functional approach

### Code

{% include code-tabs-file.html problem="serializeanddeserializenarraytree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Step By Step Directions From A Node To Another

<span id="stepbystepdirectionsfromanodetoanother"></span>

### Problem

**Stepbystepdirectionsfromanodetoanother**

**Function:** `Find Node` takes `root` (TreeNode?), `searchKey` (integer) and returns **TreeNode**.

**Key logic:**
- No output for missing source or destination



### Approach

**Solution Approach:**
1. The main function `findNode` processes the input
2. Uses helper functions: lowestCommonAncestor, getDirections, buildPath

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `sourceNode`, `destNode`, `lca`, `sourcePath`, `destPath`, `upMoves`

**Execution flow:**
- No output for missing source or destination

### Code

{% include code-tabs-file.html problem="stepbystepdirectionsfromanodetoanother" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Sum Root To Leaf Numbers

<span id="sumroottoleafnumbers"></span>

### Problem

**Sumroottoleafnumbers**

**Function:** `Sum Numbers` takes `root` (TreeNode?) and returns **integer**.



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `sum`, `newSum`

### Code

{% include code-tabs-file.html problem="sumroottoleafnumbers" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Vertical Order Traversal Of A Binary Tree

<span id="verticalordertraversalofabinarytree"></span>

### Problem

**Verticalordertraversalofabinarytree**

**Function:** `Vertical Traversal` takes `root` (TreeNode?) and returns **List**.

**Key logic:**
- Update min and max column indices



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `node`, `verticalIndex`, `columnTable`, `minColumn`, `maxColumn`, `queue`, `result`

**Execution flow:**
- Update min and max column indices

### Code

{% include code-tabs-file.html problem="verticalordertraversalofabinarytree" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Key Takeaways

1. **Core pattern recognition** — Trees are recursive data structures. Master: DFS (pre/in/post-order), BFS (level-order), and BST properties.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

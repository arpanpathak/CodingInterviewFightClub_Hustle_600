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

```kotlin
package tree

class AllNodesDistanceKinBinaryTree {
    val parentMap = mutableMapOf<TreeNode, TreeNode?>()  // To store parent references

    fun distanceK(root: TreeNode?, target: TreeNode?, k: Int): List<Int> {
        val result = mutableListOf<Int>()

        // Helper function to perform DFS and populate parent map, then find target
        fun dfs(node: TreeNode?, parent: TreeNode?) {
            if (node == null) return
            parentMap[node] = parent
            if (node == target) collectNodesAtDistanceK(node, k, mutableSetOf(), result)
            dfs(node.left, node)
            dfs(node.right, node)
        }

        // Start DFS from the root to populate parentMap and find the target
        dfs(root, null)
        return result
    }

    // Function to collect nodes at distance K from the target node
    private fun collectNodesAtDistanceK(node: TreeNode?, k: Int, visited: MutableSet<TreeNode>, result: MutableList<Int>) {
        if (node == null || visited.contains(node)) return
        visited.add(node)

        when (k) {
            0 -> result.add(node.`val`)  // If distance is 0, add node's value to result
            else -> {
                collectNodesAtDistanceK(node.left, k - 1, visited, result)
                collectNodesAtDistanceK(node.right, k - 1, visited, result)
                collectNodesAtDistanceK(parentMap[node], k - 1, visited, result)  // Explore parent node
            }
        }
    }
}
```

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

```kotlin
package tree.bfs

import tree.TreeNode
import java.util.*

class AverageOfLevelsInBinaryTree {
    fun averageOfLevels(root: TreeNode?): DoubleArray {
        var result = mutableListOf<Double>()

        val queue = LinkedList<TreeNode>()

        queue.add(root!!)

        while (queue.isNotEmpty()) {
            var sum = 0.0
            val size = queue.size

            repeat(size) {
                val node = queue.poll()
                sum+= node.`val`

                node.left?.let{ queue.add(it) }
                node.right?.let{ queue.add(it) }

            }
            result.add(sum / size)
        }

        return result.toDoubleArray()
    }
}
```

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

```kotlin
package tree

import kotlin.math.abs

class BalancedBinaryTree {
    fun isBalanced(root: TreeNode?): Boolean {
        fun checkHeight(node: TreeNode?): Int {
            if (node == null) return 0

            val leftHeight = checkHeight(node.left)
            val rightHeight = checkHeight(node.right)

            // If subtree is unbalanced, return -1 to signal it
            if (leftHeight == -1 || rightHeight == -1 || abs(leftHeight - rightHeight) > 1) {
                return -1
            }

            // Return the height of the tree rooted at this node
            return 1 + maxOf(leftHeight, rightHeight)
        }

        return checkHeight(root) != -1
    }
}
```

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

```kotlin
package tree

class BInaryTreeInOrderTraversalIterative {
    fun inorderTraversal(root: TreeNode?): List<Int> {
        val stack = ArrayDeque<TreeNode>()
        val result = mutableListOf<Int>()
        var current = root

        while (current != null || stack.isNotEmpty()) {
            // Traverse to the leftmost node
            while (current != null) {
                stack.addLast(current)
                current = current.left
            }

            // Visit the node
            current = stack.removeLast()
            result.add(current.`val`)

            // Move to the right subtree
            current = current.right
        }

        return result
    }
}
```

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

```kotlin
package tree

import java.util.*
import kotlin.collections.ArrayList


class BinaryTreeLevelOrderTraversal {
    fun levelOrder(root: TreeNode?): List<List<Int>> {
        val result: MutableList<List<Int>> = ArrayList()
        if (root == null)
            return result
        val queue: Queue<TreeNode> = LinkedList()
        queue.add(root)

        while (!queue.isEmpty()) {
            val lst: MutableList<Int> = ArrayList()
            var size: Int = queue.size

            while (size-- > 0) {
                val temp: TreeNode = queue.poll()
                lst.add(temp.`val`)

                if (temp.left != null) queue.add(temp.left)

                if (temp.right != null) queue.add(temp.right)
            }

            result.add(lst)
        }
        return result
    }
}
```

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

```kotlin
package tree.bfs

import tree.TreeNode
import java.util.*

class BinaryTreeLevelOrderTraversal_II {
    fun levelOrderBottom(root: TreeNode?): List<List<Int>> {
        val result = LinkedList<List<Int>>()
        val queue = LinkedList<TreeNode>()

        if (root == null)
            return listOf()
        queue.add(root!!)

        while (queue.isNotEmpty()) {
            val size = queue.size
            val currentLevel = mutableListOf<Int>()
            repeat(size) {
                val node = queue.poll()
                currentLevel.add(node.`val`)

                node.left?.let{ queue.add(it) }
                node.right?.let{ queue.add(it) }

            }
            result.addFirst(currentLevel)
        }

        return result.toList()
    }
}
```

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

```kotlin
package tree

class BinaryTreeMaximumPathSum {
    fun maxPathSum(root: TreeNode?): Int {
        var ans = Int.MIN_VALUE
        fun getMaxPathSum(node: TreeNode?): Int {
            if (node == null) return 0

            val left = getMaxPathSum(node.left)
            val right = getMaxPathSum(node.right)
            val currentMax = maxOf(maxOf(left, right) + node.`val`, node.`val`)
            val maxSoFar = maxOf(currentMax, left + right + node.`val`)
            ans = maxOf(maxSoFar, ans)

            return currentMax
        }

        getMaxPathSum(root)
        return ans
    }
}
```

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

```kotlin
package tree

class BinaryTreeRightSideView {
    fun rightSideView(root: TreeNode?): List<Int> {
        val rightSide = mutableListOf<Int>()

        fun dfs(node: TreeNode?, level: Int) {
            when {
                node == null -> return
                level == rightSide.size -> rightSide.add(node.`val`)
            }

            dfs(node?.right, level + 1)
            dfs(node?.left, level + 1)
        }
        dfs(root, 0)
        return rightSide
    }
}
```

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

```kotlin
package tree

import java.util.*

class BinaryTreeVerticalOrderTraversal {
//    fun verticalOrder(root: TreeNode?): List<List<Int>> {
//        val result = TreeMap<Int, LinkedList<Int>>()
//
//        fun dfs(node: TreeNode?, verticalIndex: Int = 0) {
//            if (node == null)
//                return
//            val bucket = result.getOrPut(verticalIndex) { LinkedList() }
//
//            bucket.add(node.`val`)
//            dfs(node.left, verticalIndex - 1)
//            dfs(node.right, verticalIndex + 1)
//        }
//
//        dfs(root)
//
//        return result.map { it.value }
//    }

    // Define a data class for holding a node and its vertical index
    data class VerticalIndex(val node: TreeNode, val verticalIndex: Int)

    fun verticalOrder(root: TreeNode?): List<List<Int>> {
        if (root == null) return emptyList()

        val result = TreeMap<Int, ArrayList<Int>>()
        val queue: Queue<VerticalIndex> = LinkedList()

        // Start with the root node at vertical index 0
        queue.offer(VerticalIndex(root, 0))

        while (queue.isNotEmpty()) {
            val (node, verticalIndex) = queue.poll()

            // Add node value directly to the result map
            result.computeIfAbsent(verticalIndex) { ArrayList() }.add(node.`val`)

            // Add left and right children to the queue with updated vertical indices
            node.left?.let { queue.offer(VerticalIndex(it, verticalIndex - 1)) }
            node.right?.let { queue.offer(VerticalIndex(it, verticalIndex + 1)) }
        }

        // Return the values from the TreeMap, which are already sorted by vertical index
        return result.values.toList()
    }
}
```

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

```kotlin
package tree

import java.util.*

class BinaryTreeVerticalOrderTraversal_WithoutSorting {
    data class VerticalIndex(val node: TreeNode, val verticalIndex: Int)

    fun verticalOrder(root: TreeNode?): List<List<Int>> {
        if (root == null) return emptyList()

        val columnTable = mutableMapOf<Int, MutableList<Int>>()
        var minColumn = 0
        var maxColumn = 0

        val queue: Queue<VerticalIndex> = LinkedList()
        queue.offer(VerticalIndex(root, 0))

        while (queue.isNotEmpty()) {
            val (node, column) = queue.poll()

            columnTable.computeIfAbsent(column) { mutableListOf() }.add(node.`val`)

            // Update min and max column indices
            minColumn = minOf(minColumn, column)
            maxColumn = maxOf(maxColumn, column)

            node.left?.let { queue.offer(VerticalIndex(it, column - 1)) }
            node.right?.let { queue.offer(VerticalIndex(it, column + 1)) }
        }

        val result = mutableListOf<List<Int>>()
        for (col in minColumn..maxColumn) {
            result.add(columnTable[col]!!)
        }

        return result
    }
}
```

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

```kotlin
package tree

import java.util.*

class BinaryTreeZigZagLevelOrderTraversal {
    data class IndexedNode(var node: TreeNode?, var index: Int)

    fun zigzagLevelOrder(root: TreeNode?): List<List<Int>> {
        val result = mutableListOf<MutableList<Int>>()
        if (root == null) return result

        val queue: Queue<IndexedNode> = LinkedList()
        queue.add(IndexedNode(root, 0))
        var level = 0

        while (queue.isNotEmpty()) {
            val levelSize = queue.size
            val currentLevel = LinkedList<Int>()

            for (i in 0 until levelSize) {
                val (currentNode, _) = queue.poll()

                if (level % 2 == 0) {
                    currentLevel.add(currentNode?.`val` ?: 0)
                } else {
                    currentLevel.addFirst(currentNode?.`val` ?: 0)
                }

                currentNode?.left?.let { queue.add(IndexedNode(it, 2 * i + 1)) }
                currentNode?.right?.let { queue.add(IndexedNode(it, 2 * i + 2)) }
            }

            result.add(currentLevel)
            level++
        }

        return result
    }
}
```

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

```kotlin
package tree

class BoundaryOfBinaryTree {
    fun boundaryOfBinaryTree(root: TreeNode?): List<Int> {
        val result = mutableListOf<Int>()
        if (root == null) return result

        // Step 1: Add the root node
        result.add(root.`val`)

        // Step 2: Add the left boundary (excluding leaves)
        addLeftBoundary(root.left, result)

        // Step 3: Add all leaf nodes (excluding root if it is a leaf)
        addLeaves(root, result, isRoot = true)

        // Step 4: Add the right boundary (excluding leaves, in reverse order)
        val rightBoundary = mutableListOf<Int>()
        addRightBoundary(root.right, rightBoundary)
        result.addAll(rightBoundary.reversed())

        return result
    }

    private fun addLeftBoundary(node: TreeNode?, result: MutableList<Int>) {
        var current = node
        while (current != null) {
            // Don't add leaf nodes to the left boundary
            if (current.left != null || current.right != null) {
                result.add(current.`val`)
            }
            // Move down the left child, or the right if left is null
            current = current.left ?: current.right
        }
    }

    private fun addLeaves(node: TreeNode?, result: MutableList<Int>, isRoot: Boolean) {
        if (node == null) return
        // If it's a leaf node and it's not the root, add it to the result
        if (node.left == null && node.right == null && !isRoot) {
            result.add(node.`val`)
            return
        }
        // Otherwise, continue the traversal for both subtrees
        addLeaves(node.left, result, isRoot = false)
        addLeaves(node.right, result, isRoot = false)
    }

    private fun addRightBoundary(node: TreeNode?, result: MutableList<Int>) {
        var current = node
        while (current != null) {
            // Don't add leaf nodes to the right boundary
            if (current.left != null || current.right != null) {
                result.add(current.`val`)
            }
            // Move down the right child, or the left if right is null
            current = current.right ?: current.left
        }
    }
}
```

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

```kotlin
package tree.bst

class BSTIterator(root: TreeNode?) {
    private val stack = ArrayDeque<TreeNode>()

    init {
        // Initialize the stack by adding all the leftmost nodes
        pushAllLeftNodes(root)
    }

    // Push all the left nodes of a given node to the stack
    private fun pushAllLeftNodes(node: TreeNode?) {
        var current = node
        while (current != null) {
            stack.addFirst(current)
            current = current.left
        }
    }

    // Returns the next smallest number
    fun next(): Int {
        val node = stack.removeFirst()  // Pop the node from the stack
        pushAllLeftNodes(node.right)  // Push the leftmost nodes of the right child, if any
        return node.`val`
    }

    // Returns whether we have a next smallest number
    fun hasNext(): Boolean {
        return stack.isNotEmpty()  // If the stack is not empty, there are more nodes to visit
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */
```

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

```kotlin
package tree.bfs

import tree.TreeNode

class CheckCompletenessOfBinaryTree {
    fun isCompleteTree(root: TreeNode?): Boolean {
        if (root == null) return true // Edge case: An empty tree is considered complete

        val queue = ArrayDeque<TreeNode?>()
        queue.add(root)

        var foundNull = false // A flag to indicate if a null node has been encountered

        while (queue.isNotEmpty()) {
            val current = queue.removeFirst()

            // If we have already seen a null node, we shouldn't encounter any non-null nodes after that.
            if (current == null) {
                foundNull = true
            } else {
                if (foundNull) return false // If we encounter a non-null node after a null node, it's not complete

                queue.add(current.left)
                queue.add(current.right)
            }
        }

        return true
    }
}
```

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

```kotlin
package tree.bst

import kotlin.math.abs

class ClosestBinarySearchTreeValue {
    fun closestValue(root: TreeNode?, target: Double): Int {
        var closest = root?.`val` ?: 0
        var current = root

        while (current != null) {
            val currentValue = current.`val`

            // Update closest based on the given conditions:
            if (abs(currentValue - target) < abs(closest - target) ||
                (abs(currentValue - target) == abs(closest - target) && currentValue < closest))
                closest = currentValue

            // Move to the left or right subtree based on the target
            current = if (target < currentValue) current.left else current.right
        }

        return closest
    }
}
```

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

```kotlin
package tree

class ConstructBinaryTreeFromInorderAndPostOrderTraversal {
    fun buildTree(inorder: IntArray, postorder: IntArray): TreeNode? {
        // Build Inverted InOrder Index Map
        val rootIndices = mutableMapOf<Int, Int>()
        inorder.forEachIndexed { index, value -> rootIndices[value] = index }

        var postIndex = postorder.size - 1

        fun buildTree(left: Int, right: Int): TreeNode? {
            return when {
                left > right -> null
                else -> {
                    val rootVal = postorder[postIndex--]
                    TreeNode(rootVal).apply {
                        this.right = buildTree(rootIndices[rootVal]!! + 1, right)  // Build right subtree first
                        this.left = buildTree(left, rootIndices[rootVal]!! - 1)    // Build left subtree
                    }
                }
            }
        }

        return buildTree(0, inorder.size - 1)
    }
}
```

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

```kotlin
package tree

class ConstructBinaryTreeFromPreorderAndInOrderTraversal {
    private val rootIndices = mutableMapOf<Int, Int>()

    fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
        // Build Inverted InOrder Index Map
        inorder.forEachIndexed { index, value -> rootIndices[value] = index }
        var rootIndex = 0

        fun buildTree(left: Int, right: Int): TreeNode? {
            return when {
                left > right -> null
                else -> {
                    val rootVal = preorder[rootIndex++]
                    TreeNode(rootVal).apply {
                        this.left = buildTree(left, rootIndices[rootVal]!! - 1)
                        this.right = buildTree(rootIndices[rootVal]!! + 1, right)
                    }
                }
            }
        }

        return buildTree(0, preorder.size - 1)
    }
}
```

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

```kotlin
package tree

class ConstructBinaryTreeFromString {
    fun str2tree(s: String): TreeNode? {
        if (s.isEmpty()) return null

        return buildTree(s, 0).first // We are only interested in the tree root, not the index
    }

    private fun buildTree(s: String, i: Int): Pair<TreeNode?, Int> {
        if (i >= s.length) return Pair(null, i)

        var currentIndex = i
        val start = currentIndex
        if (s[currentIndex] == '-') currentIndex++  // Handle negative numbers
        while (currentIndex < s.length && s[currentIndex].isDigit()) currentIndex++  // Skip over digits
        val valStr = s.substring(start, currentIndex)
        val root = TreeNode(valStr.toInt())

        // Check for left child (subtree)
        if (currentIndex < s.length && s[currentIndex] == '(') {
            currentIndex++  // Skip '('
            val leftResult = buildTree(s, currentIndex)
            root.left = leftResult.first
            currentIndex = leftResult.second  // Update index after processing left subtree
            if (currentIndex < s.length && s[currentIndex] == ')') currentIndex++  // Skip ')'
        }

        // Check for right child (subtree)
        if (currentIndex < s.length && s[currentIndex] == '(') {
            currentIndex++  // Skip '('
            val rightResult = buildTree(s, currentIndex)
            root.right = rightResult.first
            currentIndex = rightResult.second  // Update index after processing right subtree
            if (currentIndex < s.length && s[currentIndex] == ')') currentIndex++  // Skip ')'
        }

        return root to currentIndex  // Return the node and the updated index
    }
}
```

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

```kotlin
package tree.bst
/**
 * Definition for a Node.
 class Node(var `val`: Int) {
    var left: Node? = null
    var right: Node? = null
 }
 */
class ConvertBInarySearchTreeToSortedDoublyLinkedList {
    class Node(var `val`: Int) {
        var left: Node? = null
        var right: Node? = null
    }

    private var head: Node? = null
    private var tail: Node? = null

    fun treeToDoublyList(root: Node?): Node? {
        if (root == null) return null

        // Perform in-order traversal and link nodes
        inorderTraversal(root)

        // Complete the doubly linked list by linking head and tail
        head?.left = tail
        tail?.right = head

        return head
    }

    private fun inorderTraversal(node: Node?) {
        if (node == null) return

        inorderTraversal(node.left) // Traverse left subtree

        if (tail != null) {
            // Link the current node with the previous node (tail)
            tail!!.right = node
            node.left = tail
        } else {
            // This is the first node (head of the doubly linked list)
            head = node
        }

        // Update the tail to the current node
        tail = node

        inorderTraversal(node.right) // Traverse right subtree
    }
}
```

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

```kotlin
package tree

class CountGoodNodeInBInaryTree {
    fun goodNodes(root: TreeNode?): Int {
        return dfs(root, Int.MIN_VALUE)
    }

    private fun dfs(node: TreeNode?, maxSoFar: Int): Int {
        node ?: return 0
        
        val newMax = maxOf(maxSoFar, node.`val`)
        val good = if (node.`val` >= maxSoFar) 1 else 0

        return good + dfs(node.left, newMax) + dfs(node.right, newMax)
    }
}
```

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

```kotlin
package tree

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

data class Result (val sum: Int, val count: Int)

class CountNodeEqualsAverage {
    var count = 0

    fun averageOfSubtree(root: TreeNode?): Int {
        postOrder(root)
        return count;
    }

    private fun postOrder(root: TreeNode?): Result {
        if (root == null)
            return Result(sum = 0, count = 0)

        val left = postOrder(root.left)
        val right = postOrder(root.right)

        val nodeSum = root.`val` + left.sum + right.sum
        val nodeCount = 1 + left.count + right.count
        if ( root.`val` == nodeSum/nodeCount)
            count++

        return Result(sum = nodeSum, count = nodeCount)
    }
}
```

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

```kotlin
package tree.bst

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class DeleteNodeinABST {
    fun deleteNode(root: TreeNode?, key: Int): TreeNode? {
        when {
            root == null -> return null
            key < root.`val` -> root.left = deleteNode(root.left, key)
            key > root.`val` -> root.right = deleteNode(root.right, key)
            else -> {
                when {
                    root.left == null -> return root.right
                    root.right == null -> return root.left
                    else -> {
                        root.`val` = minValue(root.right!!)
                        root.right = deleteNode(root.right, root.`val`)
                    }
                }
            }
        }

        return root
    }

    fun minValue(node: TreeNode): Int {
        var current = node
        while (current.left != null) {
            current = current.left!!
        }

        return current.`val`
    }
}
```

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

```kotlin
package tree.bfs

import tree.TreeNode
import java.util.*

class FindLargestValueInEachTreeRow {
    fun largestValues(root: TreeNode?): List<Int> {
        val result = mutableListOf<Int>()

        val queue: Queue<TreeNode> = LinkedList()
        root?.let{ queue.offer(it) }

        while (queue.isNotEmpty()) {
            val size = queue.size
            var max = Int.MIN_VALUE

            repeat(size) {
                val current = queue.poll()
                max = maxOf(max, current.`val`)

                current.left?.let{ queue.offer(it) }
                current.right?.let{ queue.offer(it) }
            }

            result.add(max)
        }

        return result
    }
}
```

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

```kotlin
package tree.bst

class InorderSuccessor {
    fun inorderSuccessor(root: TreeNode?, p: TreeNode?): TreeNode? {
        var successor: TreeNode? = null
        var current = root

        while (current != null) {
            if (p!!.`val` < current.`val`) {
                // If p's value is less than current, the successor is possibly current
                successor = current
                current = current.left
            } else {
                // If p's value is greater or equal to current, move to the right subtree
                current = current.right
            }
        }

        return successor
    }
}
```

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

```kotlin
package tree

class LeafSimilar {
    fun leafSimilar(root1: TreeNode?, root2: TreeNode?): Boolean {
        val leaves1 = mutableListOf<Int>()
        val leaves2 = mutableListOf<Int>()

        dfs(root1, leaves1)
        dfs(root2, leaves2)

        return leaves1 == leaves2
    }

    fun dfs(node: TreeNode?, leafValues: MutableList<Int>) {
        if (node != null) {
            if (node.left == null && node.right == null) {
                leafValues.add(node.`val`)
            }
            dfs(node.left, leafValues)
            dfs(node.right, leafValues)
        }
    }
}
```

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

```kotlin
package tree

class LongestUnivaluePath {

    fun longestUnivaluePath(root: TreeNode?): Int {
        var maxLength = 0
        fun dfs(node: TreeNode?): Int {
            if (node == null) return 0

            // Get the maximum univalue chain from both left and right
            val left = dfs(node.left)
            val right = dfs(node.right)

            // Compute the branch lengthes if
            val currentLeft = if (node.left?.`val` == node.`val`) left + 1 else 0
            val currentRight = if (node.right?.`val` == node.`val`) right + 1 else 0

            // Take maximum of max found so far , OD
            maxLength = maxOf(maxLength, currentLeft + currentRight)

            // We can only propagate the maximum branch chain b/w left and right
            return maxOf(currentLeft, currentRight)
        }

        dfs(root)
        return maxLength
    }
}
```

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

```kotlin
package tree

class LowestCommonAncestor {
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
        if (root == null || root === p || root === q) return root

        val left = lowestCommonAncestor(root.left, p, q)
        val right = lowestCommonAncestor(root.right, p, q)

        return if (left != null && right != null) root else left ?: right

    }
}
```

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

```kotlin
package tree

class LowestCommonAncestor_III {
    class Node(var `val`: Int) {
        var left: TreeNode? = null
        var right: TreeNode? = null
        var parent: Node? = null
    }

    fun lowestCommonAncestor(p: Node?, q: Node?): Node? {
        var parent1 = p
        var parent2 = q

        while (parent1 != parent2) {
            // Move parent1 upwards, or switch to q if it becomes null
            parent1 = parent1?.parent ?: q
            // Move parent2 upwards, or switch to p if it becomes null
            parent2 = parent2?.parent ?: p
        }

        // parent1 and parent2 are now pointing to the same node, which is the LCA
        return parent1
    }
}

/**
 *       1 <- r
 *      / \
 *     2   3
 *    /\   /\
 *   6 7   8 9 <-l
 *            \
 *            10
 *
 */
```

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

```kotlin
package tree

class MaximumDepthOfBinaryTree {
    fun maxDepth(root: TreeNode?): Int {
        if (root == null) {
            return 0
        }

        return 1 + maxOf(maxDepth(root.left), maxDepth(root.right))
    }
}
```

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

```kotlin
package tree

class MaximumSumBSTInBinaryTree {
    data class Result(val isBST: Boolean, val sum: Int, val min: Int, val max: Int)
    private var maxSum = 0

    fun maxSumBST(root: TreeNode?): Int {
        dfs(root)
        return maxSum
    }

    private fun dfs(node: TreeNode?): Result {
        // Base case: if the node is null, it's trivially a BST with sum = 0
        if (node == null) {
            return Result(true, 0, Int.MAX_VALUE, Int.MIN_VALUE)
        }

        // Recursively traverse the left and right subtrees
        val left = dfs(node.left)
        val right = dfs(node.right)

        // Check if the current node is a valid BST
        if (left.isBST && right.isBST && node.`val` > left.max && node.`val` < right.min) {
            // Current node is part of a valid BST
            val sum = node.`val` + left.sum + right.sum
            maxSum = maxOf(maxSum, sum) // Update the global max sum if needed
            // Return the result for this subtree
            return Result(
                isBST = true,
                sum = sum,
                min = minOf(node.`val`, left.min),
                max = maxOf(node.`val`, right.max)
            )
        }

        // If it's not a valid BST, return invalid information
        return Result(false, sum=0, min=0, max=0)
    }
}
```

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

```kotlin
package tree

import java.util.*

class MaximumWidthOfBinaryTree {
    data class Node(var node: TreeNode?, var index: Int)

    fun widthOfBinaryTree(root: TreeNode?): Int {
        val queue: Queue<Node> = LinkedList<Node>()
        var max = 0
        queue.add(Node(root, 0))

        while (queue.isNotEmpty()) {
            var size = queue.size
            var left = queue.peek().index
            var right = left
            repeat(size) {
                val current = queue.poll()
                right = current.index

                current.node?.left?.let { queue.add(Node(it, 2 * current.index + 1)) }
                current.node?.right?.let { queue.add(Node(it, 2 * current.index + 2)) }
            }

            max = maxOf(max, right - left + 1)
        }

        return max
    }
}
```

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

```kotlin
package tree

class MinimumTimeToCollectAllApplesInATree {
    fun minTime(n: Int, edges: Array<IntArray>, hasApple: List<Boolean>): Int {
        // Build the graph as a list of lists (adjacency list representation)
        val graph = Array(n) { mutableListOf<Int>() }
        edges.forEach { (u, v) ->
            graph[u].add(v)
            graph[v].add(u)
        }

        // DFS function to calculate the total time
        fun dfs(node: Int, parent: Int): Int {
            var totalTime = 0
            // Use forEach to iterate over each neighbor
            graph[node].forEach { neighbor ->
                if (neighbor != parent) {
                    val time = dfs(neighbor, node)
                    // If the time is greater than 0 or the neighbor has an apple, add the time and return time (2)
                    if (time > 0 || hasApple[neighbor]) {
                        totalTime += time + 2
                    }
                }
            }
            return totalTime
        }

        // Start DFS from node 0 with no parent (-1)
        return dfs(0, -1)
    }
}
```

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

```kotlin
package tree

class PathSum {
    fun hasPathSum(root: TreeNode?, targetSum: Int): Boolean {
        return when {
            root == null -> false
            root.left == null && root.right == null && targetSum == root.`val` -> true
            else -> hasPathSum(root.left, targetSum - root.`val`)
                    || hasPathSum(root.right, targetSum - root.`val`)
        }
    }
}
```

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

```kotlin
package tree

class PathSum_II {
    fun pathSum(root: TreeNode?, targetSum: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()

        fun dfs(node: TreeNode?, currentSum: Int, path: MutableList<Int> = mutableListOf()) {
            if (node == null) return

            // Add the current node's value to the path
            path.add(node.`val`)

            // If the node is a leaf and the path sum equals targetSum, add the path to the result
            if (node.left == null && node.right == null && currentSum == node.`val`) {
                result.add(path.toList()) // copy the current path list and add
            } else {
                // Continue the search on the left and right subtree
                dfs(node.left, currentSum - node.`val`, path)
                dfs(node.right, currentSum - node.`val`, path)
            }

            // Backtrack: remove the current node from the path
            path.removeAt(path.size - 1)
        }

        dfs(root, targetSum)
        return result
    }
}
```

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

```kotlin
package tree

class PathSumIII {
    // O(N^2) solution
    fun pathSum(root: TreeNode?, targetSum: Int): Int {
        if (root == null)
            return 0

        // Count paths with targetSum starting from the current node
        fun dfs(node: TreeNode?, currentSum: Long): Int {
            if (node == null)
                return 0

            val newSum = currentSum + node.`val`
            val count = if (newSum == targetSum.toLong()) 1 else 0

            return count + dfs(node.left, newSum) + dfs(node.right, newSum)
        }

        // Start counting paths from the root
        return dfs(root, 0L) + pathSum(root.left, targetSum) + pathSum(root.right, targetSum)
    }


    // Revisit I didn't understand
    fun pathSum_prefix_sum(root: TreeNode?, targetSum: Int): Int {
        // HashMap to store prefix sums and their frequencies
        val prefixSumCount = HashMap<Long, Int>()
        // Initialize with a prefix sum of 0 having occurred once (considering no node)
        prefixSumCount[0L] = 1

        // Helper function to perform DFS
        fun dfs(node: TreeNode?, currentSum: Long): Int {
            if (node == null) return 0

            // Calculate the current sum at the current node
            val newSum = currentSum + node.`val`

            // Calculate how many valid paths end at the current node
            var pathCount = prefixSumCount.getOrDefault(newSum - targetSum.toLong(), 0)

            // Update prefix sum count
            prefixSumCount[newSum] = prefixSumCount.getOrDefault(newSum, 0) + 1

            // Recursively count paths in the left and right subtrees
            pathCount += dfs(node.left, newSum)
            pathCount += dfs(node.right, newSum)

            // Backtrack: Remove the current prefix sum to avoid influencing other paths
            prefixSumCount[newSum] = prefixSumCount.getOrDefault(newSum, 0) - 1

            return pathCount
        }

        // Start DFS traversal from the root with initial current sum of 0
        return dfs(root, 0L)
    }
}
```

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

```kotlin
package tree

import java.util.*

class PopulateNextRightPointersInEachNode_II {
    fun connect(root: Node?): Node? {
        val queue: Queue<Node> = LinkedList()
        root?.let { queue.add(it) }
        while (queue.isNotEmpty()) {
            var prev: Node? = null
            repeat(queue.size) {
                val node = queue.poll()
                node?.left?.let { queue.add(it) }
                node?.right?.let { queue.add(it) }

                prev?.let{ prev?.next = node }
                prev = node
            }
        }
        return root
    }
}
```

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

```kotlin
package tree

import java.util.*

class PopulateNextRightPointersInEachNode_II_Constant {
    fun connect(root: Node?): Node? {
        var current: Node? = root

        while (current != null) {
            var nextLevelStart: Node? = null
            var prev: Node? = null
            var node = current

            // Traverse the current level
            while (node != null) {
                // Connect left child
                if (node.left != null) {
                    if (prev != null) prev.next = node.left
                    prev = node.left
                    if (nextLevelStart == null) nextLevelStart = node.left
                }

                // Connect right child
                if (node.right != null) {
                    if (prev != null) prev.next = node.right
                    prev = node.right
                    if (nextLevelStart == null) nextLevelStart = node.right
                }

                node = node.next
            }

            // Move to the next level
            current = nextLevelStart
        }

        return root
    }
}
```

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

```kotlin
package tree

import java.util.*

class Node(var `val`: Int) {
    var left: Node? = null
    var right: Node? = null
    var next: Node? = null
}

class PopulatingNextRightPointerInEachNode {
    fun connect(root: Node?): Node? {
        root?.let { queue ->
            val q = LinkedList<Node>().apply { offer(queue) }

            while (q.isNotEmpty()) {
                val levelSize = q.size
                var prev: Node? = null

                repeat(levelSize) {
                    q.poll().also { node ->
                        prev?.next = node
                        prev = node
                        node.left?.let { q.offer(it) }
                        node.right?.let { q.offer(it) }
                    }
                }
            }
        }
        return root
    }
}
```

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

```kotlin
package graph.bst

class RangeSumOfBST {
    fun rangeSumBST(root: TreeNode?, low: Int, high: Int): Int {
        var sum = 0
        fun dfs(node: TreeNode?) {
            if (node == null)
                return

            dfs(node.left)

            if (node.`val` in low..high)
                sum += node.`val`

            dfs(node.right)
        }
        dfs(root)

        return sum
    }
}
```

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

```kotlin
package tree

class RecoverATreeFromPreOrderTraversal {
    fun recoverFromPreorder(traversal: String): TreeNode? {
        var index = 0 // Global index to track position in the string

        // Recursive function to build the tree
        fun buildTree(depth: Int): TreeNode? {
            if (index >= traversal.length) return null // Base case: end of string

            // Read the depth of the current node
            var currentDepth = 0
            while (index < traversal.length && traversal[index] == '-') {
                currentDepth++
                index++
            }

            // If the current depth doesn't match the expected depth, backtrack
            if (currentDepth != depth) {
                index -= currentDepth // Rewind the index
                return null
            }

            // Read the value of the current node
            var value = 0
            while (index < traversal.length && traversal[index].isDigit()) {
                value = value * 10 + (traversal[index] - '0')
                index++
            }

            // Create the current node
            val node = TreeNode(value)

            // Recursively build the left and right subtrees
            node.left = buildTree(depth + 1)
            node.right = buildTree(depth + 1)

            return node
        }

        return buildTree(0) // Start building the tree from depth 0
    }
}
```

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

```kotlin
package tree.bst

class RecoverBinarySearchTree {
    fun recoverTree(root: TreeNode?) {
        var first: TreeNode? = null
        var second: TreeNode? = null
        var prev: TreeNode? = null

        // Helper function to perform in-order traversal
        fun dfs(node: TreeNode?) {
            if (node == null) return

            // Traverse left subtree
            dfs(node.left)

            // Identify swapped nodes
            if (prev != null && prev!!.`val` > node.`val`) {
                if (first == null) {
                    first = prev  // First out-of-order node
                }
                second = node  // Second out-of-order node
            }

            // Update previous node
            prev = node

            // Traverse right subtree
            dfs(node.right)
        }

        // Step 1: In-order traversal to find the swapped nodes
        dfs(root)

        // Step 2: Swap the values of the two nodes
        first?.let { f ->
            second?.let { s ->
                val temp = f.`val`
                f.`val` = s.`val`
                s.`val` = temp
            }
        }
    }
}
```

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

```kotlin
package tree

/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Codec() {
    // Encodes a URL to a shortened URL.
    fun serialize(root: TreeNode?): String {
        val serializedTree = StringBuilder()

        fun dfs(node: TreeNode?) {
            if (node == null) {
                serializedTree.append("null,")
                return
            }

            serializedTree.append("${node.`val`},").also {
                dfs(node.left)
                dfs(node.right)
            }
        }
        dfs(root)
        return serializedTree.toString()
    }

    // Decodes the encoded string to tree using a recursive approach.
    fun deserialize(data: String): TreeNode? {
        val nodes = data.split(",").toMutableList()

        fun dfsDeserialize(): TreeNode? {
            if (nodes.isEmpty()) return null
            val value = nodes.removeAt(0)
            if (value == "null") return null

            val node = TreeNode(value.toInt()).apply {
                left = dfsDeserialize()
                right = dfsDeserialize()
            }

            return node
        }

        return dfsDeserialize()
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * var ser = Codec()
 * var deser = Codec()
 * var data = ser.serialize(longUrl)
 * var ans = deser.deserialize(data)
 */
```

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

```kotlin
package tree

class SerializeAndDeserializeNArrayTree {
    class Node(var `val`: Int) {
        var children: List<Node?> = listOf()
    }

    class Codec {
        // Encodes a tree to a single string.
        fun serialize(root: Node?): String = when (root) {
            null -> ""
            else -> buildString {
                fun dfs(node: Node?) {
                    node?.let {
                        append("${it.`val`}:${it.children.size}")
                        if (it.children.isNotEmpty()) append(",")
                        it.children.forEachIndexed { index, child ->
                            dfs(child)
                            if (index < it.children.size - 1) append(",")
                        }
                    }
                }
                dfs(root)
            }
        }

        // Deserialize with internal DFS
        fun deserialize(data: String): Node? {
            if (data.isEmpty()) return null

            val tokens = data.split(",")
            var index = 0

            fun parse(): Node? {
                if (index >= tokens.size) return null

                // Use destructuring declaration
                val (valueStr, childCountStr) = tokens[index++].split(":")
                val node = Node(valueStr.toInt())

                // Create children using functional approach
                node.children = List(childCountStr.toInt()) { parse() }

                return node
            }

            return parse()
        }
    }
}
```

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

```kotlin
package tree

class StepByStepDirectionsFromANodeToAnother {
    fun findNode(root: TreeNode?, searchKey: Int): TreeNode? {
        return when {
            root == null -> null
            root.`val` == searchKey -> root
            else -> findNode(root.left, searchKey) ?: findNode(root.right, searchKey)
        }
    }

    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
        if (root == null || root === p || root === q) return root

        val left = lowestCommonAncestor(root.left, p, q)
        val right = lowestCommonAncestor(root.right, p, q)

        return if (left != null && right != null) root else left ?: right

    }

    fun getDirections(root: TreeNode?, startValue: Int, destValue: Int): String {
        val sourceNode = findNode(root, startValue)
        val destNode = findNode(root, destValue)

        if (sourceNode == null || destNode == null) {
            return "" // No output for missing source or destination
        }

        val lca = lowestCommonAncestor(root, sourceNode, destNode)

        val sourcePath = StringBuilder()
        val destPath = StringBuilder()

        buildPath(lca, sourceNode, sourcePath)
        buildPath(lca, destNode, destPath)

        val upMoves = "U".repeat(sourcePath.length)
        return "$upMoves${destPath.toString()}"
    }

    private fun buildPath(node: TreeNode?, target: TreeNode?, path: StringBuilder): Boolean {
        if (node == null) return false
        if (node === target) return true

        path.append('L')
        if (buildPath(node.left, target, path)) return true
        path.deleteCharAt(path.length - 1)

        path.append('R')
        if (buildPath(node.right, target, path)) return true
        path.deleteCharAt(path.length - 1)

        return false
    }
}
```

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

```kotlin
package tree

class SumRootToLeafNumbers {
    fun sumNumbers(root: TreeNode?): Int {
        var sum = 0

        fun dfs(node: TreeNode?, sumSoFar: Int) {
            if (node == null) return
            val newSum = (sumSoFar * 10 + node.`val` )
            when {
                node.left == null && node.right == null -> sum+= newSum
                else ->  {
                    dfs(node.left, newSum)
                    dfs(node.right, newSum)
                }
            }
        }

        dfs(root, 0)
        return sum
    }
}
```

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

```kotlin
package tree

import java.util.*

class VerticalOrderTraversalOfABinaryTree {
    data class VerticalIndex(val node: TreeNode, val verticalIndex: Int)

    fun verticalTraversal(root: TreeNode?): List<List<Int>> {
        if (root == null) return emptyList()

        val columnTable = mutableMapOf<Int, TreeSet<Int>>()
        var minColumn = 0
        var maxColumn = 0

        val queue: Queue<VerticalIndex> = LinkedList()
        queue.offer(VerticalIndex(root, 0))

        while (queue.isNotEmpty()) {
            val (node, column) = queue.poll()

            columnTable.getOrPut(column) { TreeSet() }.add(node.`val`)

            // Update min and max column indices
            minColumn = minOf(minColumn, column)
            maxColumn = maxOf(maxColumn, column)

            node.left?.let { queue.offer(VerticalIndex(it, column - 1)) }
            node.right?.let { queue.offer(VerticalIndex(it, column + 1)) }
        }

        val result = mutableListOf<List<Int>>()
        for (col in minColumn..maxColumn) {
            result.add(columnTable[col]!!.toList())
        }

        return result
    }
}
```

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

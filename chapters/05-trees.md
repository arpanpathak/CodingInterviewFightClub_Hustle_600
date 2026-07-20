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

> **44 problems** — **Trees** are recursive data structures. Master DFS (pre/in/post-order), BFS (level-order), and BST properties (inorder traversal gives sorted order).

## Complete Problem Set

| # | Problem |
|---|---------|
| 1 | [All Nodes Distance Kin Binary Tree](#allnodesdistancekinbinarytree) |
| 2 | [Average Of Levels In Binary Tree](#averageoflevelsinbinarytree) |
| 3 | [Balanced Binary Tree](#balancedbinarytree) |
| 4 | [B Inary Tree In Order Traversal Iterative](#binarytreeinordertraversaliterative) |
| 5 | [Binary Tree Level Order Traversal](#binarytreelevelordertraversal) |
| 6 | [Binary Tree Level Order Traversal_II](#binarytreelevelordertraversal_ii) |
| 7 | [Binary Tree Maximum Path Sum](#binarytreemaximumpathsum) |
| 8 | [Binary Tree Right Side View](#binarytreerightsideview) |
| 9 | [Binary Tree Vertical Order Traversal](#binarytreeverticalordertraversal) |
| 10 | [Binary Tree Vertical Order Traversal_Without Sorting](#binarytreeverticalordertraversal_withoutsorting) |
| 11 | [Binary Tree Zig Zag Level Order Traversal](#binarytreezigzaglevelordertraversal) |
| 12 | [Boundary Of Binary Tree](#boundaryofbinarytree) |
| 13 | [BST Iterator](#bstiterator) |
| 14 | [Check Completeness Of Binary Tree](#checkcompletenessofbinarytree) |
| 15 | [Closest Binary Search Tree Value](#closestbinarysearchtreevalue) |
| 16 | [Construct Binary Tree From Inorder And Post Order Traversal](#constructbinarytreefrominorderandpostordertraversal) |
| 17 | [Construct Binary Tree From Preorder And In Order Traversal](#constructbinarytreefrompreorderandinordertraversal) |
| 18 | [Construct Binary Tree From String](#constructbinarytreefromstring) |
| 19 | [Convert B Inary Search Tree To Sorted Doubly Linked List](#convertbinarysearchtreetosorteddoublylinkedlist) |
| 20 | [Count Good Node In B Inary Tree](#countgoodnodeinbinarytree) |
| 21 | [Tree Node](#countnodeequalsaverage) |
| 22 | [Tree Node](#deletenodeinabst) |
| 23 | [Find Largest Value In Each Tree Row](#findlargestvalueineachtreerow) |
| 24 | [Inorder Successor](#inordersuccessor) |
| 25 | [Leaf Similar](#leafsimilar) |
| 26 | [Longest Univalue Path](#longestunivaluepath) |
| 27 | [Lowest Common Ancestor](#lowestcommonancestor) |
| 28 | [Lowest Common Ancestor_III](#lowestcommonancestor_iii) |
| 29 | [Maximum Depth Of Binary Tree](#maximumdepthofbinarytree) |
| 30 | [Maximum Sum BST In Binary Tree](#maximumsumbstinbinarytree) |
| 31 | [Maximum Width Of Binary Tree](#maximumwidthofbinarytree) |
| 32 | [Minimum Time To Collect All Apples In A Tree](#minimumtimetocollectallapplesinatree) |
| 33 | [Path Sum](#pathsum) |
| 34 | [Path Sum_II](#pathsum_ii) |
| 35 | [Path Sum III](#pathsumiii) |
| 36 | [Populate Next Right Pointers In Each Node_II](#populatenextrightpointersineachnode_ii) |
| 37 | [Range Sum Of BST](#rangesumofbst) |
| 38 | [Recover A Tree From Pre Order Traversal](#recoveratreefrompreordertraversal) |
| 39 | [Recover Binary Search Tree](#recoverbinarysearchtree) |
| 40 | [Codec](#serializeanddeserializeabinarytree) |
| 41 | [Serialize And Deserialize N Array Tree](#serializeanddeserializenarraytree) |
| 42 | [Step By Step Directions From A Node To Another](#stepbystepdirectionsfromanodetoanother) |
| 43 | [Sum Root To Leaf Numbers](#sumroottoleafnumbers) |
| 44 | [Vertical Order Traversal Of A Binary Tree](#verticalordertraversalofabinarytree) |

---

## All Nodes Distance Kin Binary Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class AllNodesDistanceKinBinaryTree {
    val parentMap = mutableMapOf<TreeNode, TreeNode?>()  // To store parent references

/**
 * distance K — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @param target the target value to search for or match against
 * @param k the number of elements/operations to consider (k parameter)
 * @return a list/collection of result elements
 */
    fun distanceK(root: TreeNode?, target: TreeNode?, k: Int): List<Int> {
        val result = mutableListOf<Int>()

        // Helper function to perform DFS and populate parent map, then find target

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @param parent the parent parameter — a tree/graph node used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
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

/**
 * collect Nodes At Distance K — executes the core logic of this algorithm on the provided input.
 *
 * @param node the root/head node of the data structure
 * @param k the number of elements/operations to consider (k parameter)
 * @param visited the visited parameter — a set of elements used in the computation
 * @param result the result parameter — a list of integers used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Average Of Levels In Binary Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree.bfs

import tree.TreeNode
import java.util.*

class AverageOfLevelsInBinaryTree {

/**
 * average Of Levels — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return a list/collection of result elements
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Balanced Binary Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

import kotlin.math.abs

class BalancedBinaryTree {

/**
 * is Balanced — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
 */
    fun isBalanced(root: TreeNode?): Boolean {

/**
 * Checks whether the specified condition holds true for the given input.
 *
 * @param node the root/head node of the data structure
 * @return the computed integer result
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## B Inary Tree In Order Traversal Iterative

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class BInaryTreeInOrderTraversalIterative {

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param root the root/head node of the data structure
 * @return the sorted/reordered list of elements
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Binary Tree Level Order Traversal

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

import java.util.*
import kotlin.collections.ArrayList


class BinaryTreeLevelOrderTraversal {

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param root the root/head node of the data structure
 * @return the sorted/reordered list of elements
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Binary Tree Level Order Traversal_II

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree.bfs

import tree.TreeNode
import java.util.*

class BinaryTreeLevelOrderTraversal_II {

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param root the root/head node of the data structure
 * @return the sorted/reordered list of elements
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Binary Tree Maximum Path Sum

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class BinaryTreeMaximumPathSum {

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param root the root/head node of the data structure
 * @return the maximum value found in the input
 */
    fun maxPathSum(root: TreeNode?): Int {
        var ans = Int.MIN_VALUE

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param node the root/head node of the data structure
 * @return the maximum value found in the input
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Binary Tree Right Side View

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class BinaryTreeRightSideView {

/**
 * right Side View — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return a list/collection of result elements
 */
    fun rightSideView(root: TreeNode?): List<Int> {
        val rightSide = mutableListOf<Int>()

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @param level the level parameter — a integer value used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Binary Tree Vertical Order Traversal

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

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

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param root the root/head node of the data structure
 * @return the sorted/reordered list of elements
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Binary Tree Vertical Order Traversal_Without Sorting

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

import java.util.*

class BinaryTreeVerticalOrderTraversal_WithoutSorting {
    data class VerticalIndex(val node: TreeNode, val verticalIndex: Int)

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param root the root/head node of the data structure
 * @return the sorted/reordered list of elements
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Binary Tree Zig Zag Level Order Traversal

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

import java.util.*

class BinaryTreeZigZagLevelOrderTraversal {
    data class IndexedNode(var node: TreeNode?, var index: Int)

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param root the root/head node of the data structure
 * @return the sorted/reordered list of elements
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Boundary Of Binary Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class BoundaryOfBinaryTree {

/**
 * boundary Of Binary Tree — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return a list/collection of result elements
 */
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

/**
 * Inserts the specified element into the data structure.
 *
 * @param node the root/head node of the data structure
 * @param result the result parameter — a list of integers used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
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

/**
 * Inserts the specified element into the data structure.
 *
 * @param node the root/head node of the data structure
 * @param result the result parameter — a list of integers used in the computation
 * @param isRoot the isRoot parameter — a boolean flag used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
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

/**
 * Inserts the specified element into the data structure.
 *
 * @param node the root/head node of the data structure
 * @param result the result parameter — a list of integers used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## BST Iterator

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

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

/**
 * Inserts the specified element into the data structure.
 *
 * @param node the root/head node of the data structure
 * @return Unit (nothing) — this function operates via side effects
 */
    private fun pushAllLeftNodes(node: TreeNode?) {
        var current = node
        while (current != null) {
            stack.addFirst(current)
            current = current.left
        }
    }

    // Returns the next smallest number

/**
 * next — executes the core logic of this algorithm on the provided input.
 *
 * @return the computed integer result
 */
    fun next(): Int {
        val node = stack.removeFirst()  // Pop the node from the stack
        pushAllLeftNodes(node.right)  // Push the leftmost nodes of the right child, if any
        return node.`val`
    }

    // Returns whether we have a next smallest number

/**
 * Checks whether the specified condition holds true for the given input.
 *
 * @return `true` if the target element/value exists, `false` otherwise
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Check Completeness Of Binary Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree.bfs

import tree.TreeNode

class CheckCompletenessOfBinaryTree {

/**
 * is Complete Tree — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Closest Binary Search Tree Value

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree.bst

import kotlin.math.abs

class ClosestBinarySearchTreeValue {

/**
 * closest Value — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @param target the target value to search for or match against
 * @return the computed integer result
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Construct Binary Tree From Inorder And Post Order Traversal

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class ConstructBinaryTreeFromInorderAndPostOrderTraversal {

/**
 * Builds and returns a new data structure from the given input parameters.
 *
 * @param inorder the inorder parameter — a array of integers used in the computation
 * @param postorder the postorder parameter — a array of integers used in the computation
 * @return the resulting tree/graph node
 */
    fun buildTree(inorder: IntArray, postorder: IntArray): TreeNode? {
        // Build Inverted InOrder Index Map
        val rootIndices = mutableMapOf<Int, Int>()
        inorder.forEachIndexed { index, value -> rootIndices[value] = index }

        var postIndex = postorder.size - 1

/**
 * Builds and returns a new data structure from the given input parameters.
 *
 * @param left the left/starting boundary of the search range (inclusive)
 * @param right the right/ending boundary of the search range (inclusive)
 * @return the resulting tree/graph node
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Construct Binary Tree From Preorder And In Order Traversal

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class ConstructBinaryTreeFromPreorderAndInOrderTraversal {
    private val rootIndices = mutableMapOf<Int, Int>()

/**
 * Builds and returns a new data structure from the given input parameters.
 *
 * @param preorder the preorder parameter — a array of integers used in the computation
 * @param inorder the inorder parameter — a array of integers used in the computation
 * @return the resulting tree/graph node
 */
    fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
        // Build Inverted InOrder Index Map
        inorder.forEachIndexed { index, value -> rootIndices[value] = index }
        var rootIndex = 0

/**
 * Builds and returns a new data structure from the given input parameters.
 *
 * @param left the left/starting boundary of the search range (inclusive)
 * @param right the right/ending boundary of the search range (inclusive)
 * @return the resulting tree/graph node
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Construct Binary Tree From String

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class ConstructBinaryTreeFromString {

/**
 * str2tree — executes the core logic of this algorithm on the provided input.
 *
 * @param s the input string to process
 * @return the resulting tree/graph node
 */
    fun str2tree(s: String): TreeNode? {
        if (s.isEmpty()) return null

        return buildTree(s, 0).first // We are only interested in the tree root, not the index
    }

/**
 * Builds and returns a new data structure from the given input parameters.
 *
 * @param s the input string to process
 * @param i the index position in the collection
 * @return the resulting tree/graph node
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Convert B Inary Search Tree To Sorted Doubly Linked List

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

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

/**
 * Converts/transforms the input from one representation to another.
 *
 * @param root the root/head node of the data structure
 * @return the resulting tree/graph node
 */
    fun treeToDoublyList(root: Node?): Node? {
        if (root == null) return null

        // Perform in-order traversal and link nodes
        inorderTraversal(root)

        // Complete the doubly linked list by linking head and tail
        head?.left = tail
        tail?.right = head

        return head
    }

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param node the root/head node of the data structure
 * @return Unit (nothing) — this function operates via side effects
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Count Good Node In B Inary Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class CountGoodNodeInBInaryTree {

/**
 * good Nodes — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return the computed integer result
 */
    fun goodNodes(root: TreeNode?): Int {
        return dfs(root, Int.MIN_VALUE)
    }

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @param maxSoFar the maxSoFar parameter — a integer value used in the computation
 * @return the computed integer result
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Tree Node

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

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

/**
 * average Of Subtree — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return the computed integer result
 */
    fun averageOfSubtree(root: TreeNode?): Int {
        postOrder(root)
        return count;
    }

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param root the root/head node of the data structure
 * @return the computed result of type Result
 */
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Tree Node

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree.bst

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class DeleteNodeinABST {

/**
 * Removes specified elements from the collection and returns the result.
 *
 * @param root the root/head node of the data structure
 * @param key the target value to search for or match against
 * @return the resulting tree/graph node
 */
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

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param node the root/head node of the data structure
 * @return the minimum value found in the input
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Find Largest Value In Each Tree Row

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree.bfs

import tree.TreeNode
import java.util.*

class FindLargestValueInEachTreeRow {

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param root the root/head node of the data structure
 * @return a list/collection of result elements
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Inorder Successor

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree.bst

class InorderSuccessor {

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param root the root/head node of the data structure
 * @param p the search pattern or criteria to match
 * @return the resulting tree/graph node
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Leaf Similar

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class LeafSimilar {

/**
 * leaf Similar — executes the core logic of this algorithm on the provided input.
 *
 * @param root1 the root1 parameter — a tree/graph node used in the computation
 * @param root2 the root2 parameter — a tree/graph node used in the computation
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
 */
    fun leafSimilar(root1: TreeNode?, root2: TreeNode?): Boolean {
        val leaves1 = mutableListOf<Int>()
        val leaves2 = mutableListOf<Int>()

        dfs(root1, leaves1)
        dfs(root2, leaves2)

        return leaves1 == leaves2
    }

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @param leafValues the leafValues parameter — a list of integers used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Longest Univalue Path

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class LongestUnivaluePath {

/**
 * longest Univalue Path — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return the computed integer result
 */
    fun longestUnivaluePath(root: TreeNode?): Int {
        var maxLength = 0

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @return the computed integer result
 */
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Lowest Common Ancestor

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class LowestCommonAncestor {

/**
 * Converts/transforms the input from one representation to another.
 *
 * @param root the root/head node of the data structure
 * @param p the search pattern or criteria to match
 * @param q the q parameter — a tree/graph node used in the computation
 * @return the resulting tree/graph node
 */
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
| **Space** | O(h) where h = tree height |

---

## Lowest Common Ancestor_III

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class LowestCommonAncestor_III {
    class Node(var `val`: Int) {
        var left: TreeNode? = null
        var right: TreeNode? = null
        var parent: Node? = null
    }

/**
 * Converts/transforms the input from one representation to another.
 *
 * @param p the search pattern or criteria to match
 * @param q the q parameter — a tree/graph node used in the computation
 * @return the resulting tree/graph node
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Maximum Depth Of Binary Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class MaximumDepthOfBinaryTree {

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param root the root/head node of the data structure
 * @return the maximum value found in the input
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Maximum Sum BST In Binary Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class MaximumSumBSTInBinaryTree {
    data class Result(val isBST: Boolean, val sum: Int, val min: Int, val max: Int)
    private var maxSum = 0

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param root the root/head node of the data structure
 * @return the maximum value found in the input
 */
    fun maxSumBST(root: TreeNode?): Int {
        dfs(root)
        return maxSum
    }

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @return the computed result of type Result
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Maximum Width Of Binary Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

import java.util.*

class MaximumWidthOfBinaryTree {
    data class Node(var node: TreeNode?, var index: Int)

/**
 * width Of Binary Tree — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return the computed integer result
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Minimum Time To Collect All Apples In A Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class MinimumTimeToCollectAllApplesInATree {

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param n the size/dimension parameter for the algorithm
 * @param edges the graph edges represented as connections between nodes
 * @param hasApple the hasApple parameter — a list of elements used in the computation
 * @return the minimum value found in the input
 */
    fun minTime(n: Int, edges: Array<IntArray>, hasApple: List<Boolean>): Int {
        // Build the graph as a list of lists (adjacency list representation)
        val graph = Array(n) { mutableListOf<Int>() }
        edges.forEach { (u, v) ->
            graph[u].add(v)
            graph[v].add(u)
        }

        // DFS function to calculate the total time

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @param parent the parent parameter — a integer value used in the computation
 * @return the computed integer result
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Path Sum

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class PathSum {

/**
 * Checks whether the specified condition holds true for the given input.
 *
 * @param root the root/head node of the data structure
 * @param targetSum the targetSum parameter — a integer value used in the computation
 * @return `true` if the target element/value exists, `false` otherwise
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Path Sum_II

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class PathSum_II {

/**
 * path Sum — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @param targetSum the targetSum parameter — a integer value used in the computation
 * @return a list/collection of result elements
 */
    fun pathSum(root: TreeNode?, targetSum: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @param currentSum the currentSum parameter — a integer value used in the computation
 * @param path the path parameter — a list of integers used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Path Sum III

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class PathSumIII {
    // O(N^2) solution

/**
 * path Sum — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @param targetSum the targetSum parameter — a integer value used in the computation
 * @return the computed sum/total value
 */
    fun pathSum(root: TreeNode?, targetSum: Int): Int {
        if (root == null)
            return 0

        // Count paths with targetSum starting from the current node

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @param currentSum the currentSum parameter — a input parameter of type Long used in the computation
 * @return the computed integer result
 */
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

/**
 * path Sum_prefix_sum — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @param targetSum the targetSum parameter — a integer value used in the computation
 * @return the computed sum/total value
 */
    fun pathSum_prefix_sum(root: TreeNode?, targetSum: Int): Int {
        // HashMap to store prefix sums and their frequencies
        val prefixSumCount = HashMap<Long, Int>()
        // Initialize with a prefix sum of 0 having occurred once (considering no node)
        prefixSumCount[0L] = 1

        // Helper function to perform DFS

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @param currentSum the currentSum parameter — a input parameter of type Long used in the computation
 * @return the computed integer result
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Populate Next Right Pointers In Each Node_II

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

import java.util.*

class PopulateNextRightPointersInEachNode_II {

/**
 * connect — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return the resulting tree/graph node
 */
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Range Sum Of BST

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package graph.bst

class RangeSumOfBST {

/**
 * range Sum BST — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @param low the left/starting boundary of the search range (inclusive)
 * @param high the right/ending boundary of the search range (inclusive)
 * @return the computed sum/total value
 */
    fun rangeSumBST(root: TreeNode?, low: Int, high: Int): Int {
        var sum = 0

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @return Unit (nothing) — this function operates via side effects
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Recover A Tree From Pre Order Traversal

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class RecoverATreeFromPreOrderTraversal {

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param traversal the traversal parameter — a string value used in the computation
 * @return the resulting tree/graph node
 */
    fun recoverFromPreorder(traversal: String): TreeNode? {
        var index = 0 // Global index to track position in the string

        // Recursive function to build the tree

/**
 * Builds and returns a new data structure from the given input parameters.
 *
 * @param depth the depth parameter — a integer value used in the computation
 * @return the resulting tree/graph node
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Recover Binary Search Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree.bst

class RecoverBinarySearchTree {

/**
 * recover Tree — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return Unit (nothing) — this function operates via side effects
 */
    fun recoverTree(root: TreeNode?) {
        var first: TreeNode? = null
        var second: TreeNode? = null
        var prev: TreeNode? = null

        // Helper function to perform in-order traversal

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @return Unit (nothing) — this function operates via side effects
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Codec

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

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

/**
 * serialize — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return the computed string result
 */
    fun serialize(root: TreeNode?): String {
        val serializedTree = StringBuilder()

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @return Unit (nothing) — this function operates via side effects
 */
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

/**
 * deserialize — executes the core logic of this algorithm on the provided input.
 *
 * @param data the input array of numbers to process
 * @return the resulting tree/graph node
 */
    fun deserialize(data: String): TreeNode? {
        val nodes = data.split(",").toMutableList()

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @return the resulting tree/graph node
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Serialize And Deserialize N Array Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class SerializeAndDeserializeNArrayTree {
    class Node(var `val`: Int) {
        var children: List<Node?> = listOf()
    }

    class Codec {
        // Encodes a tree to a single string.

/**
 * serialize — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return the computed string result
 */
        fun serialize(root: Node?): String = when (root) {
            null -> ""
            else -> buildString {

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @return Unit (nothing) — this function operates via side effects
 */
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

/**
 * deserialize — executes the core logic of this algorithm on the provided input.
 *
 * @param data the input array of numbers to process
 * @return the resulting tree/graph node
 */
        fun deserialize(data: String): Node? {
            if (data.isEmpty()) return null

            val tokens = data.split(",")
            var index = 0

/**
 * Converts/transforms the input from one representation to another.
 *
 * @return the resulting tree/graph node
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Step By Step Directions From A Node To Another

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class StepByStepDirectionsFromANodeToAnother {

/**
 * Searches for and returns the target element/position using an efficient algorithm.
 *
 * @param root the root/head node of the data structure
 * @param searchKey the searchKey parameter — a integer value used in the computation
 * @return the resulting tree/graph node
 */
    fun findNode(root: TreeNode?, searchKey: Int): TreeNode? {
        return when {
            root == null -> null
            root.`val` == searchKey -> root
            else -> findNode(root.left, searchKey) ?: findNode(root.right, searchKey)
        }
    }

/**
 * Converts/transforms the input from one representation to another.
 *
 * @param root the root/head node of the data structure
 * @param p the search pattern or criteria to match
 * @param q the q parameter — a tree/graph node used in the computation
 * @return the resulting tree/graph node
 */
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
        if (root == null || root === p || root === q) return root

        val left = lowestCommonAncestor(root.left, p, q)
        val right = lowestCommonAncestor(root.right, p, q)

        return if (left != null && right != null) root else left ?: right

    }

/**
 * Retrieves and returns the requested element or value from the data structure.
 *
 * @param root the root/head node of the data structure
 * @param startValue the startValue parameter — a integer value used in the computation
 * @param destValue the destValue parameter — a integer value used in the computation
 * @return the computed string result
 */
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

/**
 * Builds and returns a new data structure from the given input parameters.
 *
 * @param node the root/head node of the data structure
 * @param target the target value to search for or match against
 * @param path the path parameter — a input parameter of type StringBuilder used in the computation
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
 */
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Sum Root To Leaf Numbers

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

class SumRootToLeafNumbers {

/**
 * sum Numbers — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return the total count/number of matching elements
 */
    fun sumNumbers(root: TreeNode?): Int {
        var sum = 0

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param node the root/head node of the data structure
 * @param sumSoFar the sumSoFar parameter — a integer value used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Vertical Order Traversal Of A Binary Tree

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree

import java.util.*

class VerticalOrderTraversalOfABinaryTree {
    data class VerticalIndex(val node: TreeNode, val verticalIndex: Int)

/**
 * vertical Traversal — executes the core logic of this algorithm on the provided input.
 *
 * @param root the root/head node of the data structure
 * @return a list/collection of result elements
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Key Takeaways

1. **Core pattern recognition** — Identify the problem type and apply the right algorithmic technique.
2. **Practice systematically** — Work through each problem to internalize the patterns.
3. **Understand why, not just how** — Focus on the reasoning behind each solution.

---

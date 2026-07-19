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

Trees are recursive — master DFS (pre/in/post-order), BFS (level-order), and BST properties.

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

### Problem

Solves the All Nodes Distance Kin Binary Tree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class AllNodesDistanceKinBinaryTree {
    val parentMap = mutableMapOf<TreeNode, TreeNode?>()  // To store parent references

    /**
    * Solves the All Nodes Distance Kin Binary Tree problem.
    * Takes `root` (binary tree node reference), `target` (binary tree node reference), `k` (integer).
    *
    * @param root The binary tree node reference (nullable).
    * @param target The binary tree node reference (nullable).
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    fun distanceK(root: TreeNode?, target: TreeNode?, k: Int): List<Int> {
        val result = mutableListOf<Int>()

        // Helper function to perform DFS and populate parent map, then find target
        /**
        * Solves the All Nodes Distance Kin Binary Tree problem.
        * Takes `node` (binary tree node reference), `parent` (binary tree node reference).
        *
        * @param node The binary tree node reference (nullable).
        * @param parent The binary tree node reference (nullable).
        * @return Unit (no return value, modifies state in-place).
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
    * Helper: collect nodes at distance k.
    *
    * @param node The binary tree node reference (nullable).
    * @param k The integer parameter representing k.
    * @param visited The input MutableSet<TreeNode>.
    * @param result The input mutable list of integers.
    * @return Unit (no return value, modifies state in-place).
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Average Of Levels In Binary Tree

### Problem

Solves the Average Of Levels In Binary Tree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree.bfs

import tree.TreeNode
import java.util.*

class AverageOfLevelsInBinaryTree {
    /**
    * Solves the Average Of Levels In Binary Tree problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed floating-point result.
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
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Balanced Binary Tree

### Problem

Solves the Balanced Binary Tree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

import kotlin.math.abs

class BalancedBinaryTree {
    /**
    * Solves the Balanced Binary Tree problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isBalanced(root: TreeNode?): Boolean {
        /**
        * Solves the Balanced Binary Tree problem.
        * Takes `node` (binary tree node reference).
        *
        * @param node The binary tree node reference (nullable).
        * @return The computed integer result.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## B Inary Tree In Order Traversal Iterative

### Problem

Solves the BInary Tree In Order Traversal Iterative problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class BInaryTreeInOrderTraversalIterative {
    /**
    * Solves the BInary Tree In Order Traversal Iterative problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Binary Tree Level Order Traversal

### Problem

Solves the Binary Tree Level Order Traversal problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

import java.util.*
import kotlin.collections.ArrayList


class BinaryTreeLevelOrderTraversal {
    /**
    * Solves the Binary Tree Level Order Traversal problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
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
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Binary Tree Level Order Traversal_II

### Problem

Solves the Binary Tree Level Order Traversal_II problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree.bfs

import tree.TreeNode
import java.util.*

class BinaryTreeLevelOrderTraversal_II {
    /**
    * Solves the Binary Tree Level Order Traversal_II problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
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
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Binary Tree Maximum Path Sum

### Problem

Solves the Binary Tree Maximum Path Sum problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class BinaryTreeMaximumPathSum {
    /**
    * Solves the Binary Tree Maximum Path Sum problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
    */
    fun maxPathSum(root: TreeNode?): Int {
        var ans = Int.MIN_VALUE
        /**
        * Solves the Binary Tree Maximum Path Sum problem.
        * Takes `node` (binary tree node reference).
        *
        * @param node The binary tree node reference (nullable).
        * @return The computed integer result.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Binary Tree Right Side View

### Problem

Solves the Binary Tree Right Side View problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class BinaryTreeRightSideView {
    /**
    * Solves the Binary Tree Right Side View problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
    */
    fun rightSideView(root: TreeNode?): List<Int> {
        val rightSide = mutableListOf<Int>()

        /**
        * Solves the Binary Tree Right Side View problem.
        * Takes `node` (binary tree node reference), `level` (integer).
        *
        * @param node The binary tree node reference (nullable).
        * @param level The integer parameter representing level.
        * @return Unit (no return value, modifies state in-place).
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Binary Tree Vertical Order Traversal

### Problem

Solves the Binary Tree Vertical Order Traversal problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

import java.util.*

class BinaryTreeVerticalOrderTraversal {
/**
* Solves the Binary Tree Vertical Order Traversal problem.
* Takes `root` (binary tree node reference).
*
* @param root The binary tree node reference (nullable).
* @return The computed integer result.
*/
//    fun verticalOrder(root: TreeNode?): List<List<Int>> {
//        val result = TreeMap<Int, LinkedList<Int>>()
//
/**
* Solves the Binary Tree Vertical Order Traversal problem.
* Takes `node` (binary tree node reference), `verticalIndex` (Int = 0).
*
* @param node The binary tree node reference (nullable).
* @param verticalIndex The Int = 0.
* @return Unit (no return value, modifies state in-place).
*/
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
    * Solves the Binary Tree Vertical Order Traversal problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
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
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Binary Tree Vertical Order Traversal_Without Sorting

### Problem

Solves the Binary Tree Vertical Order Traversal_Without Sorting problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

import java.util.*

class BinaryTreeVerticalOrderTraversal_WithoutSorting {
    data class VerticalIndex(val node: TreeNode, val verticalIndex: Int)

    /**
    * Solves the Binary Tree Vertical Order Traversal_Without Sorting problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
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
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Binary Tree Zig Zag Level Order Traversal

### Problem

Solves the Binary Tree Zig Zag Level Order Traversal problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

import java.util.*

class BinaryTreeZigZagLevelOrderTraversal {
    data class IndexedNode(var node: TreeNode?, var index: Int)

    /**
    * Solves the Binary Tree Zig Zag Level Order Traversal problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
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
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Boundary Of Binary Tree

### Problem

Solves the Boundary Of Binary Tree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class BoundaryOfBinaryTree {
    /**
    * Solves the Boundary Of Binary Tree problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
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
    * Helper: add left boundary.
    *
    * @param node The binary tree node reference (nullable).
    * @param result The input mutable list of integers.
    * @return Unit (no return value, modifies state in-place).
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
    * Helper: add leaves.
    *
    * @param node The binary tree node reference (nullable).
    * @param result The input mutable list of integers.
    * @param isRoot A boolean flag: isRoot.
    * @return Unit (no return value, modifies state in-place).
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
    * Helper: add right boundary.
    *
    * @param node The binary tree node reference (nullable).
    * @param result The input mutable list of integers.
    * @return Unit (no return value, modifies state in-place).
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## BST Iterator

### Problem

Helper: push all left nodes.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
    * Helper: push all left nodes.
    *
    * @param node The binary tree node reference (nullable).
    * @return Unit (no return value, modifies state in-place).
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
    * Solves the BSTIterator problem.
    *
    * @return The computed integer result.
    */
    fun next(): Int {
        val node = stack.removeFirst()  // Pop the node from the stack
        pushAllLeftNodes(node.right)  // Push the leftmost nodes of the right child, if any
        return node.`val`
    }

    // Returns whether we have a next smallest number
    /**
    * Solves the BSTIterator problem.
    *
    * @return `true` if the condition is met, `false` otherwise.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Check Completeness Of Binary Tree

### Problem

Solves the Check Completeness Of Binary Tree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree.bfs

import tree.TreeNode

class CheckCompletenessOfBinaryTree {
    /**
    * Solves the Check Completeness Of Binary Tree problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return `true` if the condition is met, `false` otherwise.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Closest Binary Search Tree Value

### Problem

Solves the Closest Binary Search Tree Value problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree.bst

import kotlin.math.abs

class ClosestBinarySearchTreeValue {
    /**
    * Solves the Closest Binary Search Tree Value problem.
    * Takes `root` (binary tree node reference), `target` (double-precision floating point).
    *
    * @param root The binary tree node reference (nullable).
    * @param target The double-precision floating point parameter representing target.
    * @return The computed integer result.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Construct Binary Tree From Inorder And Post Order Traversal

### Problem

Solves the Construct Binary Tree From Inorder And Post Order Traversal problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class ConstructBinaryTreeFromInorderAndPostOrderTraversal {
    /**
    * Solves the Construct Binary Tree From Inorder And Post Order Traversal problem.
    * Takes `inorder` (array of integers), `postorder` (array of integers).
    *
    * @param inorder The input array of integers.
    * @param postorder The input array of integers.
    * @return The result, or `null` if not found.
    */
    fun buildTree(inorder: IntArray, postorder: IntArray): TreeNode? {
        // Build Inverted InOrder Index Map
        val rootIndices = mutableMapOf<Int, Int>()
        inorder.forEachIndexed { index, value -> rootIndices[value] = index }

        var postIndex = postorder.size - 1

        /**
        * Solves the Construct Binary Tree From Inorder And Post Order Traversal problem.
        * Takes `inorder` (array of integers), `postorder` (array of integers).
        *
        * @param inorder The input array of integers.
        * @param postorder The input array of integers.
        * @return The result, or `null` if not found.
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
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Construct Binary Tree From Preorder And In Order Traversal

### Problem

Solves the Construct Binary Tree From Preorder And In Order Traversal problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class ConstructBinaryTreeFromPreorderAndInOrderTraversal {
    private val rootIndices = mutableMapOf<Int, Int>()

    /**
    * Solves the Construct Binary Tree From Preorder And In Order Traversal problem.
    * Takes `preorder` (array of integers), `inorder` (array of integers).
    *
    * @param preorder The input array of integers.
    * @param inorder The input array of integers.
    * @return The result, or `null` if not found.
    */
    fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
        // Build Inverted InOrder Index Map
        inorder.forEachIndexed { index, value -> rootIndices[value] = index }
        var rootIndex = 0

        /**
        * Solves the Construct Binary Tree From Preorder And In Order Traversal problem.
        * Takes `preorder` (array of integers), `inorder` (array of integers).
        *
        * @param preorder The input array of integers.
        * @param inorder The input array of integers.
        * @return The result, or `null` if not found.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Construct Binary Tree From String

### Problem

Solves the Construct Binary Tree From String problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class ConstructBinaryTreeFromString {
    /**
    * Solves the Construct Binary Tree From String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The result, or `null` if not found.
    */
    fun str2tree(s: String): TreeNode? {
        if (s.isEmpty()) return null

        return buildTree(s, 0).first // We are only interested in the tree root, not the index
    }

    /**
    * Helper: build tree.
    *
    * @param s The input string.
    * @param i The integer parameter representing i.
    * @return The computed integer result.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Convert B Inary Search Tree To Sorted Doubly Linked List

### Problem

Definition for a Node.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
    * Solves the Convert BInary Search Tree To Sorted Doubly Linked List problem.
    * Takes `root` (Node?).
    *
    * @param root The Node? (nullable).
    * @return The result, or `null` if not found.
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
    * Helper: inorder traversal.
    *
    * @param node The Node? (nullable).
    * @return Unit (no return value, modifies state in-place).
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
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Count Good Node In B Inary Tree

### Problem

Solves the Count Good Node In BInary Tree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class CountGoodNodeInBInaryTree {
    /**
    * Solves the Count Good Node In BInary Tree problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
    */
    fun goodNodes(root: TreeNode?): Int {
        return dfs(root, Int.MIN_VALUE)
    }

    /**
    * Helper: dfs.
    *
    * @param node The binary tree node reference (nullable).
    * @param maxSoFar The integer parameter representing maxSoFar.
    * @return The computed integer result.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Tree Node

### Problem

Solves the Tree Node problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
    * Solves the Tree Node problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
    */
    fun averageOfSubtree(root: TreeNode?): Int {
        postOrder(root)
        return count;
    }

    /**
    * Helper: post order.
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed result (Result).
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Tree Node

### Problem

Solves the Tree Node problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree.bst

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class DeleteNodeinABST {
    /**
    * Solves the Tree Node problem.
    * Takes `root` (binary tree node reference), `key` (integer).
    *
    * @param root The binary tree node reference (nullable).
    * @param key The integer parameter representing key.
    * @return The result, or `null` if not found.
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
    * Solves the Tree Node problem.
    * Takes `node` (TreeNode).
    *
    * @param node The TreeNode.
    * @return The computed integer result.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Find Largest Value In Each Tree Row

### Problem

Solves the Find Largest Value In Each Tree Row problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree.bfs

import tree.TreeNode
import java.util.*

class FindLargestValueInEachTreeRow {
    /**
    * Solves the Find Largest Value In Each Tree Row problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
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
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Inorder Successor

### Problem

Solves the Inorder Successor problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree.bst

class InorderSuccessor {
    /**
    * Solves the Inorder Successor problem.
    * Takes `root` (binary tree node reference), `p` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @param p The binary tree node reference (nullable).
    * @return The result, or `null` if not found.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Leaf Similar

### Problem

Solves the Leaf Similar problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class LeafSimilar {
    /**
    * Solves the Leaf Similar problem.
    * Takes `root1` (binary tree node reference), `root2` (binary tree node reference).
    *
    * @param root1 The binary tree node reference (nullable).
    * @param root2 The binary tree node reference (nullable).
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun leafSimilar(root1: TreeNode?, root2: TreeNode?): Boolean {
        val leaves1 = mutableListOf<Int>()
        val leaves2 = mutableListOf<Int>()

        dfs(root1, leaves1)
        dfs(root2, leaves2)

        return leaves1 == leaves2
    }

    /**
    * Solves the Leaf Similar problem.
    * Takes `node` (binary tree node reference), `leafValues` (mutable list of integers).
    *
    * @param node The binary tree node reference (nullable).
    * @param leafValues The input mutable list of integers.
    * @return Unit (no return value, modifies state in-place).
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Longest Univalue Path

### Problem

Solves the Longest Univalue Path problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class LongestUnivaluePath {

    /**
    * Solves the Longest Univalue Path problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
    */
    fun longestUnivaluePath(root: TreeNode?): Int {
        var maxLength = 0
        /**
        * Solves the Longest Univalue Path problem.
        * Takes `node` (binary tree node reference).
        *
        * @param node The binary tree node reference (nullable).
        * @return The computed integer result.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Lowest Common Ancestor

### Problem

Solves the Lowest Common Ancestor problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class LowestCommonAncestor {
    /**
    * Solves the Lowest Common Ancestor problem.
    * Takes `root` (binary tree node reference), `p` (binary tree node reference), `q` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @param p The binary tree node reference (nullable).
    * @param q The binary tree node reference (nullable).
    * @return The result, or `null` if not found.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Lowest Common Ancestor_III

### Problem

Solves the Lowest Common Ancestor_III problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
    * Solves the Lowest Common Ancestor_III problem.
    * Takes `p` (Node?), `q` (Node?).
    *
    * @param p The Node? (nullable).
    * @param q The Node? (nullable).
    * @return The result, or `null` if not found.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Maximum Depth Of Binary Tree

### Problem

Solves the Maximum Depth Of Binary Tree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class MaximumDepthOfBinaryTree {
    /**
    * Solves the Maximum Depth Of Binary Tree problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Maximum Sum BST In Binary Tree

### Problem

Solves the Maximum Sum BSTIn Binary Tree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class MaximumSumBSTInBinaryTree {
    data class Result(val isBST: Boolean, val sum: Int, val min: Int, val max: Int)
    private var maxSum = 0

    /**
    * Solves the Maximum Sum BSTIn Binary Tree problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
    */
    fun maxSumBST(root: TreeNode?): Int {
        dfs(root)
        return maxSum
    }

    /**
    * Helper: dfs.
    *
    * @param node The binary tree node reference (nullable).
    * @return The computed result (Result).
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Maximum Width Of Binary Tree

### Problem

Solves the Maximum Width Of Binary Tree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

import java.util.*

class MaximumWidthOfBinaryTree {
    data class Node(var node: TreeNode?, var index: Int)

    /**
    * Solves the Maximum Width Of Binary Tree problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
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
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Minimum Time To Collect All Apples In A Tree

### Problem

Solves the Minimum Time To Collect All Apples In ATree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class MinimumTimeToCollectAllApplesInATree {
    /**
    * Solves the Minimum Time To Collect All Apples In ATree problem.
    * Takes `n` (integer), `edges` (2D matrix of integers), `hasApple` (List<Boolean>).
    *
    * @param n The integer parameter representing n.
    * @param edges The input 2D matrix of integers.
    * @param hasApple The input List<Boolean>.
    * @return The computed integer result.
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
        * Solves the Minimum Time To Collect All Apples In ATree problem.
        * Takes `node` (integer), `parent` (integer).
        *
        * @param node The integer parameter representing node.
        * @param parent The integer parameter representing parent.
        * @return The computed integer result.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Path Sum

### Problem

Solves the Path Sum problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class PathSum {
    /**
    * Solves the Path Sum problem.
    * Takes `root` (binary tree node reference), `targetSum` (integer).
    *
    * @param root The binary tree node reference (nullable).
    * @param targetSum The integer parameter representing targetSum.
    * @return `true` if the condition is met, `false` otherwise.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Path Sum_II

### Problem

Solves the Path Sum_II problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class PathSum_II {
    /**
    * Solves the Path Sum_II problem.
    * Takes `root` (binary tree node reference), `targetSum` (integer).
    *
    * @param root The binary tree node reference (nullable).
    * @param targetSum The integer parameter representing targetSum.
    * @return The computed integer result.
    */
    fun pathSum(root: TreeNode?, targetSum: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()

        /**
        * Solves the Path Sum_II problem.
        * Takes `node` (binary tree node reference), `currentSum` (integer), `path` (MutableList<Int> = mutableListOf().
        *
        * @param node The binary tree node reference (nullable).
        * @param currentSum The integer parameter representing currentSum.
        * @param path The input MutableList<Int> = mutableListOf(.
        * @return Unit (no return value, modifies state in-place).
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Path Sum III

### Problem

Solves the Path Sum III problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class PathSumIII {
    // O(N^2) solution
    /**
    * Solves the Path Sum III problem.
    * Takes `root` (binary tree node reference), `targetSum` (integer).
    *
    * @param root The binary tree node reference (nullable).
    * @param targetSum The integer parameter representing targetSum.
    * @return The computed integer result.
    */
    fun pathSum(root: TreeNode?, targetSum: Int): Int {
        if (root == null)
            return 0

        // Count paths with targetSum starting from the current node
        /**
        * Solves the Path Sum III problem.
        * Takes `node` (binary tree node reference), `currentSum` (long integer).
        *
        * @param node The binary tree node reference (nullable).
        * @param currentSum The long integer parameter representing currentSum.
        * @return The computed integer result.
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
    * Solves the Path Sum III problem.
    * Takes `root` (binary tree node reference), `targetSum` (integer).
    *
    * @param root The binary tree node reference (nullable).
    * @param targetSum The integer parameter representing targetSum.
    * @return The computed integer result.
    */
    fun pathSum_prefix_sum(root: TreeNode?, targetSum: Int): Int {
        // HashMap to store prefix sums and their frequencies
        val prefixSumCount = HashMap<Long, Int>()
        // Initialize with a prefix sum of 0 having occurred once (considering no node)
        prefixSumCount[0L] = 1

        // Helper function to perform DFS
        /**
        * Solves the Path Sum III problem.
        * Takes `node` (binary tree node reference), `currentSum` (long integer).
        *
        * @param node The binary tree node reference (nullable).
        * @param currentSum The long integer parameter representing currentSum.
        * @return The computed integer result.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Populate Next Right Pointers In Each Node_II

### Problem

Solves the Populate Next Right Pointers In Each Node_II problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

import java.util.*

class PopulateNextRightPointersInEachNode_II {
    /**
    * Solves the Populate Next Right Pointers In Each Node_II problem.
    * Takes `root` (Node?).
    *
    * @param root The Node? (nullable).
    * @return The result, or `null` if not found.
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
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Populate Next Right Pointers In Each Node_II_Constant

### Problem

Solves the Populate Next Right Pointers In Each Node_II_Constant problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

import java.util.*

class PopulateNextRightPointersInEachNode_II_Constant {
    /**
    * Solves the Populate Next Right Pointers In Each Node_II_Constant problem.
    * Takes `root` (Node?).
    *
    * @param root The Node? (nullable).
    * @return The result, or `null` if not found.
    */
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

---

## Node

### Problem

Solves the Node problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
    /**
    * Solves the Node problem.
    * Takes `root` (Node?).
    *
    * @param root The Node? (nullable).
    * @return The result, or `null` if not found.
    */
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

---

## Range Sum Of BST

### Problem

Solves the Range Sum Of BST problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package graph.bst

class RangeSumOfBST {
    /**
    * Solves the Range Sum Of BST problem.
    * Takes `root` (binary tree node reference), `low` (integer), `high` (integer).
    *
    * @param root The binary tree node reference (nullable).
    * @param low The integer parameter representing low.
    * @param high The integer parameter representing high.
    * @return The computed integer result.
    */
    fun rangeSumBST(root: TreeNode?, low: Int, high: Int): Int {
        var sum = 0
        /**
        * Solves the Range Sum Of BST problem.
        * Takes `node` (binary tree node reference).
        *
        * @param node The binary tree node reference (nullable).
        * @return Unit (no return value, modifies state in-place).
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Recover A Tree From Pre Order Traversal

### Problem

Solves the Recover ATree From Pre Order Traversal problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class RecoverATreeFromPreOrderTraversal {
    /**
    * Solves the Recover ATree From Pre Order Traversal problem.
    * Takes `traversal` (string).
    *
    * @param traversal The input string.
    * @return The result, or `null` if not found.
    */
    fun recoverFromPreorder(traversal: String): TreeNode? {
        var index = 0 // Global index to track position in the string

        // Recursive function to build the tree
        /**
        * Solves the Recover ATree From Pre Order Traversal problem.
        * Takes `depth` (integer).
        *
        * @param depth The integer parameter representing depth.
        * @return The result, or `null` if not found.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Recover Binary Search Tree

### Problem

Solves the Recover Binary Search Tree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree.bst

class RecoverBinarySearchTree {
    /**
    * Solves the Recover Binary Search Tree problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return Unit (no return value, modifies state in-place).
    */
    fun recoverTree(root: TreeNode?) {
        var first: TreeNode? = null
        var second: TreeNode? = null
        var prev: TreeNode? = null

        // Helper function to perform in-order traversal
        /**
        * Solves the Recover Binary Search Tree problem.
        * Takes `node` (binary tree node reference).
        *
        * @param node The binary tree node reference (nullable).
        * @return Unit (no return value, modifies state in-place).
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Codec

### Problem

Solves the Codec problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }

class Codec() {
    // Encodes a URL to a shortened URL.
    * Solves the Codec problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The resulting string.
    /**
    * Solves the Codec problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The resulting string.
    */
    fun serialize(root: TreeNode?): String {
        val serializedTree = StringBuilder()

        * Solves the Codec problem.
        * Takes `node` (binary tree node reference).
        *
        * @param node The binary tree node reference (nullable).
        * @return Unit (no return value, modifies state in-place).
        /**
        * Solves the Codec problem.
        * Takes `node` (binary tree node reference).
        *
        * @param node The binary tree node reference (nullable).
        * @return Unit (no return value, modifies state in-place).
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
    * Solves the Codec problem.
    * Takes `data` (string).
    *
    * @param data The input string.
    * @return The result, or `null` if not found.
    /**
    * Solves the Codec problem.
    * Takes `data` (string).
    *
    * @param data The input string.
    * @return The result, or `null` if not found.
    */
    fun deserialize(data: String): TreeNode? {
        val nodes = data.split(",").toMutableList()

        * Solves the Codec problem.
        *
        * @return The result, or `null` if not found.
        /**
        * Solves the Codec problem.
        *
        * @return The result, or `null` if not found.
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

 * Your Codec object will be instantiated and called as such:
 * var ser = Codec()
 * var deser = Codec()
 * var data = ser.serialize(longUrl)
 * var ans = deser.deserialize(data)
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Serialize And Deserialize N Array Tree

### Problem

Solves the Serialize And Deserialize NArray Tree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
        * Solves the Serialize And Deserialize NArray Tree problem.
        * Takes `root` (Node?).
        *
        * @param root The Node? (nullable).
        * @return The resulting string.
        */
        fun serialize(root: Node?): String = when (root) {
            null -> ""
            else -> buildString {
                /**
                * Solves the Serialize And Deserialize NArray Tree problem.
                * Takes `node` (Node?).
                *
                * @param node The Node? (nullable).
                * @return Unit (no return value, modifies state in-place).
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
        * Solves the Serialize And Deserialize NArray Tree problem.
        * Takes `data` (string).
        *
        * @param data The input string.
        * @return The result, or `null` if not found.
        */
        fun deserialize(data: String): Node? {
            if (data.isEmpty()) return null

            val tokens = data.split(",")
            var index = 0

            /**
            * Solves the Serialize And Deserialize NArray Tree problem.
            *
            * @return The result, or `null` if not found.
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Step By Step Directions From A Node To Another

### Problem

Solves the Step By Step Directions From ANode To Another problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class StepByStepDirectionsFromANodeToAnother {
    /**
    * Solves the Step By Step Directions From ANode To Another problem.
    * Takes `root` (binary tree node reference), `searchKey` (integer).
    *
    * @param root The binary tree node reference (nullable).
    * @param searchKey The integer parameter representing searchKey.
    * @return The result, or `null` if not found.
    */
    fun findNode(root: TreeNode?, searchKey: Int): TreeNode? {
        return when {
            root == null -> null
            root.`val` == searchKey -> root
            else -> findNode(root.left, searchKey) ?: findNode(root.right, searchKey)
        }
    }

    /**
    * Solves the Step By Step Directions From ANode To Another problem.
    * Takes `root` (binary tree node reference), `p` (binary tree node reference), `q` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @param p The binary tree node reference (nullable).
    * @param q The binary tree node reference (nullable).
    * @return The result, or `null` if not found.
    */
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
        if (root == null || root === p || root === q) return root

        val left = lowestCommonAncestor(root.left, p, q)
        val right = lowestCommonAncestor(root.right, p, q)

        return if (left != null && right != null) root else left ?: right

    }

    /**
    * Solves the Step By Step Directions From ANode To Another problem.
    * Takes `root` (binary tree node reference), `startValue` (integer), `destValue` (integer).
    *
    * @param root The binary tree node reference (nullable).
    * @param startValue The integer parameter representing startValue.
    * @param destValue The integer parameter representing destValue.
    * @return The resulting string.
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
    * Helper: build path.
    *
    * @param node The binary tree node reference (nullable).
    * @param target The binary tree node reference (nullable).
    * @param path The input string.
    * @return `true` if the condition is met, `false` otherwise.
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
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Sum Root To Leaf Numbers

### Problem

Solves the Sum Root To Leaf Numbers problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

class SumRootToLeafNumbers {
    /**
    * Solves the Sum Root To Leaf Numbers problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
    */
    fun sumNumbers(root: TreeNode?): Int {
        var sum = 0

        /**
        * Solves the Sum Root To Leaf Numbers problem.
        * Takes `node` (binary tree node reference), `sumSoFar` (integer).
        *
        * @param node The binary tree node reference (nullable).
        * @param sumSoFar The integer parameter representing sumSoFar.
        * @return Unit (no return value, modifies state in-place).
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Vertical Order Traversal Of A Binary Tree

### Problem

Solves the Vertical Order Traversal Of ABinary Tree problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package tree

import java.util.*

class VerticalOrderTraversalOfABinaryTree {
    data class VerticalIndex(val node: TreeNode, val verticalIndex: Int)

    /**
    * Solves the Vertical Order Traversal Of ABinary Tree problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
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
| **Time** | O(V + E) |
| **Space** | O(V) |

---

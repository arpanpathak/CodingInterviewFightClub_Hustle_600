---
layout: chapter
title: "Trees - Hierarchical Thinking"
chapter_number: 5
chapter_title: "Trees"
toc: true
prev_chapter:
  url: "/chapters/04-linked-lists"
  title: "Linked Lists - Pointer Manipulation"
next_chapter:
  url: "/chapters/06-graphs"
  title: "Graphs - The Real World Is a Graph"
---

# Trees: Hierarchical Thinking

## Complete Problem Set (45+ problems)

### Tree Traversal (10 problems)
| # | Problem | File |
|---|---------|------|
| 1 | Inorder Traversal (Iterative) | tree/BInaryTreeInOrderTraversalIterative.kt |
| 2 | Level Order Traversal | tree/BinaryTreeLevelOrderTraversal.kt |
| 3 | Level Order II (Bottom-up) | tree/bfs/BinaryTreeLevelOrderTraversal_II.kt |
| 4 | Zigzag Level Order | tree/BinaryTreeZigZagLevelOrderTraversal.kt |
| 5 | Right Side View | tree/BinaryTreeRightSideView.kt |
| 6 | Vertical Order Traversal | tree/BinaryTreeVerticalOrderTraversal.kt |
| 7 | Vertical Order (no sort) | tree/BinaryTreeVerticalOrderTraversal_WithoutSorting.kt |
| 8 | Boundary of Binary Tree | tree/BoundaryOfBinaryTree.kt |
| 9 | Average of Levels | tree/bfs/AverageOfLevelsInBinaryTree.kt |
| 10 | Largest Value in Each Row | tree/bfs/FindLargestValueInEachTreeRow.kt |

### Tree Properties (13 problems)
| # | Problem | File |
|---|---------|------|
| 11 | Max Depth of Binary Tree | tree/MaximumDepthOfBinaryTree.kt |
| 12 | Balanced Binary Tree | tree/BalancedBinaryTree.kt |
| 13 | Diameter of Binary Tree | graph/DiameterOfBinaryTree.kt |
| 14 | Count Good Nodes | tree/CountGoodNodeInBInaryTree.kt |
| 15 | Count Nodes Equal to Average | tree/CountNodeEqualsAverage.kt |
| 16 | Leaf Similar Trees | tree/LeafSimilar.kt |
| 17 | Max Width of Binary Tree | tree/MaximumWidthOfBinaryTree.kt |
| 18 | Check Completeness | tree/bfs/CheckCompletenessOfBinaryTree.kt |
| 19 | Path Sum | tree/PathSum.kt |
| 20 | Path Sum II | tree/PathSum_II.kt |
| 21 | Path Sum III | tree/PathSumIII.kt |
| 22 | Sum Root to Leaf Numbers | tree/SumRootToLeafNumbers.kt |
| 23 | Longest Univalue Path | tree/LongestUnivaluePath.kt |

### Tree Construction (5 problems)
| # | Problem | File |
|---|---------|------|
| 24 | Construct from Preorder & Inorder | tree/ConstructBinaryTreeFromPreorderAndInOrderTraversal.kt |
| 25 | Construct from Inorder & Postorder | tree/ConstructBinaryTreeFromInorderAndPostOrderTraversal.kt |
| 26 | Construct from String | tree/ConstructBinaryTreeFromString.kt |
| 27 | Serialize & Deserialize Binary Tree | tree/SerializeAndDeserializeABinaryTree.kt |
| 28 | Serialize & Deserialize N-ary Tree | tree/SerializeAndDeserializeNArrayTree.kt |

### BST (8 problems)
| # | Problem | File |
|---|---------|------|
| 29 | Validate BST | tree/bst/ValidateBST.kt |
| 30 | BST Iterator | tree/bst/BSTIterator.kt |
| 31 | Inorder Successor | tree/bst/InorderSuccessor.kt |
| 32 | Delete Node in BST | tree/bst/DeleteNodeinABST.kt |
| 33 | Convert BST to Greater Sum | graph/bst/BinarySearchTreeToGreaterSumTree.kt |
| 34 | Range Sum of BST | graph/bst/RangeSumOfBST.kt |
| 35 | Recover BST | tree/bst/RecoverBinarySearchTree.kt |
| 36 | Closest BST Value | tree/bst/ClosestBinarySearchTreeValue.kt |

### Advanced (12 problems)
| # | Problem | File |
|---|---------|------|
| 37 | Lowest Common Ancestor | tree/LowestCommonAncestor.kt |
| 38 | LCA III (w/ parent) | tree/LowestCommonAncestor_III.kt |
| 39 | Binary Tree Max Path Sum | tree/BinaryTreeMaximumPathSum.kt |
| 40 | Max Sum BST in BT | tree/MaximumSumBSTInBinaryTree.kt |
| 41 | All Nodes Distance K | tree/AllNodesDistanceKinBinaryTree.kt |
| 42 | Populating Next Right | tree/PopulatingNextRightPointerInEachNode.kt |
| 43 | Populating Next II Constant | tree/PopulateNextRightPointersInEachNode_II_Constant.kt |
| 44 | Step-by-Step Directions | tree/StepByStepDirectionsFromANodeToAnother.kt |
| 45 | Recover Tree from Preorder | tree/RecoverATreeFromPreOrderTraversal.kt |
| 46 | Longest Path Diff Adjacent | tree/LongestPathWithDifferentAdjacentCharacters.kt |
| 47 | Diameter of N-ary Tree | tree/DiameterOfNArrayTree.kt |
| 48 | Convert BST to Sorted DLL | tree/bst/ConvertBInarySearchTreeToSortedDoublyLinkedList.kt |

### Fenwick Tree (3 problems)
| # | Problem | File |
|---|---------|------|
| 49 | Fenwick Tree Implementation | tree/fenwick/FenwickTree.kt |
| 50 | Count of Smaller After Self | tree/fenwick/CountOfSmallerNumberAfterSelf.kt |
| 51 | Range Sum Query Mutable | tree/fenwick/RangeSumQueryMutable.kt |

### Trie (9 problems)
| # | Problem | File |
|---|---------|------|
| 52 | Implement Trie | trie/Trie.kt |
| 53 | Word Search II | trie/WordSearch_II.kt |
| 54 | AutoComplete System | trie/AutoCompleteSystem.kt |
| 55 | AutoComplete with Heap | trie/AutoCompleteSystemWithHeap.kt |
| 56 | Design Add and Search Words | trie/DesignAddAndSearchWordsDataStructure.kt |
| 57 | Max XOR of Two Numbers | trie/MaximumXOROfTwoNumbersInAnArray.kt |
| 58 | Word Break | trie/WordBreak.kt |
| 59 | Replace Words | trie/ReplaceWords.kt |
| 60 | Index Pairs of a String | trie/IndexPairsOfAString.kt |

### Key Solutions

```kotlin
// Max Depth
fun maxDepth(root: TreeNode?): Int = if (root == null) 0 else 1 + maxOf(maxDepth(root.left), maxDepth(root.right))

// Validate BST
fun isValidBST(root: TreeNode?): Boolean {
    fun check(n: TreeNode?, min: Long, max: Long): Boolean {
        if (n == null) return true
        if (n.`val` <= min || n.`val` >= max) return false
        return check(n.left, min, n.`val`.toLong()) && check(n.right, n.`val`.toLong(), max)
    }
    return check(root, Long.MIN_VALUE, Long.MAX_VALUE)
}

// LCA
fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
    if (root == null || root == p || root == q) return root
    val l = lowestCommonAncestor(root.left, p, q)
    val r = lowestCommonAncestor(root.right, p, q)
    return if (l != null && r != null) root else l ?: r
}

// Level Order
fun levelOrder(root: TreeNode?): List<List<Int>> {
    val res = mutableListOf<List<Int>>()
    val q = ArrayDeque<TreeNode>(); root?.let { q.add(it) }
    while (q.isNotEmpty()) {
        val level = mutableListOf<Int>()
        repeat(q.size) { val n = q.removeFirst(); level.add(n.`val`); n.left?.let { q.add(it) }; n.right?.let { q.add(it) } }
        res.add(level)
    }
    return res
}

// Serialize
class Codec {
    fun serialize(root: TreeNode?): String {
        val sb = StringBuilder()
        fun dfs(n: TreeNode?) { if (n == null) { sb.append("null,"); return }; sb.append("${n.`val`},"); dfs(n.left); dfs(n.right) }
        dfs(root); return sb.toString()
    }
    fun deserialize(data: String): TreeNode? {
        val q = ArrayDeque(data.split(","))
        fun build(): TreeNode? { val v = q.removeFirst(); if (v == "null") return null; return TreeNode(v.toInt()).apply { left = build(); right = build() } }
        return build()
    }
}
```

---

> **Next up: [Graphs ->](./06-graphs.md)**

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

> **3 problems** — Master union-find for connectivity and dynamic graph components.

## The Pattern

DSU tracks connected components. Union by rank + path compression = near-O(1).

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [Account Merge](#accountmerge) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Number Of Island_II](#numberofisland_ii) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Union Find](#unionfind) | — | <span class="badge badge-medium">Medium</span> |

---

## Account Merge

### Problem

Solves the Account Merge problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package disjointset


class AccountMerge {
    class UnionFind<T> {
        data class Node<T>(var parent: T, var rank: Int)

        private val nodes = mutableMapOf<T, Node<T>>()

        /**
        * Solves the Account Merge problem.
        * Takes `x` (T).
        *
        * @param x The T.
        * @return Unit (no return value, modifies state in-place).
        */
        fun add(x: T) {
            nodes.putIfAbsent(x, Node(x, 0))
        }

        /**
        * Solves the Account Merge problem.
        * Takes `x` (T).
        *
        * @param x The T.
        * @return The computed result (T).
        */
        fun find(x: T): T {
            val node = nodes[x] ?: throw IllegalAccessException("Value $x not found")

            if (node.parent != x)
                node.parent = find(node.parent)

            return node.parent
        }

        /**
        * Solves the Account Merge problem.
        * Takes `x` (T), `y` (T).
        *
        * @param x The T.
        * @param y The T.
        * @return Unit (no return value, modifies state in-place).
        */
        fun union(x: T, y: T) {
            val rootX = find(x)
            val rootY = find(y)
            if (rootX != rootY) {
                val nodeX = nodes[rootX]!!
                val nodeY = nodes[rootY]!!
                when {
                    nodeX.rank > nodeY.rank -> nodeY.parent = rootX
                    nodeX.rank < nodeY.rank -> nodeX.parent = rootY
                    else -> {
                        nodeY.parent = rootX
                        nodeX.rank++
                    }
                }
            }
        }
    }

    /**
    * Solves the Account Merge problem.
    * Takes `accounts` (List<List<String>>).
    *
    * @param accounts The input List<List<String>>.
    * @return The resulting collection (List<List<String>).
    */
    fun accountsMerge(accounts: List<List<String>>): List<List<String>> {
        val emailToName = mutableMapOf<String, String>()
        val uf = UnionFind<String>()

        // Add emails to Union-Find, map them to their owner's name, and union them in one pass
        accounts.forEach { account ->
            val name = account.first()
            account.drop(1).let { emails ->
                val firstEmail = emails.first()
                emails.forEach { email ->
                    emailToName[email] = name
                    uf.add(email)
                    uf.union(firstEmail, email)
                }
            }
        }

        // Group emails by their root parent
        val components = emailToName.keys.groupBy { uf.find(it) }

        // Construct the result
        return components.values.map { emails ->
            emails.sorted().let { sortedEmails ->
                listOf(emailToName[sortedEmails.first()]!!) + sortedEmails
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

## Number Of Island_II

### Problem

Solves the Number Of Island_II problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package disjointset

class NumberOfIsland_II {
    private class UnionFind {
        val parent = mutableMapOf<Pair<Int, Int>, Pair<Int, Int>>()
        val rank = mutableMapOf<Pair<Int, Int>, Int>()
        var count = 0

        /**
        * Solves the Number Of Island_II problem.
        * Takes `x` (Pair<Int).
        *
        * @param x The Pair<Int.
        * @return The computed integer result.
        */
        fun find(x: Pair<Int, Int>): Pair<Int, Int> {
            if (parent[x] != x) {
                parent[x] = find(parent[x]!!) // Path compression
            }
            return parent[x]!!
        }

        /**
        * Solves the Number Of Island_II problem.
        * Takes `x` (Pair<Int), `y` (Pair<Int).
        *
        * @param x The Pair<Int.
        * @param y The Pair<Int.
        * @return Unit (no return value, modifies state in-place).
        */
        fun union(x: Pair<Int, Int>, y: Pair<Int, Int>) {
            val rootX = find(x)
            val rootY = find(y)
            if (rootX == rootY) return

            when {
                rank[rootX]!! > rank[rootY]!! -> parent[rootY] = rootX
                rank[rootX]!! < rank[rootY]!! -> parent[rootX] = rootY
                else -> {
                    parent[rootY] = rootX
                    rank[rootX] = rank[rootX]!! + 1
                }
            }
            count--
        }

        /**
        * Solves the Number Of Island_II problem.
        * Takes `position` (Pair<Int).
        *
        * @param position The Pair<Int.
        * @return Unit (no return value, modifies state in-place).
        */
        fun addLand(position: Pair<Int, Int>) {
            if (parent.containsKey(position)) return
            parent[position] = position
            rank[position] = 0
            count++
        }
    }

    /**
    * Solves the Number Of Island_II problem.
    * Takes `m` (integer), `n` (integer), `positions` (2D matrix of integers).
    *
    * @param m The integer parameter representing m.
    * @param n The integer parameter representing n.
    * @param positions The input 2D matrix of integers.
    * @return The computed integer result.
    */
    fun numIslands2(m: Int, n: Int, positions: Array<IntArray>): List<Int> {
        val uf = UnionFind()
        val result = mutableListOf<Int>()
        val directions = arrayOf(0 to 1, 1 to 0, 0 to -1, -1 to 0)

        for (pos in positions) {
            val (r, c) = pos
            val current = r to c
            uf.addLand(current)

            for ((dr, dc) in directions) {
                val nr = r + dr
                val nc = c + dc
                if (nr in 0 until m && nc in 0 until n) {
                    val neighbor = nr to nc
                    if (uf.parent.containsKey(neighbor)) {
                        uf.union(current, neighbor)
                    }
                }
            }
            result.add(uf.count)
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

## Union Find

### Problem

Solves the Union Find problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package disjointset

class UnionFind<T> {
    data class Node<T>(var parent: T, var rank: Int)

    private val nodes = mutableMapOf<T, Node<T>>()

    /**
    * Solves the Union Find problem.
    * Takes `x` (T).
    *
    * @param x The T.
    * @return Unit (no return value, modifies state in-place).
    */
    fun add(x: T) {
        nodes.putIfAbsent(x, Node(x, 0))
    }

    /**
    * Solves the Union Find problem.
    * Takes `x` (T).
    *
    * @param x The T.
    * @return The computed result (T).
    */
    fun find(x: T): T {
        val node = nodes[x] ?: throw IllegalAccessException("Value $x not found")

        if (node.parent != x)
            node.parent = find(node.parent)

        return node.parent
    }

    /**
    * Solves the Union Find problem.
    * Takes `x` (T), `y` (T).
    *
    * @param x The T.
    * @param y The T.
    * @return Unit (no return value, modifies state in-place).
    */
    fun union(x: T, y: T) {
        val rootX = find(x)
        val rootY = find(y)
        if (rootX != rootY) {
            val nodeX = nodes[rootX]!!
            val nodeY = nodes[rootY]!!
            when {
                nodeX.rank > nodeY.rank -> nodeY.parent = rootX
                nodeX.rank < nodeY.rank -> nodeX.parent = rootY
                else -> {
                    nodeY.parent = rootX
                    nodeX.rank++
                }
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

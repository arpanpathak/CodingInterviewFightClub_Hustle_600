---
layout: chapter
title: "Disjoint Set Union - Union-Find"
chapter_number: 9
chapter_title: "Disjoint Set Union"
toc: true
prev_chapter:
  url: "/chapters/08-heaps"
  title: "Heaps & Priority Queues"
next_chapter:
  url: "/chapters/10-string-matching"
  title: "String Matching - KMP, Rabin-Karp & More"
---

# Disjoint Set Union (Union-Find)

## Core Implementation

```kotlin
/**
 * UNION-FIND with path compression and union by rank.
 * Time: O(alpha(n)) per operation (inverse Ackermann - near constant)
 */
class UnionFind(n: Int) {
    private val parent = IntArray(n) { it }
    private val rank = IntArray(n) { 0 }
    
    fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])  // Path compression
        return parent[x]
    }
    
    fun union(x: Int, y: Int) {
        val (px, py) = find(x) to find(y)
        if (px == py) return
        when {
            rank[px] < rank[py] -> parent[px] = py
            rank[px] > rank[py] -> parent[py] = px
            else -> { parent[py] = px; rank[px]++ }
        }
    }
    
    fun connected(x: Int, y: Int) = find(x) == find(y)
}
```

## Complete Problem Set (3 problems)

| # | Problem | Difficulty | File |
|---|---------|------------|------|
| 1 | Number of Islands II | Hard | disjointset/NumberOfIsland_II.kt |
| 2 | Account Merge | Medium | disjointset/AccountMerge.kt |
| 3 | Union Find (Template) | Medium | disjointset/UnionFind.kt |

### Account Merge
```kotlin
fun accountsMerge(accounts: List<List<String>>): List<List<String>> {
    val emailToId = mutableMapOf<String, Int>()
    val emailToName = mutableMapOf<String, String>()
    var id = 0
    for (acct in accounts) {
        val name = acct[0]
        for (i in 1 until acct.size) {
            emailToId.putIfAbsent(acct[i], id++) 
            emailToName[acct[i]] = name
        }
    }
    val uf = UnionFind(id)
    for (acct in accounts) {
        val firstEmail = acct[1]
        for (i in 2 until acct.size) uf.union(emailToId[firstEmail]!!, emailToId[acct[i]]!!)
    }
    val groups = mutableMapOf<Int, MutableList<String>>()
    for (email in emailToId.keys) {
        groups.getOrPut(uf.find(emailToId[email]!!)) { mutableListOf() }.add(email)
    }
    return groups.map { (id, emails) -> listOf(emailToName[emails[0]]!!) + emails.sorted() }
}
```

---

> **Next up: [String Matching ->](./10-string-matching.md)**

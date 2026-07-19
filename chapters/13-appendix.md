---
layout: chapter
title: "Appendix - The Gigachad Toolkit & Original Code Vault"
chapter_number: 13
chapter_title: "Appendix"
toc: true
prev_chapter:
  url: "/chapters/12-caches"
  title: "Caches - LRU, LFU & Memory Management"
---

# Appendix: The Complete Gigachad Toolkit

> **"This is where we go beyond. The elite tier. The tools that separate L5/L6 engineers from the rest."**

## Original Fight Club Narratives

### The Motivation

The modern tech interview is less about finding a competent coder and more about passing a highly standardized, artificial test. The motivation behind creating the "Coding Interview Fight Club" is threefold:

1. **High Stakes:** The difference between landing a top-tier role and not is often measured in hundreds of thousands of dollars (TC or GTFO).
2. **The Bar is High and Unforgiving:** Companies like Google, Meta, Amazon, and Netflix have inflated interview difficulty.
3. **Efficiency and Focus:** Time is your most valuable asset.

> Signals that an interviewer is looking for a candidate (Who am I? I conducted 46 coding interviews and attended 13 debriefs.)

---

## Advanced Graph Algorithms

### Kosaraju's Algorithm (SCC)

```kotlin
class Graph<T> {
   private val adj = mutableMapOf<T, MutableList<T>>()
   private val revAdj = mutableMapOf<T, MutableList<T>>()

   fun addEdge(u: T, v: T) {
       adj.getOrPut(u) { mutableListOf() }.add(v)
       revAdj.getOrPut(v) { mutableListOf() }.add(u)
   }

   fun getSCCs(): List<List<T>> {
       val visited = mutableSetOf<T>()
       val visitOrderStack = ArrayDeque<T>()
       adj.keys.forEach { vertex ->
           if (vertex !in visited) fillOrder(vertex, visited, visitOrderStack)
       }
       visited.clear()
       return buildList {
           while (visitOrderStack.isNotEmpty()) {
               val vertex = visitOrderStack.removeLast()
               if (vertex !in visited) {
                   add(buildList { dfsOnReversed(vertex, visited, this) })
               }
           }
       }
   }
   private fun fillOrder(vertex: T, visited: MutableSet<T>, stack: ArrayDeque<T>) {
       visited.add(vertex)
       adj[vertex]?.forEach { n -> if (n !in visited) fillOrder(n, visited, stack) }
       stack.addLast(vertex)
   }
   private fun dfsOnReversed(vertex: T, visited: MutableSet<T>, comp: MutableList<T>) {
       visited.add(vertex); comp.add(vertex)
       revAdj[vertex]?.forEach { n -> if (n !in visited) dfsOnReversed(n, visited, comp) }
   }
}
```

### Tarjan's Algorithm for SCC

```kotlin
class TarjanSCC<T> {
    private val graph = mutableMapOf<T, MutableList<T>>()
    fun addEdge(from: T, to: T) { graph.getOrPut(from) { mutableListOf() }.add(to) }
    
    fun findSCC(): List<List<T>> {
        val sccs = mutableListOf<List<T>>()
        val ids = mutableMapOf<T, Int>(); val low = mutableMapOf<T, Int>()
        val stack = ArrayDeque<T>(); val inStack = mutableSetOf<T>(); var id = 0
        fun dfs(n: T) { ids[n] = id; low[n] = id; id++; stack.addLast(n); inStack.add(n)
            graph[n]?.forEach { nei ->
                when { nei !in ids -> { dfs(nei); low[n] = minOf(low[n]!!, low[nei]!!) }
                       nei in inStack -> low[n] = minOf(low[n]!!, ids[nei]!!) } }
            if (low[n] == ids[n]) { val scc = mutableListOf<T>()
                var cur: T; do { cur = stack.removeLast(); inStack.remove(cur); scc.add(cur) } while (cur != n)
                sccs.add(scc) } }
        graph.keys.forEach { if (it !in ids) dfs(it) }
        return sccs
    }
}
```

### Bipartite Graph Check

```kotlin
fun isBipartite(graph: List<List<Int>>): Boolean {
    val colors = Array(graph.size) { 0 } // 0=uncolored, 1=red, -1=blue
    fun dfs(u: Int, c: Int): Boolean {
        colors[u] = c
        return !graph[u].any { v ->
            colors[v] == c || (colors[v] == 0 && !dfs(v, -c))
        }
    }
    return (graph.indices).none { colors[it] == 0 && !dfs(it, 1) }
}
```

### Maximum Path Quality

```kotlin
fun maximalPathQuality(values: IntArray, edges: Array<IntArray>, maxTime: Int): Int {
    val graph = Array(values.size) { mutableListOf<Pair<Int,Int>>() }
    for ((u,v,t) in edges) { graph[u].add(Pair(v,t)); graph[v].add(Pair(u,t)) }
    val visited = IntArray(values.size)); var maxQ = 0
    fun dfs(n: Int, t: Int, q: Int) { visited[n]++; val cq = if (visited[n] == 1) q+values[n] else q
        if (n == 0) maxQ = maxOf(maxQ, cq)
        for ((next, time) in graph[n]) if (t+time <= maxTime) dfs(next, t+time, cq)
        visited[n]-- }
    dfs(0, 0, 0); return maxQ
}
```

## Eulerian Path & Circuit

### Reconstruct Itinerary

```kotlin
fun findItinerary(tickets: List<List<String>>): List<String> {
    val graph = mutableMapOf<String, MutableList<String>>()
    for ((from, to) in tickets) graph.getOrPut(from) { mutableListOf() }.add(to)
    graph.values.forEach { it.sort() }
    val result = mutableListOf<String>()
    fun dfs(a: String) { val d = graph[a]; while (d != null && d.isNotEmpty()) dfs(d.removeFirst()); result.add(0, a) }
    dfs("JFK"); return result
}
```

### Cracking the Safe (De Bruijn)

```kotlin
fun crackSafe(n: Int, k: Int): String {
    val visited = mutableSetOf<String>(); val result = StringBuilder()
    fun dfs(n: String) { for (i in 0 until k) { val e = "$n$i"
            if (e !in visited) { visited.add(e); dfs(e.substring(1)); result.append(i) } } }
    dfs("0".repeat(n - 1)); result.append("0".repeat(n - 1))
    return result.toString()
}
```

## Sweep Line Algorithm - The Skyline Problem

```kotlin
fun getSkyline(buildings: Array<IntArray>): List<List<Int>> {
   val points = buildings.flatMap {
       listOf(Pair(it[0], -it[2]), Pair(it[1], it[2]))
   }.sortedWith(compareBy({ it.first }, { it.second }))
   val heightMap = TreeMap<Int, Int>(reverseOrder()).also { it[0] = 1 }
   val result = mutableListOf<List<Int>>(); var prevH = 0
   for ((x, h) in points) {
       if (h < 0) heightMap[-h] = (heightMap[-h] ?: 0) + 1
       else if (heightMap[h] == 1) heightMap.remove(h)
       else heightMap[h]?.dec()
       val curH = heightMap.firstKey()
       if (curH != prevH) { result.add(listOf(x, curH)); prevH = curH }
   }
   return result
}
```

## Combinatorics - Next Permutation (Narayan Pandita)

```kotlin
fun <T: Comparable<T>> MutableList<T>.nextPermutation(): Boolean {
    val pivot = (size - 2 downTo 0).firstOrNull { this[it] < this[it + 1] } ?: return false.also { reverse() }
    val swap = (size - 1 downTo pivot + 1).first { this[pivot] < this[it] }
    this[pivot] = this[swap].also { this[swap] = this[pivot] }
    subList(pivot + 1, size).reverse()
    return true
}
```

## String Matching - Count Subsequence Words

```kotlin
fun numMatchingSubseq(s: String, words: Array<String>): Int {
    val waiting = Array(26) { ArrayDeque<Pair<Int,Int>>() }
    words.forEachIndexed { i, w -> if (w.isNotEmpty()) waiting[w[0]-'a'].add(Pair(i, 0)) }
    var count = 0
    for (c in s) { val q = waiting[c-'a']; repeat(q.size) { val (wi, ci) = q.removeFirst()
            if (ci+1 == words[wi].length) count++ else waiting[words[wi][ci+1]-'a'].add(Pair(wi, ci+1)) } }
    return count
}
```

## Computational Geometry - Count Rectangles

```kotlin
fun countRectangles(points: Array<IntArray>): Int {
    val map = mutableMapOf<Int, MutableSet<Int>>()
    for ((x, y) in points) map.getOrPut(x) { mutableSetOf() }.add(y)
    val xs = map.keys.toList(); var count = 0
    for (i in xs.indices) for (j in i+1 until xs.size) {
        val common = map[xs[i]]!!.intersect(map[xs[j]]!!)
        if (common.size >= 2) count += common.size * (common.size - 1) / 2
    }
    return count
}
```

## Weighted Stream Sampling (Big Data)

```kotlin
class WeightedStreamSampler(private val reservoirSize: Int) {
    private val reservoir = mutableListOf<Pair<Double,Any>>()
    private var totalWeight = 0.0
    fun process(element: Any, weight: Double) {
        totalWeight += weight
        if (reservoir.size < reservoirSize) reservoir.add(Pair(weight, element))
        else if (Math.random() < weight / totalWeight)
            reservoir[Math.random().toInt() % reservoirSize] = Pair(weight, element)
    }
    fun getSample(): List<Any> = reservoir.map { it.second }
}
```

## Job Scheduling

### Max Non-Overlapping Intervals
```kotlin
fun maxNonOverlapping(intervals: Array<IntArray>): Int {
    intervals.sortBy { it[1] }; var count = 0; var lastEnd = Int.MIN_VALUE
    for ((s, e) in intervals) if (s >= lastEnd) { count++; lastEnd = e }
    return count
}
```

### Weighted Interval Scheduling (DP)
```kotlin
fun weightedIntervalScheduling(intervals: Array<IntArray>, weights: IntArray): Int {
    val n = intervals.size; val idx = (0 until n).sortedBy { intervals[it][1] }
    fun lastNonOverlap(i: Int): Int {
        var lo=0; var hi=i-1
        while (lo <= hi) { val m = lo+(hi-lo)/2
            if (intervals[idx[m]][1] <= intervals[idx[i]][0]) {
                if (m+1 <= hi && intervals[idx[m+1]][1] <= intervals[idx[i]][0]) lo=m+1 else return m
            } else hi=m-1 }
        return -1
    }
    val dp = IntArray(n); dp[0] = weights[idx[0]]
    for (i in 1 until n) {
        val include = weights[idx[i]] + (if (lastNonOverlap(i) != -1) dp[lastNonOverlap(i)] else 0)
        dp[i] = maxOf(dp[i-1], include)
    }
    return dp[n-1]
}
```

## Google Questions - Count Ways K Coins Sum Divisible by M

```kotlin
fun countWays(coins: IntArray, k: Int, m: Int): Int {
    val MOD = 1_000_000_007
    val dp = Array(k+1) { IntArray(m) }; dp[0][0] = 1
    for (coin in coins)
        for (c in k downTo 1)
            for (r in 0 until m)
                dp[c][r] = (dp[c][r] + dp[c-1][((r-coin)%m+m)%m]) % MOD
    return dp[k][0]
}
```

## 💎 The Elite Tier

### 1. Persistent Data Structures
- Persistent Segment Tree: Version-controlled range queries
- Persistent Trie: Historical prefix queries

### 2. Advanced Geometric Search
- Delaunay Triangulation: Nearest neighbor O(log n)
- Voronoi Diagrams: Proximity problems

### 3. String Structures
- Suffix Automaton: All substring ops O(n)
- Lyndon Factorization: String periodicity

### 4. Optimization
- Convex Hull Trick (CHT): DP optimization
- Lagrange Multipliers (Aliens Trick): Constrained DP
- Divide & Conquer DP: Decision monotonicity

### 5. Advanced DP
- Tree Partitioning: DP on tree decomposition
- DP with Bitmask: Hamiltonian paths, TSP
- DP with Convolution: Knapsack optimization

## Google-Specific Patterns (2025)

1. **Graph + DP combo** (small graph, DP fills the rest)
2. **Interval problems with coordinate compression**
3. **Binary Search on Answer + greedy check**
4. **Data structure design** (LRU/LFU, Hit Counter)
5. **System design integration** with sharding awareness

## The Fight Club Creed

> **"We don't complain about the game. We learn the rules. We master them. And we win."**

**Now go get that bag. 🥊💰**

---

[⬅️ Back to Home](../index.md)

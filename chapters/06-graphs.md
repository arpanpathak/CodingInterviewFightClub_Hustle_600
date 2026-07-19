---
layout: chapter
title: "Graphs"
chapter_number: 6
chapter_title: "Graphs"
toc: true
prev_chapter:
  url: "/chapters/05-trees.html"
  title: "Trees"
next_chapter:
  url: "/chapters/07-bit-manipulation.html"
  title: "Bit Manipulation"
---

# Graphs

> **17 problems**

## The Pattern

_Each problem below includes: Problem, Example, Why This Approach, Code, Pattern Insight, Complexity, and Variations._

## Problems

1. [Alien Dictionary](#aliendictionary)
2. [Alien Dictionary_BFS](#aliendictionary_bfs)
3. [Apply Substitutions](#applysubstitutions)
4. [Bus Routes](#busroutes)
5. [Cheapest Flights Within K Stops](#cheapestflightswithinkstops)
6. [Cheapest Flights With K Stops](#cheapestflightswithkstops)
7. [Node](#clonegraph)
8. [Course Schedule](#courseschedule)
9. [Course Schedule_II](#courseschedule_ii)
10. [Course Schedule_II_BFS](#courseschedule_ii_bfs)
11. [Critical Connections In A Network](#criticalconnectionsinanetwork)
12. [Critical Connections In A Network Short Code](#criticalconnectionsinanetworkshortcode)
13. [Find Redundent Connections](#findredundentconnections)
14. [Tree Node](#houserobber3)
15. [Parallel Courses](#parallelcourses)
16. [Reorder Routes To Make All Paths Lead To City Zero](#reorderroutestomakeallpathsleadtocityzero)
17. [Word Ladder](#wordladder)

---

## Alien Dictionary

### Problem

Given `words` (Array<String>), `node` (Char), compute the computed result efficiently.

**Example:**

```
Input: words = input_value, node = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses **graph traversal**. Choose BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, or topological sort for dependency ordering. Track visited nodes to prevent infinite loops.

### Code

```kotlin
package graph.topological_sort

class AlienDictionary {
    enum class State {
        NOT_VISITED, VISITING, VISITED
    }

    /**
    * Solves the Alien Dictionary problem.
    * Takes `words` (Array<String>).
    *
    * @param words The input Array<String>.
    * @return The resulting string.
    */
    /**
    * Solves the Alien Dictionary problem.
    * Takes `words` (Array<String>).
    *
    * @param words The input Array<String>.
    * @return The resulting string.
    */
    /**
    * Solves the Alien Dictionary problem.
    * Takes `words` (Array<String>).
    *
    * @param words The input Array<String>.
    * @return The resulting string.
    */
    /**
    * Solves the Alien Dictionary problem.
    * Takes `words` (Array<String>).
    *
    * @param words The input Array<String>.
    * @return The resulting string.
    */
    fun alienOrder(words: Array<String>): String {
        val graph = mutableMapOf<Char, MutableSet<Char>>()
        val visited = mutableMapOf<Char, State>()  // 0 = visiting, 1 = visited, -1 = not visited
        val result = StringBuilder()

        // Step 1: Build the graph and visited map
        words.forEach { word ->
            word.forEach { char ->
                graph.putIfAbsent(char, mutableSetOf())
                visited.putIfAbsent(char, State.NOT_VISITED)
            }
        }

        // Step 2: Build edges between characters
        for (i in 1 until words.size) {
            val (word1, word2) = words[i - 1] to words[i]

            // Check if the second word is a prefix of the first
            if (word1.startsWith(word2) && word1.length > word2.length) {
                return ""  // Invalid case, prefix conflict
            }

            for (j in 0 until minOf(word1.length, word2.length)) {
                if (word1[j] != word2[j]) {
                    graph[word1[j]]?.add(word2[j])
                    break
                }
            }
        }

        // Step 3: Perform DFS to find topological sort
        /**
        * Solves the Alien Dictionary problem.
        * Takes `node` (character).
        *
        * @param node The character.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Alien Dictionary problem.
        * Takes `node` (character).
        *
        * @param node The character.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Alien Dictionary problem.
        * Takes `node` (character).
        *
        * @param node The character.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Alien Dictionary problem.
        * Takes `node` (character).
        *
        * @param node The character.
        * @return `true` if the condition is met, `false` otherwise.
        */
        fun dfs(node: Char): Boolean {
            if (visited[node] == State.VISITING) return false  // Cycle detected
            if (visited[node] == State.VISITED) return true  // Already visited

            visited[node] = State.VISITING  // Mark as visiting
            graph[node]?.forEach { if (!dfs(it)) return false }

            visited[node] = State.VISITED  // Mark as visited
            result.append(node) // Add to result in topological order
            return true
        }

        // Step 4: Process all nodes (characters)
        for (char in visited.keys) {
            if (visited[char] == State.NOT_VISITED && !dfs(char)) {
                return ""  // Cycle detected
            }
        }

        return result.reverse().toString() // Reverse to get the correct order
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations

1. What if the graph is disconnected (multiple components)?
1. What if edges have weights — does BFS still work?
1. What if you need the actual path, not just distance/existence?
1. DFS vs BFS — which is better and why?
1. What if the graph is too large to fit in memory?

---

## Alien Dictionary_BFS

### Problem

Given `words` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: words = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses **graph traversal**. Choose BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, or topological sort for dependency ordering. Track visited nodes to prevent infinite loops.

### Code

```kotlin
package graph.topological_sort

class AlienDictionary_BFS {
    /**
    * Solves the Alien Dictionary_BFS problem.
    * Takes `words` (Array<String>).
    *
    * @param words The input Array<String>.
    * @return The resulting string.
    */
    /**
    * Solves the Alien Dictionary_BFS problem.
    * Takes `words` (Array<String>).
    *
    * @param words The input Array<String>.
    * @return The resulting string.
    */
    /**
    * Solves the Alien Dictionary_BFS problem.
    * Takes `words` (Array<String>).
    *
    * @param words The input Array<String>.
    * @return The resulting string.
    */
    /**
    * Solves the Alien Dictionary_BFS problem.
    * Takes `words` (Array<String>).
    *
    * @param words The input Array<String>.
    * @return The resulting string.
    */
    fun alienOrder(words: Array<String>): String {
        val graph = mutableMapOf<Char, HashSet<Char>>()
        val inDegree = mutableMapOf<Char, Int>()
        words.forEach { word ->
            word.forEach { char ->
                inDegree.putIfAbsent(char, 0)
                graph.putIfAbsent(char, hashSetOf())
            }
        }

        for (i in 0 until words.size - 1) {
            val currentWord = words[i]
            val nextWord = words[i + 1]
            val minLength = minOf(currentWord.length, nextWord.length)
            for (j in 0 until minLength) {
                val currentChar = currentWord[j]
                val nextChar = nextWord[j]
                if (currentChar != nextChar) {
                    if (graph[currentChar]!!.add(nextChar)) {
                        inDegree[nextChar] = inDegree[nextChar]!! + 1
                    }
                    break
                }
                // Handle invalid case (e.g., "abc" before "ab")
                if (j == minLength - 1 && currentWord.length > nextWord.length) return ""
            }
        }

        val queue = ArrayDeque<Char>().apply { addAll(inDegree.filter { it.value == 0 }.keys) }
        val result = StringBuilder()
        while (queue.isNotEmpty()) {
            val char = queue.removeFirst()
            result.append(char)
            graph[char]?.forEach { neighbor ->
                inDegree[neighbor] = inDegree[neighbor]!! - 1
                if (inDegree[neighbor] == 0) queue.add(neighbor)
            }
        }

        return if (result.length == inDegree.size) result.toString() else ""
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations

1. What if the graph is disconnected (multiple components)?
1. What if edges have weights — does BFS still work?
1. What if you need the actual path, not just distance/existence?
1. DFS vs BFS — which is better and why?
1. What if the graph is too large to fit in memory?

---

## Apply Substitutions

### Problem

Given `replacements` (List<List<String>>), `text` (string), `s` (string), compute the computed result efficiently.

**Example:**

```
Input: replacements = input_value, text = "example", s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **tree traversal/recursion**. Trees are naturally recursive — each subtree is itself a tree. The key is choosing the right traversal order (preorder, inorder, postorder, level-order) for the specific problem.

### Code

```kotlin
package string

class ApplySubstitutions {
    /**
    * Solves the Apply Substitutions problem.
    * Takes `replacements` (List<List<String>>), `text` (string).
    *
    * @param replacements The input List<List<String>>.
    * @param text The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Apply Substitutions problem.
    * Takes `replacements` (List<List<String>>), `text` (string).
    *
    * @param replacements The input List<List<String>>.
    * @param text The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Apply Substitutions problem.
    * Takes `replacements` (List<List<String>>), `text` (string).
    *
    * @param replacements The input List<List<String>>.
    * @param text The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Apply Substitutions problem.
    * Takes `replacements` (List<List<String>>), `text` (string).
    *
    * @param replacements The input List<List<String>>.
    * @param text The input string.
    * @return The resulting string.
    */
    fun applySubstitutions(replacements: List<List<String>>, text: String): String {
        val map = mutableMapOf<String, String>()

        for ((key, value) in replacements) {
            map[key] = value
        }

        /**
        * Solves the Apply Substitutions problem.
        * Takes `s` (string).
        *
        * @param s The input string.
        * @return The resulting string.
        */
        /**
        * Solves the Apply Substitutions problem.
        * Takes `s` (string).
        *
        * @param s The input string.
        * @return The resulting string.
        */
        /**
        * Solves the Apply Substitutions problem.
        * Takes `s` (string).
        *
        * @param s The input string.
        * @return The resulting string.
        */
        /**
        * Solves the Apply Substitutions problem.
        * Takes `s` (string).
        *
        * @param s The input string.
        * @return The resulting string.
        */
        fun resolve(s: String): String {
            val sb = StringBuilder()
            var i = 0

            while (i < s.length) {
                if (i + 2 < s.length && s[i] == '%' && s[i + 2] == '%') {
                    val key = s[i + 1].toString()
                    sb.append(map[key] ?: "%$key%")  // Replace if found, else keep original
                    i += 3  // Move past the placeholder
                } else {
                    sb.append(s[i])
                    i++
                }
            }

            val result = sb.toString()
            return if (result == s) result else resolve(result)  // Continue resolving if changed
        }

        return resolve(text)
    }
}
```

### Pattern Insight

**Tree Pattern.** Choose traversal based on need: inorder (sorted for BST), preorder (copy/construct), postorder (bottom-up compute), level-order (BFS). Recursion uses O(h) stack space; iteration uses O(1) with Morris traversal.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

### Variations

1. What if the tree is skewed (worst case — becomes a linked list)?
1. Can you solve this iteratively instead of recursively?
1. What if the tree is an N-ary tree instead of binary?
1. What if O(1) extra space is required (Morris traversal)?
1. Can this be parallelized for different subtrees?

---

## Bus Routes

### Problem

Given `routes` (2D matrix), `source` (integer), `target` (integer), compute the computed result efficiently.

**Example:**

```
Input: routes = [1, 2, 3, 4, 5], source = 5, target = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package graph

import java.util.*

import java.util.*

class BusRoutes {
    data class Node(val stop: Int, val busCount: Int)

    /**
    * Solves the Bus Routes problem.
    * Takes `routes` (2D matrix of integers), `source` (integer), `target` (integer).
    *
    * @param routes The input 2D matrix of integers.
    * @param source The integer parameter representing source.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Bus Routes problem.
    * Takes `routes` (2D matrix of integers), `source` (integer), `target` (integer).
    *
    * @param routes The input 2D matrix of integers.
    * @param source The integer parameter representing source.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Bus Routes problem.
    * Takes `routes` (2D matrix of integers), `source` (integer), `target` (integer).
    *
    * @param routes The input 2D matrix of integers.
    * @param source The integer parameter representing source.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Bus Routes problem.
    * Takes `routes` (2D matrix of integers), `source` (integer), `target` (integer).
    *
    * @param routes The input 2D matrix of integers.
    * @param source The integer parameter representing source.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    fun numBusesToDestination(routes: Array<IntArray>, source: Int, target: Int): Int {
        if (source == target) return 0

        val graph = mutableMapOf<Int, MutableList<Int>>() // Stop -> List of buses passing through

        // Build the graph
        for (bus in routes.indices) {
            for (stop in routes[bus]) {
                graph.getOrPut(stop) { mutableListOf() }.add(bus)
            }
        }

        val queue: Queue<Node> = LinkedList()
        val visitedBuses = mutableSetOf<Int>()
        val visitedStops = mutableSetOf<Int>()

        queue.offer(Node(source, 0))
        visitedStops.add(source)

        while (queue.isNotEmpty()) {
            val (currentStop, busCount) = queue.poll()

            if (currentStop == target) return busCount

            // Explore all buses passing through the current stop
            graph[currentStop]?.let { buses ->
                for (bus in buses) {
                    if (bus !in visitedBuses) {
                        visitedBuses.add(bus)

                        for (stop in routes[bus]) {
                            if (stop !in visitedStops) {
                                queue.offer(Node(stop, busCount + 1))
                                visitedStops.add(stop)
                            }
                        }
                    }
                }
            }
        }
        return -1
    }
}

// (1) =>
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Cheapest Flights Within K Stops

### Problem

Given `n` (integer), `flights` (2D matrix), `src` (integer), `dst` (integer), `k` (integer), `graph` (MutableMap<Int), `dest` (integer), `args` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: n = 5, flights = [1, 2, 3, 4, 5], src = 5, dst = 5, k = 5, graph = input_value, dest = 5, args = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses a **heap/priority queue** to maintain a dynamic ordering of elements. Heaps provide O(log n) insertion and O(1) access to the min or max element, making them ideal for streaming/online algorithms and k-th order statistics.

### Code

```kotlin
package graph.dp

import java.util.*

class CheapestFlightsWithinKStops {
    // Define the Node class to encapsulate flight details
    data class Node(var dest: Int, var price: Int)

    // Graph map where each integer key maps to a list of Node objects
    private var graph = mutableMapOf<Int, MutableList<Node>>()

    // Solving using Bellman Ford
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `n` (integer), `flights` (2D matrix of integers), `src` (integer), `dst` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param flights The input 2D matrix of integers.
    * @param src The integer parameter representing src.
    * @param dst The integer parameter representing dst.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `n` (integer), `flights` (2D matrix of integers), `src` (integer), `dst` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param flights The input 2D matrix of integers.
    * @param src The integer parameter representing src.
    * @param dst The integer parameter representing dst.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `n` (integer), `flights` (2D matrix of integers), `src` (integer), `dst` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param flights The input 2D matrix of integers.
    * @param src The integer parameter representing src.
    * @param dst The integer parameter representing dst.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `n` (integer), `flights` (2D matrix of integers), `src` (integer), `dst` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param flights The input 2D matrix of integers.
    * @param src The integer parameter representing src.
    * @param dst The integer parameter representing dst.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    fun findCheapestPrice(n: Int, flights: Array<IntArray>, src: Int, dst: Int, k: Int): Int {
        // Build the graph from the input flights
        flights.forEach { flight ->
            val from = flight[0]
            val to = flight[1]
            val cost = flight[2]
            // Append the destination and cost to the list of nodes for the source
            graph.computeIfAbsent(from) { mutableListOf() }.add(Node(to, cost))
        }

        // DP table for storing minimum cost to each node with up to i flights
        val dp = Array(k + 2) { IntArray(n) { Int.MAX_VALUE } }
        dp[0][src] = 0  // Cost to reach source from itself is 0

        // Perform relaxation for each possible number of stops
        for (i in 1..k + 1) {
            dp[i][src] = 0  // No cost to stay at the source
            graph.forEach { (from, neighbors) ->
                neighbors.forEach { node ->
                    if (dp[i - 1][from] != Int.MAX_VALUE) { // Ensure the source node is reachable
                        dp[i][node.dest] = minOf(dp[i][node.dest], dp[i - 1][from] + node.price)
                    }
                }
            }
        }

        // Find the minimum cost to the destination node considering all possible stops
        val cheapest = (0..k + 1).minOfOrNull { dp[it][dst] } ?: Int.MAX_VALUE
        return if (cheapest == Int.MAX_VALUE) -1 else cheapest
    }

    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `n` (integer), `flights` (2D matrix of integers), `src` (integer), `dst` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param flights The input 2D matrix of integers.
    * @param src The integer parameter representing src.
    * @param dst The integer parameter representing dst.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `n` (integer), `flights` (2D matrix of integers), `src` (integer), `dst` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param flights The input 2D matrix of integers.
    * @param src The integer parameter representing src.
    * @param dst The integer parameter representing dst.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `n` (integer), `flights` (2D matrix of integers), `src` (integer), `dst` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param flights The input 2D matrix of integers.
    * @param src The integer parameter representing src.
    * @param dst The integer parameter representing dst.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `n` (integer), `flights` (2D matrix of integers), `src` (integer), `dst` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param flights The input 2D matrix of integers.
    * @param src The integer parameter representing src.
    * @param dst The integer parameter representing dst.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    fun findCheapestPriceBfs(n: Int, flights: Array<IntArray>, src: Int, dst: Int, k: Int): Int {
        // Build the graph from the input flights
        flights.forEach { flight ->
            val from = flight[0]
            val to = flight[1]
            val cost = flight[2]
            // Append the destination and cost to the list of nodes for the source
            graph.computeIfAbsent(from) { mutableListOf() }.add(Node(to, cost))
        }

        val cost = bfs(src, dst, n, k)

        return if (cost[dst] == Int.MAX_VALUE) -1 else cost[dst]
    }


    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `graph` (MutableMap<Int), `src` (integer).
    *
    * @param graph The input MutableMap<Int.
    * @param src The integer parameter representing src.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `graph` (MutableMap<Int), `src` (integer).
    *
    * @param graph The input MutableMap<Int.
    * @param src The integer parameter representing src.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `graph` (MutableMap<Int), `src` (integer).
    *
    * @param graph The input MutableMap<Int.
    * @param src The integer parameter representing src.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `graph` (MutableMap<Int), `src` (integer).
    *
    * @param graph The input MutableMap<Int.
    * @param src The integer parameter representing src.
    * @return The computed integer result.
    */
    fun dijkstra(graph: MutableMap<Int, MutableList<Node>>, src: Int): Map<Int, Int> {
        val dist = mutableMapOf<Int, Int>().apply {
            graph.keys.forEach { this[it] = Int.MAX_VALUE }
        }
        dist[src] = 0

        // Define priority queue with a comparator provided inline
        val priorityQueue = PriorityQueue<Node>(compareBy { it.price })
        priorityQueue.add(Node(src, 0))

        while (priorityQueue.isNotEmpty()) {
            val current = priorityQueue.poll()

            // If current node's distance in queue is greater than known shortest distance, skip it
            if (current.price > dist[current.dest]!!) continue

            graph[current.dest]?.forEach { neighbor ->
                val newDistance = current.price + neighbor.price
                if (newDistance < dist[neighbor.dest]!!) {
                    dist[neighbor.dest] = newDistance
                    priorityQueue.add(Node(neighbor.dest, newDistance))
                }
            }
        }

        return dist
    }

    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `src` (integer), `dest` (integer), `n` (integer), `k` (integer).
    *
    * @param src The integer parameter representing src.
    * @param dest The integer parameter representing dest.
    * @param n The integer parameter representing n.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `src` (integer), `dest` (integer), `n` (integer), `k` (integer).
    *
    * @param src The integer parameter representing src.
    * @param dest The integer parameter representing dest.
    * @param n The integer parameter representing n.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `src` (integer), `dest` (integer), `n` (integer), `k` (integer).
    *
    * @param src The integer parameter representing src.
    * @param dest The integer parameter representing dest.
    * @param n The integer parameter representing n.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `src` (integer), `dest` (integer), `n` (integer), `k` (integer).
    *
    * @param src The integer parameter representing src.
    * @param dest The integer parameter representing dest.
    * @param n The integer parameter representing n.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    fun bfs(src: Int, dest: Int, n: Int, k: Int ): IntArray {
        // To track the minimum cost to reach each destination
        val minCost = IntArray(n) { Int.MAX_VALUE }
        minCost[src] = 0

        // Using a queue for BFS; store the current node, the cost to reach it, and the number of stops made
        val queue: Queue<Triple<Int, Int, Int>> = LinkedList()
        queue.add(Triple(src, 0, 0))

        while (queue.isNotEmpty()) {
            val (current, cost, stops) = queue.poll()

            // Explore each neighbor
            if (stops > k) continue  // Do not explore further if stops exceed k

            graph[current]?.forEach { neighbor ->
                val newCost = cost + neighbor.price
                // Check if this path is better
                if (newCost < minCost[neighbor.dest]) {
                    queue.add(Triple(neighbor.dest, newCost, stops + 1))
                    minCost[neighbor.dest] = newCost
                }
            }
        }

        return minCost
    }

    // Solve using Dijkstra
    data class State(val node: Int, val cost: Int, val stops: Int)

    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `graph` (MutableMap<Int), `src` (integer), `k` (integer).
    *
    * @param graph The input MutableMap<Int.
    * @param src The integer parameter representing src.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `graph` (MutableMap<Int), `src` (integer), `k` (integer).
    *
    * @param graph The input MutableMap<Int.
    * @param src The integer parameter representing src.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `graph` (MutableMap<Int), `src` (integer), `k` (integer).
    *
    * @param graph The input MutableMap<Int.
    * @param src The integer parameter representing src.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights Within KStops problem.
    * Takes `graph` (MutableMap<Int), `src` (integer), `k` (integer).
    *
    * @param graph The input MutableMap<Int.
    * @param src The integer parameter representing src.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    fun dijkstraWithMaxKStops(graph: MutableMap<Int, MutableList<Node>>, src: Int, k: Int): Map<Int, Int> {
        val pq = PriorityQueue<State>(compareBy { it.cost })
        pq.offer(State(src, 0, 0))

        val minCostAtStops = mutableMapOf<Int, IntArray>().apply {
            graph.keys.forEach { this[it] = IntArray(k + 1) { Int.MAX_VALUE } }
        }
        minCostAtStops[src] = IntArray(k + 1) { 0 }

        while (pq.isNotEmpty()) {
            val (node, cost, stops) = pq.poll()

            if (stops > k) continue

            graph[node]?.forEach { neighbor ->
                val nextCost = cost + neighbor.price
                if (stops < k && nextCost < minCostAtStops.getOrDefault(neighbor.dest, IntArray(k + 1) { Int.MAX_VALUE })[stops + 1]) {
                    minCostAtStops[neighbor.dest]?.set(stops + 1, nextCost)
                    pq.offer(State(neighbor.dest, nextCost, stops + 1))
                }
            }
        }

        return minCostAtStops.mapValues { (_, costs) -> costs.filter { it != Int.MAX_VALUE }.minOrNull() ?: Int.MAX_VALUE }
    }

    companion object {
        @JvmStatic
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        fun main(args: Array<String>) {

        }
    }
}
```

### Pattern Insight

**Heap Pattern.** Use a min-heap to keep the k largest elements, max-heap for k smallest. Dual heaps (min + max) track median in O(1) with O(log n) insert. Each heap operation is O(log k).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

### Variations

1. What if you need the k-th smallest instead of largest?
1. What if elements are added/removed dynamically over time?
1. Sorting vs heap — compare O(n log n) vs O(n log k) tradeoffs.
1. What if k is very large (close to n) — different approach needed?
1. How to handle ties in priority ordering?

---

## Cheapest Flights With K Stops

### Problem

Given `n` (integer), `flights` (2D matrix), `src` (integer), `dst` (integer), `k` (integer), compute the computed result efficiently.

**Example:**

```
Input: n = 5, flights = [1, 2, 3, 4, 5], src = 5, dst = 5, k = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses a **heap/priority queue** to maintain a dynamic ordering of elements. Heaps provide O(log n) insertion and O(1) access to the min or max element, making them ideal for streaming/online algorithms and k-th order statistics.

### Code

```kotlin
package graph.greedy

import java.util.*

class CheapestFlightsWithKStops {
    // Define the Node class to encapsulate flight details
    data class Node(val dest: Int, val cost: Int)

    // Define the State class for priority queue elements
    data class State(val node: Int, val cost: Int, val stops: Int)

    /**
    * Solves the Cheapest Flights With KStops problem.
    * Takes `n` (integer), `flights` (2D matrix of integers), `src` (integer), `dst` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param flights The input 2D matrix of integers.
    * @param src The integer parameter representing src.
    * @param dst The integer parameter representing dst.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights With KStops problem.
    * Takes `n` (integer), `flights` (2D matrix of integers), `src` (integer), `dst` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param flights The input 2D matrix of integers.
    * @param src The integer parameter representing src.
    * @param dst The integer parameter representing dst.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights With KStops problem.
    * Takes `n` (integer), `flights` (2D matrix of integers), `src` (integer), `dst` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param flights The input 2D matrix of integers.
    * @param src The integer parameter representing src.
    * @param dst The integer parameter representing dst.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Cheapest Flights With KStops problem.
    * Takes `n` (integer), `flights` (2D matrix of integers), `src` (integer), `dst` (integer), `k` (integer).
    *
    * @param n The integer parameter representing n.
    * @param flights The input 2D matrix of integers.
    * @param src The integer parameter representing src.
    * @param dst The integer parameter representing dst.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    fun findCheapestPrice(n: Int, flights: Array<IntArray>, src: Int, dst: Int, k: Int): Int {
        // Build the graph from the input flights
        val graph = mutableMapOf<Int, MutableList<Node>>()
        flights.forEach { flight ->
            val from = flight[0]
            val to = flight[1]
            val cost = flight[2]
            graph.getOrPut(from) { mutableListOf() }.add(Node(to, cost))
        }

        // E + EK log

        // Initialize the priority queue and cost tracking
        val minStops = Array(n) { Int.MAX_VALUE }
        val pq = PriorityQueue<State>(compareBy { it.cost })
        pq.offer(State(0, src, 0))
        minStops[src] = 0

        while (pq.isNotEmpty()) {
            val (node, currentCost, stops) = pq.poll()

            // Skip if the number of stops exceeds the limit or if the path is not optimal
            if (stops > k + 1 || currentCost > minStops[node]) continue

            minStops[node] = currentCost
            // Return the cost if the destination is reached
            if (node == dst) return currentCost

            // Explore neighbors
            graph[node]?.forEach { neighbor ->
                    pq.offer(State(neighbor.dest, currentCost + neighbor.cost, stops + 1))
            }
        }

        // If no path was found within the constraints
        return -1
    }
}
```

### Pattern Insight

**Heap Pattern.** Use a min-heap to keep the k largest elements, max-heap for k smallest. Dual heaps (min + max) track median in O(1) with O(log n) insert. Each heap operation is O(log k).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

### Variations

1. What if you need the k-th smallest instead of largest?
1. What if elements are added/removed dynamically over time?
1. Sorting vs heap — compare O(n log n) vs O(n log k) tradeoffs.
1. What if k is very large (close to n) — different approach needed?
1. How to handle ties in priority ordering?

---

## Node

### Problem

Given `node` (Node?), compute the computed result efficiently.

**Example:**

```
Input: node = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses **graph traversal**. Choose BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, or topological sort for dependency ordering. Track visited nodes to prevent infinite loops.

### Code

```kotlin
package graph

data class Node(val `val`: Int, val neighbors: MutableList<Node?> = mutableListOf())

class CloneGraph {
    val map = mutableMapOf<Node, Node>()

    /**
    * Solves the Node problem.
    * Takes `node` (Node?).
    *
    * @param node The Node? (nullable).
    * @return The result, or `null` if not found.
    */
    /**
    * Solves the Node problem.
    * Takes `node` (Node?).
    *
    * @param node The Node? (nullable).
    * @return The result, or `null` if not found.
    */
    /**
    * Solves the Node problem.
    * Takes `node` (Node?).
    *
    * @param node The Node? (nullable).
    * @return The result, or `null` if not found.
    */
    /**
    * Solves the Node problem.
    * Takes `node` (Node?).
    *
    * @param node The Node? (nullable).
    * @return The result, or `null` if not found.
    */
    fun cloneGraph(node: Node?): Node? {

        if (node == null) return null
        map[node]?.let { return it }

        val clonedNode = Node(node?.`val`!!)
        map[node] = clonedNode

        node.neighbors.forEach{ clonedNode.neighbors.add(cloneGraph(it)) }

        return clonedNode
    }
}
```

### Pattern Insight

**Graph Pattern.** BFS = queue, shortest path. DFS = stack/recursion, connectivity. Topological sort = in-degree counting + queue. Union-Find = dynamic connectivity.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations

1. What if the graph is disconnected (multiple components)?
1. What if edges have weights — does BFS still work?
1. What if you need the actual path, not just distance/existence?
1. DFS vs BFS — which is better and why?
1. What if the graph is too large to fit in memory?

---

## Course Schedule

### Problem

Given `numCourses` (integer), `node` (integer), `prerequisites` (2D matrix), compute the computed result efficiently.

**Example:**

```
Input: numCourses = 5, node = 5, prerequisites = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem uses **graph traversal**. Choose BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, or topological sort for dependency ordering. Track visited nodes to prevent infinite loops.

### Code

```kotlin
package graph.cycle

class CourseSchedule {
    private var graph: MutableMap<Int, MutableList<Int>> = mutableMapOf()
    private lateinit var status: Array<NodeStatus>
    private enum class NodeStatus { UNVISITED, EXPLORING, DONE }

    /**
    * Helper: has cycle.
    *
    * @param numCourses The integer parameter representing numCourses.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: has cycle.
    *
    * @param numCourses The integer parameter representing numCourses.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: has cycle.
    *
    * @param numCourses The integer parameter representing numCourses.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: has cycle.
    *
    * @param numCourses The integer parameter representing numCourses.
    * @return `true` if the condition is met, `false` otherwise.
    */
    private fun hasCycle(numCourses: Int): Boolean {
        // Define dfs function inside hasCycle to limit its scope
        /**
        * Solves the Course Schedule problem.
        * Takes `node` (integer).
        *
        * @param node The integer parameter representing node.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Course Schedule problem.
        * Takes `node` (integer).
        *
        * @param node The integer parameter representing node.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Course Schedule problem.
        * Takes `node` (integer).
        *
        * @param node The integer parameter representing node.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Course Schedule problem.
        * Takes `node` (integer).
        *
        * @param node The integer parameter representing node.
        * @return `true` if the condition is met, `false` otherwise.
        */
        fun dfs(node: Int): Boolean = when (status[node]) {
            NodeStatus.EXPLORING -> true
            NodeStatus.DONE -> false
            NodeStatus.UNVISITED -> {
                status[node] = NodeStatus.EXPLORING
                graph[node]?.forEach {
                    if (dfs(it)) return true
                }
                status[node] = NodeStatus.DONE
                false
            }
        }

        for (i in 0 until numCourses) {
            if (status[i] == NodeStatus.UNVISITED && dfs(i)) {
                return true
            }
        }
        return false
    }

    /**
    * Solves the Course Schedule problem.
    * Takes `numCourses` (integer), `prerequisites` (2D matrix of integers).
    *
    * @param numCourses The integer parameter representing numCourses.
    * @param prerequisites The input 2D matrix of integers.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Course Schedule problem.
    * Takes `numCourses` (integer), `prerequisites` (2D matrix of integers).
    *
    * @param numCourses The integer parameter representing numCourses.
    * @param prerequisites The input 2D matrix of integers.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Course Schedule problem.
    * Takes `numCourses` (integer), `prerequisites` (2D matrix of integers).
    *
    * @param numCourses The integer parameter representing numCourses.
    * @param prerequisites The input 2D matrix of integers.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Course Schedule problem.
    * Takes `numCourses` (integer), `prerequisites` (2D matrix of integers).
    *
    * @param numCourses The integer parameter representing numCourses.
    * @param prerequisites The input 2D matrix of integers.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        // Reset graph for each invocation to handle multiple calls
        graph = mutableMapOf()
        prerequisites.forEach { (course, prereq) ->
            graph.getOrPut(prereq) { mutableListOf() }.add(course)
        }

        status = Array(numCourses) { NodeStatus.UNVISITED }

        return !hasCycle(numCourses)
    }
}
```

### Pattern Insight

**Graph Pattern.** BFS = queue, shortest path. DFS = stack/recursion, connectivity. Topological sort = in-degree counting + queue. Union-Find = dynamic connectivity.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations

1. What if the graph is disconnected (multiple components)?
1. What if edges have weights — does BFS still work?
1. What if you need the actual path, not just distance/existence?
1. DFS vs BFS — which is better and why?
1. What if the graph is too large to fit in memory?

---

## Course Schedule_II

### Problem

Given `numCourses` (integer), `prerequisites` (2D matrix), `node` (integer), compute the computed result efficiently.

**Example:**

```
Input: numCourses = 5, prerequisites = [1, 2, 3, 4, 5], node = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **graph traversal**. Choose BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, or topological sort for dependency ordering. Track visited nodes to prevent infinite loops.

### Code

```kotlin
package graph.topological_sort

class CourseSchedule_II {
    private var graph: MutableMap<Int, MutableList<Int>> = mutableMapOf()
    private lateinit var status: Array<NodeStatus>
    private lateinit var result: IntArray
    private var index: Int = 0

    private enum class NodeStatus { UNVISITED, EXPLORING, DONE }

    /**
    * Solves the Course Schedule_II problem.
    * Takes `numCourses` (integer), `prerequisites` (2D matrix of integers).
    *
    * @param numCourses The integer parameter representing numCourses.
    * @param prerequisites The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Course Schedule_II problem.
    * Takes `numCourses` (integer), `prerequisites` (2D matrix of integers).
    *
    * @param numCourses The integer parameter representing numCourses.
    * @param prerequisites The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Course Schedule_II problem.
    * Takes `numCourses` (integer), `prerequisites` (2D matrix of integers).
    *
    * @param numCourses The integer parameter representing numCourses.
    * @param prerequisites The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Course Schedule_II problem.
    * Takes `numCourses` (integer), `prerequisites` (2D matrix of integers).
    *
    * @param numCourses The integer parameter representing numCourses.
    * @param prerequisites The input 2D matrix of integers.
    * @return The computed integer result.
    */
    fun findOrder(numCourses: Int, prerequisites: Array<IntArray>): IntArray {
        // Initialize graph, status, and result array
        status = Array(numCourses) { NodeStatus.UNVISITED }
        result = IntArray(numCourses)
        index = numCourses - 1

        // Build the graph
        prerequisites.forEach { (course, prereq) ->
            graph.getOrPut(prereq) { mutableListOf() }.add(course)
        }

        // Attempt to find a topological order
        if (hasCycle(numCourses)) {
            return intArrayOf()
        }

        return result
    }

    /**
    * Helper: has cycle.
    *
    * @param numCourses The integer parameter representing numCourses.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: has cycle.
    *
    * @param numCourses The integer parameter representing numCourses.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: has cycle.
    *
    * @param numCourses The integer parameter representing numCourses.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: has cycle.
    *
    * @param numCourses The integer parameter representing numCourses.
    * @return `true` if the condition is met, `false` otherwise.
    */
    private fun hasCycle(numCourses: Int): Boolean {
        // Nested DFS function for checking cycles and building the result
        /**
        * Solves the Course Schedule_II problem.
        * Takes `node` (integer).
        *
        * @param node The integer parameter representing node.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Course Schedule_II problem.
        * Takes `node` (integer).
        *
        * @param node The integer parameter representing node.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Course Schedule_II problem.
        * Takes `node` (integer).
        *
        * @param node The integer parameter representing node.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Course Schedule_II problem.
        * Takes `node` (integer).
        *
        * @param node The integer parameter representing node.
        * @return `true` if the condition is met, `false` otherwise.
        */
        fun dfs(node: Int): Boolean {
            when (status[node]) {
                // If an already visited node re-appears then it means we looped back to an exploring node
                NodeStatus.EXPLORING -> return true
                // If an already done node re-appears it doesn't mean cycle rather it means
                // we fully explored the node previously and found no cycle in the path.
                NodeStatus.DONE -> return false
                else -> {
                    status[node] = NodeStatus.EXPLORING
                    graph[node]?.forEach { neighbor ->
                        if (dfs(neighbor)) return true
                    }

                    status[node] = NodeStatus.DONE
                    result[index--] = node
                    return false
                }
            }
        }

        for (i in 0 until numCourses) {
            if (status[i] == NodeStatus.UNVISITED) {
                if (dfs(i)) {
                    return true
                }
            }
        }
        return false
    }
}
```

### Pattern Insight

**Graph Pattern.** BFS = queue, shortest path. DFS = stack/recursion, connectivity. Topological sort = in-degree counting + queue. Union-Find = dynamic connectivity.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations

1. What if the graph is disconnected (multiple components)?
1. What if edges have weights — does BFS still work?
1. What if you need the actual path, not just distance/existence?
1. DFS vs BFS — which is better and why?
1. What if the graph is too large to fit in memory?

---

## Course Schedule_II_BFS

### Problem

Given `numCourses` (integer), `prerequisites` (2D matrix), compute the computed result efficiently.

**Example:**

```
Input: numCourses = 5, prerequisites = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem uses **graph traversal**. Choose BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, or topological sort for dependency ordering. Track visited nodes to prevent infinite loops.

### Code

```kotlin
package graph.topological_sort

class CourseSchedule_II_BFS {
    /**
    * Solves the Course Schedule_II_BFS problem.
    * Takes `numCourses` (integer), `prerequisites` (2D matrix of integers).
    *
    * @param numCourses The integer parameter representing numCourses.
    * @param prerequisites The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Course Schedule_II_BFS problem.
    * Takes `numCourses` (integer), `prerequisites` (2D matrix of integers).
    *
    * @param numCourses The integer parameter representing numCourses.
    * @param prerequisites The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Course Schedule_II_BFS problem.
    * Takes `numCourses` (integer), `prerequisites` (2D matrix of integers).
    *
    * @param numCourses The integer parameter representing numCourses.
    * @param prerequisites The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Course Schedule_II_BFS problem.
    * Takes `numCourses` (integer), `prerequisites` (2D matrix of integers).
    *
    * @param numCourses The integer parameter representing numCourses.
    * @param prerequisites The input 2D matrix of integers.
    * @return The computed integer result.
    */
    fun findOrder(numCourses: Int, prerequisites: Array<IntArray>): IntArray {
        val graph = Array<MutableList<Int>>(numCourses) { mutableListOf() }
        val inDegree = IntArray(numCourses)
        val result = mutableListOf<Int>()

        // Build the graph and calculate in-degrees
        prerequisites.forEach { (course, preReq) ->
            graph[preReq].add(course)
            inDegree[course]++
        }

        // Initialize queue with courses having no prerequisites
        val queue = ArrayDeque<Int>().apply { inDegree.indices.filter { inDegree[it] == 0 }.forEach { add(it) } }

        // Perform BFS (Kahn's Algorithm)
        while (queue.isNotEmpty()) {
            queue.removeFirst().also {
                result.add(it)
                graph[it].forEach { neighbor ->
                    if (--inDegree[neighbor] == 0) queue.add(neighbor)
                }
            }
        }

        return if (result.size == numCourses) result.toIntArray() else intArrayOf()
    }
}

/**
* Entry point for the program.
*
* @return Unit (no return value, modifies state in-place).
*/
/**
* Entry point for the program.
*
* @return Unit (no return value, modifies state in-place).
*/
/**
* Entry point for the program.
*
* @return Unit (no return value, modifies state in-place).
*/
/**
* Entry point for the program.
*
* @return Unit (no return value, modifies state in-place).
*/
fun main() {
    val solver = graph.topological_sort.CourseSchedule_II_BFS()

    // Test 1: Simple case
    val result1 = solver.findOrder(2, arrayOf(intArrayOf(1, 0)))
    assert(result1 contentEquals intArrayOf(0, 1)) { "Test 1 failed: $result1" }

    // Test 2: Multiple dependencies
    val result2 = solver.findOrder(4, arrayOf(intArrayOf(1, 0), intArrayOf(2, 0), intArrayOf(3, 1), intArrayOf(3, 2)))
    assert(result2 contentEquals intArrayOf(0, 1, 2, 3) || result2 contentEquals intArrayOf(0, 2, 1, 3)) { "Test 2 failed: $result2" }

    // Test 3: Cycle in the graph (no valid order)
    val result3 = solver.findOrder(2, arrayOf(intArrayOf(0, 1), intArrayOf(1, 0)))
    assert(result3.isEmpty()) { "Test 3 failed: $result3" }

    // Test 4: No prerequisites
    val result4 = solver.findOrder(3, arrayOf())
    assert(result4.toSet() == setOf(0, 1, 2)) { "Test 4 failed: $result4" }

    // Test 5: Self-loop (invalid schedule)
    val result5 = solver.findOrder(1, arrayOf(intArrayOf(0, 0)))
    assert(result5.isEmpty()) { "Test 5 failed: $result5" }

    println("All tests passed.")
}
```

### Pattern Insight

**Graph Pattern.** BFS = queue, shortest path. DFS = stack/recursion, connectivity. Topological sort = in-degree counting + queue. Union-Find = dynamic connectivity.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations

1. What if the graph is disconnected (multiple components)?
1. What if edges have weights — does BFS still work?
1. What if you need the actual path, not just distance/existence?
1. DFS vs BFS — which is better and why?
1. What if the graph is too large to fit in memory?

---

## Critical Connections In A Network

### Problem

Given `n` (integer), `connections` (List<List<Int>>), `node` (integer), `parent` (integer), compute the computed result efficiently.

**Example:**

```
Input: n = 5, connections = input_value, node = 5, parent = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package graph.articulation_point

class CriticalConnectionsInANetwork {
    private lateinit var G: Array<MutableList<Int>>
    private lateinit var result: MutableList<List<Int>>
    private var depth = 0
    private lateinit var label: IntArray
    private lateinit var low: IntArray
    private lateinit var visited: BooleanArray

    /**
    * Solves the Critical Connections In ANetwork problem.
    * Takes `n` (integer), `connections` (2D list of integers).
    *
    * @param n The integer parameter representing n.
    * @param connections The input 2D list of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Critical Connections In ANetwork problem.
    * Takes `n` (integer), `connections` (2D list of integers).
    *
    * @param n The integer parameter representing n.
    * @param connections The input 2D list of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Critical Connections In ANetwork problem.
    * Takes `n` (integer), `connections` (2D list of integers).
    *
    * @param n The integer parameter representing n.
    * @param connections The input 2D list of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Critical Connections In ANetwork problem.
    * Takes `n` (integer), `connections` (2D list of integers).
    *
    * @param n The integer parameter representing n.
    * @param connections The input 2D list of integers.
    * @return The computed integer result.
    */
    fun criticalConnections(n: Int, connections: List<List<Int>>): List<List<Int>> {
        G = Array(n) { mutableListOf() }
        result = mutableListOf()
        depth = 0
        label = IntArray(n)
        low = IntArray(n)
        visited = BooleanArray(n)

        for (i in 0 until n) {
            G[i] = mutableListOf()
        }

        for (edge in connections) {
            val i = edge[0]
            val j = edge[1]
            G[i].add(j)
            G[j].add(i)
        }

        dfs(0, -1)

        return result
    }

    /**
    * Helper: dfs.
    *
    * @param node The integer parameter representing node.
    * @param parent The integer parameter representing parent.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: dfs.
    *
    * @param node The integer parameter representing node.
    * @param parent The integer parameter representing parent.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: dfs.
    *
    * @param node The integer parameter representing node.
    * @param parent The integer parameter representing parent.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: dfs.
    *
    * @param node The integer parameter representing node.
    * @param parent The integer parameter representing parent.
    * @return Unit (no return value, modifies state in-place).
    */
    private fun dfs(node: Int, parent: Int) {
        visited[node] = true
        label[node] = depth
        low[node] = depth
        depth++

        for (neighbour in G[node]) {
            if (neighbour == parent) continue

            if (!visited[neighbour]) {
                dfs(neighbour, node)

                if (label[node] < low[neighbour]) {
                    result.add(listOf(node, neighbour))
                }
            }

            low[node] = minOf(low[node], low[neighbour])
        }
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Critical Connections In A Network Short Code

### Problem

Given `n` (integer), `connections` (List<List<Int>>), `node` (integer), `parent` (integer), compute the computed result efficiently.

**Example:**

```
Input: n = 5, connections = input_value, node = 5, parent = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package graph.articulation_point

class CriticalConnectionsInANetworkShortCode {
    /**
    * Solves the Critical Connections In ANetwork Short Code problem.
    * Takes `n` (integer), `connections` (2D list of integers).
    *
    * @param n The integer parameter representing n.
    * @param connections The input 2D list of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Critical Connections In ANetwork Short Code problem.
    * Takes `n` (integer), `connections` (2D list of integers).
    *
    * @param n The integer parameter representing n.
    * @param connections The input 2D list of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Critical Connections In ANetwork Short Code problem.
    * Takes `n` (integer), `connections` (2D list of integers).
    *
    * @param n The integer parameter representing n.
    * @param connections The input 2D list of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Critical Connections In ANetwork Short Code problem.
    * Takes `n` (integer), `connections` (2D list of integers).
    *
    * @param n The integer parameter representing n.
    * @param connections The input 2D list of integers.
    * @return The computed integer result.
    */
    fun criticalConnections(n: Int, connections: List<List<Int>>): List<List<Int>> {
        val graph = Array(n) { mutableListOf<Int>() }.apply {
            connections.forEach { (u, v) -> this[u].add(v); this[v].add(u) }
        }
        val result = mutableListOf<List<Int>>()
        val labels = IntArray(n) { -1 }
        val low = IntArray(n)
        var time = 0

        /**
        * Solves the Critical Connections In ANetwork Short Code problem.
        * Takes `node` (integer), `parent` (integer).
        *
        * @param node The integer parameter representing node.
        * @param parent The integer parameter representing parent.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Critical Connections In ANetwork Short Code problem.
        * Takes `node` (integer), `parent` (integer).
        *
        * @param node The integer parameter representing node.
        * @param parent The integer parameter representing parent.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Critical Connections In ANetwork Short Code problem.
        * Takes `node` (integer), `parent` (integer).
        *
        * @param node The integer parameter representing node.
        * @param parent The integer parameter representing parent.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Critical Connections In ANetwork Short Code problem.
        * Takes `node` (integer), `parent` (integer).
        *
        * @param node The integer parameter representing node.
        * @param parent The integer parameter representing parent.
        * @return Unit (no return value, modifies state in-place).
        */
        fun dfs(node: Int, parent: Int) {
            labels[node] = time.also { low[node] = it; time++ }
            graph[node].forEach { neighbour ->
                if (neighbour != parent) {
                    if (labels[neighbour] == -1) {
                        dfs(neighbour, node)
                        if (low[neighbour] > labels[node]) result.add(listOf(node, neighbour))
                    }
                    low[node] = minOf(low[node], low[neighbour])
                }
            }
        }

        dfs(0, -1)
        return result
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Find Redundent Connections

### Problem

Given `edges` (2D matrix), `x` (integer), `y` (integer), compute the computed result efficiently.

**Example:**

```
Input: edges = [1, 2, 3, 4, 5], x = 5, y = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

### Code

```kotlin
package graph.mst

class FindRedundentConnections {
    /**
    * Solves the Find Redundent Connections problem.
    * Takes `edges` (2D matrix of integers).
    *
    * @param edges The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Redundent Connections problem.
    * Takes `edges` (2D matrix of integers).
    *
    * @param edges The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Redundent Connections problem.
    * Takes `edges` (2D matrix of integers).
    *
    * @param edges The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Redundent Connections problem.
    * Takes `edges` (2D matrix of integers).
    *
    * @param edges The input 2D matrix of integers.
    * @return The computed integer result.
    */
    fun findRedundantConnection(edges: Array<IntArray>): IntArray {
        val parent = IntArray(1001) { it }

        /**
        * Solves the Find Redundent Connections problem.
        * Takes `x` (integer).
        *
        * @param x The integer parameter representing x.
        * @return The computed integer result.
        */
        /**
        * Solves the Find Redundent Connections problem.
        * Takes `x` (integer).
        *
        * @param x The integer parameter representing x.
        * @return The computed integer result.
        */
        /**
        * Solves the Find Redundent Connections problem.
        * Takes `x` (integer).
        *
        * @param x The integer parameter representing x.
        * @return The computed integer result.
        */
        /**
        * Solves the Find Redundent Connections problem.
        * Takes `x` (integer).
        *
        * @param x The integer parameter representing x.
        * @return The computed integer result.
        */
        fun find(x: Int): Int {
            if (parent[x] != x) parent[x] = find(parent[x])
            return parent[x]
        }

        /**
        * Solves the Find Redundent Connections problem.
        * Takes `x` (integer), `y` (integer).
        *
        * @param x The integer parameter representing x.
        * @param y The integer parameter representing y.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Find Redundent Connections problem.
        * Takes `x` (integer), `y` (integer).
        *
        * @param x The integer parameter representing x.
        * @param y The integer parameter representing y.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Find Redundent Connections problem.
        * Takes `x` (integer), `y` (integer).
        *
        * @param x The integer parameter representing x.
        * @param y The integer parameter representing y.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Find Redundent Connections problem.
        * Takes `x` (integer), `y` (integer).
        *
        * @param x The integer parameter representing x.
        * @param y The integer parameter representing y.
        * @return `true` if the condition is met, `false` otherwise.
        */
        fun union(x: Int, y: Int): Boolean {
            val rootX = find(x)
            val rootY = find(y)
            if (rootX == rootY) return false
            parent[rootY] = rootX
            return true
        }

        for ((u, v) in edges) {
            if (!union(u, v)) return intArrayOf(u, v)
        }
        return intArrayOf()
    }

}
```

### Pattern Insight

**Binary Search Pattern.** Identify a monotonic predicate. The predicate must be false for all values on one side of the answer and true for all values on the other side. Binary search finds the transition point.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

### Variations

1. What if the input is not sorted? Can you sort it first?
1. What if there are duplicates — need first vs last occurrence?
1. What if the search space is a range of values, not array indices?
1. What if the array is too large to fit in memory?
1. What if the predicate is not monotonic?

---

## Tree Node

### Problem

Given `root` (TreeNode?), `node` (TreeNode?), compute the computed result efficiently.

**Example:**

```
Input: root = input_value, node = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package graph

import kotlin.math.max

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class HouseRobber3 {
    /**
    * Solves the Tree Node problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
    */
    /**
    * Solves the Tree Node problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
    */
    /**
    * Solves the Tree Node problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
    */
    /**
    * Solves the Tree Node problem.
    * Takes `root` (binary tree node reference).
    *
    * @param root The binary tree node reference (nullable).
    * @return The computed integer result.
    */
    fun rob(root: TreeNode?): Int {
        fun dfs (node: TreeNode?): IntArray {
            if (node == null)
                return intArrayOf(0 , 0)


            val (left, right) = arrayOf( dfs(node?.left), dfs(node?.right) )

            // If we rob this house then we can't rob children
            val toRob = node.`val` + left[1] + right[1]

            // If we don't rob then we could rob children and add them up
            val notToRob = maxOf(left[0], left[1]) + max(right[0], right[1])

            return intArrayOf(toRob, notToRob)
        }

        val result = dfs(root)

        return result.max()
    }

}
```

### Pattern Insight

**Dynamic Programming Pattern.** Define states (changing parameters), transitions (how to compute one state from others), and base cases. Compute bottom-up (iterative, table) or top-down (recursive, memoization).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(n²) |

### Variations

1. Can you optimize space to O(1) by keeping only the previous row?
1. What if the input size is 10x larger — does the DP table still fit?
1. Can you reconstruct the optimal path, not just the optimal value?
1. What changes if constraints go from unlimited to limited (or vice versa)?
1. Is there a greedy solution? When would greedy fail?

---

## Parallel Courses

### Problem

Given `n` (integer), `relations` (2D matrix), compute the computed result efficiently.

**Example:**

```
Input: n = 5, relations = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem uses **graph traversal**. Choose BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, or topological sort for dependency ordering. Track visited nodes to prevent infinite loops.

### Code

```kotlin
package graph.cycle

class ParallelCourses {
    /**
    * Solves the Parallel Courses problem.
    * Takes `n` (integer), `relations` (2D matrix of integers).
    *
    * @param n The integer parameter representing n.
    * @param relations The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Parallel Courses problem.
    * Takes `n` (integer), `relations` (2D matrix of integers).
    *
    * @param n The integer parameter representing n.
    * @param relations The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Parallel Courses problem.
    * Takes `n` (integer), `relations` (2D matrix of integers).
    *
    * @param n The integer parameter representing n.
    * @param relations The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Parallel Courses problem.
    * Takes `n` (integer), `relations` (2D matrix of integers).
    *
    * @param n The integer parameter representing n.
    * @param relations The input 2D matrix of integers.
    * @return The computed integer result.
    */
    fun minimumSemesters(n: Int, relations: Array<IntArray>): Int {
        val inDegree = IntArray(n + 1) // One-based index
        val graph = Array(n + 1) { mutableListOf<Int>() }

        relations.forEach { (u, v) ->
            graph[u].add(v)
            inDegree[v]++
        }

        val queue = ArrayDeque<Int>()
        var semesters = 0
        var completed = 0

        // Add courses with no prerequisites (in-degree 0)
        (1..n).filter { inDegree[it] == 0 }.forEach { queue.add(it) }

        while (queue.isNotEmpty()) {
            val size = queue.size
            semesters++
            repeat(size) {
                val course = queue.removeFirst()
                completed++
                graph[course].forEach { next ->
                    if (--inDegree[next] == 0) queue.add(next)
                }
            }
        }

        return if (completed == n) semesters else -1
    }
}
```

### Pattern Insight

**Graph Pattern.** BFS = queue, shortest path. DFS = stack/recursion, connectivity. Topological sort = in-degree counting + queue. Union-Find = dynamic connectivity.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations

1. What if the graph is disconnected (multiple components)?
1. What if edges have weights — does BFS still work?
1. What if you need the actual path, not just distance/existence?
1. DFS vs BFS — which is better and why?
1. What if the graph is too large to fit in memory?

---

## Reorder Routes To Make All Paths Lead To City Zero

### Problem

Given `n` (integer), `connections` (2D matrix), `city` (integer), compute the computed result efficiently.

**Example:**

```
Input: n = 5, connections = [1, 2, 3, 4, 5], city = 5
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package graph

class ReorderRoutesToMakeAllPathsLeadToCityZero {
    /**
    * Solves the Reorder Routes To Make All Paths Lead To City Zero problem.
    * Takes `n` (integer), `connections` (2D matrix of integers).
    *
    * @param n The integer parameter representing n.
    * @param connections The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Reorder Routes To Make All Paths Lead To City Zero problem.
    * Takes `n` (integer), `connections` (2D matrix of integers).
    *
    * @param n The integer parameter representing n.
    * @param connections The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Reorder Routes To Make All Paths Lead To City Zero problem.
    * Takes `n` (integer), `connections` (2D matrix of integers).
    *
    * @param n The integer parameter representing n.
    * @param connections The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Reorder Routes To Make All Paths Lead To City Zero problem.
    * Takes `n` (integer), `connections` (2D matrix of integers).
    *
    * @param n The integer parameter representing n.
    * @param connections The input 2D matrix of integers.
    * @return The computed integer result.
    */
    fun minReorder(n: Int, connections: Array<IntArray>): Int {
        val graph = Array(n) { mutableListOf<IntArray>() }

        // Build adjacency list as an undirected graph
        for (edge in connections) {
            graph[edge[0]].add(edge)  // Forward edge
            graph[edge[1]].add(edge)  // Backward edge
        }

        var changes = 0
        val visited = BooleanArray(n)

        /**
        * Solves the Reorder Routes To Make All Paths Lead To City Zero problem.
        * Takes `city` (integer).
        *
        * @param city The integer parameter representing city.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Reorder Routes To Make All Paths Lead To City Zero problem.
        * Takes `city` (integer).
        *
        * @param city The integer parameter representing city.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Reorder Routes To Make All Paths Lead To City Zero problem.
        * Takes `city` (integer).
        *
        * @param city The integer parameter representing city.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Reorder Routes To Make All Paths Lead To City Zero problem.
        * Takes `city` (integer).
        *
        * @param city The integer parameter representing city.
        * @return Unit (no return value, modifies state in-place).
        */
        fun dfs(city: Int) {
            visited[city] = true
            for (edge in graph[city]) {
                val (from, to) = edge
                val neighbor = if (from == city) to else from
                if (!visited[neighbor]) {
                    if (from == city) changes++ // Forward edge needs reversal
                    dfs(neighbor)
                }
            }
        }

        dfs(0) // Start DFS from city 0
        return changes
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Word Ladder

### Problem

Given `beginWord` (string), `endWord` (string), `wordList` (List<String>), compute the computed result efficiently.

**Example:**

```
Input: beginWord = "example", endWord = "example", wordList = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses **graph traversal**. Choose BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, or topological sort for dependency ordering. Track visited nodes to prevent infinite loops.

### Code

```kotlin
package graph

import java.util.*

class WordLadder {
    /**
    * Solves the Word Ladder problem.
    * Takes `beginWord` (string), `endWord` (string), `wordList` (list of strings).
    *
    * @param beginWord The input string.
    * @param endWord The input string.
    * @param wordList The input list of strings.
    * @return The computed integer result.
    */
    /**
    * Solves the Word Ladder problem.
    * Takes `beginWord` (string), `endWord` (string), `wordList` (list of strings).
    *
    * @param beginWord The input string.
    * @param endWord The input string.
    * @param wordList The input list of strings.
    * @return The computed integer result.
    */
    /**
    * Solves the Word Ladder problem.
    * Takes `beginWord` (string), `endWord` (string), `wordList` (list of strings).
    *
    * @param beginWord The input string.
    * @param endWord The input string.
    * @param wordList The input list of strings.
    * @return The computed integer result.
    */
    /**
    * Solves the Word Ladder problem.
    * Takes `beginWord` (string), `endWord` (string), `wordList` (list of strings).
    *
    * @param beginWord The input string.
    * @param endWord The input string.
    * @param wordList The input list of strings.
    * @return The computed integer result.
    */
    fun ladderLength(beginWord: String, endWord: String, wordList: List<String>): Int {
        if (endWord !in wordList) return 0 // if end word is not word bank then it's not possible

        val wordSet = wordList.toHashSet() // Store the word list in a set for O(1) lookups
        val queue: Queue<Pair<String, Int>> = LinkedList() // Queue to store word and level (distance)
        queue.offer(beginWord to 1) // Start with the beginWord and level 1

        while (queue.isNotEmpty()) {
            val (currentWord, level) = queue.poll()

            // Check all possible transformations by changing each character
            for (i in currentWord.indices) {
                val originalChar = currentWord[i]
                for (ch in 'a'..'z') {
                    // Create a new word by replacing the i-th character
                    val newWord = currentWord.substring(0, i) + ch + currentWord.substring(i + 1)

                    // If the new word is the end word, return the result
                    if (newWord == endWord) return level + 1

                    // If the new word is in the word set, we can add it to the queue
                    if (newWord in wordSet) {
                        wordSet.remove(newWord) // Remove to avoid revisiting
                        queue.offer(newWord to level + 1)
                    }
                }
            }
        }

        return 0 // If no transformation is found
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

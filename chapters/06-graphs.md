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

> **18 problems** — Master graph traversals, shortest paths, and topological ordering.

## The Pattern

Graph problems reduce to choosing the right traversal: BFS for shortest path, DFS for connectivity, topological sort for dependencies.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [Alien Dictionary](#aliendictionary) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Alien Dictionary_BFS](#aliendictionary_bfs) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Apply Substitutions](#applysubstitutions) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Bus Routes](#busroutes) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [Cheapest Flights Within K Stops](#cheapestflightswithinkstops) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Cheapest Flights With K Stops](#cheapestflightswithkstops) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [Cheapest Flight With K Stops](#cheapestflightwithkstops) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [Node](#clonegraph) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Course Schedule](#courseschedule) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Course Schedule_II](#courseschedule_ii) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [Course Schedule_II_BFS](#courseschedule_ii_bfs) | — | <span class="badge badge-medium">Medium</span> |
| 12 | [Critical Connections In A Network](#criticalconnectionsinanetwork) | — | <span class="badge badge-medium">Medium</span> |
| 13 | [Critical Connections In A Network Short Code](#criticalconnectionsinanetworkshortcode) | — | <span class="badge badge-medium">Medium</span> |
| 14 | [Find Redundent Connections](#findredundentconnections) | — | <span class="badge badge-medium">Medium</span> |
| 15 | [Tree Node](#houserobber3) | — | <span class="badge badge-medium">Medium</span> |
| 16 | [Parallel Courses](#parallelcourses) | — | <span class="badge badge-medium">Medium</span> |
| 17 | [Reorder Routes To Make All Paths Lead To City Zero](#reorderroutestomakeallpathsleadtocityzero) | — | <span class="badge badge-medium">Medium</span> |
| 18 | [Word Ladder](#wordladder) | — | <span class="badge badge-medium">Medium</span> |

---

## Alien Dictionary

<span id="aliendictionary"></span>

### Problem

**Aliendictionary**

**Function:** `Alien Order` takes `words` (Array<string>) and returns **string**.

**Key logic:**
- 0 = visiting, 1 = visited, -1 = not visited
- Step 1: Build the graph and visited map
- Step 2: Build edges between characters
- Check if the second word is a prefix of the first
- Invalid case, prefix conflict



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `graph`, `visited`, `result`

**Execution flow:**
- 0 = visiting, 1 = visited, -1 = not visited
- Step 1: Build the graph and visited map
- Step 2: Build edges between characters
- Check if the second word is a prefix of the first
- Invalid case, prefix conflict
- Step 3: Perform DFS to find topological sort
- Cycle detected
- Already visited

### Code

```kotlin
package graph.topological_sort

class AlienDictionary {
    enum class State {
        NOT_VISITED, VISITING, VISITED
    }

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Alien Dictionary_BFS

<span id="aliendictionary_bfs"></span>

### Problem

**Aliendictionary Bfs**

**Function:** `Alien Order` takes `words` (Array<string>) and returns **string**.

**Key logic:**
- Handle invalid case (e.g., "abc" before "ab")



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `graph`, `inDegree`, `currentWord`, `nextWord`, `minLength`, `currentChar`, `nextChar`, `queue`

**Execution flow:**
- Handle invalid case (e.g., "abc" before "ab")

### Code

```kotlin
package graph.topological_sort

class AlienDictionary_BFS {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Apply Substitutions

<span id="applysubstitutions"></span>

### Problem

**Applysubstitutions**

**Function:** `Apply Substitutions` takes `replacements` (List<List<string>>), `text` (string) and returns **string**.

**Key logic:**
- Replace if found, else keep original
- Move past the placeholder
- Continue resolving if changed



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `map`, `sb`, `i`, `key`, `result`

**Execution flow:**
- Replace if found, else keep original
- Move past the placeholder
- Continue resolving if changed

### Code

```kotlin
package string

class ApplySubstitutions {
    fun applySubstitutions(replacements: List<List<String>>, text: String): String {
        val map = mutableMapOf<String, String>()

        for ((key, value) in replacements) {
            map[key] = value
        }

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Bus Routes

<span id="busroutes"></span>

### Problem

**Busroutes**

**Function:** `Num Buses To Destination` takes `routes` (Array<array of integers>), `source` (integer), `target` (integer) and returns **integer**.

**Key logic:**
- Stop -> List of buses passing through
- Build the graph
- Explore all buses passing through the current stop
- (1) =>



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `stop`, `busCount`, `graph`, `queue`, `visitedBuses`, `visitedStops`

**Execution flow:**
- Stop -> List of buses passing through
- Build the graph
- Explore all buses passing through the current stop

### Code

```kotlin
package graph

import java.util.*

import java.util.*

class BusRoutes {
    data class Node(val stop: Int, val busCount: Int)

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Cheapest Flights Within K Stops

<span id="cheapestflightswithinkstops"></span>

### Problem

**Cheapestflightswithinkstops**

**Function:** `Find Cheapest Price` takes `n` (integer), `flights` (Array<array of integers>), `src` (integer), `dst` (integer), `k` (integer) and returns **integer**.

**Key logic:**
- Define the Node class to encapsulate flight details
- Graph map where each integer key maps to a list of Node objects
- Solving using Bellman Ford
- Build the graph from the input flights
- Append the destination and cost to the list of nodes for the source



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dest`, `price`, `graph`, `from`, `to`, `cost`, `dp`, `cheapest`

**Execution flow:**
- Define the Node class to encapsulate flight details
- Graph map where each integer key maps to a list of Node objects
- Solving using Bellman Ford
- Build the graph from the input flights
- Append the destination and cost to the list of nodes for the source
- DP table for storing minimum cost to each node with up to i flights
- Cost to reach source from itself is 0
- Perform relaxation for each possible number of stops

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
        fun main(args: Array<String>) {

        }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

The DP table has dimensions proportional to the input size, giving O(n²) space. Each cell requires O(1) or O(n) work, totaling O(n³).

---

## Cheapest Flights With K Stops

<span id="cheapestflightswithkstops"></span>

### Problem

**Cheapestflightswithkstops**

**Function:** `Find Cheapest Price` takes `n` (integer), `flights` (Array<array of integers>), `src` (integer), `dst` (integer), `k` (integer) and returns **integer**.

**Key logic:**
- Define the Node class to encapsulate flight details
- Define the State class for priority queue elements
- Build the graph from the input flights
- E + EK log
- Initialize the priority queue and cost tracking



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dest`, `cost`, `node`, `cost`, `stops`, `graph`, `from`, `to`

**Execution flow:**
- Define the Node class to encapsulate flight details
- Define the State class for priority queue elements
- Build the graph from the input flights
- Initialize the priority queue and cost tracking
- Skip if the number of stops exceeds the limit or if the path is not optimal
- Return the cost if the destination is reached
- Explore neighbors

### Code

```kotlin
package graph.greedy

import java.util.*

class CheapestFlightsWithKStops {
    // Define the Node class to encapsulate flight details
    data class Node(val dest: Int, val cost: Int)

    // Define the State class for priority queue elements
    data class State(val node: Int, val cost: Int, val stops: Int)

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

---

## Cheapest Flight With K Stops

<span id="cheapestflightwithkstops"></span>

### Problem

**Cheapestflightwithkstops**

**Function:** `Find Cheapest Price` takes `n` (integer), `flights` (Array<array of integers>), `src` (integer), `dst` (integer), `k` (integer) and returns **integer**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `node`, `cost`, `stops`, `graph`, `pq`, `minStops`

### Code

```kotlin
package graph.greedy

import java.util.*

class CheapestFlightWithKStops {
    data class Flight(val node: Int, val cost: Int, val stops: Int)

    fun findCheapestPrice(n: Int, flights: Array<IntArray>, src: Int, dst: Int, k: Int): Int {
        val graph = flights.groupBy({ it[0] }) { Flight(it[1], it[2], 0) }
        val pq = PriorityQueue<Flight>(compareBy { it.cost })
        val minStops = IntArray(n) { Int.MAX_VALUE }

        pq.offer(Flight(src, 0, 0))

        while (pq.isNotEmpty()) {
            val (node, currentCost, stops) = pq.poll()

            if (stops > k + 1 || stops >= minStops[node]) continue
            minStops[node] = stops

            if (node == dst) return currentCost

            graph[node]?.forEach { (next, cost, _) ->
                pq.offer(Flight(next, currentCost + cost, stops + 1))
            }
        }
        return -1
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

---

## Node

<span id="clonegraph"></span>

### Problem

**Clonegraph**

**Function:** `Clone Graph` takes `node` (Node?) and returns **Node**.



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `neighbors`, `map`, `clonedNode`

### Code

```kotlin
package graph

data class Node(val `val`: Int, val neighbors: MutableList<Node?> = mutableListOf())

class CloneGraph {
    val map = mutableMapOf<Node, Node>()

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Course Schedule

<span id="courseschedule"></span>

### Problem

**Courseschedule**

**Function:** `Has Cycle` takes `numCourses` (integer) and returns **boolean**.

**Key logic:**
- Define dfs function inside hasCycle to limit its scope
- Reset graph for each invocation to handle multiple calls



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `graph`, `status`

**Execution flow:**
- Define dfs function inside hasCycle to limit its scope
- Reset graph for each invocation to handle multiple calls

### Code

```kotlin
package graph.cycle

class CourseSchedule {
    private var graph: MutableMap<Int, MutableList<Int>> = mutableMapOf()
    private lateinit var status: Array<NodeStatus>
    private enum class NodeStatus { UNVISITED, EXPLORING, DONE }

    private fun hasCycle(numCourses: Int): Boolean {
        // Define dfs function inside hasCycle to limit its scope
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Course Schedule_II

<span id="courseschedule_ii"></span>

### Problem

**Courseschedule Ii**

**Function:** `Find Order` takes `numCourses` (integer), `prerequisites` (Array<array of integers>) and returns **array of integers**.

**Key logic:**
- Initialize graph, status, and result array
- Build the graph
- Attempt to find a topological order
- Nested DFS function for checking cycles and building the result
- If an already visited node re-appears then it means we looped back to an exploring node



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `graph`, `status`, `result`, `index`

**Execution flow:**
- Initialize graph, status, and result array
- Build the graph
- Attempt to find a topological order
- Nested DFS function for checking cycles and building the result
- If an already visited node re-appears then it means we looped back to an exploring node
- If an already done node re-appears it doesn't mean cycle rather it means
- we fully explored the node previously and found no cycle in the path.

### Code

```kotlin
package graph.topological_sort

class CourseSchedule_II {
    private var graph: MutableMap<Int, MutableList<Int>> = mutableMapOf()
    private lateinit var status: Array<NodeStatus>
    private lateinit var result: IntArray
    private var index: Int = 0

    private enum class NodeStatus { UNVISITED, EXPLORING, DONE }

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

    private fun hasCycle(numCourses: Int): Boolean {
        // Nested DFS function for checking cycles and building the result
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Course Schedule_II_BFS

<span id="courseschedule_ii_bfs"></span>

### Problem

**Courseschedule Ii Bfs**

**Function:** `Find Order` takes `numCourses` (integer), `prerequisites` (Array<array of integers>) and returns **array of integers**.

**Key logic:**
- Build the graph and calculate in-degrees
- Initialize queue with courses having no prerequisites
- Perform BFS (Kahn's Algorithm)
- Test 1: Simple case
- Test 2: Multiple dependencies



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `graph`, `inDegree`, `result`, `queue`, `solver`, `result1`, `result2`, `result3`

**Execution flow:**
- Build the graph and calculate in-degrees
- Initialize queue with courses having no prerequisites
- Perform BFS (Kahn's Algorithm)
- Test 1: Simple case
- Test 2: Multiple dependencies
- Test 3: Cycle in the graph (no valid order)
- Test 4: No prerequisites
- Test 5: Self-loop (invalid schedule)

### Code

```kotlin
package graph.topological_sort

class CourseSchedule_II_BFS {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Critical Connections In A Network

<span id="criticalconnectionsinanetwork"></span>

### Problem

**Criticalconnectionsinanetwork**

**Function:** `Critical Connections` takes `n` (integer), `connections` (List<List<integer>>) and returns **List**.



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `G`, `result`, `depth`, `label`, `low`, `visited`, `i`, `j`

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Critical Connections In A Network Short Code

<span id="criticalconnectionsinanetworkshortcode"></span>

### Problem

**Criticalconnectionsinanetworkshortcode**

**Function:** `Critical Connections` takes `n` (integer), `connections` (List<List<integer>>) and returns **List**.



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `graph`, `result`, `labels`, `low`, `time`

### Code

```kotlin
package graph.articulation_point

class CriticalConnectionsInANetworkShortCode {
    fun criticalConnections(n: Int, connections: List<List<Int>>): List<List<Int>> {
        val graph = Array(n) { mutableListOf<Int>() }.apply {
            connections.forEach { (u, v) -> this[u].add(v); this[v].add(u) }
        }
        val result = mutableListOf<List<Int>>()
        val labels = IntArray(n) { -1 }
        val low = IntArray(n)
        var time = 0

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Find Redundent Connections

<span id="findredundentconnections"></span>

### Problem

**Findredundentconnections**

**Function:** `Find Redundant Connection` takes `edges` (Array<array of integers>) and returns **array of integers**.



### Approach

**Solution Approach:**
1. The main function `findRedundantConnection` processes the input
2. Uses helper functions: find, union

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `parent`, `rootX`, `rootY`

### Code

```kotlin
package graph.mst

class FindRedundentConnections {
    fun findRedundantConnection(edges: Array<IntArray>): IntArray {
        val parent = IntArray(1001) { it }

        fun find(x: Int): Int {
            if (parent[x] != x) parent[x] = find(parent[x])
            return parent[x]
        }

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Tree Node

<span id="houserobber3"></span>

### Problem

**Houserobber3**

**Function:** `Rob` takes `root` (TreeNode?) and returns **integer**.

**Key logic:**
- If we rob this house then we can't rob children
- If we don't rob then we could rob children and add them up



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `toRob`, `notToRob`, `result`

**Execution flow:**
- If we rob this house then we can't rob children
- If we don't rob then we could rob children and add them up

### Code

```kotlin
package graph

import kotlin.math.max

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class HouseRobber3 {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Parallel Courses

<span id="parallelcourses"></span>

### Problem

**Parallelcourses**

**Function:** `Minimum Semesters` takes `n` (integer), `relations` (Array<array of integers>) and returns **integer**.

**Key logic:**
- One-based index
- Add courses with no prerequisites (in-degree 0)



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `inDegree`, `graph`, `queue`, `semesters`, `completed`, `size`, `course`

**Execution flow:**
- One-based index
- Add courses with no prerequisites (in-degree 0)

### Code

```kotlin
package graph.cycle

class ParallelCourses {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Reorder Routes To Make All Paths Lead To City Zero

<span id="reorderroutestomakeallpathsleadtocityzero"></span>

### Problem

**Reorderroutestomakeallpathsleadtocityzero**

**Function:** `Min Reorder` takes `n` (integer), `connections` (Array<array of integers>) and returns **integer**.

**Key logic:**
- Build adjacency list as an undirected graph
- Forward edge
- Backward edge
- Forward edge needs reversal
- Start DFS from city 0



### Approach

**DFS (Depth-First Search) Approach:**
1. Recursively explore each path until reaching a base case
2. Backtrack when stuck to try alternative paths
3. DFS is useful for connectivity, path existence, and exhaustive search


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `graph`, `changes`, `visited`, `neighbor`

**Execution flow:**
- Build adjacency list as an undirected graph
- Forward edge
- Backward edge
- Forward edge needs reversal
- Start DFS from city 0

### Code

```kotlin
package graph

class ReorderRoutesToMakeAllPathsLeadToCityZero {
    fun minReorder(n: Int, connections: Array<IntArray>): Int {
        val graph = Array(n) { mutableListOf<IntArray>() }

        // Build adjacency list as an undirected graph
        for (edge in connections) {
            graph[edge[0]].add(edge)  // Forward edge
            graph[edge[1]].add(edge)  // Backward edge
        }

        var changes = 0
        val visited = BooleanArray(n)

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Word Ladder

<span id="wordladder"></span>

### Problem

**Wordladder**

**Function:** `Ladder Length` takes `beginWord` (string), `endWord` (string), `wordList` (List<string>) and returns **integer**.

**Key logic:**
- if end word is not word bank then it's not possible
- Store the word list in a set for O(1) lookups
- Queue to store word and level (distance)
- Start with the beginWord and level 1
- Check all possible transformations by changing each character



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `wordSet`, `queue`, `originalChar`, `newWord`

**Execution flow:**
- if end word is not word bank then it's not possible
- Store the word list in a set for O(1) lookups
- Queue to store word and level (distance)
- Start with the beginWord and level 1
- Check all possible transformations by changing each character
- Create a new word by replacing the i-th character
- If the new word is the end word, return the result
- If the new word is in the word set, we can add it to the queue

### Code

```kotlin
package graph

import java.util.*

class WordLadder {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Key Takeaways

1. **Core pattern recognition** — Graph problems reduce to choosing the right traversal: BFS for shortest path, DFS for connectivity, topological sort for dependencies.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

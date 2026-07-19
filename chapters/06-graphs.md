---
layout: chapter
title: "Graphs - The Real World Is a Graph"
chapter_number: 6
chapter_title: "Graphs"
toc: true
prev_chapter:
  url: "/chapters/05-trees"
  title: "Trees - Hierarchical Thinking"
next_chapter:
  url: "/chapters/07-bit-manipulation"
  title: "Bit Manipulation - Working at the Hardware Level"
---

# Graphs: The Real World Is a Graph

## Complete Problem Set

### Graph Traversal (6 problems)
| # | Problem | File |
|---|---------|------|
| 1 | Clone Graph | graph/CloneGraph.kt |
| 2 | Bus Routes | graph/BusRoutes.kt |
| 3 | Reorder Routes to City Zero | graph/ReorderRoutesToMakeAllPathsLeadToCityZero.kt |
| 4 | Word Ladder | graph/WordLadder.kt |
| 5 | Shortest Path in Binary Matrix | array/ShortestPathInBinaryMatrix.kt |
| 6 | House Robber III | graph/HouseRobber3.kt |

### Cycle Detection (3 problems)
| # | Problem | File |
|---|---------|------|
| 7 | Course Schedule | graph/cycle/CourseSchedule.kt |
| 8 | Course Schedule II | graph/cycle/CourseSchedule_II.kt |
| 9 | Parallel Courses | graph/cycle/ParallelCourses.kt |

### Topological Sort (5 problems)
| # | Problem | File |
|---|---------|------|
| 10 | Course Schedule II (BFS) | graph/topological_sort/CourseSchedule_II_BFS.kt |
| 11 | Alien Dictionary | graph/topological_sort/AlienDictionary.kt |
| 12 | Alien Dictionary (BFS) | graph/topological_sort/AlienDictionary_BFS.kt |
| 13 | Apply Substitutions | graph/topological_sort/ApplySubstitutions.kt |

### MST & Connectivity (5 problems)
| # | Problem | File |
|---|---------|------|
| 14 | Find Redundant Connection | graph/mst/FindRedundentConnections.kt |
| 15 | Prim's Algorithm | graph/mst/PrimsAlgorithm.kt |
| 16 | Critical Connections | graph/articulation_point/CriticalConnectionsInANetwork.kt |
| 17 | Articulation Points | graph/articulation_point/FindArticulationPoints.kt |

### Shortest Path (3 problems)
| # | Problem | File |
|---|---------|------|
| 18 | Cheapest Flights (DP) | graph/dp/CheapestFlightsWithinKStops.kt |
| 19 | Cheapest Flights (Greedy) | graph/greedy/CheapestFlightsWithKStops.kt |
| 20 | The Maze III | graph/greedy/TheMaze_III.kt |

### Key Solutions

```kotlin
// Clone Graph
fun cloneGraph(node: Node?): Node? {
    if (node == null) return null
    val visited = mutableMapOf<Node, Node>()
    fun dfs(n: Node): Node {
        if (n in visited) return visited[n]!!
        val clone = Node(n.`val`)
        visited[n] = clone
        for (nei in n.neighbors) clone.neighbors.add(dfs(nei!!))
        return clone
    }
    return dfs(node)
}

// Course Schedule (Cycle Detection)
fun canFinish(n: Int, prerequisites: Array<IntArray>): Boolean {
    val g = Array(n) { mutableListOf<Int>() }
    for ((c, p) in prerequisites) g[c].add(p)
    val v = IntArray(n) // 0=unvisited, 1=visiting, 2=visited
    fun dfs(node: Int): Boolean {
        if (v[node] == 1) return false
        if (v[node] == 2) return true
        v[node] = 1
        for (nei in g[node]) if (!dfs(nei)) return false
        v[node] = 2; return true
    }
    for (i in 0 until n) if (!dfs(i)) return false
    return true
}

// Alien Dictionary
fun alienOrder(words: Array<String>): String {
    val g = mutableMapOf<Char, MutableList<Char>>()
    val indeg = mutableMapOf<Char, Int>()
    for (w in words) for (c in w) { g.putIfAbsent(c, mutableListOf()); indeg.putIfAbsent(c, 0) }
    for (i in 0 until words.size - 1) {
        var j = 0
        while (j < minOf(words[i].length, words[i+1].length)) {
            if (words[i][j] != words[i+1][j]) {
                if (words[i+1][j] !in g[words[i][j]]!!) {
                    g[words[i][j]]!!.add(words[i+1][j]); indeg[words[i+1][j]] = indeg.getOrDefault(words[i+1][j], 0) + 1
                }
                break
            }
            j++
        }
        if (j == minOf(words[i].length, words[i+1].length) && words[i].length > words[i+1].length) return ""
    }
    val q = ArrayDeque(indeg.filter { it.value == 0 }.keys)
    val sb = StringBuilder()
    while (q.isNotEmpty()) {
        val c = q.removeFirst(); sb.append(c)
        for (n in g[c]!!) { indeg[n] = indeg[n]!! - 1; if (indeg[n] == 0) q.add(n) }
    }
    return if (sb.length == indeg.size) sb.toString() else ""
}

// Dijkstra
fun shortestPath(graph: Map<Int, List<Pair<Int, Int>>>, start: Int, n: Int): IntArray {
    val dist = IntArray(n) { Int.MAX_VALUE }; dist[start] = 0
    val pq = PriorityQueue<Pair<Int, Int>>(compareBy { it.second }); pq.add(start to 0)
    while (pq.isNotEmpty()) {
        val (node, d) = pq.poll()
        if (d > dist[node]) continue
        for ((next, w) in graph[node] ?: emptyList()) {
            if (dist[node] + w < dist[next]) { dist[next] = dist[node] + w; pq.add(next to dist[next]) }
        }
    }
    return dist
}
```

---

> **Next up: [Bit Manipulation ->](./07-bit-manipulation.md)**

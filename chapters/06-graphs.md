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

{% include code-tabs-file.html problem="aliendictionary" %}

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

{% include code-tabs-file.html problem="aliendictionary_bfs" %}

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

{% include code-tabs-file.html problem="applysubstitutions" %}

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

{% include code-tabs-file.html problem="busroutes" %}

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

{% include code-tabs-file.html problem="cheapestflightswithinkstops" %}

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

{% include code-tabs-file.html problem="cheapestflightswithkstops" %}

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

{% include code-tabs-file.html problem="cheapestflightwithkstops" %}

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

{% include code-tabs-file.html problem="clonegraph" %}

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

{% include code-tabs-file.html problem="courseschedule" %}

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

{% include code-tabs-file.html problem="courseschedule_ii" %}

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

{% include code-tabs-file.html problem="courseschedule_ii_bfs" %}

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

{% include code-tabs-file.html problem="criticalconnectionsinanetwork" %}

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

{% include code-tabs-file.html problem="criticalconnectionsinanetworkshortcode" %}

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

{% include code-tabs-file.html problem="findredundentconnections" %}

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

{% include code-tabs-file.html problem="houserobber3" %}

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

{% include code-tabs-file.html problem="parallelcourses" %}

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

{% include code-tabs-file.html problem="reorderroutestomakeallpathsleadtocityzero" %}

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

{% include code-tabs-file.html problem="wordladder" %}

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

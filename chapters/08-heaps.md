---
layout: chapter
title: "Heaps & Priority Queues"
chapter_number: 8
chapter_title: "Heaps & Priority Queues"
toc: true
prev_chapter:
  url: "/chapters/07-bit-manipulation.html"
  title: "Bit Manipulation"
next_chapter:
  url: "/chapters/09-disjoint-set-union.html"
  title: "Disjoint Set Union"
---

# Heaps & Priority Queues

> **11 problems** — Master priority queues for k-th order statistics, scheduling, and streaming data.

## The Pattern

Heaps maintain the min/max of a dynamic set. Use min-heap for k largest, max-heap for k smallest, dual heaps for median.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [Dual Balanced Heap](#dualbalancedheap) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [MK Average](#findingmkaverage) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Find K Closest Elements](#findkclosestelements) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Find Score Of An Array After Marking All Elements](#findscoreofanarrayaftermarkingallelements) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [IPO](#ipo) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Longest Happy String](#longesthappystring) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [Median From Running Stream](#medianfromrunningstream) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [Meeting Room_III](#meetingroom_iii) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Single Threaded CPU](#singlethreadedcpu) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Sliding Window Median](#slidingwindowmedian) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [Top K Frequent Elements](#topkfrequentelements) | — | <span class="badge badge-medium">Medium</span> |

---

## Dual Balanced Heap

<span id="dualbalancedheap"></span>

### Problem

**Dualbalancedheap**

**Function:** `Get Median` takes none and returns **T**.

**Key logic:**
- Min-heap for the larger half
- Max-heap for the smaller half
- Handling generic types requires a custom approach for averaging or choosing one of the elements.
- Simplification: you may need to define how to combine two elements for real applications.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `minHeap`, `maxHeap`

**Execution flow:**
- Min-heap for the larger half
- Max-heap for the smaller half
- Handling generic types requires a custom approach for averaging or choosing one of the elements.
- Simplification: you may need to define how to combine two elements for real applications.

### Code

```kotlin
package heap

import java.util.*

class DualBalancedHeap<T : Comparable<T>> {
    private val minHeap = PriorityQueue<T>() // Min-heap for the larger half
    private val maxHeap = PriorityQueue<T>(compareByDescending { it }) // Max-heap for the smaller half

    private fun balanceHeaps() {
        if (maxHeap.size > minHeap.size + 1) {
            minHeap.add(maxHeap.poll())
        } else if (minHeap.size > maxHeap.size) {
            maxHeap.add(minHeap.poll())
        }
    }

    fun add(num: T) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.add(num)
        } else {
            minHeap.add(num)
        }
        balanceHeaps()
    }

    fun remove(num: T) {
        if (maxHeap.contains(num)) {
            maxHeap.remove(num)
        } else {
            minHeap.remove(num)
        }
        balanceHeaps()
    }

    fun getMedian(): T? {
        return if (maxHeap.size == minHeap.size) {
            // Handling generic types requires a custom approach for averaging or choosing one of the elements.
            maxHeap.peek()
        // Simplification: you may need to define how to combine two elements for real applications.
        } else {
            maxHeap.peek()
        }
    }

    fun size(): Int {
        return maxHeap.size + minHeap.size
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

## MK Average

<span id="findingmkaverage"></span>

### Problem

**Findingmkaverage**

**Function:** `Calculate Mkaverage` takes none and returns **integer**.

**Key logic:**
- max heap (for k smallest elements)
- min heap (for k largest elements)
- Sum of the middle elements
- Add to deque
- Add to one of the heaps



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `m`, `k`, `deque`, `lowHeap`, `highHeap`, `sum`, `oldest`, `middleCount`

**Execution flow:**
- max heap (for k smallest elements)
- min heap (for k largest elements)
- Sum of the middle elements
- Add to deque
- Add to one of the heaps
- Add to lowHeap (max heap)
- Add to highHeap (min heap)
- Maintain the window size of m

### Code

```kotlin
package heap

import java.util.*

class MKAverage(private val m: Int, private val k: Int) {
    private val deque = LinkedList<Int>()
    private val lowHeap = PriorityQueue<Int>(compareByDescending { it }) // max heap (for k smallest elements)
    private val highHeap = PriorityQueue<Int>() // min heap (for k largest elements)
    private var sum = 0L // Sum of the middle elements

    fun addElement(num: Int) {
        // Add to deque
        deque.add(num)

        // Add to one of the heaps
        if (lowHeap.size < k) {
            lowHeap.add(num)  // Add to lowHeap (max heap)
        } else if (highHeap.size < k) {
            highHeap.add(num) // Add to highHeap (min heap)
        } else {
            // Maintain the window size of m
            val oldest = deque.poll()
            if (lowHeap.contains(oldest)) {
                lowHeap.remove(oldest)
            } else {
                highHeap.remove(oldest)
            }

            if (lowHeap.size < k) {
                lowHeap.add(num)
            } else if (highHeap.size < k) {
                highHeap.add(num)
            }
        }

        // Balance the heaps
        balanceHeaps()

        // Recalculate the sum of the middle elements
        recalculateMiddleSum()
    }

    fun calculateMKAverage(): Int {
        return if (deque.size < m) {
            -1
        } else {
            val middleCount = m - 2 * k
            (sum / middleCount).toInt()
        }
    }

    // Balance heaps to ensure there are k elements in each of the heaps
    private fun balanceHeaps() {
        // Ensure lowHeap has k elements and highHeap has k elements
        if (lowHeap.size > k) {
            highHeap.add(lowHeap.poll())
        }
        if (highHeap.size > k) {
            lowHeap.add(highHeap.poll())
        }
    }

    // Recalculate the sum of the middle elements in the sliding window
    private fun recalculateMiddleSum() {
        sum = 0L
        val remainingElements = mutableListOf<Int>()

        // Middle elements in the deque
        for (num in deque) {
            if (!lowHeap.contains(num) && !highHeap.contains(num)) {
                sum += num
            }
        }
    }
}

fun main() {
    val obj = MKAverage(3, 1)
    obj.addElement(3)
    obj.addElement(1)
    obj.addElement(10)
    println(obj.calculateMKAverage())  // Output: 5
}


/**
 * Your MKAverage object will be instantiated and called as such:
 * var obj = MKAverage(m, k)
 * obj.addElement(num)
 * var param_2 = obj.calculateMKAverage()
 */
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

**Analysis:**

Each node and edge is visited at most once, giving O(n log k) for a graph with V vertices and E edges. The O(k) space stores visited tracking and the queue/stack.

---

## Find K Closest Elements

<span id="findkclosestelements"></span>

### Problem

**Findkclosestelements**

**Function:** `Find Closest Elements` takes `arr` (Array<integer>), `k` (integer), `x` (integer) and returns **List**.

**Key logic:**
- Remove the farthest element
- We could also do



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `priorityQueue`, `diffA`, `diffB`, `result`, `testClass`

**Execution flow:**
- Remove the farthest element
- We could also do

### Code

```kotlin
package heap

import java.util.PriorityQueue
import kotlin.math.abs

class FindKClosestElements {
    class FindKClosestElements {
        /**
         * Solving using Max Heap. O ( N log K + K log K )
         */
        fun findClosestElements(arr: Array<Int>, k: Int, x: Int): List<Int> {
            /**
             * If we create a Max heap returning ( logic(b)  - logic(a) )
             * and keep adding element and remove farthest element in each iteration once heap size goes > K
             * then we'll eliminate (n - k ). Remaining elements will be K closest elements.i.e n - (n-k) = K
             *
             *
             * example of logic function could be frequency count from map eucledian distances
             */
           val priorityQueue = PriorityQueue<Int> { a,b ->
               val diffA = abs(a - x)
               val diffB = abs(b - x)
               if (diffA == diffB) b - a else  diffB - diffA
           }
            arr.forEach { element ->
                priorityQueue.offer(element)
                // Remove the farthest element
                if (priorityQueue.size > k)
                    priorityQueue.poll()
            }
            val result = mutableListOf<Int>()

            repeat(k) {
                if (priorityQueue.isNotEmpty())
                    result.add(priorityQueue.poll())
            }

            return result
        }

        // We could also do

        companion object {
            @JvmStatic
            fun main(args: Array<String>) {
                val testClass = FindKClosestElements()

                println(testClass.findClosestElements(arrayOf(1,2,3,4,5,6,7), 4, 4 ))
            }
        }
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

## Find Score Of An Array After Marking All Elements

<span id="findscoreofanarrayaftermarkingallelements"></span>

### Problem

**Findscoreofanarrayaftermarkingallelements**

**Function:** `Find Score` takes `nums` (array of integers) and returns **Long**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `n`, `marked`, `minHeap`, `score`

### Code

```kotlin
package heap

import java.util.*

class FindScoreOfAnArrayAfterMarkingAllElements {
    fun findScore(nums: IntArray): Long {
        val n = nums.size
        val marked = BooleanArray(n) { false }

        val minHeap = PriorityQueue<Pair<Int, Int>> { a, b ->
            if (a.first == b.first) a.second - b.second else a.first - b.first
        }

        nums.forEachIndexed { index, value -> minHeap.add(Pair(value, index)) }

        var score = 0L

        while (minHeap.isNotEmpty()) {
            val (value, index) = minHeap.poll()

            if (marked[index]) continue

            score += value

            marked[index] = true
            if (index > 0) marked[index - 1] = true
            if (index < n - 1) marked[index + 1] = true
        }

        return score
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

## IPO

<span id="ipo"></span>

### Problem

**Ipo**

**Function:** `Find Maximized Capital` takes `k` (integer), `w` (integer), `profits` (array of integers), `capital` (array of integers) and returns **integer**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `capital`, `profit`, `projects`, `maxHeap`, `currentCapital`, `i`

### Code

```kotlin
package heap

import java.util.*

class IPO {
    data class Project(val capital: Int, val profit: Int)

    fun findMaximizedCapital(k: Int, w: Int, profits: IntArray, capital: IntArray): Int {
        val projects = capital.indices
            .map { Project(capital[it], profits[it]) }
            .sortedBy { it.capital }

        val maxHeap = PriorityQueue<Int>(compareByDescending { it })

        var currentCapital = w
        var i = 0

        repeat(k) {
            while (i < projects.size && projects[i].capital <= currentCapital)
                maxHeap.offer(projects[i++].profit)

            maxHeap.poll()?.let { currentCapital += it } ?: return currentCapital
        }

        return currentCapital
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

## Longest Happy String

<span id="longesthappystring"></span>

### Problem

**Longesthappystring**

**Function:** `Longest Diverse String` takes `a` (integer), `b` (integer), `c` (integer) and returns **string**.

**Key logic:**
- Use a priority queue to always get the character with highest remaining count
- Add non-zero counts to the queue
- Build the result
- Get the character with highest remaining count
- If we already have two consecutive of the same character,



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `pq`, `lastChar`, `lastCount`

**Execution flow:**
- Use a priority queue to always get the character with highest remaining count
- Add non-zero counts to the queue
- Build the result
- Get the character with highest remaining count
- If we already have two consecutive of the same character,
- we need to use the second highest count character
- Put the character back with reduced count
- Put the original highest character back

### Code

```kotlin
package heap

import java.util.*

class LongestHappyString {
    fun longestDiverseString(a: Int, b: Int, c: Int): String {
        // Use a priority queue to always get the character with highest remaining count
        val pq = PriorityQueue<Pair<Char, Int>> { p1, p2 -> p2.second - p1.second }

        // Add non-zero counts to the queue
        if (a > 0) pq.offer('a' to a)
        if (b > 0) pq.offer('b' to b)
        if (c > 0) pq.offer('c' to c)

        // Build the result
        return buildString {
            var lastChar = ' '
            var lastCount = 0

            while (pq.isNotEmpty()) {
                // Get the character with highest remaining count
                val (char, count) = pq.poll()

                // If we already have two consecutive of the same character,
                // we need to use the second highest count character
                if (lastChar == char && lastCount == 2) {
                    if (pq.isEmpty()) break

                    val (nextChar, nextCount) = pq.poll()
                    append(nextChar)

                    // Put the character back with reduced count
                    if (nextCount > 1) {
                        pq.offer(nextChar to nextCount - 1)
                    }

                    // Put the original highest character back
                    pq.offer(char to count)

                    // Reset last tracking for the new character
                    lastChar = nextChar
                    lastCount = 1
                } else {
                    // Add the highest count character
                    append(char)

                    // Update last tracking
                    if (lastChar == char) {
                        lastCount++
                    } else {
                        lastChar = char
                        lastCount = 1
                    }

                    // Put the character back with reduced count
                    if (count > 1) {
                        pq.offer(char to count - 1)
                    }
                }
            }
        }
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

## Median From Running Stream

<span id="medianfromrunningstream"></span>

### Problem

**Medianfromrunningstream**

**Function:** `Find Median` takes none and returns **double**.

**Key logic:**
- Min-heap for the larger half
- Max-heap for the smaller half



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `minHeap`, `maxHeap`

**Execution flow:**
- Min-heap for the larger half
- Max-heap for the smaller half

### Code

```kotlin
package heap

import java.util.*
import kotlin.Comparator

class MedianFromRunningStream {
    private val minHeap = PriorityQueue<Int>() // Min-heap for the larger half
    private val maxHeap = PriorityQueue<Int>(compareBy() { -it }) // Max-heap for the smaller half


    fun addNum(num: Int) {
        minHeap.offer(num)
        maxHeap.offer(minHeap.poll())

        if (minHeap.size < maxHeap.size) {
            minHeap.offer(maxHeap.poll())
        }
    }

    fun findMedian(): Double {
        return if (minHeap.size > maxHeap.size) {
            minHeap.peek().toDouble()
        } else {
            (minHeap.peek() + maxHeap.peek()) / 2.0
        }
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

## Meeting Room_III

<span id="meetingroom_iii"></span>

### Problem

**Meetingroom Iii**

**Function:** `Most Booked` takes `n` (integer), `meetings` (Array<array of integers>) and returns **integer**.

**Key logic:**
- Sort meetings by start time
- Initialize available rooms
- Free up any rooms that are now available
- If a room is available, use it
- If all rooms are busy, use the one that will become available first



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `endTime`, `index`, `roomUsage`, `busyRooms`, `availableRooms`, `duration`, `room`, `earliestRoom`

**Execution flow:**
- Sort meetings by start time
- Initialize available rooms
- Free up any rooms that are now available
- If a room is available, use it
- If all rooms are busy, use the one that will become available first
- The new end time is the earliest available time plus the duration
- Find the room with maximum usage (if tied, return the smallest index)

### Code

```kotlin
package heap

import java.util.*

class MeetingRoom_III {
    data class Room(val endTime: Long, val index: Int)

    fun mostBooked(n: Int, meetings: Array<IntArray>): Int {
        // Sort meetings by start time
        meetings.sortWith(compareBy { it[0] })

        val roomUsage = IntArray(n)
        val busyRooms = PriorityQueue<Room>(compareBy({ it.endTime }, { it.index }))
        val availableRooms = PriorityQueue<Int>()

        // Initialize available rooms
        for (i in 0 until n) availableRooms.add(i)

        for ((start, end) in meetings.map { it[0].toLong() to it[1].toLong() }) {
            val duration = end - start

            // Free up any rooms that are now available
            while (busyRooms.isNotEmpty() && busyRooms.peek().endTime <= start) {
                availableRooms.add(busyRooms.poll().index)
            }

            if (availableRooms.isNotEmpty()) {
                // If a room is available, use it
                val room = availableRooms.poll()
                busyRooms.add(Room(start + duration, room))
                roomUsage[room]++
            } else {
                // If all rooms are busy, use the one that will become available first
                val earliestRoom = busyRooms.poll()
                // The new end time is the earliest available time plus the duration
                busyRooms.add(Room(earliestRoom.endTime + duration, earliestRoom.index))
                roomUsage[earliestRoom.index]++
            }
        }

        // Find the room with maximum usage (if tied, return the smallest index)
        var maxUsage = -1
        var result = -1

        for (i in 0 until n) {
            if (roomUsage[i] > maxUsage) {
                maxUsage = roomUsage[i]
                result = i
            }
        }

        return result
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

## Single Threaded CPU

<span id="singlethreadedcpu"></span>

### Problem

**Singlethreadedcpu**

**Function:** `Get Order` takes `tasks` (Array<array of integers>) and returns **array of integers**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `enqueueTime`, `processingTime`, `index`, `allTasks`, `pq`, `result`, `time`, `i`

### Code

```kotlin
package heap

import java.util.*

class SingleThreadedCPU {
    data class Task(val enqueueTime: Int, val processingTime: Int, val index: Int)

    fun getOrder(tasks: Array<IntArray>): IntArray {
        val allTasks = tasks.mapIndexed { i, (enq, proc) -> Task(enq, proc, i) }
            .sortedBy { it.enqueueTime }

        val pq = PriorityQueue(compareBy<Task> { it.processingTime }.thenBy { it.index })
        val result = mutableListOf<Int>()

        var time = 0
        var i = 0

        while (i < allTasks.size || pq.isNotEmpty()) {
            while (i < allTasks.size && allTasks[i].enqueueTime <= time) {
                pq.add(allTasks[i++])
            }

            if (pq.isNotEmpty()) {
                val task = pq.poll()
                time += task.processingTime
                result.add(task.index)
            } else {
                time = allTasks[i].enqueueTime
            }
        }

        return result.toIntArray()
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

## Sliding Window Median

<span id="slidingwindowmedian"></span>

### Problem

**Slidingwindowmedian**

**Function:** `Get Median` takes none and returns **double**.

**Key logic:**
- Min-heap for the larger half
- Max-heap for the smaller half
- TreeMap to track delayed removals



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `minHeap`, `maxHeap`, `delayedRemoval`, `result`

**Execution flow:**
- Min-heap for the larger half
- Max-heap for the smaller half
- TreeMap to track delayed removals

### Code

```kotlin
package heap

import java.util.*

class SlidingWindowMedian {
    private val minHeap = PriorityQueue<Double>() // Min-heap for the larger half
    private val maxHeap = PriorityQueue<Double> ( compareBy{-it} ) // Max-heap for the smaller half
    private val delayedRemoval = TreeMap<Double, Int>() // TreeMap to track delayed removals

    private fun balanceHeaps() {
        if (maxHeap.size > minHeap.size + 1) {
            minHeap.add(maxHeap.poll())
        } else if (minHeap.size > maxHeap.size) {
            maxHeap.add(minHeap.poll())
        }
    }

    private fun add(num: Int) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.add(num.toDouble())
        } else {
            minHeap.add(num.toDouble())
        }
        balanceHeaps()
    }

    private fun remove(num: Int) {
        if (num <= maxHeap.peek()) {
            maxHeap.remove(num.toDouble())
        } else {
            minHeap.remove(num.toDouble())
        }
        balanceHeaps()
    }

    private fun getMedian(): Double {
        return if (maxHeap.size == minHeap.size) {
            (maxHeap.peek().toDouble() + minHeap.peek().toDouble()) / 2.0
        } else {
            maxHeap.peek().toDouble()
        }
    }

    fun medianSlidingWindow(nums: IntArray, k: Int): DoubleArray {
        val result = DoubleArray(nums.size - k + 1)

        for (i in nums.indices) {
            add(nums[i])

            if (i >= k) {
                remove(nums[i - k])
            }

            if (i >= k - 1) {
                result[i - k + 1] = getMedian()
            }
        }

        return result
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

## Top K Frequent Elements

<span id="topkfrequentelements"></span>

### Problem

**Topkfrequentelements**

**Function:** `Top Kfrequent` takes `nums` (array of integers), `k` (integer) and returns **array of integers**.

**Key logic:**
- Randomized Quick Partition...
- Swap pivot with the end
- Swap back the pivot to the correct position



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `map`, `uniqueNums`, `start`, `end`, `partitionIndex`, `randomIndex`, `pivot`, `partitionIndex`

**Execution flow:**
- Randomized Quick Partition...
- Swap pivot with the end
- Swap back the pivot to the correct position

### Code

```kotlin
package quicksort

import oracle.net.aso.k
import kotlin.random.Random

class TopKFrequentElements {
    private val map = HashMap<Int, Int>()

    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        nums.forEach { map[it] = map.getOrPut(it) { 0 } + 1 }

        val uniqueNums = map.keys.toIntArray()
        var start = 0
        var end = uniqueNums.size - 1

        while (start < end) {
            val partitionIndex = partition(uniqueNums, start, end)
            when {
                partitionIndex < k - 1 -> start = partitionIndex + 1
                partitionIndex > k - 1 -> end = partitionIndex - 1
                else -> break
            }
        }

        return uniqueNums.copyOfRange(0, k)
    }

    // Randomized Quick Partition...
    private fun partition(nums: IntArray, start: Int, end: Int): Int {
        val randomIndex = Random.nextInt(start, end + 1)
        swap(nums, randomIndex, end)  // Swap pivot with the end
        val pivot = map[nums[end]] ?: 0

        var partitionIndex = start
        for (i in start until end) {
            if (map[nums[i]]!! >= pivot) {
                swap(nums, i, partitionIndex++)
            }
        }

        swap(nums, partitionIndex, end)  // Swap back the pivot to the correct position
        return partitionIndex
    }

    private fun swap(nums: IntArray, i: Int, j: Int) {
       nums[i] = nums[j].also { nums[i] = it }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Key Takeaways

1. **Core pattern recognition** — Heaps maintain the min/max of a dynamic set. Use min-heap for k largest, max-heap for k smallest, dual heaps for median.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

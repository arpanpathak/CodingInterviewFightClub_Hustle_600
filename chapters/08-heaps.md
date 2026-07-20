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

> **10 problems** — **Heaps/Priority Queues** maintain min/max of a dynamic set. Use min-heap for k-largest, max-heap for k-smallest, dual-heaps for median tracking.

## Complete Problem Set

| # | Problem |
|---|---------|
| 1 | [Dual Balanced Heap](#dualbalancedheap) |
| 2 | [MK Average](#findingmkaverage) |
| 3 | [Find K Closest Elements](#findkclosestelements) |
| 4 | [Find Score Of An Array After Marking All Elements](#findscoreofanarrayaftermarkingallelements) |
| 5 | [IPO](#ipo) |
| 6 | [Longest Happy String](#longesthappystring) |
| 7 | [Meeting Room_III](#meetingroom_iii) |
| 8 | [Single Threaded CPU](#singlethreadedcpu) |
| 9 | [Sliding Window Median](#slidingwindowmedian) |
| 10 | [Top K Frequent Elements](#topkfrequentelements) |

---

## Dual Balanced Heap

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package heap

import java.util.*

class DualBalancedHeap<T : Comparable<T>> {
    private val minHeap = PriorityQueue<T>() // Min-heap for the larger half
    private val maxHeap = PriorityQueue<T>(compareByDescending { it }) // Max-heap for the smaller half

/**
 * balance Heaps — executes the core logic of this algorithm on the provided input.
 *
 * @return Unit (nothing) — this function operates via side effects
 */
    private fun balanceHeaps() {
        if (maxHeap.size > minHeap.size + 1) {
            minHeap.add(maxHeap.poll())
        } else if (minHeap.size > maxHeap.size) {
            maxHeap.add(minHeap.poll())
        }
    }

/**
 * Inserts the specified element into the data structure.
 *
 * @param num the num parameter — a input parameter of type T used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
    fun add(num: T) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.add(num)
        } else {
            minHeap.add(num)
        }
        balanceHeaps()
    }

/**
 * Removes specified elements from the collection and returns the result.
 *
 * @param num the num parameter — a input parameter of type T used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
    fun remove(num: T) {
        if (maxHeap.contains(num)) {
            maxHeap.remove(num)
        } else {
            minHeap.remove(num)
        }
        balanceHeaps()
    }

/**
 * Retrieves and returns the requested element or value from the data structure.
 *
 * @return the computed result of type T?
 */
    fun getMedian(): T? {
        return if (maxHeap.size == minHeap.size) {
            // Handling generic types requires a custom approach for averaging or choosing one of the elements.
            maxHeap.peek()
        // Simplification: you may need to define how to combine two elements for real applications.
        } else {
            maxHeap.peek()
        }
    }

/**
 * size — executes the core logic of this algorithm on the provided input.
 *
 * @return the total count/number of matching elements
 */
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

---

## MK Average

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package heap

import java.util.*

class MKAverage(private val m: Int, private val k: Int) {
    private val deque = LinkedList<Int>()
    private val lowHeap = PriorityQueue<Int>(compareByDescending { it }) // max heap (for k smallest elements)
    private val highHeap = PriorityQueue<Int>() // min heap (for k largest elements)
    private var sum = 0L // Sum of the middle elements

/**
 * Inserts the specified element into the data structure.
 *
 * @param num the num parameter — a integer value used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
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

/**
 * Performs the core computation/algorithm and returns the result.
 *
 * @return the computed integer result
 */
    fun calculateMKAverage(): Int {
        return if (deque.size < m) {
            -1
        } else {
            val middleCount = m - 2 * k
            (sum / middleCount).toInt()
        }
    }

    // Balance heaps to ensure there are k elements in each of the heaps

/**
 * balance Heaps — executes the core logic of this algorithm on the provided input.
 *
 * @return Unit (nothing) — this function operates via side effects
 */
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

/**
 * Performs the core computation/algorithm and returns the result.
 *
 * @return Unit (nothing) — this function operates via side effects
 */
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

/**
 * main — executes the core logic of this algorithm on the provided input.
 *
 * @return Unit (nothing) — this function operates via side effects
 */
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

---

## Find K Closest Elements

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

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

/**
 * main — executes the core logic of this algorithm on the provided input.
 *
 * @param args the args parameter — a array of elements used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
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
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Find Score Of An Array After Marking All Elements

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package heap

import java.util.*

class FindScoreOfAnArrayAfterMarkingAllElements {

/**
 * Searches for and returns the target element/position using an efficient algorithm.
 *
 * @param nums the input array of numbers to process
 * @return the computed result of type Long
 */
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

---

## IPO

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package heap

import java.util.*

class IPO {
    data class Project(val capital: Int, val profit: Int)

/**
 * Searches for and returns the target element/position using an efficient algorithm.
 *
 * @param k the number of elements/operations to consider (k parameter)
 * @param w the w parameter — a integer value used in the computation
 * @param profits the profits parameter — a array of integers used in the computation
 * @param capital the capital parameter — a array of integers used in the computation
 * @return the maximum value found in the input
 */
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Longest Happy String

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package heap

import java.util.*

class LongestHappyString {

/**
 * longest Diverse String — executes the core logic of this algorithm on the provided input.
 *
 * @param a the first input array for comparison/merging
 * @param b the second input array for comparison/merging
 * @param c the c parameter — a integer value used in the computation
 * @return the computed string result
 */
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

---

## Meeting Room_III

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package heap

import java.util.*

class MeetingRoom_III {
    data class Room(val endTime: Long, val index: Int)

/**
 * most Booked — executes the core logic of this algorithm on the provided input.
 *
 * @param n the size/dimension parameter for the algorithm
 * @param meetings the meetings parameter — a array of integers used in the computation
 * @return the computed integer result
 */
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

---

## Single Threaded CPU

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package heap

import java.util.*

class SingleThreadedCPU {
    data class Task(val enqueueTime: Int, val processingTime: Int, val index: Int)

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param tasks the tasks parameter — a array of integers used in the computation
 * @return the sorted/reordered list of elements
 */
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

---

## Sliding Window Median

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package heap

import java.util.*

class SlidingWindowMedian {
    private val minHeap = PriorityQueue<Double>() // Min-heap for the larger half
    private val maxHeap = PriorityQueue<Double> ( compareBy{-it} ) // Max-heap for the smaller half
    private val delayedRemoval = TreeMap<Double, Int>() // TreeMap to track delayed removals

/**
 * balance Heaps — executes the core logic of this algorithm on the provided input.
 *
 * @return Unit (nothing) — this function operates via side effects
 */
    private fun balanceHeaps() {
        if (maxHeap.size > minHeap.size + 1) {
            minHeap.add(maxHeap.poll())
        } else if (minHeap.size > maxHeap.size) {
            maxHeap.add(minHeap.poll())
        }
    }

/**
 * Inserts the specified element into the data structure.
 *
 * @param num the num parameter — a integer value used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
    private fun add(num: Int) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.add(num.toDouble())
        } else {
            minHeap.add(num.toDouble())
        }
        balanceHeaps()
    }

/**
 * Removes specified elements from the collection and returns the result.
 *
 * @param num the num parameter — a integer value used in the computation
 * @return Unit (nothing) — this function operates via side effects
 */
    private fun remove(num: Int) {
        if (num <= maxHeap.peek()) {
            maxHeap.remove(num.toDouble())
        } else {
            minHeap.remove(num.toDouble())
        }
        balanceHeaps()
    }

/**
 * Retrieves and returns the requested element or value from the data structure.
 *
 * @return the computed result of type Double
 */
    private fun getMedian(): Double {
        return if (maxHeap.size == minHeap.size) {
            (maxHeap.peek().toDouble() + minHeap.peek().toDouble()) / 2.0
        } else {
            maxHeap.peek().toDouble()
        }
    }

/**
 * median Sliding Window — executes the core logic of this algorithm on the provided input.
 *
 * @param nums the input array of numbers to process
 * @param k the number of elements/operations to consider (k parameter)
 * @return a list/collection of result elements
 */
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

---

## Top K Frequent Elements

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package quicksort

import oracle.net.aso.k
import kotlin.random.Random

class TopKFrequentElements {
    private val map = HashMap<Int, Int>()

/**
 * Converts/transforms the input from one representation to another.
 *
 * @param nums the input array of numbers to process
 * @param k the number of elements/operations to consider (k parameter)
 * @return a list/collection of result elements
 */
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

/**
 * partition — executes the core logic of this algorithm on the provided input.
 *
 * @param nums the input array of numbers to process
 * @param start the left/starting boundary of the search range (inclusive)
 * @param end the right/ending boundary of the search range (inclusive)
 * @return the computed integer result
 */
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

/**
 * swap — executes the core logic of this algorithm on the provided input.
 *
 * @param nums the input array of numbers to process
 * @param i the index position in the collection
 * @param j the index position in the collection
 * @return Unit (nothing) — this function operates via side effects
 */
    private fun swap(nums: IntArray, i: Int, j: Int) {
       nums[i] = nums[j].also { nums[i] = it }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

---

## Key Takeaways

1. **Core pattern recognition** — Identify the problem type and apply the right algorithmic technique.
2. **Practice systematically** — Work through each problem to internalize the patterns.
3. **Understand why, not just how** — Focus on the reasoning behind each solution.

---

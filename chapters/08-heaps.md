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

> **11 problems**

## The Pattern

_Each problem below includes: Problem, Example, Why This Approach, Code, Pattern Insight, Complexity, and Variations._

## Problems

1. [Dual Balanced Heap](#dualbalancedheap)
2. [MK Average](#findingmkaverage)
3. [Find K Closest Elements](#findkclosestelements)
4. [Find Score Of An Array After Marking All Elements](#findscoreofanarrayaftermarkingallelements)
5. [IPO](#ipo)
6. [Longest Happy String](#longesthappystring)
7. [Median From Running Stream](#medianfromrunningstream)
8. [Meeting Room_III](#meetingroom_iii)
9. [Single Threaded CPU](#singlethreadedcpu)
10. [Sliding Window Median](#slidingwindowmedian)
11. [Top K Frequent Elements](#topkfrequentelements)

---

## Dual Balanced Heap

### Problem

Given `num` (T), compute the computed result efficiently.

**Example:**

```
Input: num = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses a **heap/priority queue** to maintain a dynamic ordering of elements. Heaps provide O(log n) insertion and O(1) access to the min or max element, making them ideal for streaming/online algorithms and k-th order statistics.

### Code

```kotlin
package heap

import java.util.*

class DualBalancedHeap<T : Comparable<T>> {
    private val minHeap = PriorityQueue<T>() // Min-heap for the larger half
    private val maxHeap = PriorityQueue<T>(compareByDescending { it }) // Max-heap for the smaller half

    /**
    * Helper: balance heaps.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: balance heaps.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: balance heaps.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: balance heaps.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    private fun balanceHeaps() {
        if (maxHeap.size > minHeap.size + 1) {
            minHeap.add(maxHeap.poll())
        } else if (minHeap.size > maxHeap.size) {
            maxHeap.add(minHeap.poll())
        }
    }

    /**
    * Solves the Dual Balanced Heap problem.
    * Takes `num` (T).
    *
    * @param num The T.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Dual Balanced Heap problem.
    * Takes `num` (T).
    *
    * @param num The T.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Dual Balanced Heap problem.
    * Takes `num` (T).
    *
    * @param num The T.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Dual Balanced Heap problem.
    * Takes `num` (T).
    *
    * @param num The T.
    * @return Unit (no return value, modifies state in-place).
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
    * Solves the Dual Balanced Heap problem.
    * Takes `num` (T).
    *
    * @param num The T.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Dual Balanced Heap problem.
    * Takes `num` (T).
    *
    * @param num The T.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Dual Balanced Heap problem.
    * Takes `num` (T).
    *
    * @param num The T.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Dual Balanced Heap problem.
    * Takes `num` (T).
    *
    * @param num The T.
    * @return Unit (no return value, modifies state in-place).
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
    * Solves the Dual Balanced Heap problem.
    *
    * @return The result, or `null` if not found.
    */
    /**
    * Solves the Dual Balanced Heap problem.
    *
    * @return The result, or `null` if not found.
    */
    /**
    * Solves the Dual Balanced Heap problem.
    *
    * @return The result, or `null` if not found.
    */
    /**
    * Solves the Dual Balanced Heap problem.
    *
    * @return The result, or `null` if not found.
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
    * Solves the Dual Balanced Heap problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the Dual Balanced Heap problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the Dual Balanced Heap problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the Dual Balanced Heap problem.
    *
    * @return The computed integer result.
    */
    fun size(): Int {
        return maxHeap.size + minHeap.size
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

## MK Average

### Problem

Given `num` (integer), compute the computed result efficiently.

**Example:**

```
Input: num = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

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
    * Solves the MKAverage problem.
    * Takes `num` (integer).
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the MKAverage problem.
    * Takes `num` (integer).
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the MKAverage problem.
    * Takes `num` (integer).
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the MKAverage problem.
    * Takes `num` (integer).
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
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
    * Solves the MKAverage problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the MKAverage problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the MKAverage problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the MKAverage problem.
    *
    * @return The computed integer result.
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
    * Helper: balance heaps.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: balance heaps.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: balance heaps.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: balance heaps.
    *
    * @return Unit (no return value, modifies state in-place).
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
    * Helper: recalculate middle sum.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: recalculate middle sum.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: recalculate middle sum.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: recalculate middle sum.
    *
    * @return Unit (no return value, modifies state in-place).
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

## Find K Closest Elements

### Problem

Given `arr` (Array<Int>), `k` (integer), `x` (integer), `args` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: arr = input_value, k = 5, x = 5, args = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

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
                val testClass = FindKClosestElements()

                println(testClass.findClosestElements(arrayOf(1,2,3,4,5,6,7), 4, 4 ))
            }
        }
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

## Find Score Of An Array After Marking All Elements

### Problem

Given `nums` (array of integers), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

### Code

```kotlin
package heap

import java.util.*

class FindScoreOfAnArrayAfterMarkingAllElements {
    /**
    * Solves the Find Score Of An Array After Marking All Elements problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Score Of An Array After Marking All Elements problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Score Of An Array After Marking All Elements problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Score Of An Array After Marking All Elements problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
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

## IPO

### Problem

Given `k` (integer), `w` (integer), `profits` (array of integers), `capital` (array of integers), compute the computed result efficiently.

**Example:**

```
Input: k = 5, w = 5, profits = [1, 2, 3, 4, 5], capital = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package heap

import java.util.*

class IPO {
    data class Project(val capital: Int, val profit: Int)

    /**
    * Solves the IPO problem.
    * Takes `k` (integer), `w` (integer), `profits` (array of integers), `capital` (array of integers).
    *
    * @param k The integer parameter representing k.
    * @param w The integer parameter representing w.
    * @param profits The input array of integers.
    * @param capital The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the IPO problem.
    * Takes `k` (integer), `w` (integer), `profits` (array of integers), `capital` (array of integers).
    *
    * @param k The integer parameter representing k.
    * @param w The integer parameter representing w.
    * @param profits The input array of integers.
    * @param capital The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the IPO problem.
    * Takes `k` (integer), `w` (integer), `profits` (array of integers), `capital` (array of integers).
    *
    * @param k The integer parameter representing k.
    * @param w The integer parameter representing w.
    * @param profits The input array of integers.
    * @param capital The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the IPO problem.
    * Takes `k` (integer), `w` (integer), `profits` (array of integers), `capital` (array of integers).
    *
    * @param k The integer parameter representing k.
    * @param w The integer parameter representing w.
    * @param profits The input array of integers.
    * @param capital The input array of integers.
    * @return The computed integer result.
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

## Longest Happy String

### Problem

Given `a` (integer), `b` (integer), `c` (integer), compute the computed result efficiently.

**Example:**

```
Input: a = 5, b = 5, c = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package heap

import java.util.*

class LongestHappyString {
    /**
    * Solves the Longest Happy String problem.
    * Takes `a` (integer), `b` (integer), `c` (integer).
    *
    * @param a The integer parameter representing a.
    * @param b The integer parameter representing b.
    * @param c The integer parameter representing c.
    * @return The resulting string.
    */
    /**
    * Solves the Longest Happy String problem.
    * Takes `a` (integer), `b` (integer), `c` (integer).
    *
    * @param a The integer parameter representing a.
    * @param b The integer parameter representing b.
    * @param c The integer parameter representing c.
    * @return The resulting string.
    */
    /**
    * Solves the Longest Happy String problem.
    * Takes `a` (integer), `b` (integer), `c` (integer).
    *
    * @param a The integer parameter representing a.
    * @param b The integer parameter representing b.
    * @param c The integer parameter representing c.
    * @return The resulting string.
    */
    /**
    * Solves the Longest Happy String problem.
    * Takes `a` (integer), `b` (integer), `c` (integer).
    *
    * @param a The integer parameter representing a.
    * @param b The integer parameter representing b.
    * @param c The integer parameter representing c.
    * @return The resulting string.
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

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Median From Running Stream

### Problem

Given `num` (integer), compute the computed result efficiently.

**Example:**

```
Input: num = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses a **heap/priority queue** to maintain a dynamic ordering of elements. Heaps provide O(log n) insertion and O(1) access to the min or max element, making them ideal for streaming/online algorithms and k-th order statistics.

### Code

```kotlin
package heap

import java.util.*
import kotlin.Comparator

class MedianFromRunningStream {
    private val minHeap = PriorityQueue<Int>() // Min-heap for the larger half
    private val maxHeap = PriorityQueue<Int>(compareBy() { -it }) // Max-heap for the smaller half


    /**
    * Solves the Median From Running Stream problem.
    * Takes `num` (integer).
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Median From Running Stream problem.
    * Takes `num` (integer).
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Median From Running Stream problem.
    * Takes `num` (integer).
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Median From Running Stream problem.
    * Takes `num` (integer).
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    fun addNum(num: Int) {
        minHeap.offer(num)
        maxHeap.offer(minHeap.poll())

        if (minHeap.size < maxHeap.size) {
            minHeap.offer(maxHeap.poll())
        }
    }

    /**
    * Solves the Median From Running Stream problem.
    *
    * @return The computed floating-point result.
    */
    /**
    * Solves the Median From Running Stream problem.
    *
    * @return The computed floating-point result.
    */
    /**
    * Solves the Median From Running Stream problem.
    *
    * @return The computed floating-point result.
    */
    /**
    * Solves the Median From Running Stream problem.
    *
    * @return The computed floating-point result.
    */
    fun findMedian(): Double {
        return if (minHeap.size > maxHeap.size) {
            minHeap.peek().toDouble()
        } else {
            (minHeap.peek() + maxHeap.peek()) / 2.0
        }
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Meeting Room_III

### Problem

Given `n` (integer), `meetings` (2D matrix), compute the computed result efficiently.

**Example:**

```
Input: n = 5, meetings = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package heap

import java.util.*

class MeetingRoom_III {
    data class Room(val endTime: Long, val index: Int)

    /**
    * Solves the Meeting Room_III problem.
    * Takes `n` (integer), `meetings` (2D matrix of integers).
    *
    * @param n The integer parameter representing n.
    * @param meetings The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Meeting Room_III problem.
    * Takes `n` (integer), `meetings` (2D matrix of integers).
    *
    * @param n The integer parameter representing n.
    * @param meetings The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Meeting Room_III problem.
    * Takes `n` (integer), `meetings` (2D matrix of integers).
    *
    * @param n The integer parameter representing n.
    * @param meetings The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Meeting Room_III problem.
    * Takes `n` (integer), `meetings` (2D matrix of integers).
    *
    * @param n The integer parameter representing n.
    * @param meetings The input 2D matrix of integers.
    * @return The computed integer result.
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

## Single Threaded CPU

### Problem

Given `tasks` (2D matrix), compute the computed result efficiently.

**Example:**

```
Input: tasks = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package heap

import java.util.*

class SingleThreadedCPU {
    data class Task(val enqueueTime: Int, val processingTime: Int, val index: Int)

    /**
    * Solves the Single Threaded CPU problem.
    * Takes `tasks` (2D matrix of integers).
    *
    * @param tasks The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Single Threaded CPU problem.
    * Takes `tasks` (2D matrix of integers).
    *
    * @param tasks The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Single Threaded CPU problem.
    * Takes `tasks` (2D matrix of integers).
    *
    * @param tasks The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Single Threaded CPU problem.
    * Takes `tasks` (2D matrix of integers).
    *
    * @param tasks The input 2D matrix of integers.
    * @return The computed integer result.
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

## Sliding Window Median

### Problem

Given `num` (integer), `nums` (array of integers), `k` (integer), compute the computed result efficiently.

**Example:**

```
Input: num = 5, nums = [1, 2, 3, 4, 5], k = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses a **heap/priority queue** to maintain a dynamic ordering of elements. Heaps provide O(log n) insertion and O(1) access to the min or max element, making them ideal for streaming/online algorithms and k-th order statistics.

### Code

```kotlin
package heap

import java.util.*

class SlidingWindowMedian {
    private val minHeap = PriorityQueue<Double>() // Min-heap for the larger half
    private val maxHeap = PriorityQueue<Double> ( compareBy{-it} ) // Max-heap for the smaller half
    private val delayedRemoval = TreeMap<Double, Int>() // TreeMap to track delayed removals

    /**
    * Helper: balance heaps.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: balance heaps.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: balance heaps.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: balance heaps.
    *
    * @return Unit (no return value, modifies state in-place).
    */
    private fun balanceHeaps() {
        if (maxHeap.size > minHeap.size + 1) {
            minHeap.add(maxHeap.poll())
        } else if (minHeap.size > maxHeap.size) {
            maxHeap.add(minHeap.poll())
        }
    }

    /**
    * Helper: add.
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: add.
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: add.
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: add.
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
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
    * Helper: remove.
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: remove.
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: remove.
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: remove.
    *
    * @param num The integer parameter representing num.
    * @return Unit (no return value, modifies state in-place).
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
    * Helper: get median.
    *
    * @return The computed floating-point result.
    */
    /**
    * Helper: get median.
    *
    * @return The computed floating-point result.
    */
    /**
    * Helper: get median.
    *
    * @return The computed floating-point result.
    */
    /**
    * Helper: get median.
    *
    * @return The computed floating-point result.
    */
    private fun getMedian(): Double {
        return if (maxHeap.size == minHeap.size) {
            (maxHeap.peek().toDouble() + minHeap.peek().toDouble()) / 2.0
        } else {
            maxHeap.peek().toDouble()
        }
    }

    /**
    * Solves the Sliding Window Median problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed floating-point result.
    */
    /**
    * Solves the Sliding Window Median problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed floating-point result.
    */
    /**
    * Solves the Sliding Window Median problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed floating-point result.
    */
    /**
    * Solves the Sliding Window Median problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed floating-point result.
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

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Top K Frequent Elements

### Problem

Given `nums` (array of integers), `k` (integer), `start` (integer), `end` (integer), `i` (integer), `j` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], k = 5, start = 5, end = 5, i = 5, j = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package quicksort

import oracle.net.aso.k
import kotlin.random.Random

class TopKFrequentElements {
    private val map = HashMap<Int, Int>()

    /**
    * Solves the Top KFrequent Elements problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Top KFrequent Elements problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Top KFrequent Elements problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Top KFrequent Elements problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
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
    * Helper: partition.
    *
    * @param nums The input array of integers.
    * @param start The integer parameter representing start.
    * @param end The integer parameter representing end.
    * @return The computed integer result.
    */
    /**
    * Helper: partition.
    *
    * @param nums The input array of integers.
    * @param start The integer parameter representing start.
    * @param end The integer parameter representing end.
    * @return The computed integer result.
    */
    /**
    * Helper: partition.
    *
    * @param nums The input array of integers.
    * @param start The integer parameter representing start.
    * @param end The integer parameter representing end.
    * @return The computed integer result.
    */
    /**
    * Helper: partition.
    *
    * @param nums The input array of integers.
    * @param start The integer parameter representing start.
    * @param end The integer parameter representing end.
    * @return The computed integer result.
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
    * Helper: swap.
    *
    * @param nums The input array of integers.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: swap.
    *
    * @param nums The input array of integers.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: swap.
    *
    * @param nums The input array of integers.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: swap.
    *
    * @param nums The input array of integers.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    private fun swap(nums: IntArray, i: Int, j: Int) {
       nums[i] = nums[j].also { nums[i] = it }
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

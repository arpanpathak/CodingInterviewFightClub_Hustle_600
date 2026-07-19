---
layout: chapter
title: "Binary Search"
chapter_number: 1
chapter_title: "Binary Search"
toc: true
next_chapter:
  url: "/chapters/02-dynamic-programming.html"
  title: "Dynamic Programming"
---

# Binary Search

> **21 problems** — Master the art of divide-and-conquer searching. Binary search finds elements in sorted arrays in O(log n) time.

## The Pattern

Sorted array + search → Binary Search. The key insight: find a predicate that splits the search space into 'yes' and 'no', then binary search finds the transition point.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [Apartmenthunting](#apartmenthunting) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Capacity To Ship Package Within D Days](#capacitytoshippackagewithinddays) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Closest Sebsequence Sum](#closestsebsequencesum) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Find First And Last Position](#findfirstandlastposition) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [Find K Closest Elements](#findkclosestelements) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Find Minimum In Rotated Sorted Array](#findminimuminrotatedsortedarray) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [Find Peak Element](#findpeakelement) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [Find Peak Element Better Solution](#findpeakelementbettersolution) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Version Control](#firstbadversion) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Solution](#guessnumberhigherorlower) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [House Robber_IV](#houserobber_iv) | — | <span class="badge badge-medium">Medium</span> |
| 12 | [K Th Missing Positive Number](#kthmissingpositivenumber) | — | <span class="badge badge-medium">Medium</span> |
| 13 | [Koko Eating Banana](#kokoeatingbanana) | — | <span class="badge badge-medium">Medium</span> |
| 14 | [Median Of Two Sorted A Rrays](#medianoftwosortedarrays) | — | <span class="badge badge-medium">Medium</span> |
| 15 | [Random Pick With Weight](#randompickwithweight) | — | <span class="badge badge-medium">Medium</span> |
| 16 | [Search A2d Matrix](#searcha2dmatrix) | — | <span class="badge badge-medium">Medium</span> |
| 17 | [Search In Rotated Array_II](#searchinrotatedarray_ii) | — | <span class="badge badge-medium">Medium</span> |
| 18 | [Search In Rotated Sorted Array](#searchinrotatedsortedarray) | — | <span class="badge badge-medium">Medium</span> |
| 19 | [Search Insertion Position](#searchinsertionposition) | — | <span class="badge badge-medium">Medium</span> |
| 20 | [Single Element In A Sorted Array](#singleelementinasortedarray) | — | <span class="badge badge-medium">Medium</span> |
| 21 | [Valley Element](#valleyelement) | — | <span class="badge badge-medium">Medium</span> |

---

## Apartmenthunting

<span id="apartmenthunting"></span>

### Problem

**Apartmenthunting**

**Function:** `Find Best Block` takes `blocks` (List<Map<string), `Boolean>>` (?), `requirements` (List<string>) and returns **integer**.

**Key logic:**
- Step 1: Create a HashMap where each key is an amenity and each value is a sorted list of blocks where the amenity is present
- Ensure all required amenities are present
- Return -1 if any required amenity is not present in any block
- Step 2: Determine the optimal block
- N * R * Log(K) , K = number of unique amininties present across all the blocks



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `amenityMap`, `bestBlock`, `bestMaxDistance`, `maxDistance`, `pos`, `insertPoint`, `leftDistance`, `rightDistance`

**Execution flow:**
- Step 1: Create a HashMap where each key is an amenity and each value is a sorted list of blocks where the amenity is present
- Ensure all required amenities are present
- Return -1 if any required amenity is not present in any block
- Step 2: Determine the optimal block
- N * R * Log(K) , K = number of unique amininties present across all the blocks
- Check if the current block has the smallest maximum distance
- Function to find the minimum distance to the closest block with the given amenity
- Custom Binary Search implementation

### Code

```kotlin
package binarysearch

fun findBestBlock(blocks: List<Map<String, Boolean>>, requirements: List<String>): Int {
    // Step 1: Create a HashMap where each key is an amenity and each value is a sorted list of blocks where the amenity is present
    val amenityMap = mutableMapOf<String, MutableList<Int>>()
    blocks.forEachIndexed { index, block ->
        block.forEach { (amenity, present) ->
            if (present) {
                amenityMap.getOrPut(amenity) { mutableListOf() }.add(index)
            }
        }
    }

    // Ensure all required amenities are present
    requirements.forEach {
        if (amenityMap[it].isNullOrEmpty()) return -1 // Return -1 if any required amenity is not present in any block
    }

    // Step 2: Determine the optimal block
    var bestBlock = -1
    var bestMaxDistance = Int.MAX_VALUE

    // N * R * Log(K) , K = number of unique amininties present across all the blocks
    blocks.forEachIndexed { index, _ ->
        val maxDistance = requirements.map { amenity ->
            closestDistance(index, amenityMap[amenity]!!)
        }.maxOrNull()!!

        // Check if the current block has the smallest maximum distance
        if (maxDistance < bestMaxDistance) {
            bestMaxDistance = maxDistance
            bestBlock = index
        }
    }

    return bestBlock
}

// Function to find the minimum distance to the closest block with the given amenity
fun closestDistance(blockIndex: Int, blocksWithAmenity: List<Int>): Int {
    val pos = blocksWithAmenity.binarySearch(blockIndex)
    return if (pos >= 0) 0
    else {
        val insertPoint = -pos - 1
        val leftDistance = if (insertPoint > 0) blockIndex - blocksWithAmenity[insertPoint - 1] else Int.MAX_VALUE
        val rightDistance = if (insertPoint < blocksWithAmenity.size) blocksWithAmenity[insertPoint] - blockIndex else Int.MAX_VALUE
        minOf(leftDistance, rightDistance)
    }
}

// Custom Binary Search implementation
fun binarySearch(arr: List<Int>, target: Int): Int {
    var (low, high) = listOf(0, arr.lastIndex)

    while (low<= high) {
        val mid = low + (high - low) / 2
        when {
            arr[mid] < target -> low = mid + 1
            arr[mid] > target -> high = mid - 1
            else -> return mid
        }
    }

    return -(low + 1)
}



fun main() {
    val blocks = listOf(
        mapOf("gym" to false, "school" to true, "store" to false),
        mapOf("gym" to true, "school" to false, "store" to false),
        mapOf("gym" to true, "school" to true, "store" to false),
        mapOf("gym" to false, "school" to true, "store" to false),
        mapOf("gym" to false, "school" to true, "store" to true)
    )
    val requirements = listOf("gym", "school", "store")


    val bestBlock = findBestBlock(blocks, requirements)
    println("The best block to choose is: $bestBlock")
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

## Capacity To Ship Package Within D Days

<span id="capacitytoshippackagewithinddays"></span>

### Problem

**Capacitytoshippackagewithinddays**

**Function:** `Feasible` takes `weights` (array of integers), `mid` (integer), `days` (integer) and returns **boolean**.



### Approach

**Solution Approach:**
1. The main function `feasible` processes the input
2. Uses helper functions: shipWithinDays

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`

### Code

```kotlin
package binarysearch

class CapacityToShipPackageWithinDDays {
    fun feasible(weights: IntArray, mid:Int, days: Int): Boolean {
        var (daysNeeded, currentLoad) = 1 to 0
        weights.forEach { weight ->
            currentLoad += weight
            if (currentLoad > mid) {
                daysNeeded++
                currentLoad = weight
            }
        }

        return daysNeeded <= days
    }

    fun shipWithinDays(weights: IntArray, days: Int): Int {
        var (sum, max) = 0 to 0

        weights.forEach{ weight ->
            sum += weight
            max = maxOf(max, weight)
        }

        var (l, r) = max to sum

        while ( l < r) {
            val mid = l + (r - l) / 2
            when {
                feasible(weights, mid, days) -> r = mid
                else -> l = mid + 1
            }
        }

        return l
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

## Closest Sebsequence Sum

<span id="closestsebsequencesum"></span>

### Problem

**Closestsebsequencesum**

**Function:** `Min Abs Difference` takes `nums` (array of integers), `goal` (integer) and returns **integer**.

**Key logic:**
- exclude
- include
- exact match found



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `leftSums`, `rightSums`, `n`, `mid`, `minDiff`, `target`, `idx`, `insertPoint`

**Execution flow:**
- exact match found

### Code

```kotlin
package binarysearch

import kotlin.math.abs

class ClosestSebsequenceSum {
    fun minAbsDifference(nums: IntArray, goal: Int): Int {
        val leftSums = mutableListOf<Int>()
        val rightSums = mutableListOf<Int>()
        val n = nums.size
        val mid = n / 2

        fun dfs(start: Int, end: Int, currentSum: Int, result: MutableList<Int>) {
            if (start == end) {
                result.add(currentSum)
                return
            }
            dfs(start + 1, end, currentSum, result) // exclude
            dfs(start + 1, end, currentSum + nums[start], result) // include
        }

        dfs(0, mid, 0, leftSums)
        dfs(mid, n, 0, rightSums)

        rightSums.sort()
        var minDiff = Int.MAX_VALUE

        for (sumLeft in leftSums) {
            val target = goal - sumLeft
            val idx = rightSums.binarySearch(target)
            if (idx >= 0) return 0 // exact match found

            val insertPoint = -idx - 1
            if (insertPoint < rightSums.size)
                minDiff = minOf(minDiff, abs(sumLeft + rightSums[insertPoint] - goal))
            if (insertPoint > 0)
                minDiff = minOf(minDiff, abs(sumLeft + rightSums[insertPoint - 1] - goal))
        }

        return minDiff
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

## Find First And Last Position

<span id="findfirstandlastposition"></span>

### Problem

**Findfirstandlastposition**

**Function:** `Search Range` takes `nums` (array of integers), `target` (integer) and returns **array of integers**.

**Key logic:**
- Find the first occurrence
- If the first occurrence is not found, return [-1, -1]
- Find the last occurrence
- Adjust the search range based on whether we are looking for the first or last occurrence
- Move left to find the first occurrence



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `left`, `right`, `result`, `mid`

**Execution flow:**
- Find the first occurrence
- If the first occurrence is not found, return [-1, -1]
- Find the last occurrence
- Adjust the search range based on whether we are looking for the first or last occurrence
- Move left to find the first occurrence
- Move right to find the last occurrence

### Code

```kotlin
package binarysearch

class FindFirstAndLastPosition {

    fun searchRange(nums: IntArray, target: Int): IntArray {
        val result = intArrayOf(-1, -1)

        // Find the first occurrence
        result[0] = binarySearch(nums, target, true)

        // If the first occurrence is not found, return [-1, -1]
        if (result[0] == -1) return result

        // Find the last occurrence
        result[1] = binarySearch(nums, target, false)

        return result
    }

    private fun binarySearch(nums: IntArray, target: Int, findFirst: Boolean): Int {
        var left = 0
        var right = nums.lastIndex
        var result = -1

        while (left <= right) {
            val mid = left + (right - left) / 2
            when {
                nums[mid] == target -> {
                    result = mid
                    // Adjust the search range based on whether we are looking for the first or last occurrence
                    if (findFirst) {
                        right = mid - 1  // Move left to find the first occurrence
                    } else {
                        left = mid + 1   // Move right to find the last occurrence
                    }
                }
                nums[mid] < target -> left = mid + 1
                else -> right = mid - 1
            }
        }

        return result
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

## Find Minimum In Rotated Sorted Array

<span id="findminimuminrotatedsortedarray"></span>

### Problem

**Findminimuminrotatedsortedarray**

**Function:** `Find Min` takes `nums` (array of integers) and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`

### Code

```kotlin
package binarysearch

class FindMinimumInRotatedSortedArray {
    fun findMin(nums: IntArray): Int {
        var (left, right) = 0 to nums.size - 1
        while (left < right) {
            val mid = left + (right - left) / 2
            when {
                nums[mid] > nums[right] -> left = mid + 1
                else -> right = mid
            }
        }

        return nums[left]
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

## Find Peak Element

<span id="findpeakelement"></span>

### Problem

**Findpeakelement**

**Function:** `Find Peak Element` takes `nums` (array of integers) and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `mid`

### Code

```kotlin
package binarysearch

class FindPeakElement {
    fun findPeakElement(nums: IntArray): Int {
        var left = 0
        var right = nums.lastIndex

        while ( left < right) {
            val mid = left + (right - left)/2

            if (nums[mid] > nums[mid + 1]) {
                right = mid
            } else {
                left = mid + 1
            }
        }

        return left
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

## Find Peak Element Better Solution

<span id="findpeakelementbettersolution"></span>

### Problem

**Findpeakelementbettersolution**

**Function:** `Find Peak Element` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Safely handle boundaries
- Found peak
- Move to the right
- Move to the left
- Single peak element when the range narrows down



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`, `leftNeighbor`, `rightNeighbor`

**Execution flow:**
- Safely handle boundaries
- Move to the right
- Move to the left
- Single peak element when the range narrows down

### Code

```kotlin
package binarysearch

class FindPeakElementBetterSolution {
    fun findPeakElement(nums: IntArray): Int? {
        if (nums.isEmpty()) return null

        var (left, right) = 0 to nums.size - 1

        while (left < right) {
            val mid = left + (right - left) / 2

            // Safely handle boundaries
            val leftNeighbor = if (mid > 0) nums[mid - 1] else Int.MIN_VALUE
            val rightNeighbor = if (mid < nums.size - 1) nums[mid + 1] else Int.MIN_VALUE

            when {
                nums[mid] > leftNeighbor && nums[mid] > rightNeighbor -> return mid // Found peak
                nums[mid] < rightNeighbor -> left = mid + 1 // Move to the right
                else -> right = mid // Move to the left
            }
        }

        return left // Single peak element when the range narrows down
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

## Version Control

<span id="firstbadversion"></span>

### Problem

**Firstbadversion**

**Function:** `Is Bad Version` takes `mid` (integer) and returns **boolean**.

**Key logic:**
- Return dummy value



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `start`, `end`, `mid`

**Execution flow:**
- Return dummy value

### Code

```kotlin
package binarysearch

abstract class VersionControl {
    fun isBadVersion(mid: Int): Boolean {
        return false // Return dummy value
    }

    abstract fun firstBadVersion(n: Int) : Int
}
class FirstBadVersion: VersionControl() {
    override fun firstBadVersion(n: Int) : Int {
        var start = 1
        var end = n

        while (start < end) {
            val mid = start + (end - start) / 2
            when {
                isBadVersion(mid) -> end = mid
                else -> start = mid + 1
            }
        }

        return start
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

## Solution

<span id="guessnumberhigherorlower"></span>

### Problem

**Guessnumberhigherorlower**

**Function:** `Guess` takes `num` (integer) and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `start`, `end`, `mid`, `distance`

### Code

```kotlin
package binarysearch

/**
 * The API guess is defined in the parent class.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * fun guess(num:Int):Int {}
 */

class Solution:GuessGame() {
    override fun guessNumber(n:Int):Int {
        var start = 1
        var end = n

        while (start <= end) {
            val mid = start + (end-start) / 2

            val distance = guess(mid)


            when {
                distance == 0 -> return mid
                distance < 0 -> end = mid - 1
                else -> start = mid + 1
            }
        }

        return -1
    }


}

open class GuessGame {

    open fun guessNumber(n: Int): Int {
        TODO("Not yet implemented")
    }

    fun guess(mid: Int): Int {
        return 0
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

## House Robber_IV

<span id="houserobber_iv"></span>

### Problem

**Houserobber Iv**

**Function:** `Min Capability` takes `nums` (array of integers), `k` (integer) and returns **integer**.

**Key logic:**
- skip adjacent



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This uses a **feasibility function** that checks if a candidate value satisfies the constraint, making it a 'minimize/maximize with binary search' pattern.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `robbed`, `i`, `mid`

**Execution flow:**
- skip adjacent

### Code

```kotlin
package binarysearch

class HouseRobber_IV {
    fun minCapability(nums: IntArray, k: Int): Int {
        var left = nums.minOrNull() ?: 0
        var right = nums.maxOrNull() ?: 0

        fun canRob(cap: Int): Boolean {
            var robbed = 0
            var i = 0
            while (i < nums.size) {
                if (nums[i] <= cap) {
                    robbed++
                    i += 2  // skip adjacent
                } else {
                    i++
                }
            }
            return robbed >= k
        }

        while (left < right) {
            val mid = (left + right) / 2
            if (canRob(mid)) {
                right = mid
            } else {
                left = mid + 1
            }
        }

        return left
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

## K Th Missing Positive Number

<span id="kthmissingpositivenumber"></span>

### Problem

**Kthmissingpositivenumber**

**Function:** `Find Kth Positive` takes `arr` (array of integers), `k` (integer) and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`, `missingCount`

### Code

```kotlin
package binarysearch

class KThMissingPositiveNumber {
    fun findKthPositive(arr: IntArray, k: Int): Int {
        var (left, right) = 0 to arr.size

        while (left < right) {
            val mid = left + (right - left) / 2
            val missingCount = arr[mid] - ( mid + 1 )

            when {
                missingCount < k -> left = mid + 1
                else -> right = mid
            }
        }

        return left + k
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

## Koko Eating Banana

**Problem:** Koko loves bananas. There are `n` piles, the `i`-th pile has `piles[i]` bananas. The guards have gone and will return in `h` hours.

Koko can decide her eating speed `k` (bananas per hour). Each hour, she chooses one pile and eats `k` bananas from it. If the pile has fewer than `k` bananas, she eats the entire pile and cannot eat more that hour.

Return the **minimum integer `k`** such that Koko can eat all bananas within `h` hours.

**Input constraints:**
- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

**Example:**
```
Input: piles = [3, 6, 7, 11], h = 8
Output: 4

Explanation:
- At k = 4:  pile 0: ceil(3/4)=1h, pile 1: ceil(6/4)=2h, pile 2: ceil(7/4)=2h, pile 3: ceil(11/4)=3h. Total = 1+2+2+3 = 8h  ✅
- At k = 3:  ceil(3/3)=1h + ceil(6/3)=2h + ceil(7/3)=3h + ceil(11/3)=4h = 10h > 8h  ❌
So the minimum k is 4.
```

**Why binary search?** The eating speed `k` is a positive integer. If speed `k` works (Koko finishes in ≤ h hours), then any speed larger than `k` also works (she eats faster, finishes earlier). This **monotonic property** — feasibility increases with `k` — means we can binary search for the minimum feasible speed.

**The search space:**
- **Lower bound:** `1` (she must eat at least 1 banana per hour)
- **Upper bound:** `max(piles)` (eating faster than the largest pile doesn't help because the bottleneck is the biggest single pile)
- **Feasibility function:** `canEatAllBananas(k)` computes whether speed `k` lets Koko finish in ≤ `h` hours

**Dry run:**
```
piles = [3, 6, 7, 11], h = 8
Binary search on k in [1, 11]:

  Step 1: left=1, right=11, mid = 1 + (11-1)/2 = 6
    canEatAllBananas(6): ceil(3/6)+ceil(6/6)+ceil(7/6)+ceil(11/6) = 1+1+2+2 = 6 ≤ 8 ✅
    → Too fast, try slower: right = 6

  Step 2: left=1, right=6, mid = 1 + (6-1)/2 = 3
    canEatAllBananas(3): ceil(3/3)+ceil(6/3)+ceil(7/3)+ceil(11/3) = 1+2+3+4 = 10 > 8 ❌
    → Too slow, need faster: left = 4

  Step 3: left=4, right=6, mid = 4 + (6-4)/2 = 5
    canEatAllBananas(5): ceil(3/5)+ceil(6/5)+ceil(7/5)+ceil(11/5) = 1+2+2+3 = 8 ≤ 8 ✅
    → Still fast enough: right = 5

  Step 4: left=4, right=5, mid = 4 + (5-4)/2 = 4
    canEatAllBananas(4): ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8 ≤ 8 ✅
    → Fast enough: right = 4

  Step 5: left=4, right=4, loop exits. Return 4.
```

### Code

```kotlin
package binarysearch

/**
 * Problem: Koko loves bananas. There are n piles, pile i has piles[i] bananas.
 * Guards return in h hours. Koko eats at speed k bananas/hour.
 * Find minimum k to finish all bananas within h hours.
 *
 * Pattern: Binary search on answer (minimize k such that canEatAll(k) is feasible).
 * The predicate canEatAll(k) is monotonic: if speed k works, any speed > k also works.
 *
 * Search space: k ∈ [1, max(piles)]
 * - Lower bound: must eat at least 1 banana/hour
 * - Upper bound: eating faster than largest pile doesn't help further
 */
class KokoEatingBanana {

    /**
     * Finds the minimum integer eating speed k such that Koko
     * can eat all piles within h hours.
     *
     * @param piles Array where piles[i] = number of bananas in pile i
     *              Constraints: 1 <= piles.length <= 10^4
     *                           piles.length <= h <= 10^9
     *                           1 <= piles[i] <= 10^9
     * @param h     Hours available before guards return
     *              Constraints: h >= piles.length
     * @return      Minimum integer eating speed k
     *
     * Time  Complexity: O(n log m) where n = piles.size, m = max(piles)
     * Space Complexity: O(1)
     */
    fun minEatingSpeed(piles: IntArray, h: Int): Int {
        // Left: slowest possible speed (1 banana/hour)
        var left = 1
        // Right: fastest useful speed = largest pile
        var right = piles.maxOrNull()!!

        // Binary search: answer is always in [left, right]
        while (left < right) {
            // Safe midpoint: avoids overflow from (left + right)
            val mid = left + (right - left) / 2

            if (canEatAllBananas(piles, h, mid)) {
                // Speed mid works — try slower speed
                right = mid
            } else {
                // Speed mid too slow — need faster
                left = mid + 1
            }
        }
        return left
    }

    /**
     * Checks whether eating speed `k` lets Koko finish all piles
     * within `h` hours.
     *
     * Hours per pile = ceil(pile / k).
     * Total hours = sum of ceil(pile / k) for all piles.
     * Feasible if total hours <= h.
     *
     * Integer ceil trick: (pile + k - 1) / k
     *   (7 + 4 - 1) / 4 = 10 / 4 = 2 (integer division truncates)
     *
     * @param piles Array of banana piles
     * @param h     Hours available
     * @param k     Eating speed in bananas per hour
     * @return      True if total hours needed <= h
     */
    private fun canEatAllBananas(piles: IntArray, h: Int, k: Int): Boolean {
        var totalHours = 0
        for (pile in piles) {
            totalHours += (pile + k - 1) / k
            if (totalHours > h) return false  // early exit
        }
        return totalHours <= h
    }
}
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n log m) — binary search over [1, max(piles)] takes log₂m iterations. Each iteration scans n piles. Total = O(n) × O(log m) = O(n log m) |
| **Space** | O(1) — only integer variables regardless of input size |

### Pattern Insight

This is a **"minimize X such that predicate(X) is true"** problem. The predicate `canEatAllBananas(k)` is monotonic (once true at k, true for all larger k). We binary search for the first k where the predicate becomes true.

### Variations

1. What if Koko can eat from multiple piles simultaneously?
2. What if piles are refilled at a constant rate?
3. What if there's a maximum speed limit enforced?
4. What if Koko can skip hours but must meet a minimum daily consumption?
5. What if each pile has a spoilage time?

---


## Median Of Two Sorted A Rrays

<span id="medianoftwosortedarrays"></span>

### Problem

**Medianoftwosortedarrays**

**Function:** `Find Median Sorted Arrays` takes `nums1` (array of integers), `nums2` (array of integers) and returns **double**.

**Key logic:**
- These are the challenges that I need to somewhoe solve to get
- Use getOrNull with the Elvis operator to handle boundaries
- Check if we have found the correct partition



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `m`, `n`, `start`, `end`, `partitionX`, `partitionY`, `leftX`, `rightX`

**Execution flow:**
- These are the challenges that I need to somewhoe solve to get
- Use getOrNull with the Elvis operator to handle boundaries
- Check if we have found the correct partition

### Code

```kotlin
package binarysearch

// These are the challenges that I need to somewhoe solve to get
class MedianOfTwoSortedARrays {
    fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {

        if (nums1.size > nums2.size ) {
            return findMedianSortedArrays(nums2, nums1)
        }

        val m = nums1.size
        val n = nums2.size
        var start = 0
        var end = m

        while (start <= end) {
            val partitionX = (start + end) / 2
            val partitionY = (m + n + 1) / 2 - partitionX

            // Use getOrNull with the Elvis operator to handle boundaries
            val leftX = nums1.getOrNull(partitionX - 1) ?: Int.MIN_VALUE
            val rightX = nums1.getOrNull(partitionX) ?: Int.MAX_VALUE

            val leftY = nums2.getOrNull(partitionY - 1) ?: Int.MIN_VALUE
            val rightY = nums2.getOrNull(partitionY) ?: Int.MAX_VALUE

            // Check if we have found the correct partition
            when {
                leftX <= rightY && leftY <= rightX -> {
                    return if ((m + n) % 2 == 0) {
                        (maxOf(leftX, leftY) + minOf(rightX, rightY)) / 2.0
                    } else {
                        maxOf(leftX, leftY).toDouble()
                    }
                }
                leftX > rightY -> end = partitionX - 1
                else -> start = partitionX + 1
            }
        }
        return -1.0
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

## Random Pick With Weight

<span id="randompickwithweight"></span>

### Problem

**Randompickwithweight**

**Function:** `Pick Index` takes none and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `prefixSum`, `totalSum`, `w`, `randomPick`, `mid`

### Code

```kotlin
package binarysearch

import kotlin.random.Random

class RandomPickWithWeight (w: IntArray) {
    private val prefixSum = IntArray(w.size){ 0 }
    private val totalSum: Int
    private val w: IntArray = w
    init {
        for (i in w.indices) {
            prefixSum[i] = if(i > 0) prefixSum[i-1] + w[i] else w[i]
        }

        totalSum = prefixSum.last()
    }

    fun pickIndex(): Int {
        val randomPick = Random.nextInt(totalSum)
        var (start, end) = 0 to w.size

        while (start < end) {
            val mid = start + (end - start)/2

            when {
                prefixSum[mid] > randomPick -> end = mid
                else -> start = mid + 1
            }
        }

        return start
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

## Search A2d Matrix

<span id="searcha2dmatrix"></span>

### Problem

**Searcha2Dmatrix**

**Function:** `Search Matrix` takes `matrix` (Array<array of integers>), `target` (integer) and returns **boolean**.

**Key logic:**
- Convert 1D index to 2D



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`, `midValue`

**Execution flow:**
- Convert 1D index to 2D

### Code

```kotlin
package binarysearch

class SearchA2dMatrix {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        if (matrix.isEmpty() || matrix[0].isEmpty()) return false

        val (m, n) = matrix.size to matrix[0].size

        var (left, right) = 0 to m * n - 1

        while (left <= right) {
            val mid = left + (right - left) / 2
            val midValue = matrix[mid / n][mid % n]  // Convert 1D index to 2D

            when {
                midValue == target -> return true
                midValue < target -> left = mid + 1
                else -> right = mid - 1
            }
        }

        return false
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

## Search In Rotated Array_II

<span id="searchinrotatedarray_ii"></span>

### Problem

**Searchinrotatedarray Ii**

**Function:** `Search` takes `nums` (array of integers), `target` (integer) and returns **boolean**.

**Key logic:**
- Handle duplicates: skip the duplicates
- Left portion is sorted
- Target in left portion
- Target in right portion
- Right portion is sorted



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `mid`

**Execution flow:**
- Handle duplicates: skip the duplicates
- Left portion is sorted
- Target in left portion
- Target in right portion
- Right portion is sorted
- Target in right portion
- Target in left portion

### Code

```kotlin
package binarysearch

class SearchInRotatedArray_II {
    fun search(nums: IntArray, target: Int): Boolean {
        var left = 0
        var right = nums.lastIndex

        while (left <= right) {
            val mid = left + (right - left) / 2

            when {
                nums[mid] == target -> return true

                // Handle duplicates: skip the duplicates
                nums[left] == nums[mid] && nums[mid] == nums[right] -> {
                    left++
                    right--
                }

                // Left portion is sorted
                nums[left] <= nums[mid] -> {
                    if (nums[left] <= target && target < nums[mid]) {
                        right = mid - 1 // Target in left portion
                    } else {
                        left = mid + 1 // Target in right portion
                    }
                }

                // Right portion is sorted
                else -> {
                    if (nums[mid] < target && target <= nums[right]) {
                        left = mid + 1 // Target in right portion
                    } else {
                        right = mid - 1 // Target in left portion
                    }
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
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Search In Rotated Sorted Array

<span id="searchinrotatedsortedarray"></span>

### Problem

**Searchinrotatedsortedarray**

**Function:** `Search` takes `nums` (array of integers), `target` (integer) and returns **integer**.

**Key logic:**
- Determine if Left half is sorted
- Right half is sorted



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`

**Execution flow:**
- Determine if Left half is sorted
- Right half is sorted

### Code

```kotlin
package binarysearch

class SearchInRotatedSortedArray {
    fun search(nums: IntArray, target: Int): Int {
        var (start, end) = listOf(0, nums.lastIndex)

        while (start <= end) {
            val mid = start + (end - start) / 2

            if (nums[mid] == target) return mid

            // Determine if Left half is sorted
            if (nums[start] <= nums[mid]) {
                if (nums[start] <= target && target < nums[mid]) {
                    end = mid - 1
                } else {
                    start = mid + 1
                }
            } else {
                // Right half is sorted
                if (nums[mid] < target && target <= nums[end]) {
                    start = mid + 1
                } else {
                    end = mid - 1
                }
            }
        }

        return -1

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

## Search Insertion Position

<span id="searchinsertionposition"></span>

### Problem

**Searchinsertionposition**

**Function:** `Search Insert` takes `nums` (array of integers), `target` (integer) and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `start`, `end`, `mid`

### Code

```kotlin
package binarysearch

class SearchInsertionPosition {
    fun searchInsert(nums: IntArray, target: Int): Int {
        var start = 0
        var end = nums.size - 1

        while (start <= end) {
            val mid = start + ( end - start ) / 2

            when {
                nums[mid] == target -> return mid
                nums[mid] > target -> end = mid - 1
                else -> start = mid + 1
            }
        }

        return start
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

## Single Element In A Sorted Array

<span id="singleelementinasortedarray"></span>

### Problem

**Singleelementinasortedarray**

**Function:** `Single Non Duplicate` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Ensure mid is even for checking pair with the next element
- Check if the pair is valid
- Move to the right half
- Move to the left half
- low == high will give the unique element



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `low`, `high`, `mid`

**Execution flow:**
- Ensure mid is even for checking pair with the next element
- Check if the pair is valid
- Move to the right half
- Move to the left half
- low == high will give the unique element

### Code

```kotlin
package binarysearch

class SingleElementInASortedArray {
    fun singleNonDuplicate(nums: IntArray): Int {
        var low = 0
        var high = nums.size - 1

        while (low < high) {
            var mid = low + (high - low) / 2
            // Ensure mid is even for checking pair with the next element
            if (mid % 2 == 1) {
                mid--
            }

            // Check if the pair is valid
            if (nums[mid] == nums[mid + 1]) {
                low = mid + 2 // Move to the right half
            } else {
                high = mid // Move to the left half
            }
        }

        return nums[low] // low == high will give the unique element
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

## Valley Element

<span id="valleyelement"></span>

### Problem

**Valleyelement**

**Function:** `Find Valley Element Binary` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Safely handle boundaries
- Found valley
- Move to the right
- Move to the left
- No valley found (unlikely for a valid array)



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mid`, `leftNeighbor`, `rightNeighbor`

**Execution flow:**
- Safely handle boundaries
- Found valley
- Move to the right
- Move to the left
- No valley found (unlikely for a valid array)

### Code

```kotlin
package binarysearch

class ValleyElement {
    fun findValleyElementBinary(nums: IntArray): Int? {
        if (nums.isEmpty()) return null

        var (left, right) = 0 to nums.size

        while (left < right) {
            val mid = left + (right - left) / 2

            // Safely handle boundaries
            val leftNeighbor = if (mid > 0) nums[mid - 1] else Int.MAX_VALUE
            val rightNeighbor = if (mid < nums.size - 1) nums[mid + 1] else Int.MAX_VALUE

            when {
                nums[mid] < leftNeighbor && nums[mid] < rightNeighbor -> return nums[mid] // Found valley
                nums[mid] > rightNeighbor -> left = mid + 1 // Move to the right
                else -> right = mid // Move to the left
            }
        }

        return null // No valley found (unlikely for a valid array)
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

1. **Core pattern recognition** — Sorted array + search → Binary Search. The key insight: find a predicate that splits the search space into 'yes' and 'no', then binary search finds the transition point.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

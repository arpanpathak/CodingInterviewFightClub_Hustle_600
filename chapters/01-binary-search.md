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

> **21 problems**

## The Pattern

_Each problem below includes: Problem, Example, Why This Approach, Code, Pattern Insight, Complexity, and Variations._

## Problems

1. [Apartmenthunting](#apartmenthunting)
2. [Capacity To Ship Package Within D Days](#capacitytoshippackagewithinddays)
3. [Closest Sebsequence Sum](#closestsebsequencesum)
4. [Find First And Last Position](#findfirstandlastposition)
5. [Find K Closest Elements](#findkclosestelements)
6. [Find Minimum In Rotated Sorted Array](#findminimuminrotatedsortedarray)
7. [Find Peak Element](#findpeakelement)
8. [Find Peak Element Better Solution](#findpeakelementbettersolution)
9. [Version Control](#firstbadversion)
10. [Solution](#guessnumberhigherorlower)
11. [House Robber_IV](#houserobber_iv)
12. [K Th Missing Positive Number](#kthmissingpositivenumber)
13. [Koko Eating Banana](#kokoeatingbanana)
14. [Median Of Two Sorted A Rrays](#medianoftwosortedarrays)
15. [Random Pick With Weight](#randompickwithweight)
16. [Search A2d Matrix](#searcha2dmatrix)
17. [Search In Rotated Array_II](#searchinrotatedarray_ii)
18. [Search In Rotated Sorted Array](#searchinrotatedsortedarray)
19. [Search Insertion Position](#searchinsertionposition)
20. [Single Element In A Sorted Array](#singleelementinasortedarray)
21. [Valley Element](#valleyelement)

---

## Apartmenthunting

### Problem

Given `blocks` (List<Map<String), `requirements` (List<String>), `blockIndex` (integer), `blocksWithAmenity` (list of integers), `arr` (list of integers), `target` (integer), compute the computed result efficiently.

**Example:**

```
Input: blocks = input_value, requirements = input_value, blockIndex = 5, blocksWithAmenity = [1, 2, 3, 4, 5], arr = [1, 2, 3, 4, 5], target = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package binarysearch

/**
* Solves the apartmenthunting problem.
* Takes `blocks` (List<Map<String), `requirements` (list of strings).
*
* @param blocks The input List<Map<String.
* @param requirements The input list of strings.
* @return The computed integer result.
*/
/**
* Solves the apartmenthunting problem.
* Takes `blocks` (List<Map<String), `requirements` (list of strings).
*
* @param blocks The input List<Map<String.
* @param requirements The input list of strings.
* @return The computed integer result.
*/
/**
* Solves the apartmenthunting problem.
* Takes `blocks` (List<Map<String), `requirements` (list of strings).
*
* @param blocks The input List<Map<String.
* @param requirements The input list of strings.
* @return The computed integer result.
*/
/**
* Solves the apartmenthunting problem.
* Takes `blocks` (List<Map<String), `requirements` (list of strings).
*
* @param blocks The input List<Map<String.
* @param requirements The input list of strings.
* @return The computed integer result.
*/
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
/**
* Solves the apartmenthunting problem.
* Takes `blockIndex` (integer), `blocksWithAmenity` (list of integers).
*
* @param blockIndex The integer parameter representing blockIndex.
* @param blocksWithAmenity The input list of integers.
* @return The computed integer result.
*/
/**
* Solves the apartmenthunting problem.
* Takes `blockIndex` (integer), `blocksWithAmenity` (list of integers).
*
* @param blockIndex The integer parameter representing blockIndex.
* @param blocksWithAmenity The input list of integers.
* @return The computed integer result.
*/
/**
* Solves the apartmenthunting problem.
* Takes `blockIndex` (integer), `blocksWithAmenity` (list of integers).
*
* @param blockIndex The integer parameter representing blockIndex.
* @param blocksWithAmenity The input list of integers.
* @return The computed integer result.
*/
/**
* Solves the apartmenthunting problem.
* Takes `blockIndex` (integer), `blocksWithAmenity` (list of integers).
*
* @param blockIndex The integer parameter representing blockIndex.
* @param blocksWithAmenity The input list of integers.
* @return The computed integer result.
*/
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
/**
* Solves the apartmenthunting problem.
* Takes `arr` (list of integers), `target` (integer).
*
* @param arr The input list of integers.
* @param target The integer parameter representing target.
* @return The computed integer result.
*/
/**
* Solves the apartmenthunting problem.
* Takes `arr` (list of integers), `target` (integer).
*
* @param arr The input list of integers.
* @param target The integer parameter representing target.
* @return The computed integer result.
*/
/**
* Solves the apartmenthunting problem.
* Takes `arr` (list of integers), `target` (integer).
*
* @param arr The input list of integers.
* @param target The integer parameter representing target.
* @return The computed integer result.
*/
/**
* Solves the apartmenthunting problem.
* Takes `arr` (list of integers), `target` (integer).
*
* @param arr The input list of integers.
* @param target The integer parameter representing target.
* @return The computed integer result.
*/
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

## Capacity To Ship Package Within D Days

### Problem

Given `weights` (array of integers), `mid` (integer), `days` (integer), compute the computed result efficiently.

**Example:**

```
Input: weights = [1, 2, 3, 4, 5], mid = 5, days = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package binarysearch

class CapacityToShipPackageWithinDDays {
    /**
    * Solves the Capacity To Ship Package Within DDays problem.
    * Takes `weights` (array of integers), `mid` (integer), `days` (integer).
    *
    * @param weights The input array of integers.
    * @param mid The integer parameter representing mid.
    * @param days The integer parameter representing days.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Capacity To Ship Package Within DDays problem.
    * Takes `weights` (array of integers), `mid` (integer), `days` (integer).
    *
    * @param weights The input array of integers.
    * @param mid The integer parameter representing mid.
    * @param days The integer parameter representing days.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Capacity To Ship Package Within DDays problem.
    * Takes `weights` (array of integers), `mid` (integer), `days` (integer).
    *
    * @param weights The input array of integers.
    * @param mid The integer parameter representing mid.
    * @param days The integer parameter representing days.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Capacity To Ship Package Within DDays problem.
    * Takes `weights` (array of integers), `mid` (integer), `days` (integer).
    *
    * @param weights The input array of integers.
    * @param mid The integer parameter representing mid.
    * @param days The integer parameter representing days.
    * @return `true` if the condition is met, `false` otherwise.
    */
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

    /**
    * Solves the Capacity To Ship Package Within DDays problem.
    * Takes `weights` (array of integers), `days` (integer).
    *
    * @param weights The input array of integers.
    * @param days The integer parameter representing days.
    * @return The computed integer result.
    */
    /**
    * Solves the Capacity To Ship Package Within DDays problem.
    * Takes `weights` (array of integers), `days` (integer).
    *
    * @param weights The input array of integers.
    * @param days The integer parameter representing days.
    * @return The computed integer result.
    */
    /**
    * Solves the Capacity To Ship Package Within DDays problem.
    * Takes `weights` (array of integers), `days` (integer).
    *
    * @param weights The input array of integers.
    * @param days The integer parameter representing days.
    * @return The computed integer result.
    */
    /**
    * Solves the Capacity To Ship Package Within DDays problem.
    * Takes `weights` (array of integers), `days` (integer).
    *
    * @param weights The input array of integers.
    * @param days The integer parameter representing days.
    * @return The computed integer result.
    */
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

## Closest Sebsequence Sum

### Problem

Given `nums` (array of integers), `goal` (integer), `start` (integer), `end` (integer), `currentSum` (integer), `result` (list of integers), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], goal = 5, start = 5, end = 5, currentSum = 5, result = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package binarysearch

import kotlin.math.abs

class ClosestSebsequenceSum {
    /**
    * Solves the Closest Sebsequence Sum problem.
    * Takes `nums` (array of integers), `goal` (integer).
    *
    * @param nums The input array of integers.
    * @param goal The integer parameter representing goal.
    * @return The computed integer result.
    */
    /**
    * Solves the Closest Sebsequence Sum problem.
    * Takes `nums` (array of integers), `goal` (integer).
    *
    * @param nums The input array of integers.
    * @param goal The integer parameter representing goal.
    * @return The computed integer result.
    */
    /**
    * Solves the Closest Sebsequence Sum problem.
    * Takes `nums` (array of integers), `goal` (integer).
    *
    * @param nums The input array of integers.
    * @param goal The integer parameter representing goal.
    * @return The computed integer result.
    */
    /**
    * Solves the Closest Sebsequence Sum problem.
    * Takes `nums` (array of integers), `goal` (integer).
    *
    * @param nums The input array of integers.
    * @param goal The integer parameter representing goal.
    * @return The computed integer result.
    */
    fun minAbsDifference(nums: IntArray, goal: Int): Int {
        val leftSums = mutableListOf<Int>()
        val rightSums = mutableListOf<Int>()
        val n = nums.size
        val mid = n / 2

        /**
        * Solves the Closest Sebsequence Sum problem.
        * Takes `start` (integer), `end` (integer), `currentSum` (integer), `result` (mutable list of integers).
        *
        * @param start The integer parameter representing start.
        * @param end The integer parameter representing end.
        * @param currentSum The integer parameter representing currentSum.
        * @param result The input mutable list of integers.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Closest Sebsequence Sum problem.
        * Takes `start` (integer), `end` (integer), `currentSum` (integer), `result` (mutable list of integers).
        *
        * @param start The integer parameter representing start.
        * @param end The integer parameter representing end.
        * @param currentSum The integer parameter representing currentSum.
        * @param result The input mutable list of integers.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Closest Sebsequence Sum problem.
        * Takes `start` (integer), `end` (integer), `currentSum` (integer), `result` (mutable list of integers).
        *
        * @param start The integer parameter representing start.
        * @param end The integer parameter representing end.
        * @param currentSum The integer parameter representing currentSum.
        * @param result The input mutable list of integers.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Closest Sebsequence Sum problem.
        * Takes `start` (integer), `end` (integer), `currentSum` (integer), `result` (mutable list of integers).
        *
        * @param start The integer parameter representing start.
        * @param end The integer parameter representing end.
        * @param currentSum The integer parameter representing currentSum.
        * @param result The input mutable list of integers.
        * @return Unit (no return value, modifies state in-place).
        */
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

## Find First And Last Position

### Problem

Given `nums` (array of integers), `target` (integer), `findFirst` (boolean), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], target = 5, findFirst = true
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

### Code

```kotlin
package binarysearch

class FindFirstAndLastPosition {

    /**
    * Solves the Find First And Last Position problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Find First And Last Position problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Find First And Last Position problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Find First And Last Position problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
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

    /**
    * Helper: binary search.
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @param findFirst A boolean flag: findFirst.
    * @return The computed integer result.
    */
    /**
    * Helper: binary search.
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @param findFirst A boolean flag: findFirst.
    * @return The computed integer result.
    */
    /**
    * Helper: binary search.
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @param findFirst A boolean flag: findFirst.
    * @return The computed integer result.
    */
    /**
    * Helper: binary search.
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @param findFirst A boolean flag: findFirst.
    * @return The computed integer result.
    */
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

## Find Minimum In Rotated Sorted Array

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
package binarysearch

class FindMinimumInRotatedSortedArray {
    /**
    * Solves the Find Minimum In Rotated Sorted Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Minimum In Rotated Sorted Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Minimum In Rotated Sorted Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Minimum In Rotated Sorted Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
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

## Find Peak Element

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
package binarysearch

class FindPeakElement {
    /**
    * Solves the Find Peak Element problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Peak Element problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Peak Element problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Peak Element problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
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

## Find Peak Element Better Solution

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
package binarysearch

class FindPeakElementBetterSolution {
    /**
    * Solves the Find Peak Element Better Solution problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Peak Element Better Solution problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Peak Element Better Solution problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Find Peak Element Better Solution problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
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

## Version Control

### Problem

Given `mid` (integer), `n` (integer), compute the computed result efficiently.

**Example:**

```
Input: mid = 5, n = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package binarysearch

abstract class VersionControl {
    /**
    * Solves the Version Control problem.
    * Takes `mid` (integer).
    *
    * @param mid The integer parameter representing mid.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Version Control problem.
    * Takes `mid` (integer).
    *
    * @param mid The integer parameter representing mid.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Version Control problem.
    * Takes `mid` (integer).
    *
    * @param mid The integer parameter representing mid.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Version Control problem.
    * Takes `mid` (integer).
    *
    * @param mid The integer parameter representing mid.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isBadVersion(mid: Int): Boolean {
        return false // Return dummy value
    }

    /**
    * Solves the Version Control problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Version Control problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Version Control problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Version Control problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    abstract fun firstBadVersion(n: Int) : Int
}
class FirstBadVersion: VersionControl() {
    /**
    * Implements/overrides the base class method.
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Implements/overrides the base class method.
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Implements/overrides the base class method.
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Implements/overrides the base class method.
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
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

## Solution

### Problem

Given `num` (integer), `n` (integer), `mid` (integer), compute the computed result efficiently.

**Example:**

```
Input: num = 5, n = 5, mid = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package binarysearch

/**
 * The API guess is defined in the parent class.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 /**
 * Solves the Solution problem.
 * Takes `num` (integer).
 *
 * @param num The integer parameter representing num.
 * @return The computed integer result.
 */
 /**
 * Solves the Solution problem.
 * Takes `num` (integer).
 *
 * @param num The integer parameter representing num.
 * @return The computed integer result.
 */
 /**
 * Solves the Solution problem.
 * Takes `num` (integer).
 *
 * @param num The integer parameter representing num.
 * @return The computed integer result.
 */
 /**
 * Solves the Solution problem.
 * Takes `num` (integer).
 *
 * @param num The integer parameter representing num.
 * @return The computed integer result.
 */
 * fun guess(num:Int):Int {}
 */

class Solution:GuessGame() {
    /**
    * Implements/overrides the base class method.
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Implements/overrides the base class method.
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Implements/overrides the base class method.
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Implements/overrides the base class method.
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
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

    /**
    * Solves the Solution problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Solution problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Solution problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Solution problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    open fun guessNumber(n: Int): Int {
        TODO("Not yet implemented")
    }

    /**
    * Solves the Solution problem.
    * Takes `num` (integer).
    *
    * @param num The integer parameter representing num.
    * @return The computed integer result.
    */
    /**
    * Solves the Solution problem.
    * Takes `num` (integer).
    *
    * @param num The integer parameter representing num.
    * @return The computed integer result.
    */
    /**
    * Solves the Solution problem.
    * Takes `num` (integer).
    *
    * @param num The integer parameter representing num.
    * @return The computed integer result.
    */
    /**
    * Solves the Solution problem.
    * Takes `num` (integer).
    *
    * @param num The integer parameter representing num.
    * @return The computed integer result.
    */
    fun guess(mid: Int): Int {
        return 0
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

## House Robber_IV

### Problem

Given `nums` (array of integers), `k` (integer), `cap` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], k = 5, cap = 5
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package binarysearch

class HouseRobber_IV {
    /**
    * Solves the House Robber_IV problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the House Robber_IV problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the House Robber_IV problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the House Robber_IV problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    fun minCapability(nums: IntArray, k: Int): Int {
        var left = nums.minOrNull() ?: 0
        var right = nums.maxOrNull() ?: 0

        /**
        * Solves the House Robber_IV problem.
        * Takes `cap` (integer).
        *
        * @param cap The integer parameter representing cap.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the House Robber_IV problem.
        * Takes `cap` (integer).
        *
        * @param cap The integer parameter representing cap.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the House Robber_IV problem.
        * Takes `cap` (integer).
        *
        * @param cap The integer parameter representing cap.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the House Robber_IV problem.
        * Takes `cap` (integer).
        *
        * @param cap The integer parameter representing cap.
        * @return `true` if the condition is met, `false` otherwise.
        */
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

## K Th Missing Positive Number

### Problem

Given `arr` (array of integers), `k` (integer), compute the computed result efficiently.

**Example:**

```
Input: arr = [1, 2, 3, 4, 5], k = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses a **heap/priority queue** to maintain a dynamic ordering of elements. Heaps provide O(log n) insertion and O(1) access to the min or max element, making them ideal for streaming/online algorithms and k-th order statistics.

### Code

```kotlin
package binarysearch

class KThMissingPositiveNumber {
    /**
    * Solves the KTh Missing Positive Number problem.
    * Takes `arr` (array of integers), `k` (integer).
    *
    * @param arr The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the KTh Missing Positive Number problem.
    * Takes `arr` (array of integers), `k` (integer).
    *
    * @param arr The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the KTh Missing Positive Number problem.
    * Takes `arr` (array of integers), `k` (integer).
    *
    * @param arr The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the KTh Missing Positive Number problem.
    * Takes `arr` (array of integers), `k` (integer).
    *
    * @param arr The input array of integers.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
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

## Koko Eating Banana

### Problem

Given `piles` (array of integers), `h` (integer), `k` (integer), compute the computed result efficiently.

**Example:**

```
Input: piles = [1, 2, 3, 4, 5], h = 5, k = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
     *              Constraints: h >= piles.length (must be able to eat at least
     *              one pile per hour in worst case)
     * @return      Minimum integer eating speed k
     *
     * Time  Complexity: O(n log m) where n = piles.size, m = max(piles)
     * Space Complexity: O(1)
     */
    /**
    * Solves the Koko Eating Banana problem.
    * Takes `piles` (array of integers), `h` (integer).
    *
    * @param piles The input array of integers.
    * @param h The integer parameter representing h.
    * @return The computed integer result.
    */
    /**
    * Solves the Koko Eating Banana problem.
    * Takes `piles` (array of integers), `h` (integer).
    *
    * @param piles The input array of integers.
    * @param h The integer parameter representing h.
    * @return The computed integer result.
    */
    /**
    * Solves the Koko Eating Banana problem.
    * Takes `piles` (array of integers), `h` (integer).
    *
    * @param piles The input array of integers.
    * @param h The integer parameter representing h.
    * @return The computed integer result.
    */
    fun minEatingSpeed(piles: IntArray, h: Int): Int {
        // ── Step 1: Define binary search bounds ──
        // Left: slowest possible speed (1 banana/hour)
        var left = 1
        // Right: fastest useful speed = largest pile
        // (eating faster doesn't reduce total hours because
        //  the bottleneck is always the biggest pile)
        var right = piles.maxOrNull()!!

        // ── Step 2: Binary search for minimum feasible speed ──
        // Loop invariant: answer is always in [left, right]
        while (left < right) {
            // Safe midpoint: avoids overflow from (left + right)
            val mid = left + (right - left) / 2

            if (canEatAllBananas(piles, h, mid)) {
                // Speed `mid` works — we can finish in ≤ h hours.
                // Try an even slower speed by bringing right bound down.
                // We keep mid in range because it might be the answer.
                right = mid
            } else {
                // Speed `mid` is too slow — cannot finish in time.
                // Need to eat faster, so move left bound past mid.
                left = mid + 1
            }
        }

        // left == right == the minimum feasible speed
        return left
    }

    /**
     * Checks whether eating speed `k` lets Koko finish all piles
     * within `h` hours.
     *
     * For each pile, the hours needed = ceil(pile / k).
     * Total hours = sum of ceil(pile / k) for all piles.
     * Feasible if total hours <= h.
     *
     * Why ceil(pile / k)?
     *   Koko eats k bananas per hour from one pile.
     *   If pile has 7 bananas and k=4:
     *     Hour 1: eats 4, pile left = 3
     *     Hour 2: eats 3 (the rest), pile done
     *     Total: 2 hours = ceil(7/4) = ceil(1.75) = 2 ✓
     *
     * Integer ceil trick: (pile + k - 1) / k
     *   (7 + 4 - 1) / 4 = 10 / 4 = 2 ✓ (integer division truncates)
     *
     * @param piles Array of banana piles
     * @param h     Hours available (piles.size <= h)
     * @param k     Eating speed in bananas per hour
     * @return      True if total hours needed <= h
     */
    /**
    * Helper: can eat all bananas.
    *
    * @param piles The input array of integers.
    * @param h The integer parameter representing h.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: can eat all bananas.
    *
    * @param piles The input array of integers.
    * @param h The integer parameter representing h.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: can eat all bananas.
    *
    * @param piles The input array of integers.
    * @param h The integer parameter representing h.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    private fun canEatAllBananas(piles: IntArray, h: Int, k: Int): Boolean {
        var totalHours = 0
        for (pile in piles) {
            // Integer ceil division: (pile + k - 1) / k
            totalHours += (pile + k - 1) / k
            
            // Early exit optimization: if we've already exceeded h,
            // no need to process remaining piles
            if (totalHours > h) return false
        }
        return totalHours <= h
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

## Median Of Two Sorted A Rrays

### Problem

Given `nums1` (array of integers), `nums2` (array of integers), compute the computed result efficiently.

**Example:**

```
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem uses a **heap/priority queue** to maintain a dynamic ordering of elements. Heaps provide O(log n) insertion and O(1) access to the min or max element, making them ideal for streaming/online algorithms and k-th order statistics.

### Code

```kotlin
package binarysearch

// These are the challenges that I need to somewhoe solve to get
class MedianOfTwoSortedARrays {
    /**
    * Solves the Median Of Two Sorted ARrays problem.
    * Takes `nums1` (array of integers), `nums2` (array of integers).
    *
    * @param nums1 The input array of integers.
    * @param nums2 The input array of integers.
    * @return The computed floating-point result.
    */
    /**
    * Solves the Median Of Two Sorted ARrays problem.
    * Takes `nums1` (array of integers), `nums2` (array of integers).
    *
    * @param nums1 The input array of integers.
    * @param nums2 The input array of integers.
    * @return The computed floating-point result.
    */
    /**
    * Solves the Median Of Two Sorted ARrays problem.
    * Takes `nums1` (array of integers), `nums2` (array of integers).
    *
    * @param nums1 The input array of integers.
    * @param nums2 The input array of integers.
    * @return The computed floating-point result.
    */
    /**
    * Solves the Median Of Two Sorted ARrays problem.
    * Takes `nums1` (array of integers), `nums2` (array of integers).
    *
    * @param nums1 The input array of integers.
    * @param nums2 The input array of integers.
    * @return The computed floating-point result.
    */
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

## Random Pick With Weight

### Problem

Given the input, compute the result efficiently.

**Example:**

```
Input: 
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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

    /**
    * Solves the Random Pick With Weight problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the Random Pick With Weight problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the Random Pick With Weight problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the Random Pick With Weight problem.
    *
    * @return The computed integer result.
    */
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

## Search A2d Matrix

### Problem

Given `matrix` (2D matrix), `target` (integer), compute the computed result efficiently.

**Example:**

```
Input: matrix = [1, 2, 3, 4, 5], target = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

### Code

```kotlin
package binarysearch

class SearchA2dMatrix {
    /**
    * Solves the Search A2d Matrix problem.
    * Takes `matrix` (2D matrix of integers), `target` (integer).
    *
    * @param matrix The input 2D matrix of integers.
    * @param target The integer parameter representing target.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Search A2d Matrix problem.
    * Takes `matrix` (2D matrix of integers), `target` (integer).
    *
    * @param matrix The input 2D matrix of integers.
    * @param target The integer parameter representing target.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Search A2d Matrix problem.
    * Takes `matrix` (2D matrix of integers), `target` (integer).
    *
    * @param matrix The input 2D matrix of integers.
    * @param target The integer parameter representing target.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Search A2d Matrix problem.
    * Takes `matrix` (2D matrix of integers), `target` (integer).
    *
    * @param matrix The input 2D matrix of integers.
    * @param target The integer parameter representing target.
    * @return `true` if the condition is met, `false` otherwise.
    */
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

## Search In Rotated Array_II

### Problem

Given `nums` (array of integers), `target` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], target = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

### Code

```kotlin
package binarysearch

class SearchInRotatedArray_II {
    /**
    * Solves the Search In Rotated Array_II problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Search In Rotated Array_II problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Search In Rotated Array_II problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Search In Rotated Array_II problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return `true` if the condition is met, `false` otherwise.
    */
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

## Search In Rotated Sorted Array

### Problem

Given `nums` (array of integers), `target` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], target = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

### Code

```kotlin
package binarysearch

class SearchInRotatedSortedArray {
    /**
    * Solves the Search In Rotated Sorted Array problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Search In Rotated Sorted Array problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Search In Rotated Sorted Array problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Search In Rotated Sorted Array problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
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

## Search Insertion Position

### Problem

Given `nums` (array of integers), `target` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], target = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

### Code

```kotlin
package binarysearch

class SearchInsertionPosition {
    /**
    * Solves the Search Insertion Position problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Search Insertion Position problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Search Insertion Position problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Search Insertion Position problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
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

## Single Element In A Sorted Array

### Problem

Given `nums` (array of integers), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package binarysearch

class SingleElementInASortedArray {
    /**
    * Solves the Single Element In ASorted Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Single Element In ASorted Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Single Element In ASorted Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Single Element In ASorted Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
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

## Valley Element

### Problem

Given `nums` (array of integers), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package binarysearch

class ValleyElement {
    /**
    * Solves the Valley Element problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Valley Element problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Valley Element problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Valley Element problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
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

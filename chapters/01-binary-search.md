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

Sorted array + search → Binary Search. Find a predicate that splits the search space into yes/no.

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

### Problem

Solve the **Apartmenthunting** problem efficiently.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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

**Pattern:** Binary search on sorted data. Key insight: the predicate must be monotonic — once it becomes true, it stays true for all larger values.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

### Variations

1. What if the array is not sorted? Can you sort first?
1. What if there are duplicates? How does that affect the search?
1. What if the search space is a range of values rather than array indices?
1. What if you need to find the FIRST vs LAST occurrence?
1. What if the input is too large to fit in memory (external search)?

---
## Capacity To Ship Package Within D Days

### Problem

Solves the Capacity To Ship Package Within DDays problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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

**Pattern:** Study the code's approach — identify the core data structure and traversal method.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger? Can you optimize?
1. What if you need O(1) extra space instead of O(n)?
1. What if there are duplicates or edge cases to handle?
1. What if the problem constraints change (positive only, sorted, etc.)?
1. Can this solution be parallelized?

---
## Closest Sebsequence Sum

### Problem

Solves the Closest Sebsequence Sum problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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

**Pattern:** Binary search on sorted data. Key insight: the predicate must be monotonic — once it becomes true, it stays true for all larger values.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

### Variations

1. What if the array is not sorted? Can you sort first?
1. What if there are duplicates? How does that affect the search?
1. What if the search space is a range of values rather than array indices?
1. What if you need to find the FIRST vs LAST occurrence?
1. What if the input is too large to fit in memory (external search)?

---
rrence
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

---

## Find K Closest Elements

### Problem

Solving using Max Heap. O ( N log K + K log K )

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
            fun main(args: Array<String>) {
                val testClass = FindKClosestElements()

                println(testClass.findClosestElements(arrayOf(1,2,3,4,5,6,7), 4, 4 ))
            }
        }
    }
}
```


### Pattern Insight

**Pattern:** Dijkstra / priority-queue BFS. Use a min-heap to always expand the cheapest node first.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log k) |
| **Space** | O(k) |

### Variations

1. What if the graph is disconnected?
1. What if edges have weights (non-uniform cost)?
1. Can this be solved with DFS instead? What's the tradeoff?
1. What if you need the path, not just the distance/existence?
1. What if the graph is too large for BFS? Iterative deepening?

---
## Find Minimum In Rotated Sorted Array

### Problem

Solves the Find Minimum In Rotated Sorted Array problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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

**Pattern:** Disjoint Set Union (Union-Find). Track connected components with near-O(1) operations.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger? Can you optimize?
1. What if you need O(1) extra space instead of O(n)?
1. What if there are duplicates or edge cases to handle?
1. What if the problem constraints change (positive only, sorted, etc.)?
1. Can this solution be parallelized?

---
(n³) |
| **Space** | O(n²) |

---

## Find Peak Element Better Solution

### Problem

Solves the Find Peak Element Better Solution problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Version Control

### Problem

Solves the Version Control problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
    abstract fun firstBadVersion(n: Int) : Int
}
class FirstBadVersion: VersionControl() {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Solution

### Problem

The API guess is defined in the parent class.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
 * fun guess(num:Int):Int {}
 */

class Solution:GuessGame() {
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
    fun guess(mid: Int): Int {
        return 0
    }
}
```


### Pattern Insight

Study the code and identify the algorithmic pattern.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

### Variations


---

        return left
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## K Th Missing Positive Number

### Problem

Solves the KTh Missing Positive Number problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
| **Time** | O(n²) |
| **Space** | O(1) |

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

**Why binary search?** The eating speed `k` is a positive integer. If speed `k` works (Koko finishes in ≤ h hours), then any speed larger than `k` also works. This **monotonic property** means we can binary search for the minimum feasible speed.

**The search space:**
- **Lower bound:** `1` (she must eat at least 1 banana per hour)
- **Upper bound:** `max(piles)` (eating faster than the largest pile doesn't help)
- **Feasibility function:** `canEatAllBananas(k)` computes whether speed `k` lets Koko finish in ≤ `h` hours

**Dry run:**
```
piles = [3, 6, 7, 11], h = 8

Binary search on k in [1, 11]:

  Step 1: left=1, right=11, mid = 1 + (11-1)/2 = 6
    Hours at k=6: ceil(3/6)+ceil(6/6)+ceil(7/6)+ceil(11/6) = 1+1+2+2 = 6 ≤ 8  → right = 6

  Step 2: left=1, right=6, mid = 1 + (6-1)/2 = 3
    Hours at k=3: 1+2+3+4 = 10 > 8  → left = 4

  Step 3: left=4, right=6, mid = 4 + (6-4)/2 = 5
    Hours at k=5: 1+2+2+3 = 8 ≤ 8  → right = 5

  Step 4: left=4, right=5, mid = 4 + (5-4)/2 = 4
    Hours at k=4: 1+2+2+3 = 8 ≤ 8  → right = 4

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
     *              Constraints: h >= piles.length (must be able to eat at least
     *              one pile per hour in worst case)
     * @return      Minimum integer eating speed k
     *
     * Time  Complexity: O(n log m) where n = piles.size, m = max(piles)
     * Space Complexity: O(1)
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

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n log m) — binary search over [1, max(piles)] takes log₂m iterations. Each iteration scans n piles. |
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

### Problem

Solves the Median Of Two Sorted ARrays problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Random Pick With Weight

### Problem

Solves the Random Pick With Weight problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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

**Pattern:** Disjoint Set Union (Union-Find). Track connected components with near-O(1) operations.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Search A2d Matrix

### Problem

Solves the Search A2d Matrix problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
| **Time** | O(n²) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger? Can you optimize?
1. What if you need O(1) extra space instead of O(n)?
1. What if there are duplicates or edge cases to handle?
1. What if the problem constraints change (positive only, sorted, etc.)?
1. Can this solution be parallelized?

---
ers), `target` (integer).
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

**Pattern:** Bit manipulation. Use bitwise operations for fast computation and compact state tracking.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger? Can you optimize?
1. What if you need O(1) extra space instead of O(n)?
1. What if there are duplicates or edge cases to handle?
1. What if the problem constraints change (positive only, sorted, etc.)?
1. Can this solution be parallelized?

---
Left half is sorted
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

**Pattern:** Bit manipulation. Use bitwise operations for fast computation and compact state tracking.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Search Insertion Position

### Problem

Solves the Search Insertion Position problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
| **Time** | O(n²) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger? Can you optimize?
1. What if you need O(1) extra space instead of O(n)?
1. What if there are duplicates or edge cases to handle?
1. What if the problem constraints change (positive only, sorted, etc.)?
1. Can this solution be parallelized?

---
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

**Pattern:** Bit manipulation. Use bitwise operations for fast computation and compact state tracking.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger? Can you optimize?
1. What if you need O(1) extra space instead of O(n)?
1. What if there are duplicates or edge cases to handle?
1. What if the problem constraints change (positive only, sorted, etc.)?
1. Can this solution be parallelized?

---
or -> left = mid + 1 // Move to the right
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
| **Time** | O(n²) |
| **Space** | O(1) |

---

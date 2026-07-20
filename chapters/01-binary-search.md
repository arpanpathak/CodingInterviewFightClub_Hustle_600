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

## Apartment Hunting

**Problem:** You're looking for an apartment in a city of blocks. Each block has certain amenities (gym, school, store). You want to pick a block such that the **maximum distance** to any required amenity is **minimized**.

Given a list of blocks (each is a map of amenity → boolean) and a list of required amenities, return the index of the optimal block.

**Example:**
```
blocks = [
  {"gym": false, "school": true,  "store": false},
  {"gym": true,  "school": false, "store": false},
  {"gym": true,  "school": true,  "store": false},
  {"gym": false, "school": true,  "store": false},
  {"gym": false, "school": true,  "store": true}
]
requirements = ["gym", "school", "store"]

Block 3 is optimal: gym at distance 1, school at 0, store at 1. Max distance = 1.
```

**Why this approach:** For each block, find the farthest distance to any required amenity. Pick the block with the smallest max distance. Binary search on sorted amenity position lists gives O(log k) lookup.

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
| **Time** | O(B × R × log K) — B blocks, R requirements, K amenity occurrences |
| **Space** | O(K) — amenity position map |

### Pattern Insight

**Binary Search on Sorted Lists + Greedy.** Build amenity → sorted position list. Binary search finds nearest block with each amenity.

### Variations

1. What if amenities have weights?
2. What if you can walk diagonally (Manhattan vs Euclidean)?
3. What if requirements change dynamically?
4. Are there multiple optimal blocks?
5. What if some amenities are optional?

---

## Capacity To Ship Package Within D Days

**Problem:** A conveyor belt has packages with given weights. You must ship them within `days` days in order (no reordering). Each day, you load as many as possible without exceeding the ship's capacity. Find the **minimum capacity** that makes shipping possible.

**Example:**
```
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: Day1: 1+2+3+4+5=15, Day2: 6+7=13, Day3: 8, Day4: 9, Day5: 10
```

**Why binary search:** Capacity is between max(weight) and sum(weights). The predicate `canShip(capacity)` is monotonic — if capacity works, any larger capacity works. Binary search finds the minimum.

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
| **Time** | O(N log S) — N packages, S = sum weights |
| **Space** | O(1) |

### Pattern Insight

**Minimize Max with Binary Search.** Classic "minimize maximum" pattern. Define a feasibility check, binary search the answer.

### Variations

1. What if packages can be reordered?
2. What if you must use exactly D days?
3. What if multiple ships run in parallel?
4. What if packages have dependencies?
5. What if there's a fixed cost per day?

---

## Closest Subsequence Sum

**Problem:** Given an array `nums` and a `goal`, find the minimum absolute difference between `goal` and the sum of any subsequence of `nums`.

**Example:**
```
Input: nums = [5, -7, 3, 5], goal = 6
Output: 0 (subsequence [5,-7,3,5] = 6)
```

**Why meet-in-the-middle:** With n ≤ 40, 2^n is too large. Split in half: 2^(n/2) ≈ 1M. Generate all subset sums for each half, sort one, binary search for closest complement.

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
| **Time** | O(2^(n/2) log 2^(n/2)) — meet-in-the-middle |
| **Space** | O(2^(n/2)) |

### Pattern Insight

**Meet-in-the-Middle + Binary Search.** Split large search space, enumerate each half, combine with binary search.

### Variations

1. Exact match instead of closest?
2. Constrained subsequence length?
3. Unlimited element usage?
4. Larger n (≥ 60)?
5. Must pick at least one element?

---

## Find First And Last Position

**Problem:** Find first and last index of `target` in sorted array with duplicates. Return [-1, -1] if not found. O(log n) required.

**Example:**
```
Input: nums = [5,7,7,8,8,10], target = 8 → Output: [3,4]
Input: nums = [5,7,7,8,8,10], target = 6 → Output: [-1,-1]
```

**Why binary search:** Two binary searches — left boundary (first occurrence) and right boundary (last occurrence). When `nums[mid] == target`, don't stop — narrow toward one side.

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
| **Time** | O(log n) — two binary searches |
| **Space** | O(1) |

### Pattern Insight

**Left/Right Boundary Binary Search.** Modify standard search: when equal, keep narrowing toward the boundary you want.

### Variations

1. Count frequency of target in O(log n)?
2. Find range in rotated array?
3. Find closest element when target doesn't exist?
4. What if array is very large?
5. What if all elements are the same?

---

## Find K Closest Elements

**Problem:** Find k closest elements to x in sorted array `arr`. Return in sorted order. Distance: |a - x| < |b - x|, or if equal, smaller element wins.

**Example:**
```
Input: arr = [1,2,3,4,5], k = 4, x = 3 → Output: [1,2,3,4]
Input: arr = [1,2,3,4,5], k = 4, x = -1 → Output: [1,2,3,4]
```

**Why binary search:** Find the **start** of the k-element window, not individual elements. Compare `x - arr[mid]` vs `arr[mid + k] - x` to decide direction.

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
| **Time** | O(log(n-k) + k) |
| **Space** | O(k) |

### Pattern Insight

**Binary Search for Window Position.** Find window start by comparing boundary elements. Once positioned, collect k elements.

### Variations

1. x outside array range?
2. All elements equally close?
3. Array not sorted?
4. k > n?
5. Duplicates?

---

## Find Minimum In Rotated Sorted Array

**Problem:** Find minimum in rotated sorted array (distinct elements). O(log n) required.

**Example:**
```
Input: nums = [3,4,5,1,2] → Output: 1
Input: nums = [4,5,6,7,0,1,2] → Output: 0
```

**Why binary search:** In a rotated sorted array, the minimum is the pivot where order breaks. Compare `nums[mid]` with `nums[right]` — if mid > right, pivot is on the right.

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

### Pattern Insight

**Rotated Array Binary Search.** Compare mid with right boundary to find the sorted half vs the rotated half.

### Variations

1. With duplicates?
2. Find maximum instead?
3. Search for a target in rotated array?
4. Count rotations?
5. Multiple rotations?

---

## Find Peak Element
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
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Find Peak Element Better Solution

Same as Find Peak Element but with explicit boundary safety — out-of-bounds treated as `Int.MIN_VALUE`.

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

### Variations

Same as Find Peak Element.

---

## First Bad Version

**Problem:** Find the first bad version in versions [1..n] using `isBadVersion(version)` API. All subsequent versions after a bad one are also bad. Minimize API calls.

**Example:**
```
n = 5, bad = 4
isBadVersion(3) → false
isBadVersion(5) → true
isBadVersion(4) → true
Output: 4
```

**Why binary search:** The predicate `isBadVersion(v)` is monotonic (false → true exactly once). Binary search finds the first true in O(log n) calls.

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

### Pattern Insight

**First True (Left Boundary).** The textbook example of left-boundary binary search on a monotonic predicate.

### Variations

1. Last good version instead?
2. Multiple bad ranges?
3. Rate-limited API?
4. Unknown n in advance?
5. Skipped version numbers?

---

## Guess Number Higher Or Lower

**Problem:** Pick a number from 1 to n. API `guess(num)` returns -1 (too high), 1 (too low), or 0 (correct). Find the number.

**Example:**
```
n = 10, pick = 6
guess(5) → 1, guess(8) → -1, guess(6) → 0
Output: 6
```

**Why binary search:** Standard binary search on an integer range. The guess API provides the comparison.

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

### Pattern Insight

**Standard Binary Search.** Pure form — the guess API is the comparison function.

### Variations

1. Unreliable API (occasional lies)?
2. 64-bit range?
3. Limited number of guesses?
4. Unknown range?
5. Multiple correct numbers?

---

## House Robber_IV
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
| **Time** | O(log n) |
| **Space** | O(1) |
---
## K Th Missing Positive Number
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
| **Time** | O(log n) |
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
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Random Pick With Weight
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
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Search A2d Matrix
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
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Search In Rotated Array_II
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
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Search In Rotated Sorted Array
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
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Search Insertion Position
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
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Single Element In A Sorted Array
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
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Valley Element
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
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Key Takeaways

1. **Core pattern recognition** — Sorted array + search → Binary Search. The key insight: find a predicate that splits the search space into 'yes' and 'no', then binary search finds the transition point.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

---
layout: chapter
title: "Arrays & Two Pointers"
chapter_number: 3
chapter_title: "Arrays & Two Pointers"
toc: true
prev_chapter:
  url: "/chapters/02-dynamic-programming.html"
  title: "Dynamic Programming"
next_chapter:
  url: "/chapters/04-linked-lists.html"
  title: "Linked Lists"
---

# Arrays & Two Pointers

> **38 problems** — Master array manipulation, two-pointer technique, and sliding windows.

## The Pattern

Two pointers create O(n) passes where brute force would be O(n^2).

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [4sum](#4sum) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Add Strings](#addstrings) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [List Node](#addtwonumbers) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Can Place Flowers](#canplaceflowers) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [Container With Most Water](#containerwithmostwater) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Contains Duplicate_II](#containsduplicate_ii) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [Contiguous Array](#contiguousarray) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [Continuous Subarray Sum](#continuoussubarraysum) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Diagonal Traverse](#diagonaltraverse) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Point](#diagonaltraverse_ii) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [Randomized Set](#insertdeletegetrandomato1) | — | <span class="badge badge-medium">Medium</span> |
| 12 | [Interval List Intersection](#intervallistintersection) | — | <span class="badge badge-medium">Medium</span> |
| 13 | [K Items With Maximum Sum](#kitemswithmaximumsum) | — | <span class="badge badge-medium">Medium</span> |
| 14 | [Linked List Random Node](#linkedlistrandomnode) | — | <span class="badge badge-medium">Medium</span> |
| 15 | [Merge Intervals](#mergeintervals) | — | <span class="badge badge-medium">Medium</span> |
| 16 | [Merge Sorted Array](#mergesortedarray) | — | <span class="badge badge-medium">Medium</span> |
| 17 | [Missing Ranges](#missingranges) | — | <span class="badge badge-medium">Medium</span> |
| 18 | [Move Zeroes](#movezeroes) | — | <span class="badge badge-medium">Medium</span> |
| 19 | [Next Permutation](#nextpermutation) | — | <span class="badge badge-medium">Medium</span> |
| 20 | [Palindrome Number](#palindromenumber) | — | <span class="badge badge-medium">Medium</span> |
| 21 | [Plus One](#plusone) | — | <span class="badge badge-medium">Medium</span> |
| 22 | [Remove Element](#removeelement) | — | <span class="badge badge-medium">Medium</span> |
| 23 | [Reservoir Sampling](#reservoirsampling) | — | <span class="badge badge-medium">Medium</span> |
| 24 | [Rotate Array](#rotatearray) | — | <span class="badge badge-medium">Medium</span> |
| 25 | [Rotate Image](#rotateimage) | — | <span class="badge badge-medium">Medium</span> |
| 26 | [Search A2d Matrix_II](#searcha2dmatrix_ii) | — | <span class="badge badge-medium">Medium</span> |
| 27 | [Shortest Path In Binary Matrix](#shortestpathinbinarymatrix) | — | <span class="badge badge-medium">Medium</span> |
| 28 | [Sign Of The Product Of An Array](#signoftheproductofanarray) | — | <span class="badge badge-medium">Medium</span> |
| 29 | [Sort Colors](#sortcolors) | — | <span class="badge badge-medium">Medium</span> |
| 30 | [Spiral Matrix](#spiralmatrix) | — | <span class="badge badge-medium">Medium</span> |
| 31 | [Spiral Matrix_II](#spiralmatrix_ii) | — | <span class="badge badge-medium">Medium</span> |
| 32 | [Squares Of A Sorted Array](#squaresofasortedarray) | — | <span class="badge badge-medium">Medium</span> |
| 33 | [Three Sum](#threesum) | — | <span class="badge badge-medium">Medium</span> |
| 34 | [Three Sum Closest](#threesumclosest) | — | <span class="badge badge-medium">Medium</span> |
| 35 | [Toeplitz Matrix](#toeplitzmatrix) | — | <span class="badge badge-medium">Medium</span> |
| 36 | [Transpose Matrix](#transposematrix) | — | <span class="badge badge-medium">Medium</span> |
| 37 | [Trapping Rain Water](#trappingrainwater) | — | <span class="badge badge-medium">Medium</span> |
| 38 | [Two Sum_II](#twosum_ii) | — | <span class="badge badge-medium">Medium</span> |

---

## 4sum

### Problem

Solves the 4sum problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.twopointer

class `4Sum` {
    /**
    * Solves the 4sum problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    fun fourSum(nums: IntArray, target: Int): List<List<Int>> {
        nums.sort()
        return kSum(nums, target.toLong(), 0, 4)
    }

    /**
    * Helper: k sum.
    *
    * @param nums The input array of integers.
    * @param target The long integer parameter representing target.
    * @param start The integer parameter representing start.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    private fun kSum(
        nums: IntArray,
        target: Long,
        start: Int,
        k: Int
    ): List<List<Int>> {
        val res = mutableListOf<List<Int>>()

        // If we've run out of numbers to add, return res.
        if (start == nums.size) {
            return res
        }

        // The average of the remaining k values is at least target / k.
        val averageValue = target / k

        // Early termination if the smallest number is too large or the largest is too small.
        if (nums[start] > averageValue || averageValue > nums[nums.size - 1]) {
            return res
        }

        // Base case: 2Sum (optimized with two pointers)
        if (k == 2) {
            return twoSum(nums, target, start)
        }

        for (i in start until nums.size) {
            // Skip duplicates
            if (i == start || nums[i - 1] != nums[i]) {
                // Recursively reduce to (k-1)Sum
                for (subset in kSum(nums, target - nums[i], i + 1, k - 1)) {
                    res.add(listOf(nums[i]) + subset)
                }
            }
        }

        return res
    }

    /**
    * Helper: two sum.
    *
    * @param nums The input array of integers.
    * @param target The long integer parameter representing target.
    * @param start The integer parameter representing start.
    * @return The computed integer result.
    */
    private fun twoSum(
        nums: IntArray,
        target: Long,
        start: Int
    ): List<List<Int>> {
        val res = mutableListOf<List<Int>>()
        val seen = HashSet<Long>()

        for (i in start until nums.size) {
            // Skip duplicates
            if (res.isEmpty() || res.last()[1] != nums[i]) {
                val complement = target - nums[i]
                if (seen.contains(complement)) {
                    res.add(listOf(complement.toInt(), nums[i]))
                }
            }
            seen.add(nums[i].toLong())
        }

        return res
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
## Add Strings

### Problem

Solves the Add Strings problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package math

class AddStrings {
    /**
    * Solves the Add Strings problem.
    * Takes `num1` (string), `num2` (string).
    *
    * @param num1 The input string.
    * @param num2 The input string.
    * @return The resulting string.
    */
    fun addStrings(num1: String, num2: String): String {
        val sb = StringBuilder()
        var (i, j) = num1.length - 1 to num2.length - 1
        var carry = 0

        // Process digits from right to left
        while (i >= 0 || j >= 0 || carry != 0) {
            // Get the current digits (or 0 if we've run out of digits)
            val digit1 = if (i >= 0) num1[i--] - '0' else 0
            val digit2 = if (j >= 0) num2[j--] - '0' else 0

            // Calculate the sum of digits and the carry
            val sum = digit1 + digit2 + carry
            carry = sum / 10  // New carry for the next iteration
            sb.append(sum % 10)  // Append the current digit (sum % 10)
        }

        // The string is built in reverse order, so we need to reverse it
        return sb.reverse().toString()
    }
}
```


### Pattern Insight

**Pattern:** Bit manipulation. Use bitwise operations for fast computation and compact state tracking.


### Pattern Insight

Study the code and identify the algorithmic pattern.

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
## List Node

### Problem

Solves the List Node problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package linkedlist

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class AddTwoNumbers {
    /**
    * Solves the List Node problem.
    * Takes `l1` (linked list node reference), `l2` (linked list node reference).
    *
    * @param l1 The input linked list node reference.
    * @param l2 The input linked list node reference.
    * @return The resulting collection (linked list node reference).
    */
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var carry = 0
        val head = ListNode(0)
        var ptr = head
        var (n1, n2) = Pair(l1, l2)

        while (n1!= null || n2 != null) {
            val sum = (n1?.`val` ?: 0) + (n2?.`val` ?: 0) + carry
            ptr.next = ListNode(sum % 10)
            ptr = ptr.next!!

            carry = if (sum > 9) 1 else 0

            if (n1 != null) n1 = n1.next

            if (n2 != null) n2 = n2.next
        }

        if (carry > 0) {
            ptr.next = ListNode(carry)
        }

        return head.next
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
## Can Place Flowers

### Problem

Solves the Can Place Flowers problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.greedy

class CanPlaceFlowers {
    /**
    * Solves the Can Place Flowers problem.
    * Takes `flowerbed` (array of integers), `n` (integer).
    *
    * @param flowerbed The input array of integers.
    * @param n The integer parameter representing n.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
        var flowers = 0
        for (i in 0 until flowerbed.size) {
            val isLeftEmpty = ( i == 0 || flowerbed[i-1] == 0)
            val isRightEmpty = ( i == flowerbed.lastIndex || flowerbed[i+1] == 0 )
            if ( flowerbed[i] == 0 && isLeftEmpty && isRightEmpty ) {
                flowers++
                flowerbed[i] = 1
            }

            if (flowers >= n) {
                return true
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
xity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Contains Duplicate_II

### Problem

Solves the Contains Duplicate_II problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.hashtable

class ContainsDuplicate_II {
    /**
    * Solves the Contains Duplicate_II problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
        val map = mutableMapOf<Int, Int>()
        for (i in nums.indices) {
            val previousIndex = map[nums[i]]

            previousIndex?.let {  if ( i - it <= k) return true }
            map[nums[i]] = i
        }

        return false
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
pOf<Int, Int>()
        var sum = 0
        var maxLen = 0

        map[0] = -1

        for (i in nums.indices) {
            sum += if (nums[i] == 0) -1 else 1

            if (map.containsKey(sum)) {
                maxLen = maxOf(maxLen, i - map[sum]!!)
            } else {
                map[sum] = i
            }
        }

        return maxLen
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

    * @return `true` if the condition is met, `false` otherwise.
    */
    fun checkSubarraySum(nums: IntArray, k: Int): Boolean {
        val sumsSet: HashSet<Int> = HashSet(nums.size)
        var sum = 0
        var prevSum: Int

        for (num in nums) {
            prevSum = sum
            sum = (sum + num) % k
            if (sumsSet.contains(sum)) {
                return true
            }
            sumsSet.add(prevSum)
        }

        return false
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
istOf<Int>()  // List to store the diagonal traversal result

        var i = 0  // Row index
        var j = 0  // Column index
        var direction = Direction.UP  // Start moving diagonally in the UP direction

        // Continue traversing until we collect all matrix elements
        while (result.size < m * n) {
            // Add the current element to the result list
            result.add(mat[i][j])

            // Handle the change in direction and boundary checks using `when`
            direction = when (direction) {
                Direction.UP -> when {
                    // If we're at the top row (i == 0) or last column (j == n - 1)
                    i == 0 || j == n - 1 -> {
                        // If at the last column, move down
                        // Otherwise, move right
                        if (j == n - 1) i++ else j++
                        Direction.DOWN  // Switch direction to DOWN
                    }
                    else -> {
                        // Otherwise, continue moving up-left: decrement i and increment j
                        i--; j++
                        Direction.UP  // Continue moving UP
                    }
                }
                Direction.DOWN -> when {
                    // If we're at the left column (j == 0) or last row (i == m - 1)
                    j == 0 || i == m - 1 -> {
                        // If at the last row, move right
                        // Otherwise, move down
                        if (i == m - 1) j++ else i++
                        Direction.UP  // Switch direction to UP
                    }
                    else -> {
                        // Otherwise, continue moving down-right: increment i and decrement j
                        i++; j--
                        Direction.DOWN  // Continue moving DOWN
                    }
                }
            }
        }

        // Convert the result list to an array and return it
        return result.toIntArray()
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Point

### Problem

Solves the Point problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array

import java.util.*

data class Point(val row: Int, val col: Int)

class DiagonalTraverse_II {
    /**
    * Solves the Point problem.
    * Takes `nums` (2D list of integers).
    *
    * @param nums The input 2D list of integers.
    * @return The computed integer result.
    */
    fun findDiagonalOrder(nums: List<List<Int>>): List<Int> {
        val result = mutableListOf<Int>()
        val queue: Queue<Pair<Int, Int>> = LinkedList()
        val visited = mutableSetOf<Pair<Int, Int>>()

        // Start with the first element
        queue.offer(0 to 0)

        while (queue.isNotEmpty()) {
            val (i, j) = queue.poll()
            result.add(nums[i][j])

            // Move to the next row (i+1, j)
            if (i + 1 < nums.size && j < nums[i + 1].size) {
                queue.offer(i + 1 to j)
                visited.add(i + 1 to j)
            }

            // Move to the next column (i, j+1)
            if (j + 1 < nums[i].size) {
                queue.offer(i to j + 1)
                visited.add(i to j + 1)
            }
        }

        return result
    }
}
```


### Pattern Insight

Study the code and identify the algorithmic pattern.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations


---
)
        list[index] = lastElement
        map[lastElement] = index

        list.removeLast()
        map.remove(`val`)

        return true
    }

    /**
    * Solves the Randomized Set problem.
    *
    * @return The computed integer result.
    */
    fun getRandom(): Int {
        return list[Random.nextInt(list.size)]
    }

}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Interval List Intersection

### Problem

Solves the Interval List Intersection problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.twopointer

class IntervalListIntersection {
    /**
    * Solves the Interval List Intersection problem.
    * Takes `firstList` (2D matrix of integers), `secondList` (2D matrix of integers).
    *
    * @param firstList The input 2D matrix of integers.
    * @param secondList The input 2D matrix of integers.
    * @return The computed integer result.
    */
    fun intervalIntersection(firstList: Array<IntArray>, secondList: Array<IntArray>): Array<IntArray> {
        val result = mutableListOf<IntArray>()

        var (i, j) = 0 to 0

        while (i < firstList.size && j < secondList.size) {
            val (start1, end1) = firstList[i]
            val (start2, end2) = secondList[j]

            val startMax = maxOf(start1, start2)
            val endMin = minOf(end1, end2)

            if (startMax <= endMin) {
                result.add(intArrayOf(startMax, endMin))
            }

            if (end1 < end2) i++ else j++
        }

        return result.toTypedArray()
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## K Items With Maximum Sum

### Problem

Solves the KItems With Maximum Sum problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.greedy

class KItemsWithMaximumSum {
    /**
    * Solves the KItems With Maximum Sum problem.
    * Takes `numOnes` (integer), `numZeros` (integer), `numNegOnes` (integer), `k` (integer).
    *
    * @param numOnes The integer parameter representing numOnes.
    * @param numZeros The integer parameter representing numZeros.
    * @param numNegOnes The integer parameter representing numNegOnes.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    fun kItemsWithMaximumSum(numOnes: Int, numZeros: Int, numNegOnes: Int, k: Int): Int {
        var (K, ones, zeroes, negatives, sum) = listOf( k, numOnes,numZeros, numNegOnes, 0 )
        while (K-- > 0) {
            when {
                ones > 0 -> {
                    sum+= 1
                    ones--
                }
                zeroes == 0 && negatives > 0 ->   {
                    sum-=1
                    negatives--
                }
                else -> zeroes--
            }
        }

        return sum
    }

    // Alternative way
    /**
    * Solves the KItems With Maximum Sum problem.
    * Takes `numOnes` (integer), `numZeros` (integer), `numNegOnes` (integer), `k` (integer).
    *
    * @param numOnes The integer parameter representing numOnes.
    * @param numZeros The integer parameter representing numZeros.
    * @param numNegOnes The integer parameter representing numNegOnes.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    fun kItemsWithMaximumSumAlternative(numOnes: Int, numZeros: Int, numNegOnes: Int, k: Int): Int {

        if(k <= numOnes)
            return k

        if(k <= numOnes + numZeros)
            return numOnes

        var remainingSum = k - (numOnes + numZeros)

        return numOnes - remainingSum

    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Linked List Random Node

### Problem

Solves the Linked List Random Node problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package probability

import linkedlist.ListNode
import kotlin.random.Random

class LinkedListRandomNode (private val head: ListNode?) {
    /**
    * Solves the Linked List Random Node problem.
    *
    * @return The computed integer result.
    */
    fun getRandom(): Int {
        var (count, result) = 0 to 0
        var ptr = head

        while (ptr != null) {
            count++

            if (Random.nextInt(count) == 0) {
                result = ptr.`val`
            }

            ptr = ptr.next
        }

        return result
    }

    // Another possible solution
    /**
    * Solves the Linked List Random Node problem.
    *
    * @return The computed integer result.
    */
    fun getRandom_2(): Int {
        var current = head
        var result = current?.`val` ?: throw IllegalArgumentException("List is empty")
        var count = 0

        while (current != null) {
            count++
            // Select the current node if Random.nextInt(count) == count - 1
            if (Random.nextInt(count) == count - 1) {
                result = current.`val`
            }
            current = current.next
        }

        return result
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Merge Intervals

### Problem

Solves the Merge Intervals problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array

class MergeIntervals {
    /**
    * Solves the Merge Intervals problem.
    * Takes `intervals` (2D matrix of integers).
    *
    * @param intervals The input 2D matrix of integers.
    * @return The computed integer result.
    */
    fun merge(intervals: Array<IntArray>): Array<IntArray> {
        // Sort the internals by start
        intervals.sortWith(compareBy { it[0] })
        var index = 0
        for (i in 1..intervals.lastIndex) {
            if (intervals[i][0] > intervals[index][1]) {
                intervals[++index] = intervals[i]
            } else {
                intervals[index][1] = maxOf(intervals[index][1], intervals[i][1])
            }
        }

        return intervals.copyOfRange(0, index + 1)
    }
}
```


### Pattern Insight

**Pattern:** BFS (Breadth-First Search). Use a queue to explore nodes level by level, guaranteeing shortest path in unweighted graphs.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

### Variations

1. What if the graph is disconnected?
1. What if edges have weights (non-uniform cost)?
1. Can this be solved with DFS instead? What's the tradeoff?
1. What if you need the path, not just the distance/existence?
1. What if the graph is too large for BFS? Iterative deepening?

---
ontentToString())
    }

    companion object {
        @JvmStatic
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        fun main(args: Array<String>) {
            val testClass = MergeSortedArray()

            // Declaring a 2d Array in Kotlin is tricky
            // Not that Bad. It's still idiomatic and nice....
            var arr = Array(5) { IntArray(6)}


            testClass.merge(intArrayOf(1,5,7,8, 0, 0, 0), 4, intArrayOf(3,6,17),3)
        }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Missing Ranges

### Problem

Solves the Missing Ranges problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array

class MissingRanges {
    /**
    * Solves the Missing Ranges problem.
    * Takes `nums` (array of integers), `lower` (integer), `upper` (integer).
    *
    * @param nums The input array of integers.
    * @param lower The integer parameter representing lower.
    * @param upper The integer parameter representing upper.
    * @return The computed integer result.
    */
    fun findMissingRanges(nums: IntArray, lower: Int, upper: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        var currentRangePointer = lower

        for(num in nums) {
            if (num > currentRangePointer)
                result.add(listOf(currentRangePointer, num - 1))
            currentRangePointer = num + 1
        }

        if (currentRangePointer <= upper) {
            result.add(listOf(currentRangePointer, upper))
        }

        return result
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

## Move Zeroes

### Problem

Solves the Move Zeroes problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array

class MoveZeroes {
    /**
    * Solves the Move Zeroes problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return Unit (no return value, modifies state in-place).
    */
    fun moveZeroes(nums: IntArray): Unit {
        var nonZeroPointer = 0

        // Move all non-zero elements to the front
        for (i in nums.indices) {
            if (nums[i] != 0) {
                nums[nonZeroPointer++] = nums[i]
            }
        }

        // Fill the rest of the array with zeros
        while (nonZeroPointer < nums.size) {
            nums[nonZeroPointer++] = 0
        }
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
roblem.
    * Takes `nums` (array of integers), `startIndex` (integer).
    *
    * @param nums The input array of integers.
    * @param startIndex The integer parameter representing startIndex.
    * @return Unit (no return value, modifies state in-place).
    */
    fun reverse(nums: IntArray, startIndex: Int) {
        var (left, right) = Pair(startIndex, nums.lastIndex)
        while(left < right) {
            swap(nums, left++, right--)
        }
    }

    /**
    * Solves the Next Permutation problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun nextPermutation(nums: IntArray): Boolean {
        var index = nums.lastIndex - 1

        // Find increasing sequence right to left
        // Intuition: By traversing from right to left and finding the first pair where nums[index] < nums[index + 1],
        // we identify the pivot point where the next permutation should change.
        // If no such point exists (i.e., the array is in descending order), the array is the highest permutation
        // and should be reversed to form the lowest permutation.
        while (index >=0 && nums[index] >= nums[index + 1]) {
            index --
        }

        // If all the sequence from right to left
        if (index < 0) {
            reverse(nums, 0)
            return false
        }

        // index is reduced by 1 in while loop. Hence incrementing to get the highest number
        // in this increasing sequence
        index++
        var pivot = nums[index - 1]
        var indexToSwap = index

        // Find index to swap such that nums[indexToSwap] > nums[pivot]
        // Intuition: By finding the smallest element greater than nums[index - 1] from the right part of the array,
        // we ensure that the next permutation is the smallest lexicographical order greater than the current one.
        for (i in index until nums.size) {
            if (nums[i] > pivot) {
                indexToSwap = i
            }
        }

        swap(nums, indexToSwap, index - 1)
        reverse(nums, index)
        return true
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Palindrome Number

### Problem

Solves the Palindrome Number problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package numbers

class PalindromeNumber {
    /**
    * Solves the Palindrome Number problem.
    * Takes `x` (integer).
    *
    * @param x The integer parameter representing x.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isPalindrome(x: Int): Boolean {
        var (reduced, sum) = listOf(x, 0, 1)

        while (reduced > 0)  {
            sum = sum * 10 + reduced % 10
            reduced /= 10
        }
        return sum == x
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Plus One

### Problem

Solves the Plus One problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package math

class PlusOne {
    /**
    * Solves the Plus One problem.
    * Takes `digits` (array of integers).
    *
    * @param digits The input array of integers.
    * @return The computed integer result.
    */
    fun plusOne(digits: IntArray): IntArray {
        for (i in digits.lastIndex downTo 0) {
            if (digits[i] < 9) {
                digits[i]++
                return digits
            }
            digits[i] = 0
        }

        return intArrayOf(1) + digits
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Remove Element

### Problem

Solves the Remove Element problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array

class RemoveElement {
    /**
    * Solves the Remove Element problem.
    * Takes `nums` (array of integers), ``val`` (integer).
    *
    * @param nums The input array of integers.
    * @param `val` The integer parameter representing `val`.
    * @return The computed integer result.
    */
    fun removeElement(nums: IntArray, `val`: Int): Int {
        var i = 0

        for (j in nums.indices) {
            if (nums[j] != `val`) {
                nums[i++] = nums[j]
            }
        }

        return i
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Reservoir Sampling

### Problem

Solve the **Reservoir Sampling** problem efficiently.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package probability

import kotlin.random.Random

class ReservoirSampling {
    fun <T> reservoirSampling(stream: Sequence<T>, k: Int): List<T> {
        val reservoir = mutableListOf<T>()
        var count = 0

        stream.forEach { item ->
            count++
            when {
                count <= k -> reservoir.add(item)
                else -> {
                    val index = Random.nextInt(count)
                    // Replace item
                    if ( index < k)
                        reservoir[index] = item
                }
            }
        }

        return reservoir
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
 0, n - 1)
        reverse(nums, 0, steps - 1)
        reverse(nums, steps, n - 1)
    }

    /**
    * Helper: reverse.
    *
    * @param nums The input array of integers.
    * @param start The integer parameter representing start.
    * @param end The integer parameter representing end.
    * @return Unit (no return value, modifies state in-place).
    */
    private fun reverse(nums: IntArray, start: Int, end: Int): Unit {
        var s = start
        var e = end
        while (s < e) {
            nums[s] = nums[e].also { nums[e] = nums[s] }
            s++
            e--
        }
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
  */
    fun rotate(matrix: Array<IntArray>): Unit {
        for (i in matrix.indices)
            for (j in i until matrix[i].size) {
            swap(matrix, i, j, j, i)
        }

        for (i in matrix.indices) {
            var l = 0
            var r: Int = matrix[i].size - 1
            while (l < r) {
                swap(matrix, i, l, i, r)
                l++
                r--
            }
        }
    }

    /**
    * Solves the Rotate Image problem.
    * Takes `matrix` (2D matrix of integers), `i` (integer), `j` (integer), `m` (integer), `n` (integer).
    *
    * @param matrix The input 2D matrix of integers.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @param m The integer parameter representing m.
    * @param n The integer parameter representing n.
    * @return Unit (no return value, modifies state in-place).
    */
    fun swap(matrix: Array<IntArray>, i: Int, j: Int, m: Int, n: Int) {
        matrix[i][j] = matrix[m][n].also { matrix[m][n] = matrix[i][j] }
    }
}

/**
 * 1,2,3
 * 4,5,6
 * 7,8,9
 *
 * 1,4,7
 * 2,5,8
 * 3,6,9
 */
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
erwise.
    */
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        var (row, col) = matrix.size - 1 to 0

        while (row >=0 && col < matrix[0].size) {
            when {
                matrix[row][col] > target -> row--
                matrix[row][col] < target -> col++
                else -> return true
            }
        }

        return false
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
  -1 to -1, -1 to 1, 1 to -1, 1 to 1 // Diagonal directions
        )

        val queue = LinkedList<State>()
        queue.add(State(0, 0, 1))  // Start at (0,0) with distance 1

        while (queue.isNotEmpty()) {
            val (row, col, dist) = queue.poll()

            // If we reached the bottom-right corner
            if (row == n - 1 && col == m - 1) return dist

            // Explore all 8 possible directions
            for ((dr, dc) in directions) {
                val (newRow, newCol) = row + dr to col + dc

                // Skip invalid positions or visited cells
                if (newRow !in 0 until n || newCol !in 0 until m || grid[newRow][newCol] != 0)
                    continue

                // Mark the cell as visited and add it to the queue
                grid[newRow][newCol] = 2
                queue.add(State(newRow, newCol, dist + 1))
            }
        }

        return -1  // No path found
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Sign Of The Product Of An Array

### Problem

Solves the Sign Of The Product Of An Array problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array

class SignOfTheProductOfAnArray {
    /**
    * Solves the Sign Of The Product Of An Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun arraySign(nums: IntArray): Int {
        var negativeCount = 0

        nums.forEach {
            if (it == 0)    return 0
            if (it < 0) negativeCount++
        }

        return when {
            negativeCount % 2 == 0 -> 1
            else -> -1
        }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Sort Colors

### Problem

Solves the Sort Colors problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.sorting

class SortColors {
    /**
    * Solves the Sort Colors problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return Unit (no return value, modifies state in-place).
    */
    fun sortColors(nums: IntArray): Unit {
        /**
        * Solves the Sort Colors problem.
        * Takes `i` (integer), `j` (integer).
        *
        * @param i The integer parameter representing i.
        * @param j The integer parameter representing j.
        * @return Unit (no return value, modifies state in-place).
        */
        fun swap(i: Int, j: Int) {
            nums[i] = nums[j].also { nums[j] = nums[i] }
        }

        var (low, high) = 0 to nums.size - 1
        var i = 0

        while (i <= high) {
            when (nums[i]) {
                0 -> swap(i++, low++)
                1 -> i++
                2 -> swap(i, high--)
            }
        }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Spiral Matrix

### Problem

Solves the Spiral Matrix problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array

class SpiralMatrix {
    /**
    * Solves the Spiral Matrix problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return The computed integer result.
    */
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {
        if (matrix.isEmpty()) return emptyList()

        val result = mutableListOf<Int>()
        var (top, bottom, left, right) = listOf(0, matrix.size - 1, 0, matrix[0].size - 1)
        var count = 0
        val totalElements = matrix.size * matrix[0].size

        while (count < totalElements) {
            // Traverse top row
            for (j in left..right) if (count++ < totalElements) result.add(matrix[top][j])
            top++

            // Traverse right column
            for (i in top..bottom) if (count++ < totalElements) result.add(matrix[i][right])
            right--

            // Traverse bottom row
            for (j in right downTo left) if (count++ < totalElements) result.add(matrix[bottom][j])
            bottom--

            // Traverse left column
            for (i in bottom downTo top) if (count++ < totalElements) result.add(matrix[i][left])
            left++
        }

        return result
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Spiral Matrix_II

### Problem

Solves the Spiral Matrix_II problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array

class SpiralMatrix_II {
    class Solution {
        /**
        * Solves the Spiral Matrix_II problem.
        * Takes `n` (integer).
        *
        * @param n The integer parameter representing n.
        * @return The computed integer result.
        */
        fun generateMatrix(n: Int): Array<IntArray> {
            val matrix = Array(n) { IntArray(n) }
            var (top, bottom, left, right, num) = arrayOf(0, n - 1, 0, n - 1, 1)

            while (top <= bottom && left <= right) {
                // Fill top row
                for (i in left..right) matrix[top][i] = num++
                top++

                // Fill right column
                for (i in top..bottom) matrix[i][right] = num++
                right--

                // Fill bottom row
                if (top <= bottom) {
                    for (i in right downTo left) matrix[bottom][i] = num++
                    bottom--
                }

                // Fill left column
                if (left <= right) {
                    for (i in bottom downTo top) matrix[i][left] = num++
                    left++
                }
            }

            return matrix
        }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Squares Of A Sorted Array

### Problem

Solves the Squares Of ASorted Array problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.sorting

import kotlin.math.abs

class SquaresOfASortedArray {
    /**
    * Solves the Squares Of ASorted Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun sortedSquares(nums: IntArray): IntArray {
        val result = IntArray(nums.size)

        var (left, right, index) = listOf(0, nums.lastIndex, nums.lastIndex)

        while (left <= right) {
            when {
                abs(nums[left]) > abs(nums[right]) -> result[index--] = nums[left] * nums[left++]
                else -> result[index--] = nums[right] * nums[right--]
            }
        }

        return result
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Three Sum

### Problem

Solves the Three Sum problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.twopointer


class ThreeSum {
    /**
    * Solves the Three Sum problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun threeSum(nums: IntArray): List<List<Int>> {
        val result = mutableSetOf<List<Int>>()
        nums.sort()

        for (i in nums.indices) {

            if (i > 0 && nums[i] == nums[i - 1]) continue

            var start = i + 1
            var end = nums.lastIndex

            while (start < end) {
                val sum = nums[start] + nums[end] + nums[i]
                when {
                    sum == 0 -> {
                        result.add(listOf(nums[i], nums[start], nums[end]))

                        // Skip duplicates for the second and third numbers
                        while (start < end && nums[start] == nums[start + 1]) start++
                        while (start < end && nums[end] == nums[end - 1]) end--

                        start++
                        end--
                    }
                    sum > 0 -> end--
                    else -> start++
                }
            }
        }

        return result.toList()
    }

    // This can be done using set too . Reducing it to 2 sum problem.
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Three Sum Closest

### Problem

Solves the Three Sum Closest problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.twopointer

import kotlin.math.abs

class ThreeSumClosest {
    /**
    * Solves the Three Sum Closest problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    fun threeSumClosest(nums: IntArray, target: Int): Int {
        nums.sort()
        var closestSum = nums[0] + nums[1] + nums[2]

        for (i in 0 until nums.size - 2) {
            var left = i + 1
            var right = nums.size - 1

            while (left < right) {
                val sum = nums[i] + nums[left] + nums[right]
                if (abs(target - sum) < abs(target - closestSum)) {
                    closestSum = sum
                }
                when {
                    sum < target -> left++
                    sum > target -> right--
                    else -> return sum
                }
            }
        }
        return closestSum
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Toeplitz Matrix

### Problem

Solves the Toeplitz Matrix problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array

class ToeplitzMatrix {
    /**
    * Solves the Toeplitz Matrix problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isToeplitzMatrix(matrix: Array<IntArray>): Boolean {
        val m = matrix.size
        val n = matrix[0].size

        var row = m - 1
        var col = 0

        while (row < m && col < n) {
            var i = row
            var j = col

            val first = matrix[i][j]

            while (i < m && j < n) {
                if (matrix[i][j] != first)
                    return false
                i++
                j++
            }

            when(row) {
                0 -> col++
                else -> row --
            }
        }

        return true
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Transpose Matrix

### Problem

Solves the Transpose Matrix problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array

class TransposeMatrix {
    /**
    * Solves the Transpose Matrix problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return The computed integer result.
    */
    fun transpose(matrix: Array<IntArray>): Array<IntArray> {
        val rows = matrix.size
        val cols = matrix[0].size
        val transposed = Array(cols) { IntArray(rows) }

        for (i in matrix.indices) {
            for (j in matrix[i].indices) {
                transposed[j][i] = matrix[i][j]
            }
        }

        return transposed
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Trapping Rain Water

### Problem

Using Dynamic Programming.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.twopointer

class TrappingRainWater {
    /**
     * Using Dynamic Programming.
     */
    fun trap(height: IntArray): Int {
        val h = height.size
        if (h == 0) return 0

        val leftMax = IntArray(h).apply {
            this[0] = height[0]
            for (i in 1 until h) {
                this[i] = maxOf(this[i - 1], height[i])
            }
        }

        val rightMax = IntArray(h).also {
            it[h - 1] = height[h - 1]
            for (i in h - 2 downTo 0) {
                it[i] = maxOf(it[i + 1], height[i])
            }
        }

        return (0 until h).sumOf { i ->
            val minLeftRight = minOf(leftMax[i], rightMax[i])
            when {
                minLeftRight > height[i] -> minLeftRight - height[i]
                else -> 0
            }
        }

        // Another way
//        return (0 until n).sumOf { index ->
//            maxOf(minOf(leftMax[index], rightMax[index]) - height[index], 0)
//        }
    }

    // Two pointer method.
    /**
    * Solves the Trapping Rain Water problem.
    * Takes `height` (array of integers).
    *
    * @param height The input array of integers.
    * @return The computed integer result.
    */
    fun trapConstantSpace(height: IntArray): Int {
        var (left, right, leftMax, rightMax, waterTrapped) = listOf(0, height.lastIndex, 0, 0, 0)

        while (left <= right) {
            if (height[left] <= height[right]) {
                waterTrapped += (leftMax - height[left]).coerceAtLeast(0)
                leftMax = maxOf(leftMax, height[left])
                left++
            } else {
                waterTrapped += (rightMax - height[right]).coerceAtLeast(0)
                rightMax = maxOf(rightMax, height[right])
                right--
            }
        }

        return waterTrapped
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Two Sum_II

### Problem

Solves the Two Sum_II problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.twopointer

class TwoSum_II {
    /**
    * Solves the Two Sum_II problem.
    * Takes `numbers` (array of integers), `target` (integer).
    *
    * @param numbers The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    fun twoSum(numbers: IntArray, target: Int): IntArray {
        var start = 0
        var end = numbers.lastIndex

        while ( start < end ) {
            val sum = numbers[start] + numbers[end]

            when {
                sum == target -> {
                    return intArrayOf(start + 1, end + 1)
                }
                sum < target -> start++
                else -> end--
            }
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

---

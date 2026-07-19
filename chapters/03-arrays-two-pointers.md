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

Two pointers create an O(n) pass where a brute force would be O(n²). The pointers track a window, boundary, or comparison pair.

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

<span id="4sum"></span>

### Problem

**4Sum**

**Function:** `Four Sum` takes `nums` (array of integers), `target` (integer) and returns **List**.

**Key logic:**
- If we've run out of numbers to add, return res.
- The average of the remaining k values is at least target / k.
- Early termination if the smallest number is too large or the largest is too small.
- Base case: 2Sum (optimized with two pointers)
- Skip duplicates



### Approach

**Solution Approach:**
1. The main function `fourSum` processes the input
2. Uses helper functions: kSum, twoSum

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `res`, `averageValue`, `res`, `seen`, `complement`

**Execution flow:**
- If we've run out of numbers to add, return res.
- The average of the remaining k values is at least target / k.
- Early termination if the smallest number is too large or the largest is too small.
- Base case: 2Sum (optimized with two pointers)
- Skip duplicates
- Recursively reduce to (k-1)Sum
- Skip duplicates

### Code

```kotlin
package array.twopointer

class `4Sum` {
    fun fourSum(nums: IntArray, target: Int): List<List<Int>> {
        nums.sort()
        return kSum(nums, target.toLong(), 0, 4)
    }

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Add Strings

<span id="addstrings"></span>

### Problem

**Addstrings**

**Function:** `Add Strings` takes `num1` (string), `num2` (string) and returns **string**.

**Key logic:**
- Process digits from right to left
- Get the current digits (or 0 if we've run out of digits)
- Calculate the sum of digits and the carry
- New carry for the next iteration
- Append the current digit (sum % 10)



### Approach

**Solution Approach:**
1. The main function `addStrings` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `sb`, `carry`, `digit1`, `digit2`, `sum`

**Execution flow:**
- Process digits from right to left
- Get the current digits (or 0 if we've run out of digits)
- Calculate the sum of digits and the carry
- New carry for the next iteration
- Append the current digit (sum % 10)
- The string is built in reverse order, so we need to reverse it

### Code

```kotlin
package math

class AddStrings {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## List Node

<span id="addtwonumbers"></span>

### Problem

**Addtwonumbers**

**Function:** `Add Two Numbers` takes `l1` (ListNode?), `l2` (ListNode?) and returns **ListNode**.



### Approach

**Solution Approach:**
1. The main function `addTwoNumbers` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `next`, `carry`, `head`, `ptr`, `sum`

### Code

```kotlin
package linkedlist

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class AddTwoNumbers {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Can Place Flowers

<span id="canplaceflowers"></span>

### Problem

**Canplaceflowers**

**Function:** `Can Place Flowers` takes `flowerbed` (array of integers), `n` (integer) and returns **boolean**.



### Approach

**Solution Approach:**
1. The main function `canPlaceFlowers` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `flowers`, `isLeftEmpty`, `isRightEmpty`

### Code

```kotlin
package array.greedy

class CanPlaceFlowers {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Container With Most Water

<span id="containerwithmostwater"></span>

### Problem

**Containerwithmostwater**

**Function:** `Max Area` takes `height` (array of integers) and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `maxWater`

### Code

```kotlin
package array.greedy

class ContainerWithMostWater {
    fun maxArea(height: IntArray): Int {
        var (start, end) = Pair(0, height.lastIndex)
        var maxWater = 0
        while (start < end) {
            maxWater = maxOf(maxWater, minOf(height[start], height[end]) * (end - start))

            if (height[start] <= height[end]) {
                start++
            } else {
                end--
            }
        }

        return maxWater
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

## Contains Duplicate_II

<span id="containsduplicate_ii"></span>

### Problem

**Containsduplicate Ii**

**Function:** `Contains Nearby Duplicate` takes `nums` (array of integers), `k` (integer) and returns **boolean**.



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `map`, `previousIndex`

### Code

```kotlin
package array.hashtable

class ContainsDuplicate_II {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Contiguous Array

<span id="contiguousarray"></span>

### Problem

**Contiguousarray**

**Function:** `Find Max Length` takes `nums` (array of integers) and returns **integer**.



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `map`, `sum`, `maxLen`

### Code

```kotlin
package array.prefixsum

class ContiguousArray {
    fun findMaxLength(nums: IntArray): Int {
        val map = mutableMapOf<Int, Int>()
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Continuous Subarray Sum

<span id="continuoussubarraysum"></span>

### Problem

**Continuoussubarraysum**

**Function:** `Check Subarray Sum` takes `nums` (array of integers), `k` (integer) and returns **boolean**.

**Key logic:**
- Pattern https://leetcode.com/problems/continuous-subarray-sum/discuss/5276981/prefix-sum-hashmap-patterns-7-problems



### Approach

**Solution Approach:**
1. The main function `checkSubarraySum` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `sumsSet`, `sum`, `prevSum`

**Execution flow:**
- Pattern https://leetcode.com/problems/continuous-subarray-sum/discuss/5276981/prefix-sum-hashmap-patterns-7-problems

### Code

```kotlin
package array.prefixsum

// Pattern https://leetcode.com/problems/continuous-subarray-sum/discuss/5276981/prefix-sum-hashmap-patterns-7-problems
class ContinuousSubarraySum {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Diagonal Traverse

<span id="diagonaltraverse"></span>

### Problem

**Diagonaltraverse**

**Function:** `Find Diagonal Order` takes `mat` (Array<array of integers>) and returns **array of integers**.

**Key logic:**
- Enum to represent the direction of diagonal traversal: UP or DOWN
- Number of rows in the matrix
- Number of columns in the matrix
- List to store the diagonal traversal result
- Row index



### Approach

**Solution Approach:**
1. The main function `findDiagonalOrder` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `m`, `n`, `result`, `i`, `j`, `direction`

**Execution flow:**
- Enum to represent the direction of diagonal traversal: UP or DOWN
- Number of rows in the matrix
- Number of columns in the matrix
- List to store the diagonal traversal result
- Column index
- Start moving diagonally in the UP direction
- Continue traversing until we collect all matrix elements

### Code

```kotlin
package array

class DiagonalTraverse {
    // Enum to represent the direction of diagonal traversal: UP or DOWN
    enum class Direction {
        UP, DOWN
    }

    fun findDiagonalOrder(mat: Array<IntArray>): IntArray {
        val m = mat.size        // Number of rows in the matrix
        val n = mat[0].size     // Number of columns in the matrix
        val result = mutableListOf<Int>()  // List to store the diagonal traversal result

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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Point

<span id="diagonaltraverse_ii"></span>

### Problem

**Diagonaltraverse Ii**

**Function:** `Find Diagonal Order` takes `nums` (List<List<integer>>) and returns **List**.

**Key logic:**
- Start with the first element
- Move to the next row (i+1, j)
- Move to the next column (i, j+1)



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `row`, `col`, `result`, `queue`, `visited`

**Execution flow:**
- Start with the first element
- Move to the next row (i+1, j)
- Move to the next column (i, j+1)

### Code

```kotlin
package array

import java.util.*

data class Point(val row: Int, val col: Int)

class DiagonalTraverse_II {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Randomized Set

<span id="insertdeletegetrandomato1"></span>

### Problem

**Insertdeletegetrandomato1**

**Function:** `Insert` takes ``val`` (integer) and returns **boolean**.



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `list`, `map`, `index`, `lastElement`

### Code

```kotlin
package probability

import kotlin.random.Random

class RandomizedSet() {
    private val list = mutableListOf<Int>()
    private val map = mutableMapOf<Int, Int>()

    fun insert(`val`: Int): Boolean {
        if (!map.containsKey(`val`))
            return false
        map[`val`] = list.size
        list.add(`val`)
        return true
    }

    fun remove(`val`: Int): Boolean {
        if (map.containsKey(`val`))
            return false

        val index = map[`val`]!!
        val lastElement = list.last()
        list[index] = lastElement
        map[lastElement] = index

        list.removeLast()
        map.remove(`val`)

        return true
    }

    fun getRandom(): Int {
        return list[Random.nextInt(list.size)]
    }

}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Interval List Intersection

<span id="intervallistintersection"></span>

### Problem

**Intervallistintersection**

**Function:** `Interval Intersection` takes `firstList` (Array<array of integers>), `secondList` (Array<array of integers>) and returns **Array**.



### Approach

**Solution Approach:**
1. The main function `intervalIntersection` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `startMax`, `endMin`

### Code

```kotlin
package array.twopointer

class IntervalListIntersection {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## K Items With Maximum Sum

<span id="kitemswithmaximumsum"></span>

### Problem

**Kitemswithmaximumsum**

**Function:** `K Items With Maximum Sum` takes `numOnes` (integer), `numZeros` (integer), `numNegOnes` (integer), `k` (integer) and returns **integer**.

**Key logic:**
- Alternative way



### Approach

**Solution Approach:**
1. The main function `kItemsWithMaximumSum` processes the input
2. Uses helper functions: kItemsWithMaximumSumAlternative

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `remainingSum`

**Execution flow:**
- Alternative way

### Code

```kotlin
package array.greedy

class KItemsWithMaximumSum {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Linked List Random Node

<span id="linkedlistrandomnode"></span>

### Problem

**Linkedlistrandomnode**

**Function:** `Get Random` takes none and returns **integer**.

**Key logic:**
- Another possible solution
- Select the current node if Random.nextInt(count) == count - 1



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `head`, `ptr`, `current`, `result`, `count`

**Execution flow:**
- Another possible solution
- Select the current node if Random.nextInt(count) == count - 1

### Code

```kotlin
package probability

import linkedlist.ListNode
import kotlin.random.Random

class LinkedListRandomNode (private val head: ListNode?) {
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

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Merge Intervals

<span id="mergeintervals"></span>

### Problem

**Mergeintervals**

**Function:** `Merge` takes `intervals` (Array<array of integers>) and returns **Array**.

**Key logic:**
- Sort the internals by start



### Approach

**Solution Approach:**
1. The main function `merge` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `index`

**Execution flow:**
- Sort the internals by start

### Code

```kotlin
package array

class MergeIntervals {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Merge Sorted Array

<span id="mergesortedarray"></span>

### Problem

**Mergesortedarray**

**Function:** `Merge` takes `nums1` (array of integers), `m` (integer), `nums2` (array of integers), `n` (integer) and returns **nothing (modifies in-place)**.

**Key logic:**
- Declaring a 2d Array in Kotlin is tricky
- Not that Bad. It's still idiomatic and nice....



### Approach

**Solution Approach:**
1. The main function `merge` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `testClass`, `arr`

**Execution flow:**
- Declaring a 2d Array in Kotlin is tricky
- Not that Bad. It's still idiomatic and nice....

### Code

```kotlin
package array

import binarysearch.FindKClosestElements
import kotlin.math.max

class MergeSortedArray {

    fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
        var (x, y, ptr) = listOf(m-1, n-1, m + n - 1)

        while (x >=0  && y > 0) {
            if (nums1[x] > nums2[y] )
                nums1[ptr--] = nums1[x--]
            else
                nums1[ptr--] = nums2[y--]
        }

        while ( y >= 0) {
            nums1[ptr--] = nums2[y--]
        }

        print(nums1.contentToString())
    }

    companion object {
        @JvmStatic
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Missing Ranges

<span id="missingranges"></span>

### Problem

**Missingranges**

**Function:** `Find Missing Ranges` takes `nums` (array of integers), `lower` (integer), `upper` (integer) and returns **List**.



### Approach

**Solution Approach:**
1. The main function `findMissingRanges` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `currentRangePointer`

### Code

```kotlin
package array

class MissingRanges {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Move Zeroes

<span id="movezeroes"></span>

### Problem

**Movezeroes**

**Function:** `Move Zeroes` takes `nums` (array of integers) and returns **nothing (modifies in-place)**.

**Key logic:**
- Move all non-zero elements to the front
- Fill the rest of the array with zeros



### Approach

**Solution Approach:**
1. The main function `moveZeroes` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `nonZeroPointer`

**Execution flow:**
- Move all non-zero elements to the front
- Fill the rest of the array with zeros

### Code

```kotlin
package array

class MoveZeroes {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Next Permutation

<span id="nextpermutation"></span>

### Problem

**Nextpermutation**

**Function:** `Next Permutation` takes `nums` (array of integers) and returns **boolean**.

**Key logic:**
- Find increasing sequence right to left
- Intuition: By traversing from right to left and finding the first pair where nums[index] < nums[index + 1],
- we identify the pivot point where the next permutation should change.
- If no such point exists (i.e., the array is in descending order), the array is the highest permutation
- and should be reversed to form the lowest permutation.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `index`, `pivot`, `indexToSwap`

**Execution flow:**
- Find increasing sequence right to left
- Intuition: By traversing from right to left and finding the first pair where nums[index] < nums[index + 1],
- we identify the pivot point where the next permutation should change.
- If no such point exists (i.e., the array is in descending order), the array is the highest permutation
- and should be reversed to form the lowest permutation.
- If all the sequence from right to left
- index is reduced by 1 in while loop. Hence incrementing to get the highest number
- in this increasing sequence

### Code

```kotlin
package array.Combinatorics

class NextPermutation {
    fun swap(nums: IntArray, i: Int, j: Int) {
        nums[j] = nums[i].also { nums[i] = nums[j] }
    }

    fun reverse(nums: IntArray, startIndex: Int) {
        var (left, right) = Pair(startIndex, nums.lastIndex)
        while(left < right) {
            swap(nums, left++, right--)
        }
    }

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
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Palindrome Number

<span id="palindromenumber"></span>

### Problem

**Palindromenumber**

**Function:** `Is Palindrome` takes `x` (integer) and returns **boolean**.



### Approach

**Solution Approach:**
1. The main function `isPalindrome` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

### Code

```kotlin
package numbers

class PalindromeNumber {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Plus One

<span id="plusone"></span>

### Problem

**Plusone**

**Function:** `Plus One` takes `digits` (array of integers) and returns **array of integers**.



### Approach

**Solution Approach:**
1. The main function `plusOne` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

### Code

```kotlin
package math

class PlusOne {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Remove Element

<span id="removeelement"></span>

### Problem

**Removeelement**

**Function:** `Remove Element` takes `nums` (array of integers), ``val`` (integer) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `removeElement` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `i`

### Code

```kotlin
package array

class RemoveElement {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Reservoir Sampling

<span id="reservoirsampling"></span>

### Problem

**Reservoirsampling**

**Key logic:**
- Replace item



### Approach



### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `reservoir`, `count`, `index`

**Execution flow:**
- Replace item

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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Rotate Array

<span id="rotatearray"></span>

### Problem

**Rotatearray**

**Function:** `Rotate` takes `nums` (array of integers), `k` (integer) and returns **nothing (modifies in-place)**.

**Key logic:**
- In case k is greater than n



### Approach

**Solution Approach:**
1. The main function `rotate` processes the input
2. Uses helper functions: reverse

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `n`, `steps`, `s`, `e`

**Execution flow:**
- In case k is greater than n

### Code

```kotlin
package array.twopointer

class RotateArray {
    fun rotate(nums: IntArray, k: Int): Unit {
        val n = nums.size
        val steps = k % n // In case k is greater than n

        reverse(nums, 0, n - 1)
        reverse(nums, 0, steps - 1)
        reverse(nums, steps, n - 1)
    }

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Rotate Image

<span id="rotateimage"></span>

### Problem

**Rotateimage**

**Function:** `Rotate` takes `matrix` (Array<array of integers>) and returns **nothing (modifies in-place)**.



### Approach

**Solution Approach:**
1. The main function `rotate` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `l`, `r`

### Code

```kotlin
package array

class RotateImage {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Search A2d Matrix_II

<span id="searcha2dmatrix_ii"></span>

### Problem

**Searcha2Dmatrix Ii**

**Function:** `Search Matrix` takes `matrix` (Array<array of integers>), `target` (integer) and returns **boolean**.



### Approach

**Solution Approach:**
1. The main function `searchMatrix` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

### Code

```kotlin
package array

class SearchA2dMatrix_II {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Shortest Path In Binary Matrix

<span id="shortestpathinbinarymatrix"></span>

### Problem

**Shortestpathinbinarymatrix**

**Function:** `Shortest Path Binary Matrix` takes `grid` (Array<array of integers>) and returns **integer**.

**Key logic:**
- Early return if start or end is blocked
- Directions for 8 neighbors (horizontal, vertical, and diagonal)
- Left, right, up, down
- Diagonal directions
- Start at (0,0) with distance 1



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `row`, `col`, `dist`, `n`, `m`, `directions`, `queue`

**Execution flow:**
- Early return if start or end is blocked
- Directions for 8 neighbors (horizontal, vertical, and diagonal)
- Left, right, up, down
- Diagonal directions
- Start at (0,0) with distance 1
- If we reached the bottom-right corner
- Explore all 8 possible directions
- Skip invalid positions or visited cells

### Code

```kotlin
package array

import java.util.*

class ShortestPathInBinaryMatrix {
    data class State(val row: Int, val col: Int, val dist: Int)

    fun shortestPathBinaryMatrix(grid: Array<IntArray>): Int {
        val n = grid.size
        val m = grid[0].size

        // Early return if start or end is blocked
        if (grid[0][0] == 1 || grid[n - 1][m - 1] == 1) return -1

        // Directions for 8 neighbors (horizontal, vertical, and diagonal)
        val directions = arrayOf(
            -1 to 0, 1 to 0, 0 to -1, 0 to 1,  // Left, right, up, down
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

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Sign Of The Product Of An Array

<span id="signoftheproductofanarray"></span>

### Problem

**Signoftheproductofanarray**

**Function:** `Array Sign` takes `nums` (array of integers) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `arraySign` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `negativeCount`

### Code

```kotlin
package array

class SignOfTheProductOfAnArray {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Sort Colors

<span id="sortcolors"></span>

### Problem

**Sortcolors**

**Function:** `Sort Colors` takes `nums` (array of integers) and returns **nothing (modifies in-place)**.



### Approach

**Solution Approach:**
1. The main function `sortColors` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `i`

### Code

```kotlin
package array.sorting

class SortColors {
    fun sortColors(nums: IntArray): Unit {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Spiral Matrix

<span id="spiralmatrix"></span>

### Problem

**Spiralmatrix**

**Function:** `Spiral Order` takes `matrix` (Array<array of integers>) and returns **List**.

**Key logic:**
- Traverse top row
- Traverse right column
- Traverse bottom row
- Traverse left column



### Approach

**Solution Approach:**
1. The main function `spiralOrder` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `count`, `totalElements`

**Execution flow:**
- Traverse top row
- Traverse right column
- Traverse bottom row
- Traverse left column

### Code

```kotlin
package array

class SpiralMatrix {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Spiral Matrix_II

<span id="spiralmatrix_ii"></span>

### Problem

**Spiralmatrix Ii**

**Function:** `Generate Matrix` takes `n` (integer) and returns **Array**.

**Key logic:**
- Fill top row
- Fill right column
- Fill bottom row
- Fill left column



### Approach

**Solution Approach:**
1. The main function `generateMatrix` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `matrix`

**Execution flow:**
- Fill top row
- Fill right column
- Fill bottom row
- Fill left column

### Code

```kotlin
package array

class SpiralMatrix_II {
    class Solution {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Squares Of A Sorted Array

<span id="squaresofasortedarray"></span>

### Problem

**Squaresofasortedarray**

**Function:** `Sorted Squares` takes `nums` (array of integers) and returns **array of integers**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`

### Code

```kotlin
package array.sorting

import kotlin.math.abs

class SquaresOfASortedArray {
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
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Three Sum

<span id="threesum"></span>

### Problem

**Threesum**

**Function:** `Three Sum` takes `nums` (array of integers) and returns **List**.

**Key logic:**
- Skip duplicates for the second and third numbers
- This can be done using set too . Reducing it to 2 sum problem.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `start`, `end`, `sum`

**Execution flow:**
- Skip duplicates for the second and third numbers
- This can be done using set too . Reducing it to 2 sum problem.

### Code

```kotlin
package array.twopointer


class ThreeSum {
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
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Three Sum Closest

<span id="threesumclosest"></span>

### Problem

**Threesumclosest**

**Function:** `Three Sum Closest` takes `nums` (array of integers), `target` (integer) and returns **integer**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `closestSum`, `left`, `right`, `sum`

### Code

```kotlin
package array.twopointer

import kotlin.math.abs

class ThreeSumClosest {
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
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Toeplitz Matrix

<span id="toeplitzmatrix"></span>

### Problem

**Toeplitzmatrix**

**Function:** `Is Toeplitz Matrix` takes `matrix` (Array<array of integers>) and returns **boolean**.



### Approach

**Solution Approach:**
1. The main function `isToeplitzMatrix` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `m`, `n`, `row`, `col`, `i`, `j`, `first`

### Code

```kotlin
package array

class ToeplitzMatrix {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Transpose Matrix

<span id="transposematrix"></span>

### Problem

**Transposematrix**

**Function:** `Transpose` takes `matrix` (Array<array of integers>) and returns **Array**.



### Approach

**Solution Approach:**
1. The main function `transpose` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `rows`, `cols`, `transposed`

### Code

```kotlin
package array

class TransposeMatrix {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Trapping Rain Water

<span id="trappingrainwater"></span>

### Problem

**Trappingrainwater**

**Function:** `Trap` takes `height` (array of integers) and returns **integer**.

**Key logic:**
- Another way
- return (0 until n).sumOf { index ->
- maxOf(minOf(leftMax[index], rightMax[index]) - height[index], 0)
- }
- Two pointer method.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `h`, `leftMax`, `rightMax`, `minLeftRight`

**Execution flow:**
- Another way
- return (0 until n).sumOf { index ->
- maxOf(minOf(leftMax[index], rightMax[index]) - height[index], 0)
- Two pointer method.

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
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Two Sum_II

<span id="twosum_ii"></span>

### Problem

**Twosum Ii**

**Function:** `Two Sum` takes `numbers` (array of integers), `target` (integer) and returns **array of integers**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work

This searches for an exact target value in a sorted structure.


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `start`, `end`, `sum`

### Code

```kotlin
package array.twopointer

class TwoSum_II {
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
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Key Takeaways

1. **Core pattern recognition** — Two pointers create an O(n) pass where a brute force would be O(n²). The pointers track a window, boundary, or comparison pair.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

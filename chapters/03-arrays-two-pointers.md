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

> **37 problems**

## The Pattern

_Each problem below includes: Problem, Example, Why This Approach, Code, Pattern Insight, Complexity, and Variations._

## Problems

1. [4sum](#4sum)
2. [Add Strings](#addstrings)
3. [Can Place Flowers](#canplaceflowers)
4. [Container With Most Water](#containerwithmostwater)
5. [Contains Duplicate_II](#containsduplicate_ii)
6. [Contiguous Array](#contiguousarray)
7. [Continuous Subarray Sum](#continuoussubarraysum)
8. [Diagonal Traverse](#diagonaltraverse)
9. [Point](#diagonaltraverse_ii)
10. [Randomized Set](#insertdeletegetrandomato1)
11. [Interval List Intersection](#intervallistintersection)
12. [K Items With Maximum Sum](#kitemswithmaximumsum)
13. [Linked List Random Node](#linkedlistrandomnode)
14. [Merge Intervals](#mergeintervals)
15. [Merge Sorted Array](#mergesortedarray)
16. [Missing Ranges](#missingranges)
17. [Move Zeroes](#movezeroes)
18. [Next Permutation](#nextpermutation)
19. [Palindrome Number](#palindromenumber)
20. [Plus One](#plusone)
21. [Remove Element](#removeelement)
22. [Reservoir Sampling](#reservoirsampling)
23. [Rotate Array](#rotatearray)
24. [Rotate Image](#rotateimage)
25. [Search A2d Matrix_II](#searcha2dmatrix_ii)
26. [Shortest Path In Binary Matrix](#shortestpathinbinarymatrix)
27. [Sign Of The Product Of An Array](#signoftheproductofanarray)
28. [Sort Colors](#sortcolors)
29. [Spiral Matrix](#spiralmatrix)
30. [Spiral Matrix_II](#spiralmatrix_ii)
31. [Squares Of A Sorted Array](#squaresofasortedarray)
32. [Three Sum](#threesum)
33. [Three Sum Closest](#threesumclosest)
34. [Toeplitz Matrix](#toeplitzmatrix)
35. [Transpose Matrix](#transposematrix)
36. [Trapping Rain Water](#trappingrainwater)
37. [Two Sum_II](#twosum_ii)

---

## 4sum

### Problem

Given `nums` (array of integers), `target` (integer), `start` (integer), `k` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], target = 5, start = 5, k = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the 4sum problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the 4sum problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
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
    /**
    * Helper: k sum.
    *
    * @param nums The input array of integers.
    * @param target The long integer parameter representing target.
    * @param start The integer parameter representing start.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Helper: k sum.
    *
    * @param nums The input array of integers.
    * @param target The long integer parameter representing target.
    * @param start The integer parameter representing start.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
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
    /**
    * Helper: two sum.
    *
    * @param nums The input array of integers.
    * @param target The long integer parameter representing target.
    * @param start The integer parameter representing start.
    * @return The computed integer result.
    */
    /**
    * Helper: two sum.
    *
    * @param nums The input array of integers.
    * @param target The long integer parameter representing target.
    * @param start The integer parameter representing start.
    * @return The computed integer result.
    */
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

## Add Strings

### Problem

Given `num1` (string), `num2` (string), compute the computed result efficiently.

**Example:**

```
Input: num1 = "example", num2 = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

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
    /**
    * Solves the Add Strings problem.
    * Takes `num1` (string), `num2` (string).
    *
    * @param num1 The input string.
    * @param num2 The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Add Strings problem.
    * Takes `num1` (string), `num2` (string).
    *
    * @param num1 The input string.
    * @param num2 The input string.
    * @return The resulting string.
    */
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

## Can Place Flowers

### Problem

Given `flowerbed` (array of integers), `n` (integer), compute the computed result efficiently.

**Example:**

```
Input: flowerbed = [1, 2, 3, 4, 5], n = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Can Place Flowers problem.
    * Takes `flowerbed` (array of integers), `n` (integer).
    *
    * @param flowerbed The input array of integers.
    * @param n The integer parameter representing n.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Can Place Flowers problem.
    * Takes `flowerbed` (array of integers), `n` (integer).
    *
    * @param flowerbed The input array of integers.
    * @param n The integer parameter representing n.
    * @return `true` if the condition is met, `false` otherwise.
    */
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

## Container With Most Water

### Problem

Given `height` (array of integers), compute the computed result efficiently.

**Example:**

```
Input: height = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package array.greedy

class ContainerWithMostWater {
    /**
    * Solves the Container With Most Water problem.
    * Takes `height` (array of integers).
    *
    * @param height The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Container With Most Water problem.
    * Takes `height` (array of integers).
    *
    * @param height The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Container With Most Water problem.
    * Takes `height` (array of integers).
    *
    * @param height The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Container With Most Water problem.
    * Takes `height` (array of integers).
    *
    * @param height The input array of integers.
    * @return The computed integer result.
    */
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

## Contains Duplicate_II

### Problem

Given `nums` (array of integers), `k` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], k = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Contains Duplicate_II problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Contains Duplicate_II problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
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

## Contiguous Array

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
package array.prefixsum

class ContiguousArray {
    /**
    * Solves the Contiguous Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Contiguous Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Contiguous Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Contiguous Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
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

## Continuous Subarray Sum

### Problem

Given `nums` (array of integers), `k` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], k = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package array.prefixsum

// Pattern https://leetcode.com/problems/continuous-subarray-sum/discuss/5276981/prefix-sum-hashmap-patterns-7-problems
class ContinuousSubarraySum {
    /**
    * Solves the Continuous Subarray Sum problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Continuous Subarray Sum problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Continuous Subarray Sum problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Continuous Subarray Sum problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
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

## Diagonal Traverse

### Problem

Given `mat` (2D matrix), compute the computed result efficiently.

**Example:**

```
Input: mat = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package array

class DiagonalTraverse {
    // Enum to represent the direction of diagonal traversal: UP or DOWN
    enum class Direction {
        UP, DOWN
    }

    /**
    * Solves the Diagonal Traverse problem.
    * Takes `mat` (2D matrix of integers).
    *
    * @param mat The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Diagonal Traverse problem.
    * Takes `mat` (2D matrix of integers).
    *
    * @param mat The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Diagonal Traverse problem.
    * Takes `mat` (2D matrix of integers).
    *
    * @param mat The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Diagonal Traverse problem.
    * Takes `mat` (2D matrix of integers).
    *
    * @param mat The input 2D matrix of integers.
    * @return The computed integer result.
    */
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

## Point

### Problem

Given `nums` (List<List<Int>>), compute the computed result efficiently.

**Example:**

```
Input: nums = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Point problem.
    * Takes `nums` (2D list of integers).
    *
    * @param nums The input 2D list of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Point problem.
    * Takes `nums` (2D list of integers).
    *
    * @param nums The input 2D list of integers.
    * @return The computed integer result.
    */
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

## Randomized Set

### Problem

Given `val` (integer), compute the computed result efficiently.

**Example:**

```
Input: val = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package probability

import kotlin.random.Random

class RandomizedSet() {
    private val list = mutableListOf<Int>()
    private val map = mutableMapOf<Int, Int>()

    /**
    * Solves the Randomized Set problem.
    * Takes ``val`` (integer).
    *
    * @param `val` The integer parameter representing `val`.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Randomized Set problem.
    * Takes ``val`` (integer).
    *
    * @param `val` The integer parameter representing `val`.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Randomized Set problem.
    * Takes ``val`` (integer).
    *
    * @param `val` The integer parameter representing `val`.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Randomized Set problem.
    * Takes ``val`` (integer).
    *
    * @param `val` The integer parameter representing `val`.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun insert(`val`: Int): Boolean {
        if (!map.containsKey(`val`))
            return false
        map[`val`] = list.size
        list.add(`val`)
        return true
    }

    /**
    * Solves the Randomized Set problem.
    * Takes ``val`` (integer).
    *
    * @param `val` The integer parameter representing `val`.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Randomized Set problem.
    * Takes ``val`` (integer).
    *
    * @param `val` The integer parameter representing `val`.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Randomized Set problem.
    * Takes ``val`` (integer).
    *
    * @param `val` The integer parameter representing `val`.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Randomized Set problem.
    * Takes ``val`` (integer).
    *
    * @param `val` The integer parameter representing `val`.
    * @return `true` if the condition is met, `false` otherwise.
    */
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

    /**
    * Solves the Randomized Set problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the Randomized Set problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the Randomized Set problem.
    *
    * @return The computed integer result.
    */
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

## Interval List Intersection

### Problem

Given `firstList` (2D matrix), `secondList` (2D matrix), compute the computed result efficiently.

**Example:**

```
Input: firstList = [1, 2, 3, 4, 5], secondList = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem uses **linked list manipulation**. Linked lists are about pointer rearrangement. Key techniques include using dummy head nodes (to handle empty cases uniformly), slow/fast pointers (for cycle detection, finding the middle), and in-place pointer reversal.

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
    /**
    * Solves the Interval List Intersection problem.
    * Takes `firstList` (2D matrix of integers), `secondList` (2D matrix of integers).
    *
    * @param firstList The input 2D matrix of integers.
    * @param secondList The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Interval List Intersection problem.
    * Takes `firstList` (2D matrix of integers), `secondList` (2D matrix of integers).
    *
    * @param firstList The input 2D matrix of integers.
    * @param secondList The input 2D matrix of integers.
    * @return The computed integer result.
    */
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

### Pattern Insight

**Linked List Pattern.** Dummy head simplifies edge cases. Slow/fast pointer detects cycles and finds middle. In-place reversal uses three pointers (prev, curr, next).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the list has a cycle — how does that affect the solution?
1. What if O(1) extra space is required?
1. What if the list is doubly linked — does that simplify things?
1. Recursive vs iterative approach — what are the tradeoffs?
1. Can slow/fast pointer technique be used?

---

## K Items With Maximum Sum

### Problem

Given `numOnes` (integer), `numZeros` (integer), `numNegOnes` (integer), `k` (integer), compute the computed result efficiently.

**Example:**

```
Input: numOnes = 5, numZeros = 5, numNegOnes = 5, k = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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

## Linked List Random Node

### Problem

Given the input, compute the result efficiently.

**Example:**

```
Input: 
Output: 42 (expected result)

```

### Why This Approach

This problem uses **tree traversal/recursion**. Trees are naturally recursive — each subtree is itself a tree. The key is choosing the right traversal order (preorder, inorder, postorder, level-order) for the specific problem.

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
    /**
    * Solves the Linked List Random Node problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the Linked List Random Node problem.
    *
    * @return The computed integer result.
    */
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
    /**
    * Solves the Linked List Random Node problem.
    *
    * @return The computed integer result.
    */
    /**
    * Solves the Linked List Random Node problem.
    *
    * @return The computed integer result.
    */
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

### Pattern Insight

**Linked List Pattern.** Dummy head simplifies edge cases. Slow/fast pointer detects cycles and finds middle. In-place reversal uses three pointers (prev, curr, next).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the list has a cycle — how does that affect the solution?
1. What if O(1) extra space is required?
1. What if the list is doubly linked — does that simplify things?
1. Recursive vs iterative approach — what are the tradeoffs?
1. Can slow/fast pointer technique be used?

---

## Merge Intervals

### Problem

Given `intervals` (2D matrix), compute the computed result efficiently.

**Example:**

```
Input: intervals = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Merge Intervals problem.
    * Takes `intervals` (2D matrix of integers).
    *
    * @param intervals The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Merge Intervals problem.
    * Takes `intervals` (2D matrix of integers).
    *
    * @param intervals The input 2D matrix of integers.
    * @return The computed integer result.
    */
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

## Merge Sorted Array

### Problem

Given `nums1` (array of integers), `m` (integer), `nums2` (array of integers), `n` (integer), `args` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: nums1 = [1, 2, 3, 4, 5], m = 5, nums2 = [1, 2, 3, 4, 5], n = 5, args = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package array

import binarysearch.FindKClosestElements
import kotlin.math.max

class MergeSortedArray {

    /**
    * Solves the Merge Sorted Array problem.
    * Takes `nums1` (array of integers), `m` (integer), `nums2` (array of integers), `n` (integer).
    *
    * @param nums1 The input array of integers.
    * @param m The integer parameter representing m.
    * @param nums2 The input array of integers.
    * @param n The integer parameter representing n.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Merge Sorted Array problem.
    * Takes `nums1` (array of integers), `m` (integer), `nums2` (array of integers), `n` (integer).
    *
    * @param nums1 The input array of integers.
    * @param m The integer parameter representing m.
    * @param nums2 The input array of integers.
    * @param n The integer parameter representing n.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Merge Sorted Array problem.
    * Takes `nums1` (array of integers), `m` (integer), `nums2` (array of integers), `n` (integer).
    *
    * @param nums1 The input array of integers.
    * @param m The integer parameter representing m.
    * @param nums2 The input array of integers.
    * @param n The integer parameter representing n.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Merge Sorted Array problem.
    * Takes `nums1` (array of integers), `m` (integer), `nums2` (array of integers), `n` (integer).
    *
    * @param nums1 The input array of integers.
    * @param m The integer parameter representing m.
    * @param nums2 The input array of integers.
    * @param n The integer parameter representing n.
    * @return Unit (no return value, modifies state in-place).
    */
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
            val testClass = MergeSortedArray()

            // Declaring a 2d Array in Kotlin is tricky
            // Not that Bad. It's still idiomatic and nice....
            var arr = Array(5) { IntArray(6)}


            testClass.merge(intArrayOf(1,5,7,8, 0, 0, 0), 4, intArrayOf(3,6,17),3)
        }
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

## Missing Ranges

### Problem

Given `nums` (array of integers), `lower` (integer), `upper` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], lower = 5, upper = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Missing Ranges problem.
    * Takes `nums` (array of integers), `lower` (integer), `upper` (integer).
    *
    * @param nums The input array of integers.
    * @param lower The integer parameter representing lower.
    * @param upper The integer parameter representing upper.
    * @return The computed integer result.
    */
    /**
    * Solves the Missing Ranges problem.
    * Takes `nums` (array of integers), `lower` (integer), `upper` (integer).
    *
    * @param nums The input array of integers.
    * @param lower The integer parameter representing lower.
    * @param upper The integer parameter representing upper.
    * @return The computed integer result.
    */
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

## Move Zeroes

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
package array

class MoveZeroes {
    /**
    * Solves the Move Zeroes problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Move Zeroes problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Move Zeroes problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return Unit (no return value, modifies state in-place).
    */
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

## Next Permutation

### Problem

Given `nums` (array of integers), `i` (integer), `j` (integer), `startIndex` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], i = 5, j = 5, startIndex = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package array.Combinatorics

class NextPermutation {
    /**
    * Solves the Next Permutation problem.
    * Takes `nums` (array of integers), `i` (integer), `j` (integer).
    *
    * @param nums The input array of integers.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Next Permutation problem.
    * Takes `nums` (array of integers), `i` (integer), `j` (integer).
    *
    * @param nums The input array of integers.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Next Permutation problem.
    * Takes `nums` (array of integers), `i` (integer), `j` (integer).
    *
    * @param nums The input array of integers.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Next Permutation problem.
    * Takes `nums` (array of integers), `i` (integer), `j` (integer).
    *
    * @param nums The input array of integers.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    fun swap(nums: IntArray, i: Int, j: Int) {
        nums[j] = nums[i].also { nums[i] = nums[j] }
    }

    /**
    * Solves the Next Permutation problem.
    * Takes `nums` (array of integers), `startIndex` (integer).
    *
    * @param nums The input array of integers.
    * @param startIndex The integer parameter representing startIndex.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Next Permutation problem.
    * Takes `nums` (array of integers), `startIndex` (integer).
    *
    * @param nums The input array of integers.
    * @param startIndex The integer parameter representing startIndex.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Next Permutation problem.
    * Takes `nums` (array of integers), `startIndex` (integer).
    *
    * @param nums The input array of integers.
    * @param startIndex The integer parameter representing startIndex.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Next Permutation problem.
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
    /**
    * Solves the Next Permutation problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Next Permutation problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return `true` if the condition is met, `false` otherwise.
    */
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

## Palindrome Number

### Problem

Given `x` (integer), compute the computed result efficiently.

**Example:**

```
Input: x = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

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
    /**
    * Solves the Palindrome Number problem.
    * Takes `x` (integer).
    *
    * @param x The integer parameter representing x.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Palindrome Number problem.
    * Takes `x` (integer).
    *
    * @param x The integer parameter representing x.
    * @return `true` if the condition is met, `false` otherwise.
    */
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

## Plus One

### Problem

Given `digits` (array of integers), compute the computed result efficiently.

**Example:**

```
Input: digits = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Plus One problem.
    * Takes `digits` (array of integers).
    *
    * @param digits The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Plus One problem.
    * Takes `digits` (array of integers).
    *
    * @param digits The input array of integers.
    * @return The computed integer result.
    */
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

## Remove Element

### Problem

Given `nums` (array of integers), `val` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], val = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Remove Element problem.
    * Takes `nums` (array of integers), ``val`` (integer).
    *
    * @param nums The input array of integers.
    * @param `val` The integer parameter representing `val`.
    * @return The computed integer result.
    */
    /**
    * Solves the Remove Element problem.
    * Takes `nums` (array of integers), ``val`` (integer).
    *
    * @param nums The input array of integers.
    * @param `val` The integer parameter representing `val`.
    * @return The computed integer result.
    */
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

## Reservoir Sampling

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

## Rotate Array

### Problem

Given `nums` (array of integers), `k` (integer), `start` (integer), `end` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], k = 5, start = 5, end = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package array.twopointer

class RotateArray {
    /**
    * Solves the Rotate Array problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Rotate Array problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Rotate Array problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Rotate Array problem.
    * Takes `nums` (array of integers), `k` (integer).
    *
    * @param nums The input array of integers.
    * @param k The integer parameter representing k.
    * @return Unit (no return value, modifies state in-place).
    */
    fun rotate(nums: IntArray, k: Int): Unit {
        val n = nums.size
        val steps = k % n // In case k is greater than n

        reverse(nums, 0, n - 1)
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
    /**
    * Helper: reverse.
    *
    * @param nums The input array of integers.
    * @param start The integer parameter representing start.
    * @param end The integer parameter representing end.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Helper: reverse.
    *
    * @param nums The input array of integers.
    * @param start The integer parameter representing start.
    * @param end The integer parameter representing end.
    * @return Unit (no return value, modifies state in-place).
    */
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

## Rotate Image

### Problem

Given `matrix` (2D matrix), `i` (integer), `j` (integer), `m` (integer), `n` (integer), compute the computed result efficiently.

**Example:**

```
Input: matrix = [1, 2, 3, 4, 5], i = 5, j = 5, m = 5, n = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package array

class RotateImage {
    /**
    * Solves the Rotate Image problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Rotate Image problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Rotate Image problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Rotate Image problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return Unit (no return value, modifies state in-place).
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

## Search A2d Matrix_II

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
package array

class SearchA2dMatrix_II {
    /**
    * Solves the Search A2d Matrix_II problem.
    * Takes `matrix` (2D matrix of integers), `target` (integer).
    *
    * @param matrix The input 2D matrix of integers.
    * @param target The integer parameter representing target.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Search A2d Matrix_II problem.
    * Takes `matrix` (2D matrix of integers), `target` (integer).
    *
    * @param matrix The input 2D matrix of integers.
    * @param target The integer parameter representing target.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Search A2d Matrix_II problem.
    * Takes `matrix` (2D matrix of integers), `target` (integer).
    *
    * @param matrix The input 2D matrix of integers.
    * @param target The integer parameter representing target.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Search A2d Matrix_II problem.
    * Takes `matrix` (2D matrix of integers), `target` (integer).
    *
    * @param matrix The input 2D matrix of integers.
    * @param target The integer parameter representing target.
    * @return `true` if the condition is met, `false` otherwise.
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

## Shortest Path In Binary Matrix

### Problem

Given `grid` (2D matrix), compute the computed result efficiently.

**Example:**

```
Input: grid = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

### Code

```kotlin
package array

import java.util.*

class ShortestPathInBinaryMatrix {
    data class State(val row: Int, val col: Int, val dist: Int)

    /**
    * Solves the Shortest Path In Binary Matrix problem.
    * Takes `grid` (2D matrix of integers).
    *
    * @param grid The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Shortest Path In Binary Matrix problem.
    * Takes `grid` (2D matrix of integers).
    *
    * @param grid The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Shortest Path In Binary Matrix problem.
    * Takes `grid` (2D matrix of integers).
    *
    * @param grid The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Shortest Path In Binary Matrix problem.
    * Takes `grid` (2D matrix of integers).
    *
    * @param grid The input 2D matrix of integers.
    * @return The computed integer result.
    */
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

## Sign Of The Product Of An Array

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
package array

class SignOfTheProductOfAnArray {
    /**
    * Solves the Sign Of The Product Of An Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Sign Of The Product Of An Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Sign Of The Product Of An Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
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

## Sort Colors

### Problem

Given `nums` (array of integers), `i` (integer), `j` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], i = 5, j = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Sort Colors problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Sort Colors problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return Unit (no return value, modifies state in-place).
    */
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
        /**
        * Solves the Sort Colors problem.
        * Takes `i` (integer), `j` (integer).
        *
        * @param i The integer parameter representing i.
        * @param j The integer parameter representing j.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Sort Colors problem.
        * Takes `i` (integer), `j` (integer).
        *
        * @param i The integer parameter representing i.
        * @param j The integer parameter representing j.
        * @return Unit (no return value, modifies state in-place).
        */
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

## Spiral Matrix

### Problem

Given `matrix` (2D matrix), compute the computed result efficiently.

**Example:**

```
Input: matrix = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Spiral Matrix problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Spiral Matrix problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return The computed integer result.
    */
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

## Spiral Matrix_II

### Problem

Given `n` (integer), compute the computed result efficiently.

**Example:**

```
Input: n = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
        /**
        * Solves the Spiral Matrix_II problem.
        * Takes `n` (integer).
        *
        * @param n The integer parameter representing n.
        * @return The computed integer result.
        */
        /**
        * Solves the Spiral Matrix_II problem.
        * Takes `n` (integer).
        *
        * @param n The integer parameter representing n.
        * @return The computed integer result.
        */
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

## Squares Of A Sorted Array

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
    /**
    * Solves the Squares Of ASorted Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Squares Of ASorted Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
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

## Three Sum

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
package array.twopointer


class ThreeSum {
    /**
    * Solves the Three Sum problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Three Sum problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Three Sum problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
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

## Three Sum Closest

### Problem

Given `nums` (array of integers), `target` (integer), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], target = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Three Sum Closest problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Three Sum Closest problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
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

## Toeplitz Matrix

### Problem

Given `matrix` (2D matrix), compute the computed result efficiently.

**Example:**

```
Input: matrix = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Toeplitz Matrix problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Toeplitz Matrix problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return `true` if the condition is met, `false` otherwise.
    */
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

## Transpose Matrix

### Problem

Given `matrix` (2D matrix), compute the computed result efficiently.

**Example:**

```
Input: matrix = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Transpose Matrix problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Transpose Matrix problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return The computed integer result.
    */
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

## Trapping Rain Water

### Problem

Given `height` (array of integers), compute the computed result efficiently.

**Example:**

```
Input: height = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Trapping Rain Water problem.
    * Takes `height` (array of integers).
    *
    * @param height The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Trapping Rain Water problem.
    * Takes `height` (array of integers).
    *
    * @param height The input array of integers.
    * @return The computed integer result.
    */
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

## Two Sum_II

### Problem

Given `numbers` (array of integers), `target` (integer), compute the computed result efficiently.

**Example:**

```
Input: numbers = [1, 2, 3, 4, 5], target = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

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
    /**
    * Solves the Two Sum_II problem.
    * Takes `numbers` (array of integers), `target` (integer).
    *
    * @param numbers The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    /**
    * Solves the Two Sum_II problem.
    * Takes `numbers` (array of integers), `target` (integer).
    *
    * @param numbers The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
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

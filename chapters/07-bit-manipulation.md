---
layout: chapter
title: "Bit Manipulation"
chapter_number: 7
chapter_title: "Bit Manipulation"
toc: true
prev_chapter:
  url: "/chapters/06-graphs.html"
  title: "Graphs"
next_chapter:
  url: "/chapters/08-heaps.html"
  title: "Heaps & Priority Queues"
---

# Bit Manipulation

> **9 problems**

## The Pattern

_Each problem below includes: Problem, Example, Why This Approach, Code, Pattern Insight, Complexity, and Variations._

## Problems

1. [First Letter To Appear Twice](#firstlettertoappeartwice)
2. [Longest Nice Subarray](#longestnicesubarray)
3. [Maximum Xor Of Two Nums In Array](#maximumxoroftwonumsinarray)
4. [Number Of Steps To Reduceaanumberinbinaryrepresentationtoone](#number_of_steps_to_reduceaanumberinbinaryrepresentationtoone)
5. [Number Of One Bits](#numberofonebits)
6. [Reverse Bits](#reversebits)
7. [Single Number](#singlenumber)
8. [Single Number3](#singlenumber3)
9. [Sum Of All Subset Xor Total](#sumofallsubsetxortotal)

---

## First Letter To Appear Twice

### Problem

Given `s` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package bitset

import java.util.*

class FirstLetterToAppearTwice {
    /**
     * This is more memory efficient approach...
     */
    fun repeatedCharacter(s: String): Char {

        var bits = 0
        for (ch in s) {
            val ascii = ch - 'a'
            val bit = 1 shl ascii

            if ( (bits and bit) >= 1 ) {
                return ch
            }

            bits = bits or bit

        }

        return 'x'
    }

    /**
    * Solves the First Letter To Appear Twice problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed result (character).
    */
    /**
    * Solves the First Letter To Appear Twice problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed result (character).
    */
    /**
    * Solves the First Letter To Appear Twice problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed result (character).
    */
    /**
    * Solves the First Letter To Appear Twice problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed result (character).
    */
    fun repeatedCharacterBitset(s: String): Char {

        val seen = BitSet(26)  // BitSet for 26 lowercase English letters

        for (ch in s) {
            val index = ch - 'a'  // Calculate the index for the character

            if (seen.get(index)) {  // Check if the bit at index is already set
                return ch
            }

            seen.set(index)  // Set the bit at index
        }

        return 'x'  // Return null if no repeated character is found
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

## Longest Nice Subarray

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
package bitset

class LongestNiceSubarray {
    /**
    * Solves the Longest Nice Subarray problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest Nice Subarray problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest Nice Subarray problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest Nice Subarray problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun longestNiceSubarray(nums: IntArray): Int {
        var left = 0
        var bitMask = 0
        var maxLen = 0

        for (right in nums.indices) {
            while ((bitMask and nums[right]) != 0) {
                bitMask = bitMask xor nums[left]
                left++
            }
            bitMask = bitMask or nums[right]
            maxLen = maxOf(maxLen, right - left + 1)
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

## Maximum Xor Of Two Nums In Array

### Problem

Given `nums` (array of integers), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem uses **bit manipulation** — operating directly on binary representations. Bitwise operations (AND, OR, XOR, shifts) are extremely fast and can represent sets, toggle flags, or detect patterns that would be cumbersome with arithmetic.

### Code

```kotlin
package bitset

class MaximumXorOfTwoNumsInArray {
    data class Trie(val children: Array<Trie?> = arrayOfNulls(2))

    /**
    * Solves the Maximum Xor Of Two Nums In Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Maximum Xor Of Two Nums In Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Maximum Xor Of Two Nums In Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Maximum Xor Of Two Nums In Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun findMaximumXOR(nums: IntArray): Int {
        val root = buildTrie(nums)

        var max = Int.MIN_VALUE
        for (num in nums) {

            var curNode = root
            var curSum = 0
            for (i in 31 downTo 0) {
                val curBit = if ((1 shl i and num) != 0) 1 else 0
                if (curNode.children[curBit xor 1] != null) {
                    curSum += (1 shl i)
                    curNode = curNode.children[curBit xor 1]!!
                } else {
                    curNode = curNode.children[curBit]!!
                }
            }
            max = maxOf(max, curSum)
        }

        return max
    }

    /**
    * Helper: build trie.
    *
    * @param nums The input array of integers.
    * @return The computed result (Trie).
    */
    /**
    * Helper: build trie.
    *
    * @param nums The input array of integers.
    * @return The computed result (Trie).
    */
    /**
    * Helper: build trie.
    *
    * @param nums The input array of integers.
    * @return The computed result (Trie).
    */
    /**
    * Helper: build trie.
    *
    * @param nums The input array of integers.
    * @return The computed result (Trie).
    */
    private fun buildTrie(nums: IntArray): Trie {
        val root = Trie()

        for (num in nums) {
            var ptr = root
            for (i in 31 downTo 0) {
                val currBit = if((1 shl i) and num !=0) 1 else 0
                if (ptr.children[currBit] == null) {
                    ptr.children[currBit] = Trie()
                }

                ptr = ptr.children[currBit] !!
            }
        }

        return root
    }
}
```

### Pattern Insight

**Bit Manipulation Pattern.** XOR: x^x=0, x^0=x — useful for finding unique elements. AND: mask off bits. Shift: multiply/divide by powers of 2. Bit counting: n & (n-1) clears lowest set bit.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the numbers are 64-bit instead of 32-bit?
1. What if you need to find numbers appearing 3 times instead of 2?
1. Can you solve this without bit manipulation (using hash sets)?
1. What if there are negative numbers involved?
1. Can this be generalized for k occurrences?

---

## Number Of Steps To Reduceaanumberinbinaryrepresentationtoone

### Problem

Given `s` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

### Code

```kotlin
package bitset

class `Number of Steps to ReduceaANumberInBinaryRepresentationtoOne` {
    /**
    * Solves the number of steps to reduceaanumberinbinaryrepresentationtoone problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the number of steps to reduceaanumberinbinaryrepresentationtoone problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the number of steps to reduceaanumberinbinaryrepresentationtoone problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the number of steps to reduceaanumberinbinaryrepresentationtoone problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    fun numSteps(s: String): Int {
        var steps = 0
        var carry = 0

        for (i in s.length - 1 downTo 1) {
            val digit = (s[i] - '0') + carry
            if (digit % 2 == 1) {
                steps += 2  // Add 1 (makes it even) + divide by 2
                carry = 1   // Propagate carry
            } else {
                steps += 1  // Just divide by 2
            }
        }

        return steps + carry  // Handle remaining carry at the first digit
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

## Number Of One Bits

### Problem

Given `n` (integer), compute the computed result efficiently.

**Example:**

```
Input: n = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **bit manipulation** — operating directly on binary representations. Bitwise operations (AND, OR, XOR, shifts) are extremely fast and can represent sets, toggle flags, or detect patterns that would be cumbersome with arithmetic.

### Code

```kotlin
package bitset

class NumberOfOneBits {
    /**
    * Solves the Number Of One Bits problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Number Of One Bits problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Number Of One Bits problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Number Of One Bits problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    fun hammingWeight(n: Int): Int {
        var number = n
        var count = 0

        while (number > 0) {
            number = number and (number - 1)
            count++
        }

        return count
    }
}
```

### Pattern Insight

**Bit Manipulation Pattern.** XOR: x^x=0, x^0=x — useful for finding unique elements. AND: mask off bits. Shift: multiply/divide by powers of 2. Bit counting: n & (n-1) clears lowest set bit.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the numbers are 64-bit instead of 32-bit?
1. What if you need to find numbers appearing 3 times instead of 2?
1. Can you solve this without bit manipulation (using hash sets)?
1. What if there are negative numbers involved?
1. Can this be generalized for k occurrences?

---

## Reverse Bits

### Problem

Given `n` (integer), compute the computed result efficiently.

**Example:**

```
Input: n = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **bit manipulation** — operating directly on binary representations. Bitwise operations (AND, OR, XOR, shifts) are extremely fast and can represent sets, toggle flags, or detect patterns that would be cumbersome with arithmetic.

### Code

```kotlin
package bitset

class ReverseBits {
    /**
    * Solves the Reverse Bits problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Reverse Bits problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Reverse Bits problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    /**
    * Solves the Reverse Bits problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    fun reverseBits(n: Int): Int {
        var num = n
        var result = 0

        for (i in 0 until 32) {
            val bit = num and 1   // Extract the last bit
            result = (result shl 1) or bit  // Shift left and add the bit
            num = num ushr 1       // Unsigned right shift n
        }

        return result
    }
}
```

### Pattern Insight

**Bit Manipulation Pattern.** XOR: x^x=0, x^0=x — useful for finding unique elements. AND: mask off bits. Shift: multiply/divide by powers of 2. Bit counting: n & (n-1) clears lowest set bit.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the numbers are 64-bit instead of 32-bit?
1. What if you need to find numbers appearing 3 times instead of 2?
1. Can you solve this without bit manipulation (using hash sets)?
1. What if there are negative numbers involved?
1. Can this be generalized for k occurrences?

---

## Single Number

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
package bitset

class SingleNumber {
    /**
    * Solves the Single Number problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Single Number problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Single Number problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Single Number problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun singleNumber(nums: IntArray): Int {
        var xorSum = 0
        nums.forEach { xorSum = xorSum xor it}
        return xorSum
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

## Single Number3

### Problem

Given `nums` (array of integers), `args` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5], args = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package bitset

class SingleNumber3 {
    /**
    * Solves the Single Number3 problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Single Number3 problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Single Number3 problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Single Number3 problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun singleNumber(nums: IntArray): IntArray {
        var xorSum = 0
        for (num in nums) {
            xorSum = xorSum.xor(num)
        }

        val rightmostSetBit = xorSum and xorSum
        var (a, b) = listOf(0, 0)

        for (num in nums) {
            if (num and rightmostSetBit !=0) {
                a = a.xor(num)
            } else {
                b = b.xor(num)
            }
        }

        return intArrayOf(a, b)
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
            val test = SingleNumber3()

            println("Single numbers are ${test.singleNumber(intArrayOf(1,2,1,3,2,5))}")
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

## Sum Of All Subset Xor Total

### Problem

Given `nums` (array of integers), compute the computed result efficiently.

**Example:**

```
Input: nums = [1, 2, 3, 4, 5]
Output: 42 (expected result)

```

### Why This Approach

This problem uses **bit manipulation** — operating directly on binary representations. Bitwise operations (AND, OR, XOR, shifts) are extremely fast and can represent sets, toggle flags, or detect patterns that would be cumbersome with arithmetic.

### Code

```kotlin
package bitset

class SumOfAllSubsetXorTotal {
    /**
    * Solves the Sum Of All Subset Xor Total problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Sum Of All Subset Xor Total problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Sum Of All Subset Xor Total problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    /**
    * Solves the Sum Of All Subset Xor Total problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun subsetXORSum(nums: IntArray): Int {
        var result = 0
        // Capture each bit that is set in any of the elements
        for (num in nums) {
            result = result or num // Update the result by OR-ing each number
        }
        // Multiply by the number of subset XOR totals that will have each bit set
        return result shl (nums.size - 1) // Shift by (n-1) to account for all subsets
    }
}
```

### Pattern Insight

**Bit Manipulation Pattern.** XOR: x^x=0, x^0=x — useful for finding unique elements. AND: mask off bits. Shift: multiply/divide by powers of 2. Bit counting: n & (n-1) clears lowest set bit.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the numbers are 64-bit instead of 32-bit?
1. What if you need to find numbers appearing 3 times instead of 2?
1. Can you solve this without bit manipulation (using hash sets)?
1. What if there are negative numbers involved?
1. Can this be generalized for k occurrences?

---

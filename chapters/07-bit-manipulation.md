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

> **9 problems** — Master bitwise operations: AND, OR, XOR, shifts, and bit masking.

## The Pattern

XOR for pairing, AND for masking, shifts for powers of 2.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [First Letter To Appear Twice](#firstlettertoappeartwice) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Longest Nice Subarray](#longestnicesubarray) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Maximum Xor Of Two Nums In Array](#maximumxoroftwonumsinarray) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Number Of Steps To Reduceaanumberinbinaryrepresentationtoone](#number_of_steps_to_reduceaanumberinbinaryrepresentationtoone) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [Number Of One Bits](#numberofonebits) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Reverse Bits](#reversebits) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [Single Number](#singlenumber) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [Single Number3](#singlenumber3) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Sum Of All Subset Xor Total](#sumofallsubsetxortotal) | — | <span class="badge badge-medium">Medium</span> |

---

## First Letter To Appear Twice

### Problem

This is more memory efficient approach...

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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

**Pattern:** Bottom-up DP. Build solutions from smallest subproblems upward using a table.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

### Variations

1. Can you optimize space by using only the previous row?
1. What if the input size is too large for 2D DP? Can you reduce dimensions?
1. Can this be solved greedily instead? When does greedy fail?
1. What if you need to reconstruct the path, not just the optimal value?
1. What changes if you can make unlimited vs limited moves/choices?

---
## Longest Nice Subarray

### Problem

Solves the Longest Nice Subarray problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
## Maximum Xor Of Two Nums In Array

### Problem

Solves the Maximum Xor Of Two Nums In Array problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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

Study the code and identify the algorithmic pattern.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

### Variations


---
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Number Of One Bits

### Problem

Solves the Number Of One Bits problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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

**Pattern:** Study the code's approach — identify the core data structure and traversal method.


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
## Reverse Bits

### Problem

Solves the Reverse Bits problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Single Number

### Problem

Solves the Single Number problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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
    fun singleNumber(nums: IntArray): Int {
        var xorSum = 0
        nums.forEach { xorSum = xorSum xor it}
        return xorSum
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
        fun main(args: Array<String>) {
            val test = SingleNumber3()

            println("Single numbers are ${test.singleNumber(intArrayOf(1,2,1,3,2,5))}")
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

## Sum Of All Subset Xor Total

### Problem

Solves the Sum Of All Subset Xor Total problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

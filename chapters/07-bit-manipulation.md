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

> **9 problems** — **Bit Manipulation** exploits binary representation. Key ops: XOR for pairing/cancellation, AND for masking, shifts for powers of 2.

## Complete Problem Set

| # | Problem |
|---|---------|
| 1 | [First Letter To Appear Twice](#firstlettertoappeartwice) |
| 2 | [Longest Nice Subarray](#longestnicesubarray) |
| 3 | [Maximum Xor Of Two Nums In Array](#maximumxoroftwonumsinarray) |
| 4 | [Number Of Steps To Reduceaanumberinbinaryrepresentationtoone](#number_of_steps_to_reduceaanumberinbinaryrepresentationtoone) |
| 5 | [Number Of One Bits](#numberofonebits) |
| 6 | [Reverse Bits](#reversebits) |
| 7 | [Single Number](#singlenumber) |
| 8 | [Single Number3](#singlenumber3) |
| 9 | [Sum Of All Subset Xor Total](#sumofallsubsetxortotal) |

---

## First Letter To Appear Twice

**Problem:** This is more memory efficient approach...

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Longest Nice Subarray

**Problem:** Solve this classic algorithmic challenge efficiently.

### Code

```kotlin
package bitset

class LongestNiceSubarray {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Maximum Xor Of Two Nums In Array

**Problem:** Solve this classic algorithmic challenge efficiently.

### Code

```kotlin
package bitset

class MaximumXorOfTwoNumsInArray {
    data class Trie(val children: Array<Trie?> = arrayOfNulls(2))

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Number Of Steps To Reduceaanumberinbinaryrepresentationtoone

**Problem:** Solve this classic algorithmic challenge efficiently.

### Code

```kotlin
package bitset

class `Number of Steps to ReduceaANumberInBinaryRepresentationtoOne` {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

---

## Number Of One Bits

**Problem:** Solve this classic algorithmic challenge efficiently.

### Code

```kotlin
package bitset

class NumberOfOneBits {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Reverse Bits

**Problem:** Solve this classic algorithmic challenge efficiently.

### Code

```kotlin
package bitset

class ReverseBits {
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Single Number

**Problem:** Solve this classic algorithmic challenge efficiently.

### Code

```kotlin
package bitset

class SingleNumber {
    fun singleNumber(nums: IntArray): Int {
        var xorSum = 0
        nums.forEach { xorSum = xorSum xor it}
        return xorSum
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Single Number3

**Problem:** Solve this classic algorithmic challenge efficiently.

### Code

```kotlin
package bitset

class SingleNumber3 {
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Sum Of All Subset Xor Total

**Problem:** Solve this classic algorithmic challenge efficiently.

### Code

```kotlin
package bitset

class SumOfAllSubsetXorTotal {
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Key Takeaways

1. **Core pattern recognition** — Identify the problem type and apply the right technique.
2. **Practice systematically** — Work through each problem to internalize the patterns.
3. **Understand why, not just how** — Focus on the reasoning behind each solution.

---

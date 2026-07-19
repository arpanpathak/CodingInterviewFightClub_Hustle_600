---
layout: chapter
title: "Bit Manipulation - Working at the Hardware Level"
chapter_number: 7
chapter_title: "Bit Manipulation"
toc: true
prev_chapter:
  url: "/chapters/06-graphs"
  title: "Graphs - The Real World Is a Graph"
next_chapter:
  url: "/chapters/08-heaps"
  title: "Heaps & Priority Queues"
---

# Bit Manipulation: Working at the Hardware Level

## Core Bit Operations

and: a & b, or: a | b, xor: a ^ b, not: ~a, left shift: a << n, right shift: a >> n

### Common Tricks
- Check if bit i is set: `(num >> i) & 1`
- Set bit i: `num or (1 << i)`
- Clear bit i: `num and (1 << i).inv()`
- Toggle bit i: `num xor (1 << i)`
- Get LSB: `num and -num`
- Clear LSB: `num and (num - 1)`

## Complete Problem Set (9 problems)

| # | Problem | Difficulty | File |
|---|---------|------------|------|
| 1 | Single Number | Easy | bitset/SingleNumber.kt |
| 2 | Single Number III | Medium | bitset/SingleNumber3.kt |
| 3 | Number of 1 Bits | Easy | bitset/NumberOfOneBits.kt |
| 4 | Reverse Bits | Easy | bitset/ReverseBits.kt |
| 5 | Sum of All Subset XOR Totals | Easy | bitset/SumOfAllSubsetXorTotal.kt |
| 6 | Maximum XOR of Two Numbers | Medium | bitset/MaximumXorOfTwoNumsInArray.kt |
| 7 | First Letter to Appear Twice | Easy | bitset/FirstLetterToAppearTwice.kt |
| 8 | Longest Nice Subarray | Medium | bitset/LongestNiceSubarray.kt |
| 9 | Steps to Reduce Binary to One | Medium | bitset/Number of Steps to ReduceaANumberInBinaryRepresentationtoOne.kt |

### Single Number
```kotlin
// Every element appears twice except one. Find it.
// XOR of a number with itself is 0. XOR of 0 with n is n.
fun singleNumber(nums: IntArray): Int {
    return nums.reduce { a, b -> a xor b }
}
// For [2,2,1]: 2 xor 2 xor 1 = 0 xor 1 = 1
```

### Number of 1 Bits
```kotlin
fun hammingWeight(n: Int): Int {
    var count = 0; var num = n
    while (num != 0) { count++; num = num and (num - 1) }  // Clear LSB each time
    return count
}
```

### Reverse Bits
```kotlin
fun reverseBits(n: Int): Int {
    var result = 0; var num = n
    for (i in 0 until 32) {
        result = (result shl 1) or (num and 1)
        num = num shr 1
    }
    return result
}
```

### Single Number III
```kotlin
// Two numbers appear once, rest appear twice
fun singleNumber(nums: IntArray): IntArray {
    var xor = nums.reduce { a, b -> a xor b }
    val diffBit = xor and -xor  // Rightmost set bit
    var a = 0; var b = 0
    for (num in nums) {
        if (num and diffBit == 0) a = a xor num else b = b xor num
    }
    return intArrayOf(a, b)
}
```

---

> **Next up: [Heaps ->](./08-heaps.md)**

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

Bit manipulation exploits binary representation. Key ops: XOR for pairing, AND for masking, shifts for powers of 2.

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

<span id="firstlettertoappeartwice"></span>

### Problem

**Firstlettertoappeartwice**

**Function:** `Repeated Character` takes `s` (string) and returns **Char**.

**Key logic:**
- BitSet for 26 lowercase English letters
- Calculate the index for the character
- Check if the bit at index is already set
- Set the bit at index
- Return null if no repeated character is found



### Approach

**Solution Approach:**
1. The main function `repeatedCharacter` processes the input
2. Uses helper functions: repeatedCharacterBitset

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `bits`, `ascii`, `bit`, `seen`, `index`

**Execution flow:**
- BitSet for 26 lowercase English letters
- Calculate the index for the character
- Check if the bit at index is already set
- Set the bit at index
- Return null if no repeated character is found

### Code

{% include code-tabs-file.html problem="firstlettertoappeartwice" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Longest Nice Subarray

<span id="longestnicesubarray"></span>

### Problem

**Longestnicesubarray**

**Function:** `Longest Nice Subarray` takes `nums` (array of integers) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `longestNiceSubarray` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `bitMask`, `maxLen`

### Code

{% include code-tabs-file.html problem="longestnicesubarray" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Maximum Xor Of Two Nums In Array

<span id="maximumxoroftwonumsinarray"></span>

### Problem

**Maximumxoroftwonumsinarray**

**Function:** `Find Maximum Xor` takes `nums` (array of integers) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `findMaximumXOR` processes the input
2. Uses helper functions: buildTrie

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `children`, `root`, `max`, `curNode`, `curSum`, `curBit`, `root`, `ptr`

### Code

{% include code-tabs-file.html problem="maximumxoroftwonumsinarray" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Number Of Steps To Reduceaanumberinbinaryrepresentationtoone

<span id="number_of_steps_to_reduceaanumberinbinaryrepresentationtoone"></span>

### Problem

**Number Of Steps To Reduceaanumberinbinaryrepresentationtoone**

**Function:** `Num Steps` takes `s` (string) and returns **integer**.

**Key logic:**
- Add 1 (makes it even) + divide by 2
- Propagate carry
- Just divide by 2
- Handle remaining carry at the first digit



### Approach

**Solution Approach:**
1. The main function `numSteps` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `steps`, `carry`, `digit`

**Execution flow:**
- Add 1 (makes it even) + divide by 2
- Propagate carry
- Just divide by 2
- Handle remaining carry at the first digit

### Code

{% include code-tabs-file.html problem="number_of_steps_to_reduceaanumberinbinaryrepresentationtoone" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Number Of One Bits

<span id="numberofonebits"></span>

### Problem

**Numberofonebits**

**Function:** `Hamming Weight` takes `n` (integer) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `hammingWeight` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `number`, `count`

### Code

{% include code-tabs-file.html problem="numberofonebits" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Reverse Bits

<span id="reversebits"></span>

### Problem

**Reversebits**

**Function:** `Reverse Bits` takes `n` (integer) and returns **integer**.

**Key logic:**
- Extract the last bit
- Shift left and add the bit
- Unsigned right shift n



### Approach

**Solution Approach:**
1. The main function `reverseBits` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `num`, `result`, `bit`

**Execution flow:**
- Extract the last bit
- Shift left and add the bit
- Unsigned right shift n

### Code

{% include code-tabs-file.html problem="reversebits" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Single Number

<span id="singlenumber"></span>

### Problem

**Singlenumber**

**Function:** `Single Number` takes `nums` (array of integers) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `singleNumber` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `xorSum`

### Code

{% include code-tabs-file.html problem="singlenumber" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(1) space comes from the auxiliary data structures used.

---

## Single Number3

<span id="singlenumber3"></span>

### Problem

**Singlenumber3**

**Function:** `Single Number` takes `nums` (array of integers) and returns **array of integers**.



### Approach

**Solution Approach:**
1. The main function `singleNumber` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `xorSum`, `rightmostSetBit`, `test`

### Code

{% include code-tabs-file.html problem="singlenumber3" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Sum Of All Subset Xor Total

<span id="sumofallsubsetxortotal"></span>

### Problem

**Sumofallsubsetxortotal**

**Function:** `Subset Xorsum` takes `nums` (array of integers) and returns **integer**.

**Key logic:**
- Capture each bit that is set in any of the elements
- Update the result by OR-ing each number
- Multiply by the number of subset XOR totals that will have each bit set
- Shift by (n-1) to account for all subsets



### Approach

**Solution Approach:**
1. The main function `subsetXORSum` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`

**Execution flow:**
- Capture each bit that is set in any of the elements
- Update the result by OR-ing each number
- Multiply by the number of subset XOR totals that will have each bit set
- Shift by (n-1) to account for all subsets

### Code

{% include code-tabs-file.html problem="sumofallsubsetxortotal" %}

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Key Takeaways

1. **Core pattern recognition** — Bit manipulation exploits binary representation. Key ops: XOR for pairing, AND for masking, shifts for powers of 2.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

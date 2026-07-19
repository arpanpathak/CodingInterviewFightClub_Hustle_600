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

{% include code-tabs-file.html problem="4sum" %}

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

{% include code-tabs-file.html problem="addstrings" %}

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

{% include code-tabs-file.html problem="addtwonumbers" %}

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

{% include code-tabs-file.html problem="canplaceflowers" %}

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

{% include code-tabs-file.html problem="containerwithmostwater" %}

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

{% include code-tabs-file.html problem="containsduplicate_ii" %}

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

{% include code-tabs-file.html problem="contiguousarray" %}

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

{% include code-tabs-file.html problem="continuoussubarraysum" %}

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

{% include code-tabs-file.html problem="diagonaltraverse" %}

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

{% include code-tabs-file.html problem="diagonaltraverse_ii" %}

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

{% include code-tabs-file.html problem="insertdeletegetrandomato1" %}

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

{% include code-tabs-file.html problem="intervallistintersection" %}

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

{% include code-tabs-file.html problem="kitemswithmaximumsum" %}

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

{% include code-tabs-file.html problem="linkedlistrandomnode" %}

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

{% include code-tabs-file.html problem="mergeintervals" %}

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

{% include code-tabs-file.html problem="mergesortedarray" %}

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

{% include code-tabs-file.html problem="missingranges" %}

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

{% include code-tabs-file.html problem="movezeroes" %}

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

{% include code-tabs-file.html problem="nextpermutation" %}

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

{% include code-tabs-file.html problem="palindromenumber" %}

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

{% include code-tabs-file.html problem="plusone" %}

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

{% include code-tabs-file.html problem="removeelement" %}

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

{% include code-tabs-file.html problem="reservoirsampling" %}

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

{% include code-tabs-file.html problem="rotatearray" %}

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

{% include code-tabs-file.html problem="rotateimage" %}

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

{% include code-tabs-file.html problem="searcha2dmatrix_ii" %}

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

{% include code-tabs-file.html problem="shortestpathinbinarymatrix" %}

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

{% include code-tabs-file.html problem="signoftheproductofanarray" %}

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

{% include code-tabs-file.html problem="sortcolors" %}

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

{% include code-tabs-file.html problem="spiralmatrix" %}

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

{% include code-tabs-file.html problem="spiralmatrix_ii" %}

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

{% include code-tabs-file.html problem="squaresofasortedarray" %}

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

{% include code-tabs-file.html problem="threesum" %}

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

{% include code-tabs-file.html problem="threesumclosest" %}

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

{% include code-tabs-file.html problem="toeplitzmatrix" %}

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

{% include code-tabs-file.html problem="transposematrix" %}

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

{% include code-tabs-file.html problem="trappingrainwater" %}

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

{% include code-tabs-file.html problem="twosum_ii" %}

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

---
layout: chapter
title: "Arrays & Two Pointers - The Bread and Butter"
chapter_number: 3
chapter_title: "Arrays & Two Pointers"
toc: true
prev_chapter:
  url: "/chapters/02-dynamic-programming"
  title: "Dynamic Programming - Organized Recursion"
next_chapter:
  url: "/chapters/04-linked-lists"
  title: "Linked Lists - Pointer Manipulation"
---

# Arrays & Two Pointers: The Bread and Butter

Core patterns: Two Pointers, Sliding Window, Prefix Sum, Greedy, Stack, Grid.

## Problem 1: Two Sum II (Sorted)

{% include code-tabs.html  kotlin="fun twoSum(numbers: IntArray, target: Int): IntArray {\n    var l = 0; var r = numbers.lastIndex\n    while (l < r) {\n        val sum = numbers[l] + numbers[r]\n        if (sum == target) return intArrayOf(l+1, r+1)\n        if (sum < target) l++ else r--\n    }\n    return intArrayOf(-1, -1)\n}"  java="public int[] twoSum(int[] numbers, int target) {\n    int l = 0, r = numbers.length - 1;\n    while (l < r) {\n        int sum = numbers[l] + numbers[r];\n        if (sum == target) return new int[]{l+1, r+1};\n        if (sum < target) l++; else r--;\n    }\n    return new int[]{-1, -1};\n}"  python="def two_sum(numbers: list[int], target: int) -> list[int]:\n    l, r = 0, len(numbers) - 1\n    while l < r:\n        s = numbers[l] + numbers[r]\n        if s == target: return [l+1, r+1]\n        if s < target: l += 1\n        else: r -= 1\n    return [-1, -1]" %}

## Problem 2: Trapping Rain Water
{% include code-tabs.html  kotlin="fun trap(height: IntArray): Int {\n    var l = 0; var r = height.lastIndex\n    var maxL = 0; var maxR = 0; var water = 0\n    while (l < r) {\n        if (height[l] < height[r]) {\n            if (height[l] >= maxL) maxL = height[l] else water += maxL - height[l]\n            l++\n        } else {\n            if (height[r] >= maxR) maxR = height[r] else water += maxR - height[r]\n            r--\n        }\n    }\n    return water\n}"  java="public int trap(int[] height) {\n    int l = 0, r = height.length - 1, maxL = 0, maxR = 0, water = 0;\n    while (l < r) {\n        if (height[l] < height[r]) {\n            if (height[l] >= maxL) maxL = height[l];\n            else water += maxL - height[l];\n            l++;\n        } else {\n            if (height[r] >= maxR) maxR = height[r];\n            else water += maxR - height[r];\n            r--;\n        }\n    }\n    return water;\n}"  python="def trap(height: list[int]) -> int:\n    l, r = 0, len(height) - 1\n    maxL = maxR = water = 0\n    while l < r:\n        if height[l] < height[r]:\n            if height[l] >= maxL: maxL = height[l]\n            else: water += maxL - height[l]\n            l += 1\n        else:\n            if height[r] >= maxR: maxR = height[r]\n            else: water += maxR - height[r]\n            r -= 1\n    return water" %}

## Complete Problem Index (100+ problems)

### Two Pointers (9)
Two Sum II, Three Sum, Three Sum Closest, 4Sum, Trapping Rain Water, Remove Duplicates I/II, Rotate Array, Interval Intersection

### Sliding Window (13)
Longest Substring Without Repeating, Longest Repeating Replacement, Max Consecutive Ones III, Min Size Subarray Sum, Sliding Window Maximum, Max Average I, Max Erasure Value, Longest Continuous Subarray, Partition Labels, Min Swaps Group Ones, Longest Subarray After Deleting, Max Sum Distinct K, Programmer String

### Prefix Sum (11)
Product Except Self, Subarray Sum Equals K, Subarray Divisible by K, Continuous Subarray Sum, Pivot Index, Contiguous Array, Subarray Product Less Than K, Zero-Filled Subarrays, Zero Array I, Highest Altitude, Move Balls

### Greedy (24)
Container With Most Water, Jump Game I/II, Merge Intervals, Non-overlapping Intervals, Meeting Rooms II, Task Scheduler, Car Fleet, Max Swap, Can Place Flowers, Increasing Triplet, Min Replacements, Min Deletions Balanced, Max Profit Assign Work, Min Time Rope, Max Chunks II, Max Triplet II, Min Cost Homecoming, Reschedule Meetings, K Items Max Sum, Max Distance Array, Min Swaps Balanced String

### Stack (24)
Valid Parentheses, Daily Temperatures, Next Greater Element, Largest Rectangle, Maximal Rectangle, Min Stack, Evaluate RPN, Asteroid Collision, Exclusive Time, Buildings Ocean View, Flatten Nested, Design Stack Increment, Remove K Digits, Remove Duplicate Letters, Simplify Path, Basic Calculator I/II/III

### Grid (15)
Number of Islands, Max Area Island, Rotting Oranges, Pacific Atlantic, Spiral Matrix, Rotate Image, Word Search, Shortest Bridge, Walls Gates, Flood Fill, Island Perimeter, Make Large Island, Max Fish Grid, Shortest Distance Buildings

### Math (15+)
Reverse Integer, Palindrome Number, Plus One, Sqrt(x), Pow(x,n), Multiply Strings, Add Strings, Divide Integers, Atoi, Detect Squares, Design TicTacToe, Sliding Puzzle, Pascals Triangle, Roman/Integer

---

> **Next up: [Linked Lists ->](./04-linked-lists.md)**

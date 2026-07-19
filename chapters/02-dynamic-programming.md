---
layout: chapter
title: "Dynamic Programming - Organized Recursion"
chapter_number: 2
chapter_title: "Dynamic Programming"
toc: true
prev_chapter:
  url: "/chapters/01-binary-search"
  title: "Binary Search - The Art of Halving the Search Space"
next_chapter:
  url: "/chapters/03-arrays-two-pointers"
  title: "Arrays & Two Pointers - The Bread and Butter"
---

# Dynamic Programming: Organized Recursion

> **"Dynamic Programming is not rocket science; it's simply organized recursion."**

DP transforms exponential brute force into polynomial time by caching repeated subproblem results.

## The 4-Step Framework

1. **Define the State**: What does dp[i][j] represent?
2. **Recurrence Relation**: How does dp[i][j] relate to smaller subproblems?
3. **Base Cases**: What are the minimal states?
4. **Compute Order**: Top-down (memoization) or bottom-up (tabulation)?

## Problem 1: House Robber

Cannot rob adjacent houses. Find max value.

{% include code-tabs.html  kotlin="fun rob(nums: IntArray): Int {\n    var prev2 = 0; var prev1 = 0\n    for (num in nums) {\n        val curr = maxOf(num + prev2, prev1)\n        prev2 = prev1; prev1 = curr\n    }\n    return prev1\n}"  java="public int rob(int[] nums) {\n    int prev2 = 0, prev1 = 0;\n    for (int num : nums) {\n        int curr = Math.max(num + prev2, prev1);\n        prev2 = prev1; prev1 = curr;\n    }\n    return prev1;\n}"  python="def rob(nums: list[int]) -> int:\n    prev2 = prev1 = 0\n    for num in nums:\n        curr = max(num + prev2, prev1)\n        prev2, prev1 = prev1, curr\n    return prev1" %}

## Problem 2: Maximum Subarray (Kadane's Algorithm)
{% include code-tabs.html  kotlin="fun maxSubArray(nums: IntArray): Int {\n    var local = nums[0]; var global = nums[0]\n    for (i in 1 until nums.size) {\n        local = maxOf(nums[i], local + nums[i])\n        global = maxOf(global, local)\n    }\n    return global\n}"  java="public int maxSubArray(int[] nums) {\n    int local = nums[0], global = nums[0];\n    for (int i = 1; i < nums.length; i++) {\n        local = Math.max(nums[i], local + nums[i]);\n        global = Math.max(global, local);\n    }\n    return global;\n}"  python="def max_sub_array(nums: list[int]) -> int:\n    local = global_max = nums[0]\n    for i in range(1, len(nums)):\n        local = max(nums[i], local + nums[i])\n        global_max = max(global_max, local)\n    return global_max" %}

## Problem 3: Coin Change (Minimum Coins)
{% include code-tabs.html  kotlin="fun coinChange(coins: IntArray, amount: Int): Int {\n    val dp = IntArray(amount + 1) { amount + 1 }; dp[0] = 0\n    for (a in 1..amount) for (coin in coins)\n        if (coin <= a) dp[a] = minOf(dp[a], dp[a - coin] + 1)\n    return if (dp[amount] > amount) -1 else dp[amount]\n}"  java="public int coinChange(int[] coins, int amount) {\n    int[] dp = new int[amount + 1];\n    Arrays.fill(dp, amount + 1); dp[0] = 0;\n    for (int a = 1; a <= amount; a++)\n        for (int coin : coins)\n            if (coin <= a) dp[a] = Math.min(dp[a], dp[a - coin] + 1);\n    return dp[amount] > amount ? -1 : dp[amount];\n}"  python="def coin_change(coins: list[int], amount: int) -> int:\n    dp = [amount + 1] * (amount + 1); dp[0] = 0\n    for a in range(1, amount + 1):\n        for coin in coins:\n            if coin <= a: dp[a] = min(dp[a], dp[a - coin] + 1)\n    return -1 if dp[amount] > amount else dp[amount]" %}

## Problem 4: Longest Common Subsequence
{% include code-tabs.html  kotlin="fun longestCommonSubsequence(s: String, t: String): Int {\n    val dp = Array(s.length + 1) { IntArray(t.length + 1) }\n    for (i in 1..s.length) for (j in 1..t.length)\n        dp[i][j] = if (s[i-1] == t[j-1]) dp[i-1][j-1] + 1\n                   else maxOf(dp[i-1][j], dp[i][j-1])\n    return dp[s.length][t.length]\n}"  java="public int longestCommonSubsequence(String s, String t) {\n    int m = s.length(), n = t.length();\n    int[][] dp = new int[m + 1][n + 1];\n    for (int i = 1; i <= m; i++)\n        for (int j = 1; j <= n; j++)\n            dp[i][j] = s.charAt(i-1) == t.charAt(j-1)\n                ? dp[i-1][j-1] + 1\n                : Math.max(dp[i-1][j], dp[i][j-1]);\n    return dp[m][n];\n}"  python="def longest_common_subsequence(s: str, t: str) -> int:\n    m, n = len(s), len(t)\n    dp = [[0] * (n + 1) for _ in range(m + 1)]\n    for i in range(1, m + 1):\n        for j in range(1, n + 1):\n            if s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + 1\n            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n    return dp[m][n]" %}

## Quick Reference (30+ problems)

| # | Problem | Pattern | File |
|---|---------|---------|------|
| 1 | Min Cost Climbing Stairs | Fibonacci | array/dp/MinCostClimbingStaris.kt |
| 2 | House Robber II | Circular | array/dp/HouseRobber_II.kt |
| 3 | Maximum Product Subarray | Kadane w/sign | dynamic_programming/MaximumProductSubarray.kt |
| 4 | Longest Increasing Subseq | LIS | array/dp/LongestIncreasingSubsequence.kt |
| 5 | Target Sum | Subset Sum | array/dp/TargetSum.kt |
| 6 | Partition Equal Subset Sum | 0/1 Knap | dynamic_programming/PartitionEqualSubsetSum.kt |
| 7 | Burst Balloons | Interval DP | array/dp/BurstBaloons.kt |
| 8 | Edit Distance | String DP | string/dynamic_programming/EditDistance.kt |
| 9 | Regular Expression | String DP | string/dynamic_programming/RegularExpressionMatching.kt |
| 10 | Cherry Pickup | 3D DP | grid/dynamic_programming/CherryPickup.kt |
| 11 | Stock Trading I-V | State Machine | stock_market/dp/*.kt |

---

> **Next up: [Arrays & Two Pointers ->](./03-arrays-two-pointers.md)**

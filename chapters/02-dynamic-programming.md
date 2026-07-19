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

## Why This Chapter Matters

DP is the make-or-break topic for top-tier interviews. This chapter covers 30+ problems with full solutions.

## Complete DP Problem Set

### 1D DP
| # | Problem | Pattern | Difficulty | Source |
|---|---------|---------|------------|--------|
| 1 | Min Cost Climbing Stairs | Fibonacci | Easy | array/dp/MinCostClimbingStaris.kt |
| 2 | House Robber | Non-adjacent | Easy | array/dp/HouseRobber.kt |
| 3 | House Robber II | Circular | Medium | array/dp/HouseRobber_II.kt |
| 4 | Maximum Subarray (Kadane) | Local/Global | Easy | array/dp/MaximumSumSubArray.kt |
| 5 | Maximum Product Subarray | Kadane w/sign | Medium | dynamic_programming/MaximumProductSubarray.kt |
| 6 | Longest Increasing Subsequence | LIS | Medium | array/dp/LongestIncreasingSubsequence.kt |
| 7 | Coin Change | Unbounded Knap | Medium | array/dp/CoinChange.kt |
| 8 | Coin Change II | Combinations | Medium | array/dp/CoinChange_II.kt |
| 9 | Target Sum | Subset Sum | Medium | array/dp/TargetSum.kt |
| 10 | Partition Equal Subset Sum | 0/1 Knap | Medium | dynamic_programming/PartitionEqualSubsetSum.kt |
| 11 | Split Array Largest Sum | BS+DP | Hard | array/dp/SplitArrayLargestSum.kt |
| 12 | Super Egg Drop | 2D DP | Hard | dynamic_programming/SuperEggDropping.kt |

### 2D DP / String DP
| # | Problem | Pattern | Difficulty | Source |
|---|---------|---------|------------|--------|
| 13 | Minimum Path Sum | Grid | Medium | array/dp/MinimumPathSum.kt |
| 14 | Unique Paths | Grid | Medium | grid/dynamic_programming/UniquePaths_I.kt |
| 15 | Unique Paths II | Grid w/obs | Medium | grid/dynamic_programming/UniquePaths_II.kt |
| 16 | Maximal Square | Grid | Medium | array/dp/MaximalSquare.kt |
| 17 | Longest Common Substring | String | Medium | array/dp/LongestCommonSubarray.kt |
| 18 | Longest Common Subsequence | String | Medium | string/dynamic_programming/LongestCommonSubsequence.kt |
| 19 | Edit Distance | String | Hard | string/dynamic_programming/EditDistance.kt |
| 20 | Longest Palindromic Subsequence | String | Medium | string/dynamic_programming/LongestPalindromicSubsequence.kt |
| 21 | Regular Expression Matching | String | Hard | string/dynamic_programming/RegularExpressionMatching.kt |
| 22 | Interleaving String | String | Medium | string/dynamic_programming/InterleavingString.kt |
| 23 | Burst Balloons | Interval | Hard | array/dp/BurstBaloons.kt |
| 24 | Cherry Pickup | 3D DP | Hard | grid/dynamic_programming/CherryPickup.kt |
| 25 | Longest Inc Path in Matrix | DFS+Memo | Hard | array/dp/LongestIncreasingSequenceInAMatrix.kt |

### Stock Trading DP
| # | Problem | Source |
|---|---------|--------|
| 26 | Best Time I (one tx) | stock_market/dp/BestTimeToBuyAndSellStock.kt |
| 27 | Best Time II (many tx) | stock_market/dp/BestTimeToBuyAndSellStock_II.kt |
| 28 | Best Time III (two tx) | stock_market/dp/BestTimeToBuyAndSellStock_III.kt |
| 29 | Best Time w/ Cooldown | stock_market/dp/BestTimeToBuyAndSellStockWithCooldown.kt |
| 30 | Best Time w/ Fee | stock_market/dp/BestTimeToBuyAndSellStockWithTransactionFee.kt |

---

### House Robber
```kotlin
fun rob(nums: IntArray): Int {
    var prev2 = 0; var prev1 = 0
    for (num in nums) {
        val curr = maxOf(num + prev2, prev1)
        prev2 = prev1; prev1 = curr
    }
    return prev1
}
```

### Maximum Subarray (Kadane)
```kotlin
fun maxSubArray(nums: IntArray): Int {
    var local = nums[0]; var global = nums[0]
    for (i in 1 until nums.size) {
        local = maxOf(nums[i], local + nums[i])
        global = maxOf(global, local)
    }
    return global
}
```

### Coin Change
```kotlin
fun coinChange(coins: IntArray, amount: Int): Int {
    val dp = IntArray(amount + 1) { amount + 1 }; dp[0] = 0
    for (a in 1..amount)
        for (coin in coins)
            if (coin <= a) dp[a] = minOf(dp[a], dp[a - coin] + 1)
    return if (dp[amount] > amount) -1 else dp[amount]
}
```

### Longest Common Subsequence
```kotlin
fun longestCommonSubsequence(s: String, t: String): Int {
    val dp = Array(s.length + 1) { IntArray(t.length + 1) }
    for (i in 1..s.length)
        for (j in 1..t.length)
            dp[i][j] = if (s[i-1] == t[j-1]) dp[i-1][j-1] + 1
                       else maxOf(dp[i-1][j], dp[i][j-1])
    return dp[s.length][t.length]
}
```

### Edit Distance
```kotlin
fun minDistance(s1: String, s2: String): Int {
    val m = s1.length; val n = s2.length
    if (m < n) return minDistance(s2, s1)
    val dp = IntArray(n + 1) { it }
    for (i in 1..m) {
        var prevDiag = dp[0]; dp[0] = i
        for (j in 1..n) {
            val temp = dp[j]
            dp[j] = if (s1[i-1] == s2[j-1]) prevDiag
                    else 1 + minOf(prevDiag, dp[j], dp[j-1])
            prevDiag = temp
        }
    }
    return dp[n]
}
```

### Burst Balloons (Hard)
```kotlin
fun maxCoins(nums: IntArray): Int {
    val n = nums.size
    val arr = intArrayOf(1) + nums + intArrayOf(1)
    val dp = Array(n + 2) { IntArray(n + 2) }
    for (len in 1..n)
        for (i in 1..(n - len + 1)) {
            val j = i + len - 1
            for (k in i..j)
                dp[i][j] = maxOf(dp[i][j],
                    arr[i-1] * arr[k] * arr[j+1] + dp[i][k-1] + dp[k+1][j])
        }
    return dp[1][n]
}
```

### Best Time with Cooldown
```kotlin
fun maxProfit(prices: IntArray): Int {
    var hold = Int.MIN_VALUE; var sold = 0; var rest = 0
    for (p in prices) {
        val prevSold = sold
        sold = hold + p; hold = maxOf(hold, rest - p)
        rest = maxOf(rest, prevSold)
    }
    return maxOf(sold, rest)
}
```

## DP Recurrence Cheat Sheet
```
LCS:          dp[i][j] = dp[i-1][j-1] + 1 (match) | max(dp[i-1][j], dp[i][j-1])
EDIT DIST:    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + (cost)
KNAPSACK 0/1: dp[i][w] = max(dp[i-1][w], dp[i-1][w-wi] + vi)
KNAPSACK UB:  dp[w] = max(dp[w], dp[w-wi] + vi)
KADANE:       local = max(nums[i], local+nums[i]); global = max(global, local)
INTERVAL:     dp[i][j] = max over k of (cost(k) + dp[i][k-1] + dp[k+1][j])
```

---

> **Next up: [Arrays & Two Pointers ->](./03-arrays-two-pointers.md)**

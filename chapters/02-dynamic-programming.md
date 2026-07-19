---
layout: chapter
title: "Dynamic Programming"
chapter_number: 2
chapter_title: "Dynamic Programming"
toc: true
prev_chapter:
  url: "/chapters/01-binary-search.html"
  title: "Binary Search"
next_chapter:
  url: "/chapters/03-arrays-two-pointers.html"
  title: "Arrays & Two Pointers"
---

# Dynamic Programming

> **21 problems** — Master optimal substructure and overlapping subproblems.

## The Pattern

Optimal substructure + overlapping subproblems → DP. Identify states, define transitions.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [Burst Baloons](#burstbaloons) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Closest Subsequence Sum](#closestsubsequencesum) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Maximumproductsubarray](#maximumproductsubarray) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Maximum Profit In Job Scheduling](#maximumprofitinjobscheduling) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [Partition Equal Subset Sum](#partitionequalsubsetsum) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Super Egg Dropping](#supereggdropping) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [House Robber](#houserobber) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [House Robber_II](#houserobber_ii) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Coin Change](#coinchange) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Coin Change_II](#coinchange_ii) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [Coin Change_II_Bottom Up](#coinchange_ii_bottomup) | — | <span class="badge badge-medium">Medium</span> |
| 12 | [Longest Increasing Subsequence](#longestincreasingsubsequence) | — | <span class="badge badge-medium">Medium</span> |
| 13 | [Maximal Square](#maximalsquare) | — | <span class="badge badge-medium">Medium</span> |
| 14 | [Maximum Sum Sub Array](#maximumsumsubarray) | — | <span class="badge badge-medium">Medium</span> |
| 15 | [Min Cost Climbing Staris](#mincostclimbingstaris) | — | <span class="badge badge-medium">Medium</span> |
| 16 | [Minimum Path Sum](#minimumpathsum) | — | <span class="badge badge-medium">Medium</span> |
| 17 | [Split Array Largest Sum](#splitarraylargestsum) | — | <span class="badge badge-medium">Medium</span> |
| 18 | [Target Sum](#targetsum) | — | <span class="badge badge-medium">Medium</span> |
| 19 | [Longest Increasing Sequence In A Matrix](#longestincreasingsequenceinamatrix) | — | <span class="badge badge-medium">Medium</span> |
| 20 | [Minimum Numberof Increments Subarrays Forma Target Array](#minimumnumberofincrementssubarraysformatargetarray) | — | <span class="badge badge-medium">Medium</span> |
| 21 | [Partition Array Into Two Array To Minimuze Sum Difference](#partitionarrayintotwoarraytominimuzesumdifference) | — | <span class="badge badge-medium">Medium</span> |

---

## Burst Baloons

### Problem

Solves the Burst Baloons problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.dp

// Time COmplexity O(N^3) Space O(N^2)
class BurstBaloons {
    /**
    * Solves the Burst Baloons problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun maxCoins(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        val dp = Array(nums.size) { IntArray(nums.size) }

        /**
        * Solves the Burst Baloons problem.
        * Takes `l` (integer), `r` (integer).
        *
        * @param l The integer parameter representing l.
        * @param r The integer parameter representing r.
        * @return The computed integer result.
        */
        fun dfs(l: Int, r: Int): Int {
            when {
                l > r -> return 0
                dp[l][r] != 0 -> return dp[l][r]
            }

            var res = 0
            for (mid in l..r) {
                // Calculate the maximum coins for this partition
                val left = if (l == 0) 1 else nums[l - 1]
                val right = if (r == nums.size - 1) 1 else nums[r + 1]

                res = maxOf(res, dfs(l, mid - 1) +
                        left * nums[mid] * right +
                        dfs(mid + 1, r))
            }

            return res.also {  dp[l][r] = res }
        }
        return dfs(0, nums.size - 1)
    }
}
```


### Pattern Insight

**Pattern:** Top-down DP with memoization. Cache results of recursive calls to avoid recomputing overlapping subproblems.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

### Variations

1. Can you optimize space by using only the previous row?
1. What if the input size is too large for 2D DP? Can you reduce dimensions?
1. Can this be solved greedily instead? When does greedy fail?
1. What if you need to reconstruct the path, not just the optimal value?
1. What changes if you can make unlimited vs limited moves/choices?

---
## Closest Subsequence Sum

### Problem

Solves the Closest Subsequence Sum problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.Combinatorics

import kotlin.math.abs

class ClosestSubsequenceSum {
    /**
    * Solves the Closest Subsequence Sum problem.
    * Takes `nums` (array of integers), `goal` (integer).
    *
    * @param nums The input array of integers.
    * @param goal The integer parameter representing goal.
    * @return The computed integer result.
    */
    fun minAbsDifference(nums: IntArray, goal: Int): Int {
        var possibleSums = mutableSetOf(0)
        for (num in nums) {
            val newSums = mutableSetOf<Int>()
            for (sum in possibleSums) {
                newSums.add(sum + num)
            }
            possibleSums.addAll(newSums)
        }

        var minDiff = Int.MAX_VALUE
        for (sum in possibleSums) {
            minDiff = minOf(minDiff, abs(sum - goal))
        }

        return minDiff
    }
}
```


### Pattern Insight

**Pattern:** Study the code's approach — identify the core data structure and traversal method.

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
## Maximumproductsubarray

### Problem

Solves the Maximum Product Subarray problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package dynamic_programming

import dynamic_programming.MaximumProductSubarray.maxProduct

object MaximumProductSubarray {
    /**
    * Solves the Maximum Product Subarray problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun maxProduct(nums: IntArray): Int {
        // Edge case: empty array
        if (nums.isEmpty()) return 0
        val m = mapOf(1 to 2, 2 to 4, 5 to 6)

        // Initialize trackers with first element
        var maxSoFar = nums[0]  // Tracks maximum product ending at current position
        var minSoFar = nums[0]  // Tracks minimum product ending at current position (for negative numbers)
        var result = maxSoFar   // Stores the overall maximum product found

        for (i in 1 until nums.size) {
            val currentNum = nums[i]

            // Calculate new maximum product ending at current position:
            // 1. currentNum alone (start new subarray)
            // 2. currentNum * previous max (extend positive product)
            // 3. currentNum * previous min (negative * negative = positive)
            val tempMax = maxOf(
                currentNum,                   // Case 1: Start fresh
                maxSoFar * currentNum,        // Case 2: Continue positive streak
                minSoFar * currentNum         // Case 3: Flip negative streak
            )

            // Calculate new minimum product ending at current position:
            // (Same cases as max, but tracking minimum for future negative flips)
            minSoFar = minOf(
                currentNum,                   // Case 1: Start fresh
                maxSoFar * currentNum,        // Case 2: Continue positive (but could become min)
                minSoFar * currentNum         // Case 3: Negative * negative (but track min)
            )

            maxSoFar = tempMax  // Update max product for next iteration
            result = maxOf(result, maxSoFar)  // Update global maximum
        }

        return result
    }

    @JvmStatic
    /**
    * Entry point for the program.
    *
    * @param args The input Array<String>.
    * @return Unit (no return value, modifies state in-place).
    */
    fun main(args: Array<String>) {
        val tests = listOf(
            intArrayOf(2, 3, -2, 4) to 6,     // Regular case
            intArrayOf(-2, 0, -1) to 0,       // Zero resets product
            intArrayOf(-2, 3, -4) to 24,      // Negative flip
            intArrayOf(-1, -2, -3) to 6,      // All negatives
            intArrayOf(0, 2) to 2             // Single element
        )

        tests.forEach { (input, expected) ->
            val output = maxProduct(input)
            println("Input: ${input.joinToString()}")
            println("Output: $output (Expected: $expected) ${if (output == expected) "✓" else "✗"}\n")
        }
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
          val mid = (low + high) / 2
            if (jobs[mid].end <= currentJob.start) {
                best = mid
                low = mid + 1  // Search in the right half
            } else {
                high = mid - 1  // Search in the left half
            }
        }

        return best
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Partition Equal Subset Sum

### Problem

Solves the Partition Equal Subset Sum problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package dynamic_programming

class PartitionEqualSubsetSum {
    /**
    * Solves the Partition Equal Subset Sum problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun canPartition(nums: IntArray): Boolean {
        val sum = nums.sum()
        if (sum % 2 != 0)   return false
        val target = sum / 2
        val dp = Array(nums.size) { IntArray(target + 1) { -1 } }


        /**
        * Solves the Partition Equal Subset Sum problem.
        * Takes `i` (integer), `currentSum` (integer).
        *
        * @param i The integer parameter representing i.
        * @param currentSum The integer parameter representing currentSum.
        * @return `true` if the condition is met, `false` otherwise.
        */
        fun dfs(i: Int, currentSum: Int): Boolean = when {
            currentSum == target -> true
            dp[i][currentSum] != -1 -> dp[i][currentSum] == 1
            else -> (
                dfs(i + 1, currentSum + nums[i]) ||
                dfs(i + 1, currentSum)
            ).also { dp[i][currentSum] = if (it) 1 else 0 }
        }

        return dfs(0, 0)
    }

    /**
    * Solves the Partition Equal Subset Sum problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun canPartitionBottomUp(nums: IntArray): Boolean {
        val sum = nums.sum()
        if (sum % 2 != 0)   return false

        val target = sum / 2
        val dp = BooleanArray(target + 1).apply { this[0] = true }
        for (num in nums) {
            for (i in target downTo num)
                dp[i] = dp[i] || dp[i - num]
        }

        return dp[target]
    }
}
```


### Pattern Insight

**Pattern:** Top-down DP with memoization. Cache results of recursive calls to avoid recomputing overlapping subproblems.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

### Variations

1. Can you optimize space by using only the previous row?
1. What if the input size is too large for 2D DP? Can you reduce dimensions?
1. Can this be solved greedily instead? When does greedy fail?
1. What if you need to reconstruct the path, not just the optimal value?
1. What changes if you can make unlimited vs limited moves/choices?

---
## Super Egg Dropping

### Problem

Solves the Super Egg Dropping problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package dynamic_programming

class SuperEggDropping {
    /**
    * Solves the Super Egg Dropping problem.
    * Takes `k` (integer), `n` (integer).
    *
    * @param k The integer parameter representing k.
    * @param n The integer parameter representing n.
    * @return The computed integer result.
    */
    fun superEggDrop(k: Int, n: Int): Int {
        val dp = Array(k + 1) { IntArray(n + 1) }
        var m = 0
        while (dp[k][m] < n) {
            m++
            for (eggs in 1..k) {
                dp[eggs][m] = dp[eggs][m - 1] + dp[eggs - 1][m - 1] + 1
            }
        }
        return m
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## House Robber

### Problem

Solves the House Robber problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.dp

class HouseRobber {
    /**
    * Solves the House Robber problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun rob(nums: IntArray): Int {
        val dp = IntArray(nums.size) { -1 }
        return rob(dp, nums, 0)
    }

    /**
    * Solves the House Robber problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun rob(dp: IntArray, nums: IntArray, i: Int): Int {
        return when {
            i >= nums.size -> 0
            dp[i] != -1 -> dp[i]
            else -> {
                dp[i] = maxOf(nums[i] + rob(dp, nums, i + 2), rob(dp, nums, i + 1))
                dp[i]
            }
        }
    }

    /**
    * Solves the House Robber problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun rob_iterative(nums: IntArray): Int {
        if (nums.isEmpty()) return 0

        var include = 0
        var exclude = 0

        for (num in nums) {
            val temp = include
            include = num + exclude
            exclude = maxOf(temp, exclude)
        }

        return maxOf(include, exclude)
    }
}
```


### Pattern Insight

**Pattern:** Bottom-up DP. Build solutions from smallest subproblems upward using a table.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

### Variations

1. Can you optimize space by using only the previous row?
1. What if the input size is too large for 2D DP? Can you reduce dimensions?
1. Can this be solved greedily instead? When does greedy fail?
1. What if you need to reconstruct the path, not just the optimal value?
1. What changes if you can make unlimited vs limited moves/choices?

---
p = IntArray(nums.size)

        // Base cases
        dp[start] = nums[start]
        dp[start + 1] = maxOf(nums[start], nums[start + 1])

        // Fill the dp array from start + 2 to end
        for (i in start + 2..end) {
            dp[i] = maxOf(nums[i] + (if (i >= start + 2) dp[i - 2] else 0), dp[i - 1])
        }

        // The last element of dp array contains the maximum amount that can be robbed
        return dp[end]
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Coin Change

### Problem

Solves the Coin Change problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.dp

class CoinChange {
    /**
    * Solves the Coin Change problem.
    * Takes `coins` (array of integers), `amount` (integer).
    *
    * @param coins The input array of integers.
    * @param amount The integer parameter representing amount.
    * @return The computed integer result.
    */
    fun coinChange(coins: IntArray, amount: Int): Int {
        val dp = IntArray(amount + 1) { -1 }
        return coinChange(coins, amount, dp).let { if (it != Int.MAX_VALUE) it else -1 }
    }

    /**
    * Helper: coin change.
    *
    * @param coins The input array of integers.
    * @param amount The integer parameter representing amount.
    * @return The computed integer result.
    */
    private fun coinChange(coins: IntArray, amount: Int, dp: IntArray): Int {
        return when {
            amount == 0 -> 0
            dp[amount] != -1 -> dp[amount]
            else -> {
                var minCoins = Int.MAX_VALUE
                for (coin in coins) {
                    if (coin <= amount) {
                        val result = coinChange(coins, amount - coin, dp)
                        if (result != Int.MAX_VALUE) {
                            minCoins = minOf(minCoins, 1 + result)
                        }
                    }
                }
                minCoins
            }
        }.also { dp[amount] = it }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Coin Change_II

### Problem

Solves the Coin Change_II problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.dp

class CoinChange_II {
    /**
    * Solves the Coin Change_II problem.
    * Takes `amount` (integer), `coins` (array of integers).
    *
    * @param amount The integer parameter representing amount.
    * @param coins The input array of integers.
    * @return The computed integer result.
    */
    fun change(amount: Int, coins: IntArray): Int {
        val dp = Array(amount + 1) { IntArray(coins.size) { -1 } }
        return change(dp, amount, coins, 0)
    }

    /**
    * Helper: change.
    *
    * @param amount The integer parameter representing amount.
    * @param coins The input array of integers.
    * @return The computed integer result.
    */
    private fun change(dp: Array<IntArray>, amount: Int, coins: IntArray, i: Int): Int {
        return when {
            amount < 0 || (i == coins.size && amount > 0) -> 0
            amount == 0 -> 1
            dp[amount][i] != -1 -> dp[amount][i]
            else -> {
                dp[amount][i] = change(dp, amount - coins[i], coins, i) + change(dp, amount, coins, i + 1)
                dp[amount][i]
            }
        }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Coin Change_II_Bottom Up

### Problem

Solves the Coin Change_II_Bottom Up problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.dp

class CoinChange_II_BottomUp {
    /**
    * Solves the Coin Change_II_Bottom Up problem.
    * Takes `amount` (integer), `coins` (array of integers).
    *
    * @param amount The integer parameter representing amount.
    * @param coins The input array of integers.
    * @return The computed integer result.
    */
    fun change(amount: Int, coins: IntArray): Int {
        val dp = IntArray(amount + 1) { 0 }
        dp[0] = 1  // Base case: 1 way to make amount 0 (using no coins)

        coins.forEach { coin ->
            for (j in coin..amount)
                dp[j] += dp[j - coin]
        }

        return dp[amount]
    }
}
```


### Pattern Insight

**Pattern:** Bottom-up DP. Build solutions from smallest subproblems upward using a table.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

### Variations

1. Can you optimize space by using only the previous row?
1. What if the input size is too large for 2D DP? Can you reduce dimensions?
1. Can this be solved greedily instead? When does greedy fail?
1. What if you need to reconstruct the path, not just the optimal value?
1. What changes if you can make unlimited vs limited moves/choices?

---
t is extending the subsequence with a new larger element.
            tree.add(num)
        }
        // The size of the tree at the end will represent the length of the longest
        // increasing subsequence
        return tree.size
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Maximal Square

### Problem

Solves the Maximal Square problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.dp

class MaximalSquare {
    /**
    * Solves the Maximal Square problem.
    * Takes `matrix` (Array<CharArray>).
    *
    * @param matrix The input Array<CharArray>.
    * @return The computed integer result.
    */
    fun maximalSquare(matrix: Array<CharArray>): Int {
        if (matrix.isEmpty() || matrix[0].isEmpty()) return 0
        val m = matrix.size
        val n = matrix[0].size
        val dp = Array(m) { IntArray(n) }
        var maxSize = 0

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (matrix[i][j] == '1') {
                    if (i == 0 || j == 0) {
                        dp[i][j] = 1
                    } else {
                        dp[i][j] = minOf(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    }
                    maxSize = maxOf(maxSize, dp[i][j])
                }
            }
        }

        return maxSize * maxSize
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Maximum Sum Sub Array

### Problem

Solves the Maximum Sum Sub Array problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.dp

class MaximumSumSubArray {
    // Kaden's Algorithm Dynamic Programming
    /**
    * Solves the Maximum Sum Sub Array problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun maxSubArray(nums: IntArray): Int {
        if (nums.isEmpty())
            return 0
        var (maxSum, currentSum) = listOf( nums[0], nums[0] )


        for (i in 1 until nums.size) {
            currentSum = maxOf(nums[i], currentSum + nums[i])
            maxSum = maxOf(maxSum, currentSum)
        }

        return maxSum
    }
}
```


### Pattern Insight

**Pattern:** Disjoint Set Union (Union-Find). Track connected components with near-O(1) operations.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

### Variations

1. What if the tree is not balanced (skewed)? Worst-case complexity?
1. What if you need to do this iteratively (no recursion)?
1. What if the tree is an N-ary tree instead of binary?
1. What if you need to handle both BST and non-BST trees?
1. Can this be solved with Morris traversal (O(1) space)?

---
mbingStairs_iterative(cost: IntArray): Int {
        // Handle base cases
        if (cost.size <= 2) return cost.min()

        // Initialize the dp array with the size of the cost array
        val dp = IntArray(cost.size)

        // Base cases
        dp[0] = cost[0]
        dp[1] = cost[1]

        // Fill the dp array
        for (i in 2 until cost.size) {
            dp[i] = cost[i] + minOf(dp[i - 1], dp[i - 2])
        }

        // The result is the minimum cost to reach the last or the second-to-last step
        return minOf(dp[cost.size - 1], dp[cost.size - 2])
    }

    /**
     * Constant space iterative approach
     */
    fun minCostClimbingStairs_iterative_constant_space(cost: IntArray): Int {
        // Handle base cases
        if (cost.size <= 2) return cost.min()

        // Initialize the dp array with the size of the cost array
        val dp = IntArray(cost.size)

        // Base cases
        var prev2 = cost[0] // Previous 2 steps
        var prev1 = cost[1]  // Previous 1 steps

        // Fill the dp array
        for (i in 2 until cost.size) {
            val cur = cost[i] + minOf(prev2, prev1)

            prev2 = prev1
            prev1 = cur
        }

        // The result is the minimum cost to reach the last or the second-to-last step
        return minOf(prev2, prev1)
    }


    /**
     * Top Down Dynamic Programming Approach
     */
    fun minCostClimbingStairs(cost: IntArray): Int {
        val memo = IntArray(cost.size) { -1 }
        val n = cost.size

        // We can start from step 0 or step 1, hence we take the minimum of both
        return minOf(minCost(cost, n - 1, memo), minCost(cost, n - 2, memo))
    }
    /**
    * Helper: min cost.
    *
    * @param cost The input array of integers.
    * @param i The integer parameter representing i.
    * @param memo The input array of integers.
    * @return The computed integer result.
    */
    private fun minCost(cost: IntArray, i: Int, memo: IntArray): Int {
        // Base cases
        if (i < 0) return 0
        if (i == 0 || i == 1) return cost[i]

        // If already calculated, return the stored result
        if (memo[i] != -1) return memo[i]

        // Recursive calculation with memoization
        memo[i] = cost[i] + minOf(minCost(cost, i - 1, memo), minCost(cost, i - 2, memo))
        return memo[i]
    }
    /** End of top down Dynamic Programming approach **/
}
```


### Pattern Insight

**Pattern:** Bottom-up DP. Build solutions from smallest subproblems upward using a table.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Minimum Path Sum

### Problem

Solves the Minimum Path Sum problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.dp

class MinimumPathSum {
    /**
    * Solves the Minimum Path Sum problem.
    * Takes `grid` (nullable 2D matrix).
    *
    * @param grid The input nullable 2D matrix.
    * @return The computed integer result.
    */
    fun minPathSum(grid: Array<IntArray>?): Int {
        if (grid.isNullOrEmpty()) return 0

        val dp = Array(grid.size) { IntArray(grid[0].size) }

        for (i in grid.indices) {
            for (j in 0 until grid[i].size) {
                dp[i][j] += grid[i][j]
                dp[i][j] += when {
                    i > 0 && j > 0 -> minOf(dp[i - 1][j], dp[i][j - 1])
                    i > 0 -> dp[i - 1][j]
                    j > 0 -> dp[i][j - 1]
                    else -> 0
                }
            }
        }
        return dp[grid.size - 1][grid[0].size - 1]
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

### Variations

1. Can you optimize space by using only the previous row?
1. What if the input size is too large for 2D DP? Can you reduce dimensions?
1. Can this be solved greedily instead? When does greedy fail?
1. What if you need to reconstruct the path, not just the optimal value?
1. What changes if you can make unlimited vs limited moves/choices?

---
ainingSplits = dfs(j + 1, splitsLeft - 1)
                val maxSplitSum = maxOf(currentSum, largestInRemainingSplits)

                minLargestSum = minOf(minLargestSum, maxSplitSum)

                // Prune unnecessary recursion
                if (currentSum > minLargestSum) break
            }

            memo[i to splitsLeft] = minLargestSum
            return minLargestSum
        }

        return dfs(0, k)
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Target Sum

### Problem

Solves the Target Sum problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.dp


class TargetSum {
    private val dp = mutableMapOf<String, Int>()

    /**
    * Solves the Target Sum problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    fun findTargetSumWays(nums: IntArray, target: Int): Int {
        return ways(nums, target, 0, 0)
    }

    /**
    * Helper: ways.
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @param index The integer parameter representing index.
    * @param sum The integer parameter representing sum.
    * @return The computed integer result.
    */
    private fun ways(nums: IntArray, target: Int, index: Int, sum: Int): Int {
        val state = "$index $sum"
        return when {
            index >= nums.size -> if (sum == target) 1 else 0
            dp.containsKey(state) -> dp[state]!!
            else -> {
                val count = ways(nums, target, index + 1, sum + nums[index]) +
                        ways(nums, target, index + 1, sum - nums[index])
                dp[state] = count
                count
            }
        }
    }


    /**
     * Finds the number of ways to assign a plus or minus sign to elements in the given array `nums`
     * such that their sum equals `target`.
     *
     * This problem is transformed into a subset sum problem using dynamic programming.
     * We calculate the total sum of `nums` and determine if it's possible to partition `nums`
     * into two subsets with sums `P` and `N` such that:
     *     P - N = target
     *
     * This can be simplified to finding the number of subsets of `nums` that sum up to
     * (target + sum(nums)) / 2. If this value is not an integer or is negative, return 0.
     *
     * @param nums The array of integers to assign plus or minus signs.
     * @param target The target sum to achieve.
     * @return The number of ways to achieve the target sum using plus or minus signs.
     */
    /**
    * Solves the Target Sum problem.
    * Takes `nums` (array of integers), `target` (integer).
    *
    * @param nums The input array of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    fun findTargetSumWays_subsetSum(nums: IntArray, target: Int): Int {
        val sumAll = nums.sum()
        // If the target sum is not reachable, return 0
        // If the sumAll + target is not non-negative or even, it's impossible to partition
        if ((target + sumAll) % 2 != 0 || sumAll < Math.abs(target)) return 0
        val newTarget = (target + sumAll) / 2

        // DP array to store the number of ways to reach each sum
        val dp = IntArray(newTarget + 1)
        dp[0] = 1

        for (num in nums) {
            for (j in newTarget downTo num) {
                dp[j] += dp[j - num]
            }
        }

        return dp[newTarget]
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Longest Increasing Sequence In A Matrix

### Problem

Solves the Longest Increasing Sequence In AMatrix problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.dp

class LongestIncreasingSequenceInAMatrix {
    private val dirs = arrayOf(0 to 1, 1 to 0, -1 to 0, 0 to -1)

    /**
    * Solves the Longest Increasing Sequence In AMatrix problem.
    * Takes `matrix` (2D matrix of integers).
    *
    * @param matrix The input 2D matrix of integers.
    * @return The computed integer result.
    */
    fun longestIncreasingPath(matrix: Array<IntArray>): Int {
        val (m, n) = matrix.size to matrix[0].size
        val cache = Array(m) { IntArray(n) }

        /**
        * Solves the Longest Increasing Sequence In AMatrix problem.
        * Takes `i` (integer), `j` (integer).
        *
        * @param i The integer parameter representing i.
        * @param j The integer parameter representing j.
        * @return The computed integer result.
        */
        fun dfs(i: Int, j: Int): Int {
            if (cache[i][j] != 0) return cache[i][j]

            cache[i][j] = 1
            for (delta in dirs) {
                val (x, y) = i + delta.first to j + delta.second

                if (x in matrix.indices && y in matrix[0].indices && matrix[x][y] > matrix[i][j]) {
                    cache[i][j] = maxOf(cache[i][j], 1 + dfs( x, y))
                }
            }

            return cache[i][j]
        }

        var max = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                max = maxOf(max, dfs(i, j))
            }
        }

        return max
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Minimum Numberof Increments Subarrays Forma Target Array

### Problem

Solves the Minimum Numberof Increments Subarrays Forma Target Array problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.dp

class MinimumNumberofIncrementsSubarraysFormaTargetArray {
    /**
    * Solves the Minimum Numberof Increments Subarrays Forma Target Array problem.
    * Takes `target` (array of integers).
    *
    * @param target The input array of integers.
    * @return The computed integer result.
    */
    fun minNumberOperations(target: IntArray): Int {
        var operations = target[0]

        for (i in 1..target.lastIndex) {
            operations += maxOf(0, target[i] - target[i-1])
        }

        return operations
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## Partition Array Into Two Array To Minimuze Sum Difference

### Problem

Solves the Partition Array Into Two Array To Minimuze Sum Difference problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package array.dp

import kotlin.math.abs

class PartitionArrayIntoTwoArrayToMinimuzeSumDifference {
    /**
    * Solves the Partition Array Into Two Array To Minimuze Sum Difference problem.
    * Takes `nums` (array of integers).
    *
    * @param nums The input array of integers.
    * @return The computed integer result.
    */
    fun minimumDifference(nums: IntArray): Int {
        val n = nums.size
        val totalSum = nums.sum()
        val halfSize = n / 2

        val leftSubsets = generateSubsetsBySize(nums, 0, halfSize)
        val rightSubsets = generateSubsetsBySize(nums, halfSize, n)

        var minDiff = Int.MAX_VALUE

        for (k in 0..halfSize) {
            val leftSums = leftSubsets[k] ?: continue
            val rightSums = rightSubsets[halfSize - k] ?: continue

            rightSums.sort()

            for (leftSum in leftSums) {
                val target = (totalSum - 2 * leftSum) / 2
                val closestRightSums = findClosestValues(rightSums, target)

                closestRightSums.forEach { rightSum ->
                    val currentDiff = abs(totalSum - 2 * (leftSum + rightSum))
                    minDiff = minOf(minDiff, currentDiff)
                    if (minDiff == 0) return 0  // Early exit if perfect match found
                }
            }
        }

        return minDiff
    }

    /**
    * Helper: generate subsets by size.
    *
    * @param nums The input array of integers.
    * @param start The integer parameter representing start.
    * @param end The integer parameter representing end.
    * @return The computed integer result.
    */
    private fun generateSubsetsBySize(nums: IntArray, start: Int, end: Int): Array<MutableList<Int>?> {
        val size = end - start
        val subsets = Array<MutableList<Int>?>(size + 1) { mutableListOf() }

        (0 until (1 shl size)).forEach { mask ->
            var sum = 0
            var count = 0
            for (i in 0 until size) {
                if (mask and (1 shl i) != 0) {
                    sum += nums[start + i]
                    count++
                }
            }
            subsets[count]?.add(sum)
        }

        return subsets
    }

    /**
    * Helper: find closest values.
    *
    * @param sortedList The input list of integers.
    * @param target The integer parameter representing target.
    * @return The computed integer result.
    */
    private fun findClosestValues(sortedList: List<Int>, target: Int): List<Int> {
        val index = sortedList.binarySearch(target)
        if (index >= 0) return listOf(sortedList[index])  // Exact match

        val insertPos = -index - 1
        return buildList {
            if (insertPos < sortedList.size) add(sortedList[insertPos])
            if (insertPos > 0) add(sortedList[insertPos - 1])
        }.distinct()  // Remove duplicates if adjacent values are equal
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

---

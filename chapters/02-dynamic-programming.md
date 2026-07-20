---
layout: chapter
title: "Dynamic Programming"
chapter_number: 2
chapter_title: "Dynamic Programming"
toc: true
prev_chapter:
  url: "/chapters/01-binary-search.html"
  title: "01-binary-search"
next_chapter:
  url: "/chapters/03-arrays-two-pointers.html"
  title: "Arrays & Two Pointers"
---

# Dynamic Programming

> **21 problems** — **Dynamic Programming** tackles problems with optimal substructure and overlapping subproblems. DP builds solutions from smaller subproblems using either top-down (memoization) or bottom-up (tabulation) approaches.

## Complete Problem Set

| # | Problem |
|---|---------|
| 1 | [Closest Subsequence Sum](#closestsubsequencesum) |
| 2 | [Maximum Product Subarray](#maximumproductsubarray) |
| 3 | [Maximum Profit In Job Scheduling](#maximumprofitinjobscheduling) |
| 4 | [Partition Equal Subset Sum](#partitionequalsubsetsum) |
| 5 | [Super Egg Dropping](#supereggdropping) |
| 6 | [Burst Baloons](#burstbaloons) |
| 7 | [House Robber](#houserobber) |
| 8 | [House Robber_II](#houserobber_ii) |
| 9 | [Coin Change](#coinchange) |
| 10 | [Coin Change_II](#coinchange_ii) |
| 11 | [Coin Change_II_Bottom Up](#coinchange_ii_bottomup) |
| 12 | [Longest Increasing Subsequence](#longestincreasingsubsequence) |
| 13 | [Maximal Square](#maximalsquare) |
| 14 | [Maximum Sum Sub Array](#maximumsumsubarray) |
| 15 | [Min Cost Climbing Staris](#mincostclimbingstaris) |
| 16 | [Minimum Path Sum](#minimumpathsum) |
| 17 | [Split Array Largest Sum](#splitarraylargestsum) |
| 18 | [Target Sum](#targetsum) |
| 19 | [Longest Increasing Sequence In A Matrix](#longestincreasingsequenceinamatrix) |
| 20 | [Minimum Numberof Increments Subarrays Forma Target Array](#minimumnumberofincrementssubarraysformatargetarray) |
| 21 | [Partition Array Into Two Array To Minimuze Sum Difference](#partitionarrayintotwoarraytominimuzesumdifference) |

---

## Closest Subsequence Sum

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.Combinatorics

import kotlin.math.abs

class ClosestSubsequenceSum {

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param nums the input array of numbers to process
 * @param goal the target value to search for or match against
 * @return the minimum value found in the input
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Maximum Product Subarray

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package dynamic_programming

import dynamic_programming.MaximumProductSubarray.maxProduct

object MaximumProductSubarray {

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param nums the input array of numbers to process
 * @return the maximum value found in the input
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
 * main — executes the core logic of this algorithm on the provided input.
 *
 * @param args the args parameter — a array of elements used in the computation
 * @return Unit (nothing) — this function operates via side effects
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Maximum Profit In Job Scheduling

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package dynamic_programming

class MaximumProfitInJobScheduling {
    data class Job(val start: Int, val end: Int, val profit: Int)

/**
 * job Scheduling — executes the core logic of this algorithm on the provided input.
 *
 * @param startTime the startTime parameter — a array of integers used in the computation
 * @param endTime the endTime parameter — a array of integers used in the computation
 * @param profit the profit parameter — a array of integers used in the computation
 * @return the computed integer result
 */
    fun jobScheduling(startTime: IntArray, endTime: IntArray, profit: IntArray): Int {
        // Create a list of jobs and sort them by end time
        val jobs = startTime.indices.map { Job(startTime[it], endTime[it], profit[it]) }
            .sortedBy { it.end }

        // Initialize dp array
        val dp = IntArray(jobs.size)
        dp[0] = jobs[0].profit

        for (i in 1 until jobs.size) {
            // Profit if the current job is not included
            dp[i] = dp[i - 1]

            // Find the last non-overlapping job
            val prevJobIndex = findLastNonOverlappingJob(jobs, i)

            // Profit if the current job is included
            val currentProfit = jobs[i].profit + if (prevJobIndex != -1) dp[prevJobIndex] else 0

            // Take the maximum profit between including and excluding the current job
            dp[i] = maxOf(dp[i], currentProfit)
        }

        return dp[dp.size - 1]
    }

/**
 * Searches for and returns the target element/position using an efficient algorithm.
 *
 * @param jobs the jobs parameter — a list of elements used in the computation
 * @param currentIndex the currentIndex parameter — a integer value used in the computation
 * @return the computed integer result
 */
    private fun findLastNonOverlappingJob(jobs: List<Job>, currentIndex: Int): Int {
        val currentJob = jobs[currentIndex]
        var low = 0
        var high = currentIndex - 1
        var best = -1

        while (low <= high) {
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Partition Equal Subset Sum

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package dynamic_programming

class PartitionEqualSubsetSum {

/**
 * Checks whether the specified condition holds true for the given input.
 *
 * @param nums the input array of numbers to process
 * @return `true` if the condition/constraint is satisfied, `false` otherwise
 */
    fun canPartition(nums: IntArray): Boolean {
        val sum = nums.sum()
        if (sum % 2 != 0)   return false
        val target = sum / 2
        val dp = Array(nums.size) { IntArray(target + 1) { -1 } }


/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param i the index position in the collection
 * @param currentSum the currentSum parameter — a integer value used in the computation
 * @return the computed result of type Boolean = when
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
 * Checks whether the specified condition holds true for the given input.
 *
 * @param nums the input array of numbers to process
 * @return `true` if the condition/constraint is satisfied, `false` otherwise
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) or O(n × m) |
| **Space** | O(n) or O(n²) |

---

## Super Egg Dropping

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package dynamic_programming

class SuperEggDropping {

/**
 * super Egg Drop — executes the core logic of this algorithm on the provided input.
 *
 * @param k the number of elements/operations to consider (k parameter)
 * @param n the size/dimension parameter for the algorithm
 * @return the computed integer result
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Burst Baloons

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

// Time COmplexity O(N^3) Space O(N^2)
class BurstBaloons {

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param nums the input array of numbers to process
 * @return the maximum value found in the input
 */
    fun maxCoins(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        val dp = Array(nums.size) { IntArray(nums.size) }

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param l the l parameter — a integer value used in the computation
 * @param r the r parameter — a integer value used in the computation
 * @return the computed integer result
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) or O(n × m) |
| **Space** | O(n) or O(n²) |

---

## House Robber

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

class HouseRobber {

/**
 * rob — executes the core logic of this algorithm on the provided input.
 *
 * @param nums the input array of numbers to process
 * @return the computed integer result
 */
    fun rob(nums: IntArray): Int {
        val dp = IntArray(nums.size) { -1 }
        return rob(dp, nums, 0)
    }

/**
 * rob — executes the core logic of this algorithm on the provided input.
 *
 * @param dp the dp parameter — a array of integers used in the computation
 * @param nums the input array of numbers to process
 * @param i the index position in the collection
 * @return the computed integer result
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
 * rob_iterative — executes the core logic of this algorithm on the provided input.
 *
 * @param nums the input array of numbers to process
 * @return the computed integer result
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) or O(n × m) |
| **Space** | O(n) or O(n²) |

---

## House Robber_II

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

class HouseRobber_II {

/**
 * rob — executes the core logic of this algorithm on the provided input.
 *
 * @param nums the input array of numbers to process
 * @return the computed integer result
 */
    fun rob(nums: IntArray): Int {
        return when {
            nums.size == 1 -> nums[0]
            else -> maxOf(rob(nums, 0 , nums.size ), rob(nums, 1, nums.size - 1))
        }
    }

    /**
     * Recusrive Solution
     */
    fun rob(nums: IntArray, start: Int, end: Int): Int {
        var (include, exclude, max) = Triple(0, 0, 0)

        for (i in start until  end) {
            max = maxOf(include + nums[i], exclude)

            include = exclude
            exclude = max
        }

        return max
    }


    /**
     * Bottom UP DP
     */
    fun robRange(nums: IntArray, start: Int, end: Int): Int {
        if (nums.isEmpty() || start > end) return 0
        if (start == end) return nums[start]

        // Initialize an array to store the maximum amount that can be robbed up to each house
        val dp = IntArray(nums.size)

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
| **Time** | O(n²) or O(n × m) |
| **Space** | O(n) or O(n²) |

---

## Coin Change

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

class CoinChange {

/**
 * coin Change — executes the core logic of this algorithm on the provided input.
 *
 * @param coins array of available coin denominations
 * @param amount the target amount/sum to achieve
 * @return the computed integer result
 */
    fun coinChange(coins: IntArray, amount: Int): Int {
        val dp = IntArray(amount + 1) { -1 }
        return coinChange(coins, amount, dp).let { if (it != Int.MAX_VALUE) it else -1 }
    }

/**
 * coin Change — executes the core logic of this algorithm on the provided input.
 *
 * @param coins array of available coin denominations
 * @param amount the target amount/sum to achieve
 * @param dp the dp parameter — a array of integers used in the computation
 * @return the computed integer result
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
| **Time** | O(n²) or O(n × m) |
| **Space** | O(n) or O(n²) |

---

## Coin Change_II

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

class CoinChange_II {

/**
 * change — executes the core logic of this algorithm on the provided input.
 *
 * @param amount the target amount/sum to achieve
 * @param coins array of available coin denominations
 * @return the computed integer result
 */
    fun change(amount: Int, coins: IntArray): Int {
        val dp = Array(amount + 1) { IntArray(coins.size) { -1 } }
        return change(dp, amount, coins, 0)
    }

/**
 * change — executes the core logic of this algorithm on the provided input.
 *
 * @param dp the dp parameter — a array of integers used in the computation
 * @param amount the target amount/sum to achieve
 * @param coins array of available coin denominations
 * @param i the index position in the collection
 * @return the computed integer result
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
| **Time** | O(n²) or O(n × m) |
| **Space** | O(n) or O(n²) |

---

## Coin Change_II_Bottom Up

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

class CoinChange_II_BottomUp {

/**
 * change — executes the core logic of this algorithm on the provided input.
 *
 * @param amount the target amount/sum to achieve
 * @param coins array of available coin denominations
 * @return the computed integer result
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) or O(n × m) |
| **Space** | O(n) or O(n²) |

---

## Longest Increasing Subsequence

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package tree.bst

import java.util.*

// Patience sorting algorithm
class LongestIncreasingSubsequence {

/**
 * length Of LIS — executes the core logic of this algorithm on the provided input.
 *
 * @param nums the input array of numbers to process
 * @return the computed integer result
 */
    fun lengthOfLIS(nums: IntArray): Int {
        val tree = TreeSet<Int>()
        nums.forEach { num ->
            // Find the smallest element in the tree which is greater than or equal to num
            tree.ceiling(num)?.also {
                // If such an element is found, it means num can replace it to potentially
                // form a new valid increasing subsequence or extend the current one
                tree.remove(it)
            }
            // Add num to the tree. If num is not replacing any element,
            // it is extending the subsequence with a new larger element.
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
| **Time** | O(n²) or O(n × m) |
| **Space** | O(n) or O(n²) |

---

## Maximal Square

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

class MaximalSquare {

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param matrix the 2D matrix/grid to traverse or process
 * @return the maximum value found in the input
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
| **Time** | O(n²) or O(n × m) |
| **Space** | O(n) or O(n²) |

---

## Maximum Sum Sub Array

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

class MaximumSumSubArray {
    // Kaden's Algorithm Dynamic Programming

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param nums the input array of numbers to process
 * @return the maximum value found in the input
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Min Cost Climbing Staris

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

class MinCostClimbingStaris {

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param cost the cost parameter — a array of integers used in the computation
 * @return the minimum value found in the input
 */
    fun minCostClimbingStairs_iterative(cost: IntArray): Int {
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
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param cost the cost parameter — a array of integers used in the computation
 * @param i the index position in the collection
 * @param memo the memo parameter — a array of integers used in the computation
 * @return the minimum value found in the input
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Minimum Path Sum

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

class MinimumPathSum {

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param grid the 2D matrix/grid to traverse or process
 * @return the minimum value found in the input
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
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

---

## Split Array Largest Sum

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

class SplitArrayLargestSum {

/**
 * split Array — executes the core logic of this algorithm on the provided input.
 *
 * @param nums the input array of numbers to process
 * @param k the number of elements/operations to consider (k parameter)
 * @return the computed integer result
 */
    fun splitArray(nums: IntArray, k: Int): Int {
        val n = nums.size
        val prefixSum = IntArray(n + 1)
        for (i in nums.indices) {
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        }

        val memo = mutableMapOf<Pair<Int, Int>, Int>()

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param i the index position in the collection
 * @param splitsLeft the splitsLeft parameter — a integer value used in the computation
 * @return the computed integer result
 */
        fun dfs(i: Int, splitsLeft: Int): Int {
            if (splitsLeft == 1) return prefixSum[n] - prefixSum[i] // Last split takes remaining sum
            if (i == n) return Int.MAX_VALUE
            if (memo.containsKey(i to splitsLeft)) return memo[i to splitsLeft]!!

            var minLargestSum = Int.MAX_VALUE

            for (j in i until n) {
                val currentSum = prefixSum[j + 1] - prefixSum[i]
                val largestInRemainingSplits = dfs(j + 1, splitsLeft - 1)
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
| **Time** | O(n²) or O(n × m) |
| **Space** | O(n) or O(n²) |

---

## Target Sum

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp


class TargetSum {
    private val dp = mutableMapOf<String, Int>()

/**
 * Searches for and returns the target element/position using an efficient algorithm.
 *
 * @param nums the input array of numbers to process
 * @param target the target value to search for or match against
 * @return the computed sum/total value
 */
    fun findTargetSumWays(nums: IntArray, target: Int): Int {
        return ways(nums, target, 0, 0)
    }

/**
 * ways — executes the core logic of this algorithm on the provided input.
 *
 * @param nums the input array of numbers to process
 * @param target the target value to search for or match against
 * @param index the index position in the collection
 * @param sum the target amount/sum to achieve
 * @return the computed integer result
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
 * Searches for and returns the target element/position using an efficient algorithm.
 *
 * @param nums the input array of numbers to process
 * @param target the target value to search for or match against
 * @return the computed sum/total value
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
| **Time** | O(n²) or O(n × m) |
| **Space** | O(n) or O(n²) |

---

## Longest Increasing Sequence In A Matrix

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

class LongestIncreasingSequenceInAMatrix {
    private val dirs = arrayOf(0 to 1, 1 to 0, -1 to 0, 0 to -1)

/**
 * longest Increasing Path — executes the core logic of this algorithm on the provided input.
 *
 * @param matrix the 2D matrix/grid to traverse or process
 * @return the computed integer result
 */
    fun longestIncreasingPath(matrix: Array<IntArray>): Int {
        val (m, n) = matrix.size to matrix[0].size
        val cache = Array(m) { IntArray(n) }

/**
 * Traverses the graph/tree structure using the specified strategy.
 *
 * @param i the index position in the collection
 * @param j the index position in the collection
 * @return the computed integer result
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Minimum Numberof Increments Subarrays Forma Target Array

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

class MinimumNumberofIncrementsSubarraysFormaTargetArray {

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param target the target value to search for or match against
 * @return the minimum value found in the input
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Partition Array Into Two Array To Minimuze Sum Difference

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package array.dp

import kotlin.math.abs

class PartitionArrayIntoTwoArrayToMinimuzeSumDifference {

/**
 * Computes and returns the optimal/aggregate value from the given input.
 *
 * @param nums the input array of numbers to process
 * @return the minimum value found in the input
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
 * Builds and returns a new data structure from the given input parameters.
 *
 * @param nums the input array of numbers to process
 * @param start the left/starting boundary of the search range (inclusive)
 * @param end the right/ending boundary of the search range (inclusive)
 * @return a list/collection of result elements
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
 * Searches for and returns the target element/position using an efficient algorithm.
 *
 * @param sortedList the sortedList parameter — a list of integers used in the computation
 * @param target the target value to search for or match against
 * @return a list of matching/found elements
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
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

---

## Key Takeaways

1. **Core pattern recognition** — Identify the problem type and apply the right algorithmic technique.
2. **Practice systematically** — Work through each problem to internalize the patterns.
3. **Understand why, not just how** — Focus on the reasoning behind each solution.

---

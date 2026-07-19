---
layout: chapter
title: "Binary Search"
chapter_number: 1
chapter_title: "Binary Search"
toc: true
next_chapter:
  url: "/chapters/02-dynamic-programming.html"
  title: "Dynamic Programming"
---

# Binary Search

> **21 problems** — Master the art of divide-and-conquer searching.

Binary search is the most fundamental divide-and-conquer algorithm. Given a **sorted** array, you can find an element in **O(log n)** time by repeatedly cutting the search space in half.

## The Pattern

```
Sorted array + search → Binary Search
```

### When to Use Binary Search
- Input is **sorted** (or can be sorted)
- You need to find an element, boundary, or position
- You need to **minimize/maximize** a value with a monotonic predicate
- The search space is **numerical** and you can test a candidate

### Three Templates

| Template | Use Case | Condition |
|----------|----------|-----------|
| **Standard** | Find exact target | `while (left <= right)` → return mid |
| **Left boundary** | Find first occurrence | `while (left < right)` → right = mid |
| **Right boundary** | Find last occurrence | `while (left < right)` → left = mid + 1 |

---

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|---------|-----------|
| 1 | [ApartmentHunting](#apartmenthunting) | Binary search on sorted lists | <span class="badge badge-medium">Medium</span> |
| 2 | [CapacityToShipPackageWithinDDays](#capacitytoshippackagewithinddays) | Minimize max capacity | <span class="badge badge-medium">Medium</span> |
| 3 | [ClosestSebsequenceSum](#closestsebsequencesum) | Meet in the middle + binary search | <span class="badge badge-hard">Hard</span> |
| 4 | [FindFirstAndLastPosition](#findfirstandlastposition) | Left/right boundary search | <span class="badge badge-medium">Medium</span> |
| 5 | [FindKClosestElements](#findkclosestelements) | Binary search for window start | <span class="badge badge-medium">Medium</span> |
| 6 | [FindMinimumInRotatedSortedArray](#findminimuminrotatedsortedarray) | Peak/valley in rotated array | <span class="badge badge-medium">Medium</span> |
| 7 | [FindPeakElement](#findpeakelement) | Local peak search | <span class="badge badge-medium">Medium</span> |
| 8 | [FindPeakElementBetterSolution](#findpeakelementbettersolution) | Local peak (safe boundaries) | <span class="badge badge-medium">Medium</span> |
| 9 | [FirstBadVersion](#firstbadversion) | Left boundary (first true) | <span class="badge badge-easy">Easy</span> |
| 10 | [GuessNumberHigherOrLower](#guessnumberhigherorlower) | Standard binary search | <span class="badge badge-easy">Easy</span> |
| 11 | [HouseRobber_IV](#houserobber_iv) | Minimize max with binary search | <span class="badge badge-medium">Medium</span> |
| 12 | [KThMissingPositiveNumber](#kthmissingpositivenumber) | Find k-th missing in sorted array | <span class="badge badge-easy">Easy</span> |
| 13 | [KokoEatingBanana](#kokoeatingbanana) | Minimize eating speed | <span class="badge badge-medium">Medium</span> |
| 14 | [MedianOfTwoSortedARrays](#medianoftwosortedarrays) | Partition-based median | <span class="badge badge-hard">Hard</span> |
| 15 | [RandomPickWithWeight](#randompickwithweight) | Weighted random + prefix sum | <span class="badge badge-medium">Medium</span> |
| 16 | [SearchA2dMatrix](#searcha2dmatrix) | 2D → 1D index mapping | <span class="badge badge-medium">Medium</span> |
| 17 | [SearchInRotatedArray_II](#searchinrotatedarray_ii) | Rotated array with duplicates | <span class="badge badge-medium">Medium</span> |
| 18 | [SearchInRotatedSortedArray](#searchinrotatedsortedarray) | Rotated array search | <span class="badge badge-medium">Medium</span> |
| 19 | [SearchInsertionPosition](#searchinsertionposition) | Find insert index | <span class="badge badge-easy">Easy</span> |
| 20 | [SingleElementInASortedArray](#singleelementinasortedarray) | Find unique element | <span class="badge badge-medium">Medium</span> |
| 21 | [ValleyElement](#valleyelement) | Local valley search | <span class="badge badge-easy">Easy</span> |

---

## ApartmentHunting

**Problem:** Given a list of city blocks (each with map of amenities), find the block that minimizes the maximum distance to any required amenity.

**Intuition:** This is not a direct binary search problem — it uses binary search as a helper (`closestDistance`). The core insight: for each block, compute the farthest distance to any required amenity, then pick the block with the smallest such distance. Binary search on sorted amenity position lists gives us O(log k) distance lookup per amenity.

**Pattern:** Binary search on sorted lists + greedy minimization.

**Approach:**
1. Build a map: amenity → sorted list of blocks where it exists
2. For each block, compute `maxDistance = max(closestDistance(block, amenityPositions))`
3. Pick the block with minimum `maxDistance`
4. `closestDistance` uses binary search to find the nearest block index

{% include code-tabs-file.html problem="apartmenthunting" %}

**Complexity:**
- Time: O(B × R × log K) — B blocks, R requirements, K amenity occurrences
- Space: O(K) for the amenity map

**Variations:** What if amenities have weights? What if you can walk diagonally?

---

## CapacityToShipPackageWithinDDays

**Problem:** Ship packages in `weights` within `days` days. Each day you load as many packages as possible without exceeding capacity. Find the minimum capacity that makes it possible.

**Intuition:** This is a classic "minimize X such that predicate holds" — the predicate is `canShip(capacity)` which checks if capacity is sufficient. The search space is `[max(weights), sum(weights)]`. If mid works, try smaller; if not, try larger.

**Pattern:** Binary search on answer (minimization).

**Approach:**
1. Define `feasible(capacity)`: simulate loading day by day
2. Binary search between `max(weights)` and `sum(weights)`
3. `feasible(mid)` → try smaller: `right = mid`
4. `!feasible(mid)` → try larger: `left = mid + 1`

{% include code-tabs-file.html problem="capacitytoshippackagewithinddays" %}

**Complexity:**
- Time: O(N log S) — N packages, S = sum(weights)
- Space: O(1)

**Variations:** Ship in exactly K days? Packages with dependencies?

---

## ClosestSebsequenceSum

**Problem:** Given an array `nums` and a `goal`, find the minimum absolute difference between `goal` and any subsequence sum.

**Intuition:** With n up to 40, we can't enumerate all 2^40 subsets. Use **meet-in-the-middle**: split array in half, enumerate all sums for each half (2^20 ≈ 1M each), then for each sum in left, binary search for `goal - sum` in right's sorted sums.

**Pattern:** Meet-in-the-middle + binary search on sorted sums.

**Approach:**
1. Split array at midpoint
2. DFS both halves to generate all subset sums
3. Sort right half sums
4. For each left sum, binary search for closest complement in right

{% include code-tabs-file.html problem="closestsebsequencesum" %}

**Complexity:**
- Time: O(2^(n/2) log 2^(n/2))
- Space: O(2^(n/2))

**Variations:** Exact match? Subsequence closest to target with limited length?

---

## FindFirstAndLastPosition

**Problem:** Find first and last index of `target` in sorted array with duplicates. Return [-1, -1] if not found.

**Intuition:** Two binary searches — one for left boundary (first occurrence) and one for right boundary (last occurrence). The trick: when `nums[mid] == target`, don't stop — narrow toward one side.

**Pattern:** Left/right boundary binary search.

**Approach:**
1. Binary search for first occurrence: when `nums[mid] == target`, `right = mid - 1`
2. Binary search for last occurrence: when `nums[mid] == target`, `left = mid + 1`
3. If first doesn't exist, return [-1, -1]

{% include code-tabs-file.html problem="findfirstandlastposition" %}

**Complexity:**
- Time: O(log n)
- Space: O(1)

**Variations:** Count occurrences of target? First/last position in rotated array?

---

## FindKClosestElements

**Problem:** Find `k` closest elements to `x` in sorted array `arr`. Return in sorted order.

**Intuition:** Instead of finding k closest, find the **start** of the k-element window. The window start `left` must satisfy that `arr[left]` is closer than `arr[left + k]` (otherwise we shift right). Binary search for the optimal `left`.

**Pattern:** Binary search for window position.

**Approach:**
1. Binary search `left` in `[0, arr.size - k]`
2. Compare `x - arr[mid]` vs `arr[mid + k] - x`
3. If `arr[mid]` is closer, move left; else move right

{% include code-tabs-file.html problem="findkclosestelements" %}

**Complexity:**
- Time: O(log(n - k) + k)
- Space: O(k) for result

**Variations:** What if x is outside array range? What if all elements are equally close?

---

## FindMinimumInRotatedSortedArray

**Problem:** Find minimum in a rotated sorted array (no duplicates).

**Intuition:** In a rotated sorted array, the minimum is the **pivot point** where order breaks. Compare `nums[mid]` with `nums[right]` — if `nums[mid] > nums[right]`, the pivot is in the right half; otherwise it's in the left.

**Pattern:** Binary search on rotated array (comparison with right boundary).

**Approach:**
1. While `left < right`:
2. `mid = left + (right - left) / 2`
3. If `nums[mid] > nums[right]`: pivot is on right → `left = mid + 1`
4. Else: pivot is on left (or at mid) → `right = mid`

{% include code-tabs-file.html problem="findminimuminrotatedsortedarray" %}

**Complexity:**
- Time: O(log n)
- Space: O(1)

**Variations:** Find maximum? Find minimum with duplicates? Count rotations?

---

## FindPeakElement

**Problem:** Find a peak element (element greater than its neighbors) in an array. Multiple peaks may exist — return any.

**Intuition:** On a 1D array, if `nums[mid] < nums[mid + 1]`, there is guaranteed to be a peak on the right side (because the array is bounded). This is a **local** decision that eliminates half the search space.

**Pattern:** Local peak binary search (comparison with next element).

**Approach:**
1. If `nums[mid] < nums[mid + 1]`: peak is on right → `left = mid + 1`
2. Otherwise: peak is on left (or at mid) → `right = mid`

{% include code-tabs-file.html problem="findpeakelement" %}

**Complexity:**
- Time: O(log n)
- Space: O(1)

**Variations:** Find all peaks? Peak in 2D matrix?

---

## FindPeakElementBetterSolution

**Problem:** Same as above but with safer boundary handling using sentinel values.

**Intuition:** Same logic but explicitly handle edge cases by treating out-of-bounds as `Int.MIN_VALUE`, making the comparison logic uniform.

**Pattern:** Local peak with boundary guards.

**Approach:** Same as above but check `leftNeighbor` and `rightNeighbor` with safe defaults.

{% include code-tabs-file.html problem="findpeakelementbettersolution" %}

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

## FirstBadVersion

**Problem:** You have n versions `[1, n]` and an API `isBadVersion(version)`. Find the first bad version. Minimize API calls.

**Intuition:** Classic left-boundary binary search. The predicate `isBadVersion(v)` transitions from `false` (good) to `true` (bad) exactly once. Find the first `true`.

**Pattern:** First true in boolean array (left boundary).

**Approach:**
1. Binary search `[1, n]`
2. If `isBadVersion(mid)`: it could be first → `end = mid`
3. Else: too early → `start = mid + 1`

{% include code-tabs-file.html problem="firstbadversion" %}

**Complexity:**
- Time: O(log n)
- Space: O(1)

**Variations:** Find last good version? Multiple bad version ranges?

---

## GuessNumberHigherOrLower

**Problem:** Guess a number between 1 and n using `guess(num)` API that returns -1 (too high), 1 (too low), or 0 (correct).

**Intuition:** Direct binary search on integer range with a comparison API.

**Pattern:** Standard binary search with ternary comparison.

**Approach:**
1. Binary search `[1, n]`
2. Use `guess(mid)` to decide direction

{% include code-tabs-file.html problem="guessnumberhigherorlower" %}

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

## HouseRobber_IV

**Problem:** Given `nums` representing money in houses (cannot rob adjacent), find the minimum `capability` such that you can rob at least `k` houses without alerting police.

**Intuition:** Binary search on the answer (capability). For a given `cap`, check if it's possible to rob `k` houses by taking any house with `nums[i] <= cap` and skipping the next (no adjacent).

**Pattern:** Minimize max with feasibility check (binary search on answer).

**Approach:**
1. Binary search between `min(nums)` and `max(nums)`
2. `canRob(cap)`: greedily rob houses with value ≤ cap, skip adjacent
3. If can rob ≥ k, try smaller cap; else try larger

{% include code-tabs-file.html problem="houserobber_iv" %}

**Complexity:**
- Time: O(N log range)
- Space: O(1)

---

## KThMissingPositiveNumber

**Problem:** Find the k-th missing positive integer in a strictly increasing sorted array.

**Intuition:** At index `i`, the number of missing values is `arr[i] - (i + 1)`. Binary search to find the index where missing count crosses `k`. The answer is `index + k`.

**Pattern:** Binary search on missing count.

**Approach:**
1. Binary search on indices
2. Count missing at mid: `arr[mid] - (mid + 1)`
3. If missing < k: need to go right → `left = mid + 1`
4. Else: go left → `right = mid`
5. Return `left + k`

{% include code-tabs-file.html problem="kthmissingpositivenumber" %}

**Complexity:**
- Time: O(log n)
- Space: O(1)

**Variations:** Find k-th missing starting from arbitrary `start` value instead of 1?

---

## KokoEatingBanana

**Problem:** Koko can eat `piles[i]` bananas per hour at speed `k`. She eats one pile at a time, taking `ceil(pile / k)` hours per pile. Find minimum `k` to finish all piles within `h` hours.

**Intuition:** Binary search on eating speed `k`. `canEat(k)`: sum of `ceil(pile / k)` ≤ h. The predicate is monotonic — if speed `k` works, any speed > k also works.

**Pattern:** Minimize speed with feasibility binary search.

**Approach:**
1. Binary search `k` in `[1, max(piles)]`
2. `canEat(k)`: compute total hours needed
3. If feasible, try slower speed → `right = mid`
4. Else try faster → `left = mid + 1`

{% include code-tabs-file.html problem="kokoeatingbanana" %}

**Complexity:**
- Time: O(N log max(pile))
- Space: O(1)

**Variations:** Multiple Kokos? Bananas that spoil after T hours?

---

## MedianOfTwoSortedARrays

**Problem:** Find median of two sorted arrays in O(log(min(m, n))) time.

**Intuition:** Partition the smaller array at some index. The partition defines how many elements go to the left half of the combined array. We need `leftX <= rightY && leftY <= rightX` for a valid partition. Binary search on the partition position.

**Pattern:** Partition-based binary search on two arrays.

**Approach:**
1. Ensure `nums1` is the smaller array
2. Binary search partition in `nums1`
3. Compute corresponding partition in `nums2`
4. Check if `leftX <= rightY && leftY <= rightX`
5. If valid, compute median based on even/odd total length

{% include code-tabs-file.html problem="medianoftwosortedarrays" %}

**Complexity:**
- Time: O(log min(m, n))
- Space: O(1)

**Variations:** Find k-th element instead of median? 3+ sorted arrays?

---

## RandomPickWithWeight

**Problem:** Given weights array `w`, implement `pickIndex()` that returns index with probability proportional to its weight.

**Intuition:** Build a prefix sum array. Generate random number in `[0, total)`. Binary search to find the index where prefix sum crosses the random value.

**Pattern:** Weighted random + prefix sum + binary search.

**Approach:**
1. Build `prefixSum[i] = sum(w[0..i])`
2. `pickIndex()`: generate `random = rand(total)`, binary search for first `prefixSum[mid] > random`

{% include code-tabs-file.html problem="randompickwithweight" %}

**Complexity:**
- Time: O(log n) per pick, O(n) init
- Space: O(n)

**Variations:** Dynamic weights that change? Multiple picks without replacement?

---

## SearchA2dMatrix

**Problem:** Search in a matrix where each row is sorted and first element of each row > last element of previous row. Essentially a sorted 2D array.

**Intuition:** Flatten the 2D matrix into a sorted 1D array conceptually, without actually creating it. Map 1D index `mid` to 2D coordinates: `row = mid / n`, `col = mid % n`.

**Pattern:** 2D coordinate mapping + binary search.

**Approach:**
1. Binary search on `[0, m*n - 1]`
2. Map `mid → matrix[mid / n][mid % n]`
3. Compare with target

{% include code-tabs-file.html problem="searcha2dmatrix" %}

**Complexity:**
- Time: O(log(m*n))
- Space: O(1)

**Variations:** Matrix where only rows are sorted (not columns)? Search from top-right?

---

## SearchInRotatedArray_II

**Problem:** Search for target in rotated sorted array **with duplicates**. Return true/false.

**Intuition:** Duplicates break the clean rotation detection. When `nums[left] == nums[mid] == nums[right]`, we can't determine which half is sorted — shrink both sides by 1.

**Pattern:** Rotated array binary search with duplicate handling.

**Approach:**
1. Standard rotated array binary search
2. Extra case: if `nums[left] == nums[mid] == nums[right]`, increment `left`, decrement `right`
3. Then determine which half is sorted normally

{% include code-tabs-file.html problem="searchinrotatedarray_ii" %}

**Complexity:**
- Time: O(log n) average, O(n) worst with many duplicates
- Space: O(1)

---

## SearchInRotatedSortedArray

**Problem:** Search for target in rotated sorted array (no duplicates). Return index or -1.

**Intuition:** At any mid, one half is guaranteed to be sorted. Check if target lies in the sorted half; if not, search the other half.

**Pattern:** Rotated array binary search.

**Approach:**
1. Check which half is sorted: `nums[left] <= nums[mid]`
2. If left half sorted and target in left range → search left
3. If right half sorted and target in right range → search right
4. Otherwise search the other half

{% include code-tabs-file.html problem="searchinrotatedsortedarray" %}

**Complexity:**
- Time: O(log n)
- Space: O(1)

**Variations:** Find rotation count? Search with duplicates?

---

## SearchInsertionPosition

**Problem:** Find index where target should be inserted in sorted array. If target exists, return its index.

**Intuition:** Standard lower_bound / first position where `nums[i] >= target`. When the loop exits, `left` is the correct insertion point.

**Pattern:** Lower bound binary search.

**Approach:**
1. While `start <= end`:
2. If `nums[mid] == target`: return mid
3. If `nums[mid] > target`: search left → `end = mid - 1`
4. Else: search right → `start = mid + 1`
5. Return `start` (insertion point)

{% include code-tabs-file.html problem="searchinsertionposition" %}

**Complexity:**
- Time: O(log n)
- Space: O(1)

**Variations:** Insert into range of duplicates (first vs last)?

---

## SingleElementInASortedArray

**Problem:** Every element appears twice except one that appears once. Find it in O(log n) time.

**Intuition:** Before the single element, pairs are at even/odd indices `(0,1)`, `(2,3)`, etc. After it, the pattern flips. Use binary search checking `nums[mid] == nums[mid ^ 1]` (pair check).

**Pattern:** Binary search on pair structure.

**Approach:**
1. Ensure `mid` is even (for pair checking)
2. If `nums[mid] == nums[mid + 1]`: pair intact → single is on right → `left = mid + 2`
3. Else: pair broken → single is on left → `right = mid`

{% include code-tabs-file.html problem="singleelementinasortedarray" %}

**Complexity:**
- Time: O(log n)
- Space: O(1)

**Variations:** Every element appears k times except one? Unsorted array?

---

## ValleyElement

**Problem:** Find a valley element (element smaller than both neighbors) in an array.

**Intuition:** Mirror of peak finding. If `nums[mid] > nums[mid + 1]`, valley is on the right (because the array must eventually go up since it's bounded). Works like finding a local minimum.

**Pattern:** Local valley binary search.

**Approach:**
1. Binary search on `[0, n)`
2. Compare `nums[mid]` with neighbors (safe boundaries with Int.MAX_VALUE)
3. If `nums[mid]` is smaller than both: found valley
4. If `nums[mid] > rightNeighbor`: go right
5. Else: go left

{% include code-tabs-file.html problem="valleyelement" %}

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

## Key Takeaways

1. **Search for exact value** → Standard binary search
2. **Search for boundary** → Left/right boundary binary search
3. **Minimize/Maximize** → Binary search on answer with feasibility predicate
4. **Not obviously sorted** → The search space can be a **range of values**, not just array indices
5. **Rotated array** → Compare mid with right boundary to determine sorted half
6. **Two arrays** → Partition-based binary search

The common thread: **find a predicate that splits the search space into "yes" and "no"** — then binary search finds the transition point.

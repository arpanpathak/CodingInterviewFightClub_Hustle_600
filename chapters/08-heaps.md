---
layout: chapter
title: "Heaps & Priority Queues"
chapter_number: 8
chapter_title: "Heaps & Priority Queues"
toc: true
prev_chapter:
  url: "/chapters/07-bit-manipulation"
  title: "Bit Manipulation - Working at the Hardware Level"
next_chapter:
  url: "/chapters/09-disjoint-set-union"
  title: "Disjoint Set Union - Union-Find"
---

# Heaps & Priority Queues

## Complete Problem Set (11 problems)

| # | Problem | Pattern | Difficulty | File |
|---|---------|---------|------------|------|
| 1 | Kth Largest Element | MinHeap of size k | Medium | heap/KthLargestElement.kt |
| 2 | Top K Frequent Elements | Freq map + heap | Medium | heap/TopKFrequentElements.kt |
| 3 | Find K Closest Elements | MaxHeap diff | Medium | heap/FindKClosestElements.kt |
| 4 | Median from Data Stream | Two heaps | Hard | heap/MedianFromRunningStream.kt |
| 5 | Sliding Window Median | Two heaps | Hard | heap/SlidingWindowMedian.kt |
| 6 | IPO | Capital + profit | Hard | heap/IPO.kt |
| 7 | Single-Threaded CPU | Sort + heap | Medium | heap/SingleThreadedCPU.kt |
| 8 | Meeting Rooms III | Heap of rooms | Hard | heap/MeetingRoom_III.kt |
| 9 | Longest Happy String | MaxHeap freq | Medium | heap/LongestHappyString.kt |
| 10 | Finding MK Average | Three heaps | Hard | heap/FindingMKAverage.kt |
| 11 | Dual Balanced Heap | Two heaps | Medium | heap/DualBalancedHeap.kt |
| 12 | Find Score After Marking | Sorted + heap | Medium | heap/FindScoreOfAnArrayAfterMarkingAllElements.kt |

### Top K Frequent Elements
```kotlin
fun topKFrequent(nums: IntArray, k: Int): IntArray {
    val freq = mutableMapOf<Int, Int>()
    for (n in nums) freq[n] = freq.getOrDefault(n, 0) + 1
    val heap = PriorityQueue<Pair<Int, Int>>(compareBy { it.second })
    for ((num, count) in freq) {
        heap.add(num to count)
        if (heap.size > k) heap.poll()
    }
    return IntArray(k) { heap.poll().first }
}
```

### Median from Data Stream
```kotlin
class MedianFinder {
    private val maxHeap = PriorityQueue<Int>(reverseOrder())  // Left half
    private val minHeap = PriorityQueue<Int>()                 // Right half
    
    fun addNum(num: Int) {
        maxHeap.add(num); minHeap.add(maxHeap.poll())
        if (minHeap.size > maxHeap.size) maxHeap.add(minHeap.poll())
    }
    
    fun findMedian(): Double {
        return if (maxHeap.size > minHeap.size) maxHeap.peek().toDouble()
               else (maxHeap.peek() + minHeap.peek()) / 2.0
    }
}
```

### IPO (Hard)
```kotlin
fun findMaximizedCapital(k: Int, w: Int, profits: IntArray, capital: IntArray): Int {
    val projects = capital.indices.map { capital[it] to profits[it] }.sortedBy { it.first }
    val maxHeap = PriorityQueue<Int>(reverseOrder())
    var i = 0; var currentCapital = w
    repeat(k) {
        while (i < projects.size && projects[i].first <= currentCapital) {
            maxHeap.add(projects[i].second); i++
        }
        if (maxHeap.isEmpty()) return currentCapital
        currentCapital += maxHeap.poll()
    }
    return currentCapital
}
```

---

> **Next up: [Disjoint Set Union ->](./09-disjoint-set-union.md)**

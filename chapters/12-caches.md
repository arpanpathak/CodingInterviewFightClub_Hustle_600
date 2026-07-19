---
layout: chapter
title: "Caches - LRU, LFU & Memory Management"
chapter_number: 12
chapter_title: "Caches"
toc: true
prev_chapter:
  url: "/chapters/11-backtracking"
  title: "Backtracking - Exhaustive Search Mastery"
next_chapter:
  url: "/chapters/13-appendix"
  title: "Appendix - The Gigachad Toolkit"
---

# Caches - LRU, LFU & Memory Management

This chapter covers problems from the CrackGoogle repository. All source files are linked below.

## Complete Problem Set

| # | Problem | Pattern | File |
|---|---------|---------|------|
| 1 | LRU Cache | HashMap + DLL | cache/LRUCache.kt |
| 2 | LRU Cache (LinkedList) | LinkedHashMap | cache/LRUCacheLinkedList.kt |
| 3 | LFU Cache | Freq Map | cache/LFUCache.kt |

### LRU Cache
```kotlin
class LRUCache(private val capacity: Int) {
    private val map = LinkedHashMap<Int, Int>(capacity, 0.75f, true) {
        override fun removeEldestEntry(eldest: MutableMap.MutableEntry<Int, Int>?): Boolean = size > capacity
    }
    fun get(key: Int): Int = map.getOrDefault(key, -1)
    fun put(key: Int, value: Int) { map[key] = value }
}
```


See the [Master Problem Index](./14-problem-index.md) for the full catalog of all 465+ problems.

---

> **Next up: [Appendix - The Gigachad Toolkit ->](/chapters/13-appendix.md)**

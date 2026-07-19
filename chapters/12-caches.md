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

# Caches: LRU, LFU & Memory Management

## Complete Problem Set (3 problems)

| # | Problem | Pattern | Difficulty | File |
|---|---------|---------|------------|------|
| 1 | LRU Cache | HashMap + Doubly Linked List | Medium | cache/LRUCache.kt |
| 2 | LRU Cache (Linked List) | LinkedHashMap | Medium | cache/LRUCacheLinkedList.kt |
| 3 | LFU Cache | HashMap + Frequency Map | Hard | cache/LFUCache.kt |

### LRU Cache
```kotlin
class LRUCache(private val capacity: Int) {
    private val map = LinkedHashMap<Int, Int>(capacity, 0.75f, true) {
        override fun removeEldestEntry(eldest: MutableMap.MutableEntry<Int, Int>?): Boolean {
            return size > capacity
        }
    }
    fun get(key: Int): Int = map.getOrDefault(key, -1)
    fun put(key: Int, value: Int) { map[key] = value }
}
```

### LFU Cache
```kotlin
class LFUCache(private val capacity: Int) {
    private val values = mutableMapOf<Int, Int>()
    private val counts = mutableMapOf<Int, Int>()
    private val freqMap = mutableMapOf<Int, LinkedHashSet<Int>>()
    private var minFreq = 0
    
    init { freqMap[1] = LinkedHashSet() }
    
    fun get(key: Int): Int {
        if (!values.containsKey(key)) return -1
        val count = counts[key]!!
        counts[key] = count + 1
        freqMap[count]!!.remove(key)
        freqMap.getOrPut(count + 1) { LinkedHashSet() }.add(key)
        if (count == minFreq && freqMap[count]!!.isEmpty()) minFreq++
        return values[key]!!
    }
    
    fun put(key: Int, value: Int) {
        if (capacity <= 0) return
        if (values.containsKey(key)) {
            values[key] = value; get(key); return
        }
        if (values.size >= capacity) {
            val evict = freqMap[minFreq]!!.first()
            freqMap[minFreq]!!.remove(evict)
            values.remove(evict); counts.remove(evict)
        }
        values[key] = value; counts[key] = 1
        freqMap[1]!!.add(key); minFreq = 1
    }
}
```

---

> **Next up: [Appendix ->](./13-appendix.md)**

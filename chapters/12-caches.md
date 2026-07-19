---
layout: chapter
title: "Caches & Memory Management"
chapter_number: 12
chapter_title: "Caches & Memory Management"
toc: true
prev_chapter:
  url: "/chapters/11-backtracking.html"
  title: "Backtracking"
---

# Caches & Memory Management

> **3 problems** — Master cache design: LRU, LFU, and eviction strategies.

## The Pattern

Hash map for O(1) lookup + linked list for ordering. LRU = access order, LFU = frequency.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [LFU Cache](#lfucache) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [LRU Cache](#lrucache) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [LRU Cache Linked List](#lrucachelinkedlist) | — | <span class="badge badge-medium">Medium</span> |

---

## LFU Cache

### Problem

Solves the LFUCache problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package cache

class LFUCache(capacity: Int) {

    private val vals = mutableMapOf<Int, Int>()
    private val freq = mutableMapOf<Int, Int>()
    private val lists = mutableMapOf<Int, LinkedHashSet<Int>>()

    private val MAX_SIZE = capacity
    private var min = -1

    init {
        lists[1] = LinkedHashSet()
    }

    /**
    * Solves the LFUCache problem.
    * Takes `key` (integer).
    *
    * @param key The integer parameter representing key.
    * @return The computed integer result.
    */
    fun get(key: Int): Int {
        if (!vals.containsKey(key))
            return -1
        val count = freq[key]!!
        freq[key] = count + 1
        lists[count]?.remove(key)

        if (count == min && lists[count]?.size == 0 ) {
            min++
        }

        if (!lists.containsKey(count  + 1)) {
            lists[count + 1] = LinkedHashSet()
        }

        lists[count + 1]?.add(key)

        return vals[key]!!
    }

    /**
    * Solves the LFUCache problem.
    * Takes `key` (integer), `value` (integer).
    *
    * @param key The integer parameter representing key.
    * @param value The integer parameter representing value.
    * @return Unit (no return value, modifies state in-place).
    */
    fun put(key: Int, value: Int) {
        if (MAX_SIZE <= 0)
            return ;
        if (vals.containsKey(key)) {
            vals.put(key, value)
            get(key)
            return ;
        }

        if (vals.size >= MAX_SIZE) {
            val evict = lists.get(min)?.first()

            lists.get(min)?.remove(evict)
            vals.remove(evict)
            freq.remove(evict)
        }

        vals[key] = value
        freq[key] = 1
        min = 1
        lists[1]?.add(key)
    }

}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## LRU Cache

### Problem

Solves the LRUCache problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package cache

class LRUCache(private val capacity: Int) {

    private val cache: LinkedHashMap<Int, Int> = LinkedHashMap()

    /**
    * Solves the LRUCache problem.
    * Takes `key` (integer).
    *
    * @param key The integer parameter representing key.
    * @return The computed integer result.
    */
    fun get(key: Int): Int {
        val data = cache[key] ?: -1

        // cache[key] = data // Move accessed element to the end to mark it as recently used
        if (data !=- 1)
            put(key, data)
        return data
    }

    /**
    * Solves the LRUCache problem.
    * Takes `key` (integer), `value` (integer).
    *
    * @param key The integer parameter representing key.
    * @param value The integer parameter representing value.
    * @return Unit (no return value, modifies state in-place).
    */
    fun put(key: Int, value: Int) {
        if (cache.containsKey(key)) {
            cache.remove(key)
        } else if (cache.size == this.capacity) {
            // Eviction policy
            cache.remove(cache.keys.first()) // Remove the least recently used element
        }
        cache[key] = value // Insert the new element
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

## LRU Cache Linked List

### Problem

Solves the LRUCache Linked List problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package cache

import java.util.*

class LRUCacheLinkedList(private val capacity: Int) {
    private class Node(val key: Int, var value: Int) {
        var prev: Node? = null
        var next: Node? = null
    }

    private val cache = HashMap<Int, Node>() // Hash map for O(1) access
    private val head = Node(-1, -1) // Dummy head
    private val tail = Node(-1, -1) // Dummy tail

    init {
        head.next = tail
        tail.prev = head
    }

    /**
    * Solves the LRUCache Linked List problem.
    * Takes `key` (integer).
    *
    * @param key The integer parameter representing key.
    * @return The computed integer result.
    */
    fun get(key: Int): Int {
        val node = cache[key] ?: return -1 // Key not found
        moveToHead(node) // Move the node to the head (most recently used)
        return node.value
    }

    /**
    * Solves the LRUCache Linked List problem.
    * Takes `key` (integer), `value` (integer).
    *
    * @param key The integer parameter representing key.
    * @param value The integer parameter representing value.
    * @return Unit (no return value, modifies state in-place).
    */
    fun put(key: Int, value: Int) {
        val node = cache[key]
        if (node != null) {
            // Update the value and move to head
            node.value = value
            moveToHead(node)
        } else {
            // Create a new node and add to head
            val newNode = Node(key, value)
            cache[key] = newNode
            addToHead(newNode)

            // If capacity is exceeded, remove the tail node (least recently used)
            if (cache.size > capacity) {
                val tailNode = removeTail()
                cache.remove(tailNode.key)
            }
        }
    }

    /**
    * Helper: add to head.
    *
    * @param node The Node.
    * @return Unit (no return value, modifies state in-place).
    */
    private fun addToHead(node: Node) {
        // Add the node to the head of the list
        node.prev = head
        node.next = head.next
        head.next?.prev = node
        head.next = node
    }

    /**
    * Helper: remove node.
    *
    * @param node The Node.
    * @return Unit (no return value, modifies state in-place).
    */
    private fun removeNode(node: Node) {
        // Remove the node from the list
        node.prev?.next = node.next
        node.next?.prev = node.prev
    }

    /**
    * Helper: move to head.
    *
    * @param node The Node.
    * @return Unit (no return value, modifies state in-place).
    */
    private fun moveToHead(node: Node) {
        // Move the node to the head of the list
        removeNode(node)
        addToHead(node)
    }

    /**
    * Helper: remove tail.
    *
    * @return The computed result (Node).
    */
    private fun removeTail(): Node {
        // Remove and return the tail node (least recently used)
        val tailNode = tail.prev!!
        removeNode(tailNode)
        return tailNode
    }
}

/**
* Entry point for the program.
*
* @return Unit (no return value, modifies state in-place).
*/
fun main() {
    val lruCache = LRUCache(2)
    lruCache.put(1, 1) // Cache is {1=1}
    lruCache.put(2, 2) // Cache is {1=1, 2=2}
    println(lruCache.get(1)) // Returns 1 (Cache is {2=2, 1=1})
    lruCache.put(3, 3) // Evicts key 2, cache is {1=1, 3=3}
    println(lruCache.get(2)) // Returns -1 (not found)
    lruCache.put(4, 4) // Evicts key 1, cache is {3=3, 4=4}
    println(lruCache.get(1)) // Returns -1 (not found)
    println(lruCache.get(3)) // Returns 3 (Cache is {4=4, 3=3})
    println(lruCache.get(4)) // Returns 4 (Cache is {3=3, 4=4})
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

---

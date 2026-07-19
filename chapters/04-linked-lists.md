---
layout: chapter
title: "Linked Lists"
chapter_number: 4
chapter_title: "Linked Lists"
toc: true
prev_chapter:
  url: "/chapters/03-arrays-two-pointers.html"
  title: "Arrays & Two Pointers"
next_chapter:
  url: "/chapters/05-trees.html"
  title: "Trees"
---

# Linked Lists

> **16 problems** — Master pointer manipulation and linked list operations.

## The Pattern

Linked lists are about pointer rearrangement: slow/fast pointers, dummy heads, in-place reversal.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [List Node](#addtwonumbers) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Copy Linked List With Random Pointer](#copylinkedlistwithrandompointer) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Delete Middle Node Of Linked List](#deletemiddlenodeoflinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Node](#insertintoasortedcircularlinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [Intersection Of Two Linked List](#intersectionoftwolinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Linked List Cycle](#linkedlistcycle) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [Linked List Cycle_II](#linkedlistcycle_ii) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [Merge K Sorted List](#mergeksortedlist) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Merge K Sorted List Iterative](#mergeksortedlistiterative) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Merge Two Sorted L Ist](#mergetwosortedlist) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [Odd Even Linked List](#oddevenlinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 12 | [Palindrome Linked List](#palindromelinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 13 | [Remove Nth Node From End Of List](#removenthnodefromendoflist) | — | <span class="badge badge-medium">Medium</span> |
| 14 | [Reverse Linked List](#reverselinkedlist) | — | <span class="badge badge-medium">Medium</span> |
| 15 | [Reverse Linked List Iterative](#reverselinkedlistiterative) | — | <span class="badge badge-medium">Medium</span> |
| 16 | [Reverse Nodes In K Groups](#reversenodesinkgroups) | — | <span class="badge badge-medium">Medium</span> |

---

## List Node

### Problem

Solves the List Node problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package linkedlist

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class AddTwoNumbers {
    /**
    * Solves the List Node problem.
    * Takes `l1` (linked list node reference), `l2` (linked list node reference).
    *
    * @param l1 The input linked list node reference.
    * @param l2 The input linked list node reference.
    * @return The resulting collection (linked list node reference).
    */
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var carry = 0
        val head = ListNode(0)
        var ptr = head
        var (n1, n2) = Pair(l1, l2)

        while (n1!= null || n2 != null) {
            val sum = (n1?.`val` ?: 0) + (n2?.`val` ?: 0) + carry
            ptr.next = ListNode(sum % 10)
            ptr = ptr.next!!

            carry = if (sum > 9) 1 else 0

            if (n1 != null) n1 = n1.next

            if (n2 != null) n2 = n2.next
        }

        if (carry > 0) {
            ptr.next = ListNode(carry)
        }

        return head.next
    }
}
```


### Pattern Insight

Study the code and identify the algorithmic pattern.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

### Variations


---
## Copy Linked List With Random Pointer

### Problem

Example:

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package linkedlist

class CopyLinkedListWithRandomPointer {
    /**
     * Example:
     * var ti = Node(5)
     * var v = ti.`val`
     * Definition for a Node.
     * class Node(var `val`: Int) {
     *     var next: Node? = null
     *     var random: Node? = null
     * }
     */

    class Node(var `val`: Int) {
        var next: Node? = null
        var random: Node? = null
    }

    class Solution {
        /**
        * Solves the Copy Linked List With Random Pointer problem.
        * Takes `node` (Node?).
        *
        * @param node The Node? (nullable).
        * @return The result, or `null` if not found.
        */
        fun copyRandomList(node: Node?): Node? {
            if (node == null) return null

            val nodeMap = mutableMapOf<Node, Node>()

            // Step 1: Create deep copies of all nodes and store the mapping
            var ptr = node
            while (ptr != null) {
                nodeMap[ptr] = Node(ptr.`val`)
                ptr = ptr.next
            }

            // Step 2: Set the next and random pointers for the copied nodes
            ptr = node
            while (ptr != null) {
                nodeMap[ptr]?.next = nodeMap[ptr.next]
                nodeMap[ptr]?.random = nodeMap[ptr.random]
                ptr = ptr.next
            }

            // Return the head of the new copied list
            return nodeMap[node]
        }
    }
}
```


### Pattern Insight

**Pattern:** BFS (Breadth-First Search). Use a queue to explore nodes level by level, guaranteeing shortest path in unweighted graphs.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations

1. What if the graph is disconnected?
1. What if edges have weights (non-uniform cost)?
1. Can this be solved with DFS instead? What's the tradeoff?
1. What if you need the path, not just the distance/existence?
1. What if the graph is too large for BFS? Iterative deepening?

---
y

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations


---
ent?.next = newNode
        return head
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Intersection Of Two Linked List

### Problem

Solves the Intersection Of Two Linked List problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package linkedlist

class IntersectionOfTwoLinkedList {
    /**
    * Solves the Intersection Of Two Linked List problem.
    * Takes `headA` (linked list node reference), `headB` (linked list node reference).
    *
    * @param headA The input linked list node reference.
    * @param headB The input linked list node reference.
    * @return The resulting collection (linked list node reference).
    */
    fun getIntersectionNode(headA: ListNode?, headB: ListNode?): ListNode? {
        if (headA == null || headB == null) return null

        var pA = headA
        var pB = headB

        // Traverse both lists. When one pointer reaches the end, redirect it to the head of the other list.
        while (pA != pB) {
            pA = if (pA == null) headB else pA.next
            pB = if (pB == null) headA else pB.next
        }

        return pA // This will return the intersection node, or null if no intersection.
    }
}
```


### Pattern Insight

**Pattern:** BFS (Breadth-First Search). Use a queue to explore nodes level by level, guaranteeing shortest path in unweighted graphs.


### Pattern Insight

**Pattern:** BFS (Breadth-First Search). Use a queue to explore nodes level by level, guaranteeing shortest path in unweighted graphs.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations

1. What if the graph is disconnected?
1. What if edges have weights (non-uniform cost)?
1. Can this be solved with DFS instead? What's the tradeoff?
1. What if you need the path, not just the distance/existence?
1. What if the graph is too large for BFS? Iterative deepening?

---
## Linked List Cycle

### Problem

Solves the Linked List Cycle problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package linkedlist

class LinkedListCycle {
    /**
    * Solves the Linked List Cycle problem.
    * Takes `head` (linked list node reference).
    *
    * @param head The input linked list node reference.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun hasCycle(head: ListNode?): Boolean {
        if (head == null || head.next == null) return false

        var slow = head
        var fast = head.next

        while (slow != fast ) {
            if (fast == null || fast.next == null)
                return false

            slow = slow?.next
            fast = fast?.next?.next
        }

        return true
    }

    // Better version
    /**
    * Solves the Linked List Cycle problem.
    * Takes `head` (linked list node reference).
    *
    * @param head The input linked list node reference.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun hasCycle2(head: ListNode?): Boolean {
        var slow = head
        var fast = head

        while (fast != null && fast.next != null) {
            slow = slow?.next
            fast = fast.next?.next

            if (slow == fast) {
                return true
            }
        }

        return false
    }
}
```


### Pattern Insight

**Pattern:** BFS (Breadth-First Search). Use a queue to explore nodes level by level, guaranteeing shortest path in unweighted graphs.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Linked List Cycle_II

### Problem

Solves the Linked List Cycle_II problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package linkedlist

class LinkedListCycle_II {
    /**
    * Solves the Linked List Cycle_II problem.
    * Takes `head` (linked list node reference).
    *
    * @param head The input linked list node reference.
    * @return The resulting collection (linked list node reference).
    */
    fun detectCycle(head: ListNode?): ListNode? {
        var slow = head
        var fast = head

        // Phase 1: Detect if a cycle exists
        while (fast != null && fast.next != null) {
            slow = slow?.next
            fast = fast.next?.next

            if (slow == fast) {  // Cycle detected
                // Phase 2: Find the start of the cycle
                var entry = head
                while (entry != slow) {
                    entry = entry?.next
                    slow = slow?.next
                }
                return entry
            }
        }

        return null  // No cycle
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations

1. What if the graph is disconnected?
1. What if edges have weights (non-uniform cost)?
1. Can this be solved with DFS instead? What's the tradeoff?
1. What if you need the path, not just the distance/existence?
1. What if the graph is too large for BFS? Iterative deepening?

---


### Code

```kotlin
package linkedlist

class MergeKSortedList {
    /**
    * Solves the Merge KSorted List problem.
    * Takes `list1` (linked list node reference), `list2` (linked list node reference).
    *
    * @param list1 The input linked list node reference.
    * @param list2 The input linked list node reference.
    * @return The resulting collection (linked list node reference).
    */
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        val head = ListNode(0) // dummy node
        var ptr = head

        var ptr1 = list1
        var ptr2 = list2

        while (ptr1 != null && ptr2 != null) {
            if (ptr1.`val` < ptr2.`val`) {
                ptr.next = ListNode(ptr1.`val`)
                ptr1 = ptr1.next
            } else {
                ptr.next = ListNode(ptr2.`val`)
                ptr2 = ptr2.next
            }
            ptr = ptr.next!!
        }

        ptr.next = ptr1 ?: ptr2

        return head.next
    }

    /**
    * Solves the Merge KSorted List problem.
    * Takes `lists` (Array<ListNode?>).
    *
    * @param lists The input Array<ListNode?>.
    * @return The resulting collection (linked list node reference).
    */
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        if (lists.isEmpty())
            return null
        /**
        * Solves the Merge KSorted List problem.
        * Takes `start` (integer), `end` (integer).
        *
        * @param start The integer parameter representing start.
        * @param end The integer parameter representing end.
        * @return The resulting collection (linked list node reference).
        */
        fun merge(start: Int, end: Int): ListNode? {
            if (start == end)
                return lists[start]
            val mid = start + (end - start) / 2
            val left = merge(start, mid)
            val right = merge(mid + 1, end)

            return mergeTwoLists(left, right)
        }
        return merge(0, lists.lastIndex)
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Merge K Sorted List Iterative

### Problem

Solves the Merge KSorted List Iterative problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package linkedlist

class MergeKSortedListIterative {
    /**
    * Solves the Merge KSorted List Iterative problem.
    * Takes `lists` (Array<ListNode?>).
    *
    * @param lists The input Array<ListNode?>.
    * @return The resulting collection (linked list node reference).
    */
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        if (lists.isEmpty()) return null

        var interval = 1
        val n = lists.size

        while (interval < n) {
            for (i in 0 until n - interval step interval * 2) {
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            }
            interval *= 2
        }

        return lists[0]
    }

    /**
    * Solves the Merge KSorted List Iterative problem.
    * Takes `list1` (linked list node reference), `list2` (linked list node reference).
    *
    * @param list1 The input linked list node reference.
    * @param list2 The input linked list node reference.
    * @return The resulting collection (linked list node reference).
    */
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        val head = ListNode(0) // Dummy node
        var ptr = head

        var ptr1 = list1
        var ptr2 = list2

        while (ptr1 != null && ptr2 != null) {
            if (ptr1.`val` < ptr2.`val`) {
                ptr.next = ptr1
                ptr1 = ptr1.next
            } else {
                ptr.next = ptr2
                ptr2 = ptr2.next
            }
            ptr = ptr.next!!
        }

        ptr.next = ptr1 ?: ptr2

        return head.next
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Merge Two Sorted L Ist

### Problem

Solves the Merge Two Sorted LIst problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package linkedlist

class MergeTwoSortedLIst {
    /**
    * Solves the Merge Two Sorted LIst problem.
    * Takes `list1` (linked list node reference), `list2` (linked list node reference).
    *
    * @param list1 The input linked list node reference.
    * @param list2 The input linked list node reference.
    * @return The resulting collection (linked list node reference).
    */
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        val head = ListNode(0) // dummy node
        var ptr = head

        var ptr1 = list1
        var ptr2 = list2

        while (ptr1 != null && ptr2 != null) {
            if (ptr1.`val` < ptr2.`val`) {
                ptr.next = ListNode(ptr1.`val`)
                ptr1 = ptr1.next
            } else {
                ptr.next = ListNode(ptr2.`val`)
                ptr2 = ptr2.next
            }
            ptr = ptr.next!!
        }

        ptr.next = ptr1 ?: ptr2

        return head.next
    }
}
```


### Pattern Insight

**Pattern:** Linked list manipulation. Use pointer rearrangement to achieve O(1) space solutions.


### Pattern Insight

**Pattern:** Linked list manipulation. Use pointer rearrangement to achieve O(1) space solutions.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Odd Even Linked List

### Problem

Solves the Odd Even Linked List problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package linkedlist

class OddEvenLinkedList {
    /**
    * Solves the Odd Even Linked List problem.
    * Takes `head` (linked list node reference).
    *
    * @param head The input linked list node reference.
    * @return The resulting collection (linked list node reference).
    */
    fun oddEvenList(head: ListNode?): ListNode? {
        var odd = head
        var even = head?.next
        var evenHead = even

        while (even?.next != null) {

            odd?.next = odd?.next?.next
            odd = odd?.next

            even.next = even.next?.next
            even = even.next
        }

        odd?.next = evenHead
        return head
    }

}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations

1. What if the list is circular? How does detection change?
1. What if you can't use extra memory (O(1) space constraint)?
1. What if the list is doubly linked? Any simplifications?
1. What if you need to do this recursively vs iteratively?
1. What if multiple operations need to be supported (LRU cache pattern)?

---
l algorithmic pattern._

### Code

```kotlin
package linkedlist

class PalindromeLinkedList {
    class Solution {
        /**
        * Solves the Palindrome Linked List problem.
        * Takes `head` (linked list node reference).
        *
        * @param head The input linked list node reference.
        * @return `true` if the condition is met, `false` otherwise.
        */
        fun isPalindrome(head: ListNode?): Boolean {
            if (head?.next == null) return true // Edge case: empty or single node

            var slow = head
            var fast = head

            // Step 1: Find the middle
            while (fast?.next != null && fast.next?.next != null) {
                slow = slow?.next
                fast = fast.next?.next
            }

            // Step 2: Reverse second half
            var secondHalf = reverseList(slow?.next)
            var firstHalf = head

            // Step 3: Compare both halves
            var temp = secondHalf
            while (temp != null) {
                if (firstHalf?.`val` != temp.`val`) return false
                firstHalf = firstHalf?.next
                temp = temp.next
            }

            // Step 4: Restore original list (optional)
            slow?.next = reverseList(secondHalf)

            return true
        }

        /**
        * Helper: reverse list.
        *
        * @param head The input linked list node reference.
        * @return The resulting collection (linked list node reference).
        */
        private fun reverseList(head: ListNode?): ListNode? {
            var prev: ListNode? = null
            var curr = head
            while (curr != null) {
                val next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            }
            return prev
        }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Remove Nth Node From End Of List

### Problem

Solves the Remove Nth Node From End Of List problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package linkedlist

class RemoveNthNodeFromEndOfList {
    /**
    * Solves the Remove Nth Node From End Of List problem.
    * Takes `head` (linked list node reference), `n` (integer).
    *
    * @param head The input linked list node reference.
    * @param n The integer parameter representing n.
    * @return The resulting collection (linked list node reference).
    */
    fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
        var size = 0
        var ptr = head

        while(ptr != null) {
            size++
            ptr = ptr.next
        }

        val indexToRemove = (size - n)
        return removeNthFromFront(head, indexToRemove, size)
    }

    /**
    * Helper: remove nth from front.
    *
    * @param head The input linked list node reference.
    * @param indexToRemove The integer parameter representing indexToRemove.
    * @param size The integer parameter representing size.
    * @return The resulting collection (linked list node reference).
    */
    private fun removeNthFromFront(head: ListNode?, indexToRemove: Int, size: Int): ListNode? {
        var ptr = head
        var prev: ListNode? = null
        for(i in 0 until indexToRemove) {
            prev = ptr
            ptr = ptr?.next
        }

        return when(indexToRemove) {
            0 -> head?.next
            else -> {
                prev?.next = ptr?.next
                head
            }
        }
    }

    /**
     * Two Pointer approach
     */
    fun removeNthFromEndTwoPointer(head: ListNode?, n: Int): ListNode? {
        val dummy = ListNode(0).apply { next = head }
        var first: ListNode? = dummy
        var second: ListNode? = dummy

        // Move first n + 1 steps ahead
        for (i in 0..n) {
            first = first?.next
        }

        // Move first to the end, maintaining the gap of size n
        while (first != null) {
            first = first.next
            second = second?.next
        }

        // Remove the nth node from the end
        second?.next = second?.next?.next

        return dummy.next
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

## Reverse Linked List

### Problem

Solves the Reverse Linked List problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package linkedlist

class ReverseLinkedList {
    /**
    * Solves the Reverse Linked List problem.
    * Takes `head` (linked list node reference).
    *
    * @param head The input linked list node reference.
    * @return The resulting collection (linked list node reference).
    */
    fun reverseList(head: ListNode?): ListNode? {
        if (head?.next == null) {
            return head
        }

        val reversedHead = reverseList(head.next)

        head.next?.next = head
        head.next = null

        return reversedHead
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## Reverse Linked List Iterative

### Problem

Solves the Reverse Linked List Iterative problem.

### Why This Approach

_Refer to the **Pattern** section above for the general algorithmic pattern._

### Code

```kotlin
package linkedlist

class ReverseLinkedListIterative {
    /**
    * Solves the Reverse Linked List Iterative problem.
    * Takes `head` (linked list node reference).
    *
    * @param head The input linked list node reference.
    * @return The resulting collection (linked list node reference).
    */
    fun reverseList(head: ListNode?): ListNode? {
        var prev: ListNode? = null
        var current = head
        while (current != null) {
            val nextTemp = current.next
            current.next = prev
            prev = current
            current = nextTemp
        }
        return prev
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) |

### Variations

1. What if the graph is disconnected?
1. What if edges have weights (non-uniform cost)?
1. Can this be solved with DFS instead? What's the tradeoff?
1. What if you need the path, not just the distance/existence?
1. What if the graph is too large for BFS? Iterative deepening?

---
 {
            // Move `end` k steps forward
            for (i in 0 until k) {
                end = end?.next
                if (end == null) return dummy.next // Not enough nodes to reverse
            }

            // Store the next group start
            val nextGroupStart = end?.next

            // Reverse the current group
            val (newStart, newEnd) = reverse(start?.next, end)

            // Connect the reversed group back to the list
            start?.next = newStart
            newEnd?.next = nextGroupStart

            // Move `start` to `newEnd` (which was the original `start` before reversing)
            start = newEnd
            // Set `end` back to `start` for the next iteration
            end = newEnd
        }

        return dummy.next
    }

    /**
    * Helper: reverse.
    *
    * @param start The input linked list node reference.
    * @param end The input linked list node reference.
    * @return The resulting collection (Pair<ListNode?, ListNode?>).
    */
    private fun reverse(start: ListNode?, end: ListNode?): Pair<ListNode?, ListNode?> {
        var prev: ListNode? = null
        var current = start
        val stop = end?.next

        while (current != stop) {
            val next = current?.next
            current?.next = prev
            prev = current
            current = next
        }

        return Pair(end, start) // `end` is the new start and `start` is the new end after reversing
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

---

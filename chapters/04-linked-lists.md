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

> **14 problems** — **Linked Lists** are about pointer rearrangement. Key patterns: slow/fast pointers for cycle detection, dummy heads for edge cases, recursion for reversal, and in-place merging.

## Complete Problem Set

| # | Problem |
|---|---------|
| 1 | [List Node](#addtwonumbers) |
| 2 | [Copy Linked List With Random Pointer](#copylinkedlistwithrandompointer) |
| 3 | [Delete Middle Node Of Linked List](#deletemiddlenodeoflinkedlist) |
| 4 | [Node](#insertintoasortedcircularlinkedlist) |
| 5 | [Intersection Of Two Linked List](#intersectionoftwolinkedlist) |
| 6 | [Linked List Cycle](#linkedlistcycle) |
| 7 | [Linked List Cycle_II](#linkedlistcycle_ii) |
| 8 | [Merge K Sorted List](#mergeksortedlist) |
| 9 | [Merge Two Sorted L Ist](#mergetwosortedlist) |
| 10 | [Odd Even Linked List](#oddevenlinkedlist) |
| 11 | [Palindrome Linked List](#palindromelinkedlist) |
| 12 | [Remove Nth Node From End Of List](#removenthnodefromendoflist) |
| 13 | [Reverse Linked List](#reverselinkedlist) |
| 14 | [Reverse Nodes In K Groups](#reversenodesinkgroups) |

---

## List Node

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class AddTwoNumbers {

/**
 * Inserts the specified element into the data structure.
 *
 * @param l1 the l1 parameter — a tree/graph node used in the computation
 * @param l2 the l2 parameter — a tree/graph node used in the computation
 * @return a list/collection of result elements
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

---

## Copy Linked List With Random Pointer

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

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
 * copy Random List — executes the core logic of this algorithm on the provided input.
 *
 * @param node the root/head node of the data structure
 * @return the resulting tree/graph node
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Delete Middle Node Of Linked List

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class DeleteMiddleNodeOfLinkedList {
    
    // Two Pass Approach

/**
 * Removes specified elements from the collection and returns the result.
 *
 * @param head the root/head node of the data structure
 * @return a list/collection of result elements
 */
    fun deleteMiddle(head: ListNode?): ListNode? {
        var currentNode = head
        var prevNode: ListNode? = null
        var index = 0
        var n =0
        while (currentNode != null) {
            n++
            currentNode = currentNode.next

        }

        currentNode = head
        while (currentNode != null) {
            if (index++ == n/2)
                break
            prevNode = currentNode
            currentNode = currentNode.next
        }

        if (prevNode != null)
            prevNode.next = currentNode

        return head
    }

/**
 * Removes specified elements from the collection and returns the result.
 *
 * @param head the root/head node of the data structure
 * @return a list/collection of result elements
 */
    fun deleteMiddleTwoPointer(head: ListNode?): ListNode? {
        var (slow, fast, prev) = listOf(head, head, null)

        if (head?.next == null)
            return null

        while (fast?.next != null ) {
            prev = slow
            slow = slow?.next
            fast = fast?.next?.next
        }

        prev?.next = slow?.next

        return head
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Node

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class Node(var `val`: Int) {
    var next: Node? = null
}

class InsertIntoASortedCircularLinkedList {

/**
 * Inserts the specified element into the data structure.
 *
 * @param head the root/head node of the data structure
 * @param insertVal the insertVal parameter — a integer value used in the computation
 * @return the resulting tree/graph node
 */
    fun insert(head: Node?, insertVal: Int): Node? {
        val newNode = Node(insertVal)
        if (head == null) return newNode.apply { next = newNode }

        var current: Node? = head
        do {
            when {
                current?.`val`!! <= insertVal && insertVal <= current?.next?.`val`!! -> {
                    newNode.next = current?.next
                    current?.next = newNode
                    return head
                }
                current?.`val`!! > current?.next?.`val`!! && (insertVal >= current?.`val`!! || insertVal <= current?.next?.`val`!!) -> {
                    newNode.next = current?.next
                    current?.next = newNode
                    return head
                }
            }
            current = current?.next
        } while (current != head)

        newNode.next = current?.next
        current?.next = newNode
        return head
    }
}

```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Intersection Of Two Linked List

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class IntersectionOfTwoLinkedList {

/**
 * Retrieves and returns the requested element or value from the data structure.
 *
 * @param headA the headA parameter — a tree/graph node used in the computation
 * @param headB the headB parameter — a tree/graph node used in the computation
 * @return a list/collection of result elements
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Linked List Cycle

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class LinkedListCycle {

/**
 * Checks whether the specified condition holds true for the given input.
 *
 * @param head the root/head node of the data structure
 * @return `true` if the target element/value exists, `false` otherwise
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
 * Checks whether the specified condition holds true for the given input.
 *
 * @param head the root/head node of the data structure
 * @return `true` if the target element/value exists, `false` otherwise
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Linked List Cycle_II

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class LinkedListCycle_II {

/**
 * detect Cycle — executes the core logic of this algorithm on the provided input.
 *
 * @param head the root/head node of the data structure
 * @return a list/collection of result elements
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Merge K Sorted List

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class MergeKSortedList {

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param list1 the list1 parameter — a tree/graph node used in the computation
 * @param list2 the list2 parameter — a tree/graph node used in the computation
 * @return a list/collection of result elements
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
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param lists the lists parameter — a array of elements used in the computation
 * @return a list/collection of result elements
 */
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        if (lists.isEmpty())
            return null

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param start the left/starting boundary of the search range (inclusive)
 * @param end the right/ending boundary of the search range (inclusive)
 * @return a list/collection of result elements
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Merge Two Sorted L Ist

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class MergeTwoSortedLIst {

/**
 * Sorts or reorders the input elements according to the specified criteria.
 *
 * @param list1 the list1 parameter — a tree/graph node used in the computation
 * @param list2 the list2 parameter — a tree/graph node used in the computation
 * @return a list/collection of result elements
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Odd Even Linked List

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class OddEvenLinkedList {

/**
 * odd Even List — executes the core logic of this algorithm on the provided input.
 *
 * @param head the root/head node of the data structure
 * @return a list/collection of result elements
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Palindrome Linked List

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class PalindromeLinkedList {
    class Solution {

/**
 * is Palindrome — executes the core logic of this algorithm on the provided input.
 *
 * @param head the root/head node of the data structure
 * @return `true` if the operation succeeds / condition holds, `false` otherwise
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
 * Reverses or rearranges the input elements in place.
 *
 * @param head the root/head node of the data structure
 * @return a list/collection of result elements
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Remove Nth Node From End Of List

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class RemoveNthNodeFromEndOfList {

/**
 * Removes specified elements from the collection and returns the result.
 *
 * @param head the root/head node of the data structure
 * @param n the size/dimension parameter for the algorithm
 * @return a list/collection of result elements
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
 * Removes specified elements from the collection and returns the result.
 *
 * @param head the root/head node of the data structure
 * @param indexToRemove the indexToRemove parameter — a integer value used in the computation
 * @param size the size/dimension parameter for the algorithm
 * @return a list/collection of result elements
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
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

---

## Reverse Linked List

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class ReverseLinkedList {

/**
 * Reverses or rearranges the input elements in place.
 *
 * @param head the root/head node of the data structure
 * @return a list/collection of result elements
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Reverse Nodes In K Groups

**Problem:** Solve this algorithmic challenge efficiently using the appropriate data structures and algorithms.

### Code

```kotlin
package linkedlist

class ReverseNodesInKGroups {

/**
 * Reverses or rearranges the input elements in place.
 *
 * @param head the root/head node of the data structure
 * @param k the number of elements/operations to consider (k parameter)
 * @return a list/collection of result elements
 */
    fun reverseKGroup(head: ListNode?, k: Int): ListNode? {
        if (head == null || k == 1) return head

        val dummy = ListNode(0)
        dummy.next = head
        var start: ListNode? = dummy
        var end: ListNode? = dummy

        while (end?.next != null) {
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
 * Reverses or rearranges the input elements in place.
 *
 * @param start the left/starting boundary of the search range (inclusive)
 * @param end the right/ending boundary of the search range (inclusive)
 * @return a list/collection of result elements
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
| **Time** | O(n) |
| **Space** | O(1) |

---

## Key Takeaways

1. **Core pattern recognition** — Identify the problem type and apply the right algorithmic technique.
2. **Practice systematically** — Work through each problem to internalize the patterns.
3. **Understand why, not just how** — Focus on the reasoning behind each solution.

---

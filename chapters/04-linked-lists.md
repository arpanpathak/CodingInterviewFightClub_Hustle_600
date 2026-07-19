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

Linked lists are about pointer rearrangement. Key patterns: slow/fast pointers, dummy heads, recursion, and in-place reversal.

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

<span id="addtwonumbers"></span>

### Problem

**Addtwonumbers**

**Function:** `Add Two Numbers` takes `l1` (ListNode?), `l2` (ListNode?) and returns **ListNode**.



### Approach

**Solution Approach:**
1. The main function `addTwoNumbers` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `next`, `carry`, `head`, `ptr`, `sum`

### Code

```kotlin
package linkedlist

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class AddTwoNumbers {
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
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Copy Linked List With Random Pointer

<span id="copylinkedlistwithrandompointer"></span>

### Problem

**Copylinkedlistwithrandompointer**

**Function:** `Copy Random List` takes `node` (Node?) and returns **Node**.

**Key logic:**
- Step 1: Create deep copies of all nodes and store the mapping
- Step 2: Set the next and random pointers for the copied nodes
- Return the head of the new copied list



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `ti`, `v`, `next`, `random`, `next`, `random`, `nodeMap`, `ptr`

**Execution flow:**
- Step 1: Create deep copies of all nodes and store the mapping
- Step 2: Set the next and random pointers for the copied nodes
- Return the head of the new copied list

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
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Delete Middle Node Of Linked List

<span id="deletemiddlenodeoflinkedlist"></span>

### Problem

**Deletemiddlenodeoflinkedlist**

**Function:** `Delete Middle` takes `head` (ListNode?) and returns **ListNode**.

**Key logic:**
- Two Pass Approach



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `currentNode`, `prevNode`, `index`, `n`

**Execution flow:**
- Two Pass Approach

### Code

```kotlin
package linkedlist

class DeleteMiddleNodeOfLinkedList {
    
    // Two Pass Approach
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
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Node

<span id="insertintoasortedcircularlinkedlist"></span>

### Problem

**Insertintoasortedcircularlinkedlist**

**Function:** `Insert` takes `head` (Node?), `insertVal` (integer) and returns **Node**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `next`, `newNode`, `current`

### Code

```kotlin
package linkedlist

class Node(var `val`: Int) {
    var next: Node? = null
}

class InsertIntoASortedCircularLinkedList {
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
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Intersection Of Two Linked List

<span id="intersectionoftwolinkedlist"></span>

### Problem

**Intersectionoftwolinkedlist**

**Function:** `Get Intersection Node` takes `headA` (ListNode?), `headB` (ListNode?) and returns **ListNode**.

**Key logic:**
- Traverse both lists. When one pointer reaches the end, redirect it to the head of the other list.
- This will return the intersection node, or null if no intersection.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `pA`, `pB`

**Execution flow:**
- Traverse both lists. When one pointer reaches the end, redirect it to the head of the other list.
- This will return the intersection node, or null if no intersection.

### Code

```kotlin
package linkedlist

class IntersectionOfTwoLinkedList {
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
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Linked List Cycle

<span id="linkedlistcycle"></span>

### Problem

**Linkedlistcycle**

**Function:** `Has Cycle` takes `head` (ListNode?) and returns **boolean**.

**Key logic:**
- Better version



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `slow`, `fast`, `slow`, `fast`

**Execution flow:**
- Better version

### Code

```kotlin
package linkedlist

class LinkedListCycle {
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
| **Time** | O(V + E) |
| **Space** | O(V) |

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Linked List Cycle_II

<span id="linkedlistcycle_ii"></span>

### Problem

**Linkedlistcycle Ii**

**Function:** `Detect Cycle` takes `head` (ListNode?) and returns **ListNode**.

**Key logic:**
- Phase 1: Detect if a cycle exists
- Cycle detected
- Phase 2: Find the start of the cycle
- No cycle



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `slow`, `fast`, `entry`

**Execution flow:**
- Phase 1: Detect if a cycle exists
- Cycle detected
- Phase 2: Find the start of the cycle

### Code

```kotlin
package linkedlist

class LinkedListCycle_II {
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

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Merge K Sorted List

<span id="mergeksortedlist"></span>

### Problem

**Mergeksortedlist**

**Function:** `Merge Two Lists` takes `list1` (ListNode?), `list2` (ListNode?) and returns **ListNode**.

**Key logic:**
- dummy node



### Approach

**Solution Approach:**
1. The main function `mergeTwoLists` processes the input
2. Uses helper functions: mergeKLists, merge

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `head`, `ptr`, `ptr1`, `ptr2`, `mid`, `left`, `right`

**Execution flow:**

### Code

```kotlin
package linkedlist

class MergeKSortedList {
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

    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        if (lists.isEmpty())
            return null
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Merge K Sorted List Iterative

<span id="mergeksortedlistiterative"></span>

### Problem

**Mergeksortedlistiterative**

**Function:** `Merge Klists` takes `lists` (Array<ListNode?>) and returns **ListNode**.

**Key logic:**
- Dummy node



### Approach

**Solution Approach:**
1. The main function `mergeKLists` processes the input
2. Uses helper functions: mergeTwoLists

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `interval`, `n`, `step`, `head`, `ptr`, `ptr1`, `ptr2`

**Execution flow:**

### Code

```kotlin
package linkedlist

class MergeKSortedListIterative {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Merge Two Sorted L Ist

<span id="mergetwosortedlist"></span>

### Problem

**Mergetwosortedlist**

**Function:** `Merge Two Lists` takes `list1` (ListNode?), `list2` (ListNode?) and returns **ListNode**.

**Key logic:**
- dummy node



### Approach

**Solution Approach:**
1. The main function `mergeTwoLists` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `head`, `ptr`, `ptr1`, `ptr2`

**Execution flow:**

### Code

```kotlin
package linkedlist

class MergeTwoSortedLIst {
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
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Odd Even Linked List

<span id="oddevenlinkedlist"></span>

### Problem

**Oddevenlinkedlist**

**Function:** `Odd Even List` takes `head` (ListNode?) and returns **ListNode**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `odd`, `even`, `evenHead`

### Code

```kotlin
package linkedlist

class OddEvenLinkedList {
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

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Palindrome Linked List

<span id="palindromelinkedlist"></span>

### Problem

**Palindromelinkedlist**

**Function:** `Is Palindrome` takes `head` (ListNode?) and returns **boolean**.

**Key logic:**
- Edge case: empty or single node
- Step 1: Find the middle
- Step 2: Reverse second half
- Step 3: Compare both halves
- Step 4: Restore original list (optional)



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `slow`, `fast`, `secondHalf`, `firstHalf`, `temp`, `prev`, `curr`, `next`

**Execution flow:**
- Edge case: empty or single node
- Step 1: Find the middle
- Step 2: Reverse second half
- Step 3: Compare both halves
- Step 4: Restore original list (optional)

### Code

```kotlin
package linkedlist

class PalindromeLinkedList {
    class Solution {
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

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Remove Nth Node From End Of List

<span id="removenthnodefromendoflist"></span>

### Problem

**Removenthnodefromendoflist**

**Function:** `Remove Nth From End` takes `head` (ListNode?), `n` (integer) and returns **ListNode**.

**Key logic:**
- Move first n + 1 steps ahead
- Move first to the end, maintaining the gap of size n
- Remove the nth node from the end



### Approach

**Solution Approach:**
1. The main function `removeNthFromEnd` processes the input
2. Uses helper functions: removeNthFromFront, removeNthFromEndTwoPointer

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `size`, `ptr`, `indexToRemove`, `ptr`, `prev`, `dummy`, `first`, `second`

**Execution flow:**
- Move first n + 1 steps ahead
- Move first to the end, maintaining the gap of size n
- Remove the nth node from the end

### Code

```kotlin
package linkedlist

class RemoveNthNodeFromEndOfList {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Reverse Linked List

<span id="reverselinkedlist"></span>

### Problem

**Reverselinkedlist**

**Function:** `Reverse List` takes `head` (ListNode?) and returns **ListNode**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `reversedHead`

### Code

```kotlin
package linkedlist

class ReverseLinkedList {
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

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Reverse Linked List Iterative

<span id="reverselinkedlistiterative"></span>

### Problem

**Reverselinkedlistiterative**

**Function:** `Reverse List` takes `head` (ListNode?) and returns **ListNode**.



### Approach

**BFS (Breadth-First Search) Approach:**
1. Use a queue to process nodes level by level
2. Track visited nodes to avoid cycles
3. BFS guarantees shortest path in unweighted graphs


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `prev`, `current`, `nextTemp`

### Code

```kotlin
package linkedlist

class ReverseLinkedListIterative {
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

**Analysis:**

Each node and edge is visited at most once, giving O(V + E) for a graph with V vertices and E edges. The O(V) space stores visited tracking and the queue/stack.

---

## Reverse Nodes In K Groups

<span id="reversenodesinkgroups"></span>

### Problem

**Reversenodesinkgroups**

**Function:** `Reverse Kgroup` takes `head` (ListNode?), `k` (integer) and returns **ListNode**.

**Key logic:**
- Move `end` k steps forward
- Not enough nodes to reverse
- Store the next group start
- Reverse the current group
- Connect the reversed group back to the list



### Approach

**Solution Approach:**
1. The main function `reverseKGroup` processes the input
2. Uses helper functions: reverse

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dummy`, `start`, `end`, `nextGroupStart`, `prev`, `current`, `stop`, `next`

**Execution flow:**
- Move `end` k steps forward
- Not enough nodes to reverse
- Store the next group start
- Reverse the current group
- Connect the reversed group back to the list
- Move `start` to `newEnd` (which was the original `start` before reversing)
- Set `end` back to `start` for the next iteration
- `end` is the new start and `start` is the new end after reversing

### Code

```kotlin
package linkedlist

class ReverseNodesInKGroups {
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

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Key Takeaways

1. **Core pattern recognition** — Linked lists are about pointer rearrangement. Key patterns: slow/fast pointers, dummy heads, recursion, and in-place reversal.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

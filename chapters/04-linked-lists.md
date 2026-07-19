---
layout: chapter
title: "Linked Lists - Pointer Manipulation"
chapter_number: 4
chapter_title: "Linked Lists"
toc: true
prev_chapter:
  url: "/chapters/03-arrays-two-pointers"
  title: "Arrays & Two Pointers - The Bread and Butter"
next_chapter:
  url: "/chapters/05-trees"
  title: "Trees - Hierarchical Thinking"
---

# Linked Lists - Pointer Manipulation

This chapter covers problems from the CrackGoogle repository. All source files are linked below.

## Complete Problem Set (18 problems)

| # | Problem | Pattern | File |
|---|---------|---------|------|
| 1 | Reverse Linked List | Iterative | linkedlist/ReverseLinkedList.kt |
| 2 | Merge Two Sorted Lists | Merge | linkedlist/MergeTwoSortedLIst.kt |
| 3 | Linked List Cycle | Fast & Slow | linkedlist/LinkedListCycle.kt |
| 4 | Linked List Cycle II | Cycle start | linkedlist/LinkedListCycle_II.kt |
| 5 | Remove Nth Node From End | Two ptrs | linkedlist/RemoveNthNodeFromEndOfList.kt |
| 6 | Palindrome Linked List | Reverse half | linkedlist/PalindromeLinkedList.kt |
| 7 | Add Two Numbers | Math | linkedlist/AddTwoNumbers.kt |
| 8 | Odd Even Linked List | Reorder | linkedlist/OddEvenLinkedList.kt |
| 9 | Intersection of Two Lists | Two ptrs | linkedlist/IntersectionOfTwoLinkedList.kt |
| 10 | Copy List w/ Random | Hash map | linkedlist/CopyLinkedListWithRandomPointer.kt |
| 11 | Delete Middle Node | Fast & Slow | linkedlist/DeleteMiddleNodeOfLinkedList.kt |
| 12 | Insert Sorted Circular | Traversal | linkedlist/InsertIntoASortedCircularLinkedList.kt |
| 13 | Reverse Nodes k-Group | Recursive | linkedlist/ReverseNodesInKGroups.kt |
| 14 | Merge k Sorted Lists | Divide Conquer | linkedlist/MergeKSortedList.kt |

### Reverse Linked List
```kotlin
fun reverseList(head: ListNode?): ListNode? {
    var prev: ListNode? = null; var curr = head
    while (curr != null) {
        val next = curr.next; curr.next = prev
        prev = curr; curr = next
    }
    return prev
}
```

### Merge Two Sorted Lists
```kotlin
fun mergeTwoLists(l1: ListNode?, l2: ListNode?): ListNode? {
    val dummy = ListNode(0); var curr = dummy
    var a = l1; var b = l2
    while (a != null && b != null) {
        if (a.`val` < b.`val`) { curr.next = a; a = a.next }
        else { curr.next = b; b = b.next }
        curr = curr.next!!
    }
    curr.next = a ?: b
    return dummy.next
}
```

### Cycle Detection
```kotlin
fun hasCycle(head: ListNode?): Boolean {
    var slow = head; var fast = head
    while (fast?.next != null) {
        slow = slow!!.next; fast = fast.next!!.next
        if (slow == fast) return true
    }
    return false
}
```


See the [Master Problem Index](./14-problem-index.md) for the full catalog of all 465+ problems.

---

> **Next up: [Trees - Hierarchical Thinking ->](/chapters/05-trees.md)**

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

# Linked Lists: Pointer Manipulation

## Complete Problem Set (18 problems)

| # | Problem | Pattern | Difficulty | File |
|---|---------|---------|------------|------|
| 1 | Reverse Linked List | Iterative | Easy | linkedlist/ReverseLinkedList.kt |
| 2 | Merge Two Sorted Lists | Merge | Easy | linkedlist/MergeTwoSortedLIst.kt |
| 3 | Linked List Cycle | Fast & Slow | Easy | linkedlist/LinkedListCycle.kt |
| 4 | Linked List Cycle II | Find cycle start | Medium | linkedlist/LinkedListCycle_II.kt |
| 5 | Remove Nth Node From End | Two pointers | Medium | linkedlist/RemoveNthNodeFromEndOfList.kt |
| 6 | Palindrome Linked List | Reverse half | Easy | linkedlist/PalindromeLinkedList.kt |
| 7 | Add Two Numbers | Math | Medium | linkedlist/AddTwoNumbers.kt |
| 8 | Odd Even Linked List | Reorder | Medium | linkedlist/OddEvenLinkedList.kt |
| 9 | Intersection of Two Lists | Two pointers | Easy | linkedlist/IntersectionOfTwoLinkedList.kt |
| 10 | Copy List w/ Random Pointer | Hash map | Medium | linkedlist/CopyLinkedListWithRandomPointer.kt |
| 11 | Delete Middle Node | Fast & slow | Medium | linkedlist/DeleteMiddleNodeOfLinkedList.kt |
| 12 | Insert into Sorted Circular List | Traversal | Medium | linkedlist/InsertIntoASortedCircularLinkedList.kt |
| 13 | Reverse Nodes in k-Group | Recursive | Hard | linkedlist/ReverseNodesInKGroups.kt |
| 14 | Merge k Sorted Lists | Divide & conquer | Hard | linkedlist/MergeKSortedList.kt |
| 15 | Merge k Sorted Lists (Iterative) | Iterative | Hard | linkedlist/MergeKSortedListIterative.kt |

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

### Reverse Nodes in k-Group
```kotlin
fun reverseKGroup(head: ListNode?, k: Int): ListNode? {
    var count = 0; var curr = head
    while (curr != null && count < k) { curr = curr.next; count++ }
    if (count < k) return head
    
    var prev: ListNode? = null; curr = head; count = 0
    while (count < k) {
        val next = curr!!.next; curr.next = prev
        prev = curr; curr = next; count++
    }
    head?.next = reverseKGroup(curr, k)
    return prev
}
```

---

> **Next up: [Trees ->](./05-trees.md)**

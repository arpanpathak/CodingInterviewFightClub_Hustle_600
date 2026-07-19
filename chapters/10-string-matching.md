---
layout: chapter
title: "String Matching"
chapter_number: 10
chapter_title: "String Matching"
toc: true
prev_chapter:
  url: "/chapters/09-disjoint-set-union.html"
  title: "Disjoint Set Union"
next_chapter:
  url: "/chapters/11-backtracking.html"
  title: "Backtracking"
---

# String Matching

> **52 problems**

## The Pattern

_Each problem below includes: Problem, Example, Why This Approach, Code, Pattern Insight, Complexity, and Variations._

## Problems

1. [Apply Substitutions](#applysubstitutions)
2. [Break A Palindrome](#breakapalindrome)
3. [Checkifa Parentheses String Can Be Valid](#checkifaparenthesesstringcanbevalid)
4. [Count And Say](#countandsay)
5. [Custom Sort String](#customsortstring)
6. [Decode String](#decodestring)
7. [Determine If Strings Are Close](#determineifstringsareclose)
8. [Edit Distance](#editdistance)
9. [Excel Sheet To Column Number](#excelsheettocolumnnumber)
10. [Find All Anagrams](#findallanagrams)
11. [Findtheindexofthefirstoccurrenceina String](#findtheindexofthefirstoccurrenceina_string)
12. [Find Unique Binary String](#finduniquebinarystring)
13. [Generate Parantheses](#generateparantheses)
14. [Goat Latin](#goatlatin)
15. [Greatest Common Divisor Of Strings](#greatestcommondivisorofstrings)
16. [Group Anagrams](#groupanagrams)
17. [Group Shifted Strings](#groupshiftedstrings)
18. [Interleaving String](#interleavingstring)
19. [Isomorphic String](#isomorphicstring)
20. [Is Subsequence](#issubsequence)
21. [Length Of Last Word](#lengthoflastword)
22. [Longest Common Prefix](#longestcommonprefix)
23. [Longest Common Subsequence](#longestcommonsubsequence)
24. [Longest Common Substring](#longestcommonsubstring)
25. [Longest Palidnromic Substring](#longestpalidnromicsubstring)
26. [Longest Palindromic Subsequence](#longestpalindromicsubsequence)
27. [Longest Palindromic Subsequence_Bottom Up](#longestpalindromicsubsequence_bottomup)
28. [Longest Repeating Character Replacement](#longestrepeatingcharacterreplacement)
29. [Longest String Chain](#longeststringchain)
30. [Maximum Lengthofa Concatenated Stringwith Unique Characters](#maximumlengthofaconcatenatedstringwithuniquecharacters)
31. [Maximum Value Of A String Is An Array](#maximumvalueofastringisanarray)
32. [Merge String Alternatively](#mergestringalternatively)
33. [Minimum Deletion To Make Character Frequencies Unique](#minimumdeletiontomakecharacterfrequenciesunique)
34. [Minimum Window Substring](#minimumwindowsubstring)
35. [Remove All Adjacent Duplicates In String](#removealladjacentduplicatesinstring)
36. [Reverse Words In String](#reversewordsinstring)
37. [Shortest Common Supersequence](#shortestcommonsupersequence)
38. [Simplify Path](#simplifypath)
39. [String Compression](#stringcompression)
40. [String Compression_II](#stringcompression_ii)
41. [Unique Length3 Palindromic Subsequence](#uniquelength3palindromicsubsequence)
42. [Valid Anagram](#validanagram)
43. [Valid Number](#validnumber)
44. [Valid Palindrome](#validpalindrome)
45. [Valid Palindrome_II](#validpalindrome_ii)
46. [Valid Palindrome_III](#validpalindrome_iii)
47. [Valid Palindrome_III_Space Optimized](#validpalindrome_iii_spaceoptimized)
48. [Validate IP Address](#validateipaddress)
49. [Valid Word Abbreviation](#validwordabbreviation)
50. [Maximum Numberof Vowelsin Substringof Given Length](#maximumnumberofvowelsinsubstringofgivenlength)
51. [Permutations In String](#permutationsinstring)
52. [Reverse Vowel Of String](#reversevowelofstring)

---

## Apply Substitutions

### Problem

Given `replacements` (List<List<String>>), `text` (string), `s` (string), compute the computed result efficiently.

**Example:**

```
Input: replacements = input_value, text = "example", s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **tree traversal/recursion**. Trees are naturally recursive — each subtree is itself a tree. The key is choosing the right traversal order (preorder, inorder, postorder, level-order) for the specific problem.

### Code

```kotlin
package string

class ApplySubstitutions {
    /**
    * Solves the Apply Substitutions problem.
    * Takes `replacements` (List<List<String>>), `text` (string).
    *
    * @param replacements The input List<List<String>>.
    * @param text The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Apply Substitutions problem.
    * Takes `replacements` (List<List<String>>), `text` (string).
    *
    * @param replacements The input List<List<String>>.
    * @param text The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Apply Substitutions problem.
    * Takes `replacements` (List<List<String>>), `text` (string).
    *
    * @param replacements The input List<List<String>>.
    * @param text The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Apply Substitutions problem.
    * Takes `replacements` (List<List<String>>), `text` (string).
    *
    * @param replacements The input List<List<String>>.
    * @param text The input string.
    * @return The resulting string.
    */
    fun applySubstitutions(replacements: List<List<String>>, text: String): String {
        val map = mutableMapOf<String, String>()

        for ((key, value) in replacements) {
            map[key] = value
        }

        /**
        * Solves the Apply Substitutions problem.
        * Takes `s` (string).
        *
        * @param s The input string.
        * @return The resulting string.
        */
        /**
        * Solves the Apply Substitutions problem.
        * Takes `s` (string).
        *
        * @param s The input string.
        * @return The resulting string.
        */
        /**
        * Solves the Apply Substitutions problem.
        * Takes `s` (string).
        *
        * @param s The input string.
        * @return The resulting string.
        */
        /**
        * Solves the Apply Substitutions problem.
        * Takes `s` (string).
        *
        * @param s The input string.
        * @return The resulting string.
        */
        fun resolve(s: String): String {
            val sb = StringBuilder()
            var i = 0

            while (i < s.length) {
                if (i + 2 < s.length && s[i] == '%' && s[i + 2] == '%') {
                    val key = s[i + 1].toString()
                    sb.append(map[key] ?: "%$key%")  // Replace if found, else keep original
                    i += 3  // Move past the placeholder
                } else {
                    sb.append(s[i])
                    i++
                }
            }

            val result = sb.toString()
            return if (result == s) result else resolve(result)  // Continue resolving if changed
        }

        return resolve(text)
    }
}
```

### Pattern Insight

**Tree Pattern.** Choose traversal based on need: inorder (sorted for BST), preorder (copy/construct), postorder (bottom-up compute), level-order (BFS). Recursion uses O(h) stack space; iteration uses O(1) with Morris traversal.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

### Variations

1. What if the tree is skewed (worst case — becomes a linked list)?
1. Can you solve this iteratively instead of recursively?
1. What if the tree is an N-ary tree instead of binary?
1. What if O(1) extra space is required (Morris traversal)?
1. Can this be parallelized for different subtrees?

---

## Break A Palindrome

### Problem

Given `palindrome` (string), compute the computed result efficiently.

**Example:**

```
Input: palindrome = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string.greedy

class BreakAPalindrome {
    /**
    * Solves the Break APalindrome problem.
    * Takes `palindrome` (string).
    *
    * @param palindrome The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Break APalindrome problem.
    * Takes `palindrome` (string).
    *
    * @param palindrome The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Break APalindrome problem.
    * Takes `palindrome` (string).
    *
    * @param palindrome The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Break APalindrome problem.
    * Takes `palindrome` (string).
    *
    * @param palindrome The input string.
    * @return The resulting string.
    */
    fun breakPalindrome(palindrome: String): String {
        if (palindrome.length == 1) return ""

        val arr = palindrome.toCharArray()
        for (i in 0 until palindrome.length / 2) {
            if (arr[i] != 'a') {
                arr[i] = 'a'
                return String(arr)
            }
        }
        // If all characters are 'a', change the last character to 'b'
        arr[arr.lastIndex] = 'b'
        return String(arr)
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Checkifa Parentheses String Can Be Valid

### Problem

Given `s` (string), `locked` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example", locked = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string

class CheckifaParenthesesStringCanBeValid {
    /**
    * Solves the Checkifa Parentheses String Can Be Valid problem.
    * Takes `s` (string), `locked` (string).
    *
    * @param s The input string.
    * @param locked The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Checkifa Parentheses String Can Be Valid problem.
    * Takes `s` (string), `locked` (string).
    *
    * @param s The input string.
    * @param locked The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Checkifa Parentheses String Can Be Valid problem.
    * Takes `s` (string), `locked` (string).
    *
    * @param s The input string.
    * @param locked The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Checkifa Parentheses String Can Be Valid problem.
    * Takes `s` (string), `locked` (string).
    *
    * @param s The input string.
    * @param locked The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun canBeValid(s: String, locked: String): Boolean {
        // Odd number of brackets
        if (s.length % 2 !=0) return false

        var openCount = 0
        for (i in 0 until s.length) {
            if (s[i] == '(' || s[i] == ')' && locked[i] == '0')
                openCount++
            else openCount--

            if (openCount < 0) return false

        }

        // Second pass: Right to left
        var closeCount = 0
        for (i in s.indices.reversed()) {
            // If it's locked as ')' or can be treated as ')'
            if (s[i] == ')' || (s[i] == '(' && locked[i] == '0')) {
                closeCount++
            } else {
                closeCount--
            }

            // If at any point we have more opening parentheses than closing
            if (closeCount < 0) return false
        }

        // If both counts are valid, the string is balanced
        return true
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Count And Say

### Problem

Given `n` (integer), compute the computed result efficiently.

**Example:**

```
Input: n = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package string

class CountAndSay {
    /**
    * Solves the Count And Say problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting string.
    */
    /**
    * Solves the Count And Say problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting string.
    */
    /**
    * Solves the Count And Say problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting string.
    */
    /**
    * Solves the Count And Say problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting string.
    */
    fun countAndSay(n: Int): String {
        var result = "1"
        repeat(n - 1) {
            val nextSequence = buildString {
                var count = 1
                for (i in 1 until result.length) {
                    if (result[i] == result[i - 1]) {
                        count++
                    } else {
                        append(count).append(result[i - 1])
                        count = 1
                    }
                }
                append(count).append(result.last())
            }
            result = nextSequence
        }
        return result
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Custom Sort String

### Problem

Given `order` (string), `s` (string), compute the computed result efficiently.

**Example:**

```
Input: order = "example", s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string.sorting

class CustomSortString {
    /**
    * Solves the Custom Sort String problem.
    * Takes `order` (string), `s` (string).
    *
    * @param order The input string.
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Custom Sort String problem.
    * Takes `order` (string), `s` (string).
    *
    * @param order The input string.
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Custom Sort String problem.
    * Takes `order` (string), `s` (string).
    *
    * @param order The input string.
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Custom Sort String problem.
    * Takes `order` (string), `s` (string).
    *
    * @param order The input string.
    * @param s The input string.
    * @return The resulting string.
    */
    fun customSortString(order: String, s: String): String {
        val orderMap = mutableMapOf<Char, Int>()
        order.forEachIndexed{ index, ch -> orderMap[ch] = index }

        return s.toCharArray().sortedBy{ ch -> orderMap[ch] ?: Int.MAX_VALUE }
            .joinToString("")
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Decode String

### Problem

Given `s` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string.stack

class DecodeString {
    private var index = 0

    /**
    * Solves the Decode String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Decode String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Decode String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Decode String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    fun decodeString(s: String): String {
        val result = StringBuilder()

        while (index < s.length && s[index] != ']') {
            val ch = s[index]
            when {
                !ch.isDigit() -> {
                    result.append(ch)
                    index++
                }
                else -> {
                    var k = 0
                    while (index < s.length && s[index].isDigit()) {
                        k = k * 10 + (s[index++] - '0')
                    }
                    index++ // Skip the opening bracket '['
                    val nestedDecodedString = decodeString(s)
                    index++ // Skip the closing bracket ']'

                    repeat(k) {
                        result.append(nestedDecodedString)
                    }
                }
            }
        }

        return result.toString()
    }

    // Short code
    /**
    * Solves the Decode String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Decode String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Decode String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Decode String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    fun decodeString1(s: String): String {
        var index = 0
        /**
        * Solves the Decode String problem.
        *
        * @return The resulting string.
        */
        /**
        * Solves the Decode String problem.
        *
        * @return The resulting string.
        */
        /**
        * Solves the Decode String problem.
        *
        * @return The resulting string.
        */
        /**
        * Solves the Decode String problem.
        *
        * @return The resulting string.
        */
        fun decode(): String {
            val result = StringBuilder()
            var num = 0
            while (index < s.length) {
                when (val char = s[index]) {
                    in '0'..'9' -> num = num * 10 + (char - '0')
                    '[' -> {
                        index++
                        val decodedString = decode()
                        result.append(decodedString.repeat(num))
                        num = 0
                    }
                    ']' -> return result.toString()
                    else -> result.append(char)
                }
                index++
            }
            return result.toString()
        }
        return decode()
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Determine If Strings Are Close

### Problem

Given `word1` (string), `word2` (string), compute the computed result efficiently.

**Example:**

```
Input: word1 = "example", word2 = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string.hashtable

class DetermineIfStringsAreClose {
    /**
    * Solves the Determine If Strings Are Close problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Determine If Strings Are Close problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Determine If Strings Are Close problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Determine If Strings Are Close problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun closeStrings(word1: String, word2: String): Boolean {
        if (word1.length != word2.length)
            return false

        val freq1 = mutableMapOf<Char, Int>().apply {
            word1.forEach { ch -> this[ch] = this.getOrDefault(ch, 0) + 1}
        }
        val freq2 = mutableMapOf<Char, Int>().apply {
            word2.forEach { ch -> this[ch] = this.getOrDefault(ch, 0) + 1}
        }

        return when {
            freq1.keys != freq2.keys -> false
            else -> freq1.values.sorted() == freq2.values.sorted()
        }
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Edit Distance

### Problem

Given `word1` (string), `word2` (string), `m` (integer), `n` (integer), `args` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: word1 = "example", word2 = "example", m = 5, n = 5, args = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package string.dynamic_programming

class EditDistance {
    private var dp = mutableMapOf<String,Int>()

    /**
    * Solves the Edit Distance problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Edit Distance problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Edit Distance problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Edit Distance problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return The computed integer result.
    */
    fun minDistance(word1: String, word2: String): Int {
        return minDistance(word1, word2, word1.length, word2.length)
    }

    /**
    * Solves the Edit Distance problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Edit Distance problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Edit Distance problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Edit Distance problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return The computed integer result.
    */
    fun minDistance(word1: String, word2: String, m: Int, n: Int): Int {
        val state = "$m.$n"

        return when {
            dp.contains(state) -> dp[state]!!
            m == 0 -> n
            n == 0 -> m
            word1[m - 1] == word2[n - 1] -> minDistance(word1, word2, m - 1, n - 1)
            else -> {
                val insert = minDistance(word1, word2, m, n - 1)
                val remove = minDistance(word1, word2, m - 1, n)
                val replace = minDistance(word1, word2, m - 1, n - 1)
                1 + minOf(insert, remove, replace)
            }
        }.also { dp[state] = it }
    }

    companion object {
        @JvmStatic
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        fun main(args: Array<String>) {
        }
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(n²) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Excel Sheet To Column Number

### Problem

Given `columnTitle` (string), compute the computed result efficiently.

**Example:**

```
Input: columnTitle = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package string

class ExcelSheetToColumnNumber {
    /**
    * Solves the Excel Sheet To Column Number problem.
    * Takes `columnTitle` (string).
    *
    * @param columnTitle The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Excel Sheet To Column Number problem.
    * Takes `columnTitle` (string).
    *
    * @param columnTitle The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Excel Sheet To Column Number problem.
    * Takes `columnTitle` (string).
    *
    * @param columnTitle The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Excel Sheet To Column Number problem.
    * Takes `columnTitle` (string).
    *
    * @param columnTitle The input string.
    * @return The computed integer result.
    */
    fun titleToNumber(columnTitle: String): Int {
        var base = 1
        var sum = 0
        for (i in columnTitle.length - 1 downTo 0) {
            sum += (columnTitle[i] - 'A' + 1) * base
            base *= 26
        }
        return sum
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Find All Anagrams

### Problem

Given `s` (string), `p` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example", p = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

### Code

```kotlin
package string.sliding_window

class FindAllAnagrams {
    /**
    * Solves the Find All Anagrams problem.
    * Takes `s` (string), `p` (string).
    *
    * @param s The input string.
    * @param p The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Find All Anagrams problem.
    * Takes `s` (string), `p` (string).
    *
    * @param s The input string.
    * @param p The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Find All Anagrams problem.
    * Takes `s` (string), `p` (string).
    *
    * @param s The input string.
    * @param p The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Find All Anagrams problem.
    * Takes `s` (string), `p` (string).
    *
    * @param s The input string.
    * @param p The input string.
    * @return The computed integer result.
    */
    fun findAnagrams(s: String, p: String): List<Int> {
        val result = mutableListOf<Int>()
        if (s.length < p.length) return result

        val pCount = IntArray(26)
        val sCount = IntArray(26)

        // Initialize frequency counts for p and the first window of s
        for (i in p.indices) {
            pCount[p[i] - 'a']++
            sCount[s[i] - 'a']++
        }

        // Compare the initial window and check every subsequent window
        for (i in p.length..s.length) {
            if (pCount.contentEquals(sCount)) {
                result.add(i - p.length)
            }
            if (i < s.length) {
                sCount[s[i] - 'a']++          // Add new character to the window
                sCount[s[i - p.length] - 'a']-- // Remove the old character from the window
            }
        }

        return result
    }
}
```

### Pattern Insight

**Binary Search Pattern.** Identify a monotonic predicate. The predicate must be false for all values on one side of the answer and true for all values on the other side. Binary search finds the transition point.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

### Variations

1. What if the input is not sorted? Can you sort it first?
1. What if there are duplicates — need first vs last occurrence?
1. What if the search space is a range of values, not array indices?
1. What if the array is too large to fit in memory?
1. What if the predicate is not monotonic?

---

## Findtheindexofthefirstoccurrenceina String

### Problem

Given `haystack` (string), `needle` (string), compute the computed result efficiently.

**Example:**

```
Input: haystack = "example", needle = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

### Code

```kotlin
package string.pattern_matching

import oracle.net.aso.m

class `FindTheIndexofTheFirstOccurrenceIna String` {
    /**
    * Solves the findtheindexofthefirstoccurrenceina string problem.
    * Takes `haystack` (string), `needle` (string).
    *
    * @param haystack The input string.
    * @param needle The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the findtheindexofthefirstoccurrenceina string problem.
    * Takes `haystack` (string), `needle` (string).
    *
    * @param haystack The input string.
    * @param needle The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the findtheindexofthefirstoccurrenceina string problem.
    * Takes `haystack` (string), `needle` (string).
    *
    * @param haystack The input string.
    * @param needle The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the findtheindexofthefirstoccurrenceina string problem.
    * Takes `haystack` (string), `needle` (string).
    *
    * @param haystack The input string.
    * @param needle The input string.
    * @return The computed integer result.
    */
    fun strStr(haystack: String, needle: String): Int {
        // If the needle is empty, return 0
        if (needle.isEmpty()) return 0

        // Use 'to' to assign both m and n in one line
        val (m, n) = needle.length to haystack.length

        // Step 1: Build the LPS array for the needle
        val lps = buildLPS(needle)
        println(needle)
        println(lps.contentToString())
        // Step 2: Search for the needle in the haystack using KMP algorithm
        var (i, j) = 0 to 0  // Pairing to initialize indices for haystack and needle

        while (i < n) {
            when {
                haystack[i] == needle[j] -> {  // Characters match
                    i++
                    j++
                }
                j > 0 -> j = lps[j - 1]  // Mismatch after some matches, use LPS array to skip ahead
                else -> i++  // No matches yet, move to the next character in the haystack
            }

            // If we've matched the entire needle, return the start index
            if (j == m) return i - j
        }

        return -1  // If no match found
    }

    // Function to build the LPS (Longest Prefix Suffix) array for the needle
    /**
    * Solves the findtheindexofthefirstoccurrenceina string problem.
    * Takes `needle` (string).
    *
    * @param needle The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the findtheindexofthefirstoccurrenceina string problem.
    * Takes `needle` (string).
    *
    * @param needle The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the findtheindexofthefirstoccurrenceina string problem.
    * Takes `needle` (string).
    *
    * @param needle The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the findtheindexofthefirstoccurrenceina string problem.
    * Takes `needle` (string).
    *
    * @param needle The input string.
    * @return The computed integer result.
    */
    fun buildLPS(needle: String): IntArray {
        val lps = IntArray(needle.length)
        var (i, j) = 0 to 1

        while (j < needle.length) {
            when {
                needle[j] == needle[i] -> lps[j++] = ++i
                i != 0 -> i = lps[i - 1]
                else -> lps[j++] = 0
            }
        }
        return lps
    }
}
// lps =  [0 0 0 0 0 0 0 0 0]
        // a b c x y z c b a
        //   ^             ^
        //   i             1
```

### Pattern Insight

**Binary Search Pattern.** Identify a monotonic predicate. The predicate must be false for all values on one side of the answer and true for all values on the other side. Binary search finds the transition point.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

### Variations

1. What if the input is not sorted? Can you sort it first?
1. What if there are duplicates — need first vs last occurrence?
1. What if the search space is a range of values, not array indices?
1. What if the array is too large to fit in memory?
1. What if the predicate is not monotonic?

---

## Find Unique Binary String

### Problem

Given `nums` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: nums = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses **binary search** because the search space is sorted or has a monotonic property. Binary search cuts the search space in half each iteration, achieving O(log n) time. The key is identifying a predicate that transitions from false to true at exactly one point — binary search finds that transition.

### Code

```kotlin
package string

// Cantor’s Diagonalization Trick
class FindUniqueBinaryString {
    /**
    * Solves the Find Unique Binary String problem.
    * Takes `nums` (Array<String>).
    *
    * @param nums The input Array<String>.
    * @return The resulting string.
    */
    /**
    * Solves the Find Unique Binary String problem.
    * Takes `nums` (Array<String>).
    *
    * @param nums The input Array<String>.
    * @return The resulting string.
    */
    /**
    * Solves the Find Unique Binary String problem.
    * Takes `nums` (Array<String>).
    *
    * @param nums The input Array<String>.
    * @return The resulting string.
    */
    /**
    * Solves the Find Unique Binary String problem.
    * Takes `nums` (Array<String>).
    *
    * @param nums The input Array<String>.
    * @return The resulting string.
    */
    fun findDifferentBinaryString(nums: Array<String>): String {
        val n = nums.size
        val sb = StringBuilder()

        for (i in 0 until n) {
            sb.append(if (nums[i][i] == '0') '1' else '0')
        }

        return sb.toString()
    }
}
```

### Pattern Insight

**Binary Search Pattern.** Identify a monotonic predicate. The predicate must be false for all values on one side of the answer and true for all values on the other side. Binary search finds the transition point.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

### Variations

1. What if the input is not sorted? Can you sort it first?
1. What if there are duplicates — need first vs last occurrence?
1. What if the search space is a range of values, not array indices?
1. What if the array is too large to fit in memory?
1. What if the predicate is not monotonic?

---

## Generate Parantheses

### Problem

Given `n` (integer), `open` (integer), `close` (integer), `current` (StringBuilder), `result` (MutableList<String>), compute the computed result efficiently.

**Example:**

```
Input: n = 5, open = 5, close = 5, current = input_value, result = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package string.backtracking

import java.lang.StringBuilder

class GenerateParantheses {
    /**
    * Solves the Generate Parantheses problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Generate Parantheses problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Generate Parantheses problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting collection (list of strings).
    */
    /**
    * Solves the Generate Parantheses problem.
    * Takes `n` (integer).
    *
    * @param n The integer parameter representing n.
    * @return The resulting collection (list of strings).
    */
    fun generateParenthesis(n: Int): List<String> {
        val result = mutableListOf<String>()
        generate(n, n, StringBuilder(), result)
        return result
    }

    /**
    * Solves the Generate Parantheses problem.
    * Takes `open` (integer), `close` (integer), `current` (StringBuilder), `result` (MutableList<String>).
    *
    * @param open The integer parameter representing open.
    * @param close The integer parameter representing close.
    * @param current The input string.
    * @param result The input MutableList<String>.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Generate Parantheses problem.
    * Takes `open` (integer), `close` (integer), `current` (StringBuilder), `result` (MutableList<String>).
    *
    * @param open The integer parameter representing open.
    * @param close The integer parameter representing close.
    * @param current The input string.
    * @param result The input MutableList<String>.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Generate Parantheses problem.
    * Takes `open` (integer), `close` (integer), `current` (StringBuilder), `result` (MutableList<String>).
    *
    * @param open The integer parameter representing open.
    * @param close The integer parameter representing close.
    * @param current The input string.
    * @param result The input MutableList<String>.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Generate Parantheses problem.
    * Takes `open` (integer), `close` (integer), `current` (StringBuilder), `result` (MutableList<String>).
    *
    * @param open The integer parameter representing open.
    * @param close The integer parameter representing close.
    * @param current The input string.
    * @param result The input MutableList<String>.
    * @return Unit (no return value, modifies state in-place).
    */
    fun generate(open: Int, close: Int, current: StringBuilder, result: MutableList<String>) {
        if (open == 0 && close == 0) {
            result.add(current.toString())
            return
        }

        if (open > 0) {
            current.append("(")
            generate(open-1, close, current, result)
            current.setLength(current.length - 1)
        }

        if (close > open) {
            current.append(")")
            generate(open, close - 1, current, result)
            current.deleteCharAt(current.length - 1) // backtrack
        }
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Goat Latin

### Problem

Given `sentence` (string), compute the computed result efficiently.

**Example:**

```
Input: sentence = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package string

class GoatLatin {
    /**
    * Solves the Goat Latin problem.
    * Takes `sentence` (string).
    *
    * @param sentence The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Goat Latin problem.
    * Takes `sentence` (string).
    *
    * @param sentence The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Goat Latin problem.
    * Takes `sentence` (string).
    *
    * @param sentence The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Goat Latin problem.
    * Takes `sentence` (string).
    *
    * @param sentence The input string.
    * @return The resulting string.
    */
    fun toGoatLatin(sentence: String): String {
        // Define a set of vowels for faster lookup
        val vowels = setOf('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        // Process the sentence word by word
        return sentence.split(" ").mapIndexed { index, word ->
            // Check if the word starts with a vowel
            if (word[0] in vowels) {
                // If the word starts with a vowel, append "ma" and the appropriate number of 'a's
                word + "ma" + "a".repeat(index + 1)
            } else {
                // If the word starts with a consonant, move the first letter to the end, append "ma", and the appropriate number of 'a's
                word.substring(1) + word[0] + "ma" + "a".repeat(index + 1)
            }
        }.joinToString(" ")  // Join the words back into a single string
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Greatest Common Divisor Of Strings

### Problem

Given `a` (integer), `b` (integer), `str1` (string), `str2` (string), compute the computed result efficiently.

**Example:**

```
Input: a = 5, b = 5, str1 = "example", str2 = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string

class GreatestCommonDivisorOfStrings {
    /**
    * Solves the Greatest Common Divisor Of Strings problem.
    * Takes `a` (integer), `b` (integer).
    *
    * @param a The integer parameter representing a.
    * @param b The integer parameter representing b.
    * @return The computed integer result.
    */
    /**
    * Solves the Greatest Common Divisor Of Strings problem.
    * Takes `a` (integer), `b` (integer).
    *
    * @param a The integer parameter representing a.
    * @param b The integer parameter representing b.
    * @return The computed integer result.
    */
    /**
    * Solves the Greatest Common Divisor Of Strings problem.
    * Takes `a` (integer), `b` (integer).
    *
    * @param a The integer parameter representing a.
    * @param b The integer parameter representing b.
    * @return The computed integer result.
    */
    /**
    * Solves the Greatest Common Divisor Of Strings problem.
    * Takes `a` (integer), `b` (integer).
    *
    * @param a The integer parameter representing a.
    * @param b The integer parameter representing b.
    * @return The computed integer result.
    */
    fun gcd(a: Int, b: Int): Int {
        return when {
            a == b -> a
            a > b -> gcd(a - b , b)
            else -> gcd(a, b - a)
        }
    }

    /**
    * Solves the Greatest Common Divisor Of Strings problem.
    * Takes `str1` (string), `str2` (string).
    *
    * @param str1 The input string.
    * @param str2 The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Greatest Common Divisor Of Strings problem.
    * Takes `str1` (string), `str2` (string).
    *
    * @param str1 The input string.
    * @param str2 The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Greatest Common Divisor Of Strings problem.
    * Takes `str1` (string), `str2` (string).
    *
    * @param str1 The input string.
    * @param str2 The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Greatest Common Divisor Of Strings problem.
    * Takes `str1` (string), `str2` (string).
    *
    * @param str1 The input string.
    * @param str2 The input string.
    * @return The resulting string.
    */
    fun gcdOfStrings(str1: String, str2: String): String {
        // Dhoyasha Foggy I didn't understand.
        if ((str1 + str2) != (str2 + str1))
            return ""

        val gcdLength = gcd(str1.length, str2.length)

        return str1.substring(0, gcdLength)
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Group Anagrams

### Problem

Given `strs` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: strs = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string

class GroupAnagrams {
    /**
    * Solves the Group Anagrams problem.
    * Takes `strs` (Array<String>).
    *
    * @param strs The input Array<String>.
    * @return The resulting collection (List<List<String>).
    */
    /**
    * Solves the Group Anagrams problem.
    * Takes `strs` (Array<String>).
    *
    * @param strs The input Array<String>.
    * @return The resulting collection (List<List<String>).
    */
    /**
    * Solves the Group Anagrams problem.
    * Takes `strs` (Array<String>).
    *
    * @param strs The input Array<String>.
    * @return The resulting collection (List<List<String>).
    */
    /**
    * Solves the Group Anagrams problem.
    * Takes `strs` (Array<String>).
    *
    * @param strs The input Array<String>.
    * @return The resulting collection (List<List<String>).
    */
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val anagramMap = mutableMapOf<List<Int>, MutableList<String>>()  // Using List<Int> as the key
        for (word in strs) {
            val count = IntArray(26)
            // Count the frequency of each character
            word.forEach { count[it - 'a']++ }
            anagramMap.getOrPut(count.toList()) { mutableListOf() }.add(word)
        }

        // Return the list of grouped anagrams
        return anagramMap.values.toList()
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Group Shifted Strings

### Problem

Given `strings` (Array<String>), `str` (string), compute the computed result efficiently.

**Example:**

```
Input: strings = input_value, str = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string.hashtable

class GroupShiftedStrings {
    /**
    * Solves the Group Shifted Strings problem.
    * Takes `strings` (Array<String>).
    *
    * @param strings The input Array<String>.
    * @return The resulting collection (List<List<String>).
    */
    /**
    * Solves the Group Shifted Strings problem.
    * Takes `strings` (Array<String>).
    *
    * @param strings The input Array<String>.
    * @return The resulting collection (List<List<String>).
    */
    /**
    * Solves the Group Shifted Strings problem.
    * Takes `strings` (Array<String>).
    *
    * @param strings The input Array<String>.
    * @return The resulting collection (List<List<String>).
    */
    /**
    * Solves the Group Shifted Strings problem.
    * Takes `strings` (Array<String>).
    *
    * @param strings The input Array<String>.
    * @return The resulting collection (List<List<String>).
    */
    fun groupStrings(strings: Array<String>): List<List<String>> {
        val map = mutableMapOf<String, MutableList<String>>()

        for (str in strings) {
            val key = getKey(str)
            map.computeIfAbsent(key) { mutableListOf() }.add(str)
        }

        return map.values.toList()
    }

    /**
    * Helper: get key.
    *
    * @param str The input string.
    * @return The resulting string.
    */
    /**
    * Helper: get key.
    *
    * @param str The input string.
    * @return The resulting string.
    */
    /**
    * Helper: get key.
    *
    * @param str The input string.
    * @return The resulting string.
    */
    /**
    * Helper: get key.
    *
    * @param str The input string.
    * @return The resulting string.
    */
    private fun getKey(str: String): String {
        return buildString {
            for (i in 1 until str.length) {
                append( ((str[i] - str[i - 1] + 26) % 26).toString() )
            }
        }
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Interleaving String

### Problem

Given `s1` (string), `s2` (string), `s3` (string), `i` (integer), `j` (integer), compute the computed result efficiently.

**Example:**

```
Input: s1 = "example", s2 = "example", s3 = "example", i = 5, j = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string.dynamic_programming

class InterleavingString {
    /**
    * Solves the Interleaving String problem.
    * Takes `s1` (string), `s2` (string), `s3` (string).
    *
    * @param s1 The input string.
    * @param s2 The input string.
    * @param s3 The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Interleaving String problem.
    * Takes `s1` (string), `s2` (string), `s3` (string).
    *
    * @param s1 The input string.
    * @param s2 The input string.
    * @param s3 The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Interleaving String problem.
    * Takes `s1` (string), `s2` (string), `s3` (string).
    *
    * @param s1 The input string.
    * @param s2 The input string.
    * @param s3 The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Interleaving String problem.
    * Takes `s1` (string), `s2` (string), `s3` (string).
    *
    * @param s1 The input string.
    * @param s2 The input string.
    * @param s3 The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isInterleave(s1: String, s2: String, s3: String): Boolean {
        if (s1.length + s2.length != s3.length) return false

        val memo = mutableMapOf<Pair<Int, Int>, Boolean>()

        /**
        * Solves the Interleaving String problem.
        * Takes `i` (integer), `j` (integer).
        *
        * @param i The integer parameter representing i.
        * @param j The integer parameter representing j.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Interleaving String problem.
        * Takes `i` (integer), `j` (integer).
        *
        * @param i The integer parameter representing i.
        * @param j The integer parameter representing j.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Interleaving String problem.
        * Takes `i` (integer), `j` (integer).
        *
        * @param i The integer parameter representing i.
        * @param j The integer parameter representing j.
        * @return `true` if the condition is met, `false` otherwise.
        */
        /**
        * Solves the Interleaving String problem.
        * Takes `i` (integer), `j` (integer).
        *
        * @param i The integer parameter representing i.
        * @param j The integer parameter representing j.
        * @return `true` if the condition is met, `false` otherwise.
        */
        fun dfs(i: Int, j: Int): Boolean {
            if (i == s1.length && j == s2.length) return true
            if (memo.containsKey(i to j)) return memo[i to j]!!

            val k = i + j
            var result = false

            if (i < s1.length && s1[i] == s3[k] && dfs(i + 1, j)) {
                result = true
            }
            if (j < s2.length && s2[j] == s3[k] && dfs(i, j + 1)) {
                result = true
            }

            memo[i to j] = result
            return result
        }

        return dfs(0, 0)
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Isomorphic String

### Problem

Given `s` (string), `t` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example", t = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string

class IsomorphicString {
    /**
    * Solves the Isomorphic String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Isomorphic String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Isomorphic String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Isomorphic String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    fun encode(s: String): String {
        val map = mutableMapOf<Char, Int>()
        val sb = StringBuilder()
        var code = 0

        for (c in s) {
            if (c !in map) map[c] = code++
            sb.append(map[c]).append(" ")
        }

        return sb.toString()
    }

    /**
    * Solves the Isomorphic String problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Isomorphic String problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Isomorphic String problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Isomorphic String problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isIsomorphic(s: String, t: String): Boolean {
        return encode(s) == encode(t)
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Is Subsequence

### Problem

Given `s` (string), `t` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example", t = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package string

class IsSubsequence {
    /**
    * Solves the Is Subsequence problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Is Subsequence problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Is Subsequence problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Is Subsequence problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isSubsequence(s: String, t: String): Boolean {
        var i = 0
        var j = 0

        while (i < s.length && j < t.length) {
            if (s[i] == t[j]) {
                i++
                j++
            } else {
                j++
            }
        }

        // Match found
        return i == s.length
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(n²) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Length Of Last Word

### Problem

Given `s` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **graph traversal**. Choose BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, or topological sort for dependency ordering. Track visited nodes to prevent infinite loops.

### Code

```kotlin
package string

class LengthOfLastWord {
    /**
    * Solves the Length Of Last Word problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Length Of Last Word problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Length Of Last Word problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Length Of Last Word problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    fun lengthOfLastWord(s: String): Int {
        var i = s.length - 1
        var len = 0

        while (i >= 0 && s[i] == ' ') i--     // skip trailing spaces
        while (i >= 0 && s[i] != ' ') {
            len++
            i--
        }

        return len
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Longest Common Prefix

### Problem

Given `strs` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: strs = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package string

class LongestCommonPrefix {
    /**
    * Solves the Longest Common Prefix problem.
    * Takes `strs` (Array<String>).
    *
    * @param strs The input Array<String>.
    * @return The resulting string.
    */
    /**
    * Solves the Longest Common Prefix problem.
    * Takes `strs` (Array<String>).
    *
    * @param strs The input Array<String>.
    * @return The resulting string.
    */
    /**
    * Solves the Longest Common Prefix problem.
    * Takes `strs` (Array<String>).
    *
    * @param strs The input Array<String>.
    * @return The resulting string.
    */
    /**
    * Solves the Longest Common Prefix problem.
    * Takes `strs` (Array<String>).
    *
    * @param strs The input Array<String>.
    * @return The resulting string.
    */
    fun longestCommonPrefix(strs: Array<String>): String {
        if (strs.isEmpty()) return ""

        // Use the first string as the reference
        for (i in strs[0].indices) {
            val char = strs[0][i]
            // Compare this character with the corresponding character in all other strings
            for (j in 1 until strs.size) {
                // If the current string is shorter or the characters don't match, return the prefix so far
                if (i >= strs[j].length || strs[j][i] != char) {
                    return strs[0].substring(0, i)
                }
            }
        }
        // If no mismatch is found, the entire first string is the common prefix
        return strs[0]
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Longest Common Subsequence

### Problem

Given `str1` (string), `str2` (string), `str` (string), `i` (integer), `j` (integer), `args` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: str1 = "example", str2 = "example", str = "example", i = 5, j = 5, args = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package string.dynamic_programming

class LongestCommonSubsequence {
    companion object {
        private lateinit var M: Array<IntArray>

        /**
        * Solves the Longest Common Subsequence problem.
        * Takes `str1` (string), `str2` (string).
        *
        * @param str1 The input string.
        * @param str2 The input string.
        * @return The computed integer result.
        */
        /**
        * Solves the Longest Common Subsequence problem.
        * Takes `str1` (string), `str2` (string).
        *
        * @param str1 The input string.
        * @param str2 The input string.
        * @return The computed integer result.
        */
        /**
        * Solves the Longest Common Subsequence problem.
        * Takes `str1` (string), `str2` (string).
        *
        * @param str1 The input string.
        * @param str2 The input string.
        * @return The computed integer result.
        */
        /**
        * Solves the Longest Common Subsequence problem.
        * Takes `str1` (string), `str2` (string).
        *
        * @param str1 The input string.
        * @param str2 The input string.
        * @return The computed integer result.
        */
        fun lcs(str1: String, str2: String): Int {
            M = Array(str1.length + 1) { IntArray(str2.length + 1) }
            for (i in 1..str1.length) {
                for (j in 1..str2.length) {
                    if (str1[i - 1] == str2[j - 1]) {
                        M[i][j] = M[i - 1][j - 1] + 1
                    } else {
                        M[i][j] = maxOf(M[i - 1][j], M[i][j - 1])
                    }
                }
            }
            return M[str1.length][str2.length]
        }

        /**
        * Solves the Longest Common Subsequence problem.
        * Takes `str` (string), `i` (integer), `j` (integer).
        *
        * @param str The input string.
        * @param i The integer parameter representing i.
        * @param j The integer parameter representing j.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Longest Common Subsequence problem.
        * Takes `str` (string), `i` (integer), `j` (integer).
        *
        * @param str The input string.
        * @param i The integer parameter representing i.
        * @param j The integer parameter representing j.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Longest Common Subsequence problem.
        * Takes `str` (string), `i` (integer), `j` (integer).
        *
        * @param str The input string.
        * @param i The integer parameter representing i.
        * @param j The integer parameter representing j.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Longest Common Subsequence problem.
        * Takes `str` (string), `i` (integer), `j` (integer).
        *
        * @param str The input string.
        * @param i The integer parameter representing i.
        * @param j The integer parameter representing j.
        * @return Unit (no return value, modifies state in-place).
        */
        fun printLCS(str: String, i: Int, j: Int) {
            if (i <= 0 || j <= 0) return
            if (M[i][j] != M[i][j - 1] && M[i][j] != M[i - 1][j] && M[i][j] == M[i - 1][j - 1] + 1) {
                print(str[j - 1])
                printLCS(str, i - 1, j - 1)
            } else if (M[i][j - 1] > M[i - 1][j]) {
                printLCS(str, i, j - 1)
            } else {
                printLCS(str, i - 1, j)
            }
        }

        @JvmStatic
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Entry point for the program.
        *
        * @param args The input Array<String>.
        * @return Unit (no return value, modifies state in-place).
        */
        fun main(args: Array<String>) {
            println(lcs("abcxgzggmn", "acttvvmnvt"))
            printLCS("acttvvmnvt", "abcxgzggmn".length, "acttvvmnvt".length) // Print in reverse order
        }
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(n²) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Longest Common Substring

### Problem

Given the input, compute the result efficiently.

**Example:**

```
Input: 
Output: 42 (expected result)

```

### Why This Approach

This problem uses **tree traversal/recursion**. Trees are naturally recursive — each subtree is itself a tree. The key is choosing the right traversal order (preorder, inorder, postorder, level-order) for the specific problem.

### Code

```kotlin
package string.dynamic_programming

class LongestCommonSubstring {
}
```

### Pattern Insight

**Tree Pattern.** Choose traversal based on need: inorder (sorted for BST), preorder (copy/construct), postorder (bottom-up compute), level-order (BFS). Recursion uses O(h) stack space; iteration uses O(1) with Morris traversal.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

### Variations

1. What if the tree is skewed (worst case — becomes a linked list)?
1. Can you solve this iteratively instead of recursively?
1. What if the tree is an N-ary tree instead of binary?
1. What if O(1) extra space is required (Morris traversal)?
1. Can this be parallelized for different subtrees?

---

## Longest Palidnromic Substring

### Problem

Given `s` (string), `left` (integer), `right` (integer), compute the computed result efficiently.

**Example:**

```
Input: s = "example", left = 5, right = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **tree traversal/recursion**. Trees are naturally recursive — each subtree is itself a tree. The key is choosing the right traversal order (preorder, inorder, postorder, level-order) for the specific problem.

### Code

```kotlin
package string

class LongestPalidnromicSubstring {
    /**
    * Solves the Longest Palidnromic Substring problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Longest Palidnromic Substring problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Longest Palidnromic Substring problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Longest Palidnromic Substring problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    fun longestPalindrome(s: String): String {
        if (s.isEmpty()) return ""

        var start = 0
        var maxLength = 1

        // Helper function to expand around the center
        /**
        * Solves the Longest Palidnromic Substring problem.
        * Takes `left` (integer), `right` (integer).
        *
        * @param left The integer parameter representing left.
        * @param right The integer parameter representing right.
        * @return The computed integer result.
        */
        /**
        * Solves the Longest Palidnromic Substring problem.
        * Takes `left` (integer), `right` (integer).
        *
        * @param left The integer parameter representing left.
        * @param right The integer parameter representing right.
        * @return The computed integer result.
        */
        /**
        * Solves the Longest Palidnromic Substring problem.
        * Takes `left` (integer), `right` (integer).
        *
        * @param left The integer parameter representing left.
        * @param right The integer parameter representing right.
        * @return The computed integer result.
        */
        /**
        * Solves the Longest Palidnromic Substring problem.
        * Takes `left` (integer), `right` (integer).
        *
        * @param left The integer parameter representing left.
        * @param right The integer parameter representing right.
        * @return The computed integer result.
        */
        fun expandAroundCenter(left: Int, right: Int): Int {
            var l = left
            var r = right
            while (l >= 0 && r < s.length && s[l] == s[r]) {
                l--
                r++
            }
            // Return the length of the palindrome
            return r - l - 1
        }

        for (i in 0 until s.length) {
            // Check for odd length palindrome (center is s[i])
            val len1 = expandAroundCenter(i, i)
            // Check for even length palindrome (center is between s[i] and s[i + 1])
            val len2 = expandAroundCenter(i, i + 1)

            val len = maxOf(len1, len2)

            if (len > maxLength) {
                maxLength = len
                start = i - (len - 1) / 2  // Calculate the start of the palindrome
            }
        }

        return s.substring(start, start + maxLength)
    }
}
```

### Pattern Insight

**Tree Pattern.** Choose traversal based on need: inorder (sorted for BST), preorder (copy/construct), postorder (bottom-up compute), level-order (BFS). Recursion uses O(h) stack space; iteration uses O(1) with Morris traversal.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

### Variations

1. What if the tree is skewed (worst case — becomes a linked list)?
1. Can you solve this iteratively instead of recursively?
1. What if the tree is an N-ary tree instead of binary?
1. What if O(1) extra space is required (Morris traversal)?
1. Can this be parallelized for different subtrees?

---

## Longest Palindromic Subsequence

### Problem

Given `s` (string), `start` (integer), `length` (integer), compute the computed result efficiently.

**Example:**

```
Input: s = "example", start = 5, length = 5
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package string.dynamic_programming

class LongestPalindromicSubsequence {
    /**
    * Solves the Longest Palindromic Subsequence problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest Palindromic Subsequence problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest Palindromic Subsequence problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest Palindromic Subsequence problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    fun longestPalindromeSubseq(s: String): Int {
        val dp = Array(s.length) { IntArray(s.length) }

        /**
        * Solves the Longest Palindromic Subsequence problem.
        * Takes `start` (integer), `length` (integer).
        *
        * @param start The integer parameter representing start.
        * @param length The integer parameter representing length.
        * @return The computed integer result.
        */
        /**
        * Solves the Longest Palindromic Subsequence problem.
        * Takes `start` (integer), `length` (integer).
        *
        * @param start The integer parameter representing start.
        * @param length The integer parameter representing length.
        * @return The computed integer result.
        */
        /**
        * Solves the Longest Palindromic Subsequence problem.
        * Takes `start` (integer), `length` (integer).
        *
        * @param start The integer parameter representing start.
        * @param length The integer parameter representing length.
        * @return The computed integer result.
        */
        /**
        * Solves the Longest Palindromic Subsequence problem.
        * Takes `start` (integer), `length` (integer).
        *
        * @param start The integer parameter representing start.
        * @param length The integer parameter representing length.
        * @return The computed integer result.
        */
        fun lps(start: Int, length: Int): Int {
            if (length <= 1) return length
            val end = start + length - 1

            return when {
                dp[start][end] != 0 -> dp[start][end] // Value already cached
                s[start] == s[end] -> 2 + lps(start + 1, length - 2)
                else -> maxOf(lps(start + 1, length - 1 ), lps(start, length - 1))
            }.also { dp[start][end] = it}
        }
        return lps(0, s.length)
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(n²) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Longest Palindromic Subsequence_Bottom Up

### Problem

Given `s` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package string.dynamic_programming

class LongestPalindromicSubsequence_BottomUp {
    /**
    * Solves the Longest Palindromic Subsequence_Bottom Up problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest Palindromic Subsequence_Bottom Up problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest Palindromic Subsequence_Bottom Up problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest Palindromic Subsequence_Bottom Up problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    fun longestPalindromeSubseq(s: String): Int {
        val n = s.length
        val dp = Array(n) { IntArray(n) }

        // Bottom-up fill the dp table for substrings of increasing length
        for (length in 1..n) {  // Iterate over all substring lengths
            for (start in 0..n - length) {  // Iterate over all possible start indices
                val end = start + length - 1  // Calculate the end index of the substring

                dp[start][end] = when {
                    length == 1 -> 1  // Base case: single character is a palindrome of length 1
                    s[start] == s[end] -> 2 + dp[start + 1][end - 1]  // Palindrome formed by adding the two matching characters
                    else -> maxOf(dp[start + 1][end], dp[start][end - 1])  // Max of ignoring one end
                }
            }
        }

        // The result is stored in dp[0][n-1] (the entire string)
        return dp[0][n - 1]
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(n²) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Longest Repeating Character Replacement

### Problem

Given `s` (string), `k` (integer), compute the computed result efficiently.

**Example:**

```
Input: s = "example", k = 5
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package sliding_window

class LongestRepeatingCharacterReplacement {
    /**
    * Solves the Longest Repeating Character Replacement problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest Repeating Character Replacement problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest Repeating Character Replacement problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest Repeating Character Replacement problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    fun characterReplacement(s: String, k: Int): Int {
        val count = IntArray(26)
        var maxLength = 0
        var left = 0
        var maxCount = 0

        for (right in s.indices) {
            val char = s[right]
            count[char - 'A']++
            maxCount = maxOf(maxCount, count[char - 'A'])

            if (right - left + 1 - maxCount > k) {
                count[s[left] - 'A']--
                left++
            }

            maxLength = maxOf(maxLength, right - left + 1)
        }

        return maxLength
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Longest String Chain

### Problem

Given `words` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: words = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string.dynamic_programming

class LongestStringChain {
    /**
    * Solves the Longest String Chain problem.
    * Takes `words` (Array<String>).
    *
    * @param words The input Array<String>.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest String Chain problem.
    * Takes `words` (Array<String>).
    *
    * @param words The input Array<String>.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest String Chain problem.
    * Takes `words` (Array<String>).
    *
    * @param words The input Array<String>.
    * @return The computed integer result.
    */
    /**
    * Solves the Longest String Chain problem.
    * Takes `words` (Array<String>).
    *
    * @param words The input Array<String>.
    * @return The computed integer result.
    */
    fun longestStrChain(words: Array<String>): Int {
        words.sortBy { it.length }  // Sort words by length
        val dp = mutableMapOf<String, Int>()
        var maxLen = 1

        for (word in words) {
            dp[word] = 1  // Default length of chain ending at word is 1
            for (i in word.indices) {
                val prev = word.removeRange(i, i + 1)  // Remove one character
                if (prev in dp) {
                    dp[word] = maxOf(dp[word]!!, dp[prev]!! + 1)
                }
            }
            maxLen = maxOf(maxLen, dp[word]!!)
        }

        return maxLen
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Maximum Lengthofa Concatenated Stringwith Unique Characters

### Problem

Given `arr` (List<String>), `index` (integer), `currentMask` (integer), `currentLength` (integer), compute the computed result efficiently.

**Example:**

```
Input: arr = input_value, index = 5, currentMask = 5, currentLength = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string

class MaximumLengthofaConcatenatedStringwithUniqueCharacters {
    /**
    * Solves the Maximum Lengthofa Concatenated Stringwith Unique Characters problem.
    * Takes `arr` (list of strings).
    *
    * @param arr The input list of strings.
    * @return The computed integer result.
    */
    /**
    * Solves the Maximum Lengthofa Concatenated Stringwith Unique Characters problem.
    * Takes `arr` (list of strings).
    *
    * @param arr The input list of strings.
    * @return The computed integer result.
    */
    /**
    * Solves the Maximum Lengthofa Concatenated Stringwith Unique Characters problem.
    * Takes `arr` (list of strings).
    *
    * @param arr The input list of strings.
    * @return The computed integer result.
    */
    /**
    * Solves the Maximum Lengthofa Concatenated Stringwith Unique Characters problem.
    * Takes `arr` (list of strings).
    *
    * @param arr The input list of strings.
    * @return The computed integer result.
    */
    fun maxLength(arr: List<String>): Int {
        var maxLen = 0
        val uniqueStrings = arr.filter { it.toCharArray().toSet().size == it.length }

        /**
        * Solves the Maximum Lengthofa Concatenated Stringwith Unique Characters problem.
        * Takes `index` (integer), `currentMask` (integer), `currentLength` (integer).
        *
        * @param index The integer parameter representing index.
        * @param currentMask The integer parameter representing currentMask.
        * @param currentLength The integer parameter representing currentLength.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Maximum Lengthofa Concatenated Stringwith Unique Characters problem.
        * Takes `index` (integer), `currentMask` (integer), `currentLength` (integer).
        *
        * @param index The integer parameter representing index.
        * @param currentMask The integer parameter representing currentMask.
        * @param currentLength The integer parameter representing currentLength.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Maximum Lengthofa Concatenated Stringwith Unique Characters problem.
        * Takes `index` (integer), `currentMask` (integer), `currentLength` (integer).
        *
        * @param index The integer parameter representing index.
        * @param currentMask The integer parameter representing currentMask.
        * @param currentLength The integer parameter representing currentLength.
        * @return Unit (no return value, modifies state in-place).
        */
        /**
        * Solves the Maximum Lengthofa Concatenated Stringwith Unique Characters problem.
        * Takes `index` (integer), `currentMask` (integer), `currentLength` (integer).
        *
        * @param index The integer parameter representing index.
        * @param currentMask The integer parameter representing currentMask.
        * @param currentLength The integer parameter representing currentLength.
        * @return Unit (no return value, modifies state in-place).
        */
        fun backtrack(index: Int, currentMask: Int, currentLength: Int) {
            if (index == uniqueStrings.size) {
                if (currentLength > maxLen) {
                    maxLen = currentLength
                }
                return
            }

            val str = uniqueStrings[index]
            var newMask = currentMask
            var canAdd = true

            for (c in str) {
                val bit = 1 shl (c - 'a')
                if (newMask and bit != 0) {
                    canAdd = false
                    break
                }
                newMask = newMask or bit
            }

            if (canAdd) {
                backtrack(index + 1, newMask, currentLength + str.length)
            }
            backtrack(index + 1, currentMask, currentLength)
        }

        backtrack(0, 0, 0)
        return maxLen
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Maximum Value Of A String Is An Array

### Problem

Given `strs` (Array<String>), compute the computed result efficiently.

**Example:**

```
Input: strs = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string

class MaximumValueOfAStringIsAnArray {
    /**
    * Solves the Maximum Value Of AString Is An Array problem.
    * Takes `strs` (Array<String>).
    *
    * @param strs The input Array<String>.
    * @return The computed integer result.
    */
    /**
    * Solves the Maximum Value Of AString Is An Array problem.
    * Takes `strs` (Array<String>).
    *
    * @param strs The input Array<String>.
    * @return The computed integer result.
    */
    /**
    * Solves the Maximum Value Of AString Is An Array problem.
    * Takes `strs` (Array<String>).
    *
    * @param strs The input Array<String>.
    * @return The computed integer result.
    */
    /**
    * Solves the Maximum Value Of AString Is An Array problem.
    * Takes `strs` (Array<String>).
    *
    * @param strs The input Array<String>.
    * @return The computed integer result.
    */
    fun maximumValue(strs: Array<String>): Int {
        return strs.maxOf {
            val numericValue = it.toIntOrNull()
            numericValue?: it.length
        }
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Merge String Alternatively

### Problem

Given `word1` (string), `word2` (string), compute the computed result efficiently.

**Example:**

```
Input: word1 = "example", word2 = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string

class MergeStringAlternatively {
    /**
    * Solves the Merge String Alternatively problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Merge String Alternatively problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Merge String Alternatively problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Merge String Alternatively problem.
    * Takes `word1` (string), `word2` (string).
    *
    * @param word1 The input string.
    * @param word2 The input string.
    * @return The resulting string.
    */
    fun mergeAlternately(word1: String, word2: String): String {
        val mergedString = StringBuilder()

        for (i in 0 until maxOf(word1.length, word2.length)) {
            if (i < word1.length)
                mergedString.append(word1[i])
            if (i < word2.length)
                mergedString.append(word2[i])
        }

        return mergedString.toString()
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Minimum Deletion To Make Character Frequencies Unique

### Problem

Given `s` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package string

class MinimumDeletionToMakeCharacterFrequenciesUnique {
    /**
    * Solves the Minimum Deletion To Make Character Frequencies Unique problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Minimum Deletion To Make Character Frequencies Unique problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Minimum Deletion To Make Character Frequencies Unique problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Minimum Deletion To Make Character Frequencies Unique problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    fun minDeletions(s: String): Int {
        val freq = IntArray(26)
        for (ch in s) freq[ch - 'a']++

        val seen = mutableSetOf<Int>()
        var deletions = 0

        for (f in freq) {
            var currentFreq = f
            while (currentFreq > 0 && !seen.add(currentFreq)) {
                currentFreq--
                deletions++
            }
        }

        return deletions
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Minimum Window Substring

### Problem

Given `s` (string), `t` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example", t = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **tree traversal/recursion**. Trees are naturally recursive — each subtree is itself a tree. The key is choosing the right traversal order (preorder, inorder, postorder, level-order) for the specific problem.

### Code

```kotlin
package string.sliding_window

class MinimumWindowSubstring {
    /**
    * Solves the Minimum Window Substring problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Minimum Window Substring problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Minimum Window Substring problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Minimum Window Substring problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return The resulting string.
    */
    fun minWindow(s: String, t: String): String {
        // Return early if either string is empty
        if (s.isEmpty() || t.isEmpty()) return ""

        // Frequency map for characters in t (required characters)
        val required = mutableMapOf<Char, Int>()
        t.forEach { required[it] = required.getOrDefault(it, 0) + 1 }

        // Frequency map for the current window in s
        val window = mutableMapOf<Char, Int>()

        // Track the number of characters matched from the required set
        var matched = 0
        var (left, right) = 0 to 0  // Destructuring initialization for left and right pointers

        // Initialize minLength and minStart in a single line
        var (minLength, minStart) = Int.MAX_VALUE to 0

        // Sliding window logic
        while (right < s.length) {
            // Expand the window by moving the right pointer
            val rightChar = s[right]
            window[rightChar] = window.getOrDefault(rightChar, 0) + 1

            // Check if current window has all required characters in needed quantity
            when {
                required.containsKey(rightChar) && window[rightChar] == required[rightChar] -> matched++
            }

            // Shrink the window when all required characters are matched
            while (matched == required.size) {
                val currentLength = right - left + 1
                if (currentLength < minLength) {
                    minLength = currentLength
                    minStart = left
                }

                // Move left pointer to shrink the window
                val leftChar = s[left]
                window[leftChar] = window[leftChar]!! - 1

                when {
                    required.containsKey(leftChar) && window[leftChar]!! < required[leftChar]!! -> matched--
                }

                left++
            }

            // Move right pointer to expand the window
            right++
        }

        // Return the result
        return if (minLength == Int.MAX_VALUE) "" else s.substring(minStart, minStart + minLength)
    }
}
```

### Pattern Insight

**Tree Pattern.** Choose traversal based on need: inorder (sorted for BST), preorder (copy/construct), postorder (bottom-up compute), level-order (BFS). Recursion uses O(h) stack space; iteration uses O(1) with Morris traversal.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

### Variations

1. What if the tree is skewed (worst case — becomes a linked list)?
1. Can you solve this iteratively instead of recursively?
1. What if the tree is an N-ary tree instead of binary?
1. What if O(1) extra space is required (Morris traversal)?
1. Can this be parallelized for different subtrees?

---

## Remove All Adjacent Duplicates In String

### Problem

Given `s` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string.stack

class RemoveAllAdjacentDuplicatesInString {
    /**
    * Solves the Remove All Adjacent Duplicates In String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Remove All Adjacent Duplicates In String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Remove All Adjacent Duplicates In String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Remove All Adjacent Duplicates In String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    fun removeDuplicates(s: String): String {
        val stack = ArrayDeque<Char>()

        s.forEach { ch ->
            when {
                stack.isNotEmpty() && stack.last() == ch -> stack.removeLast()
                else -> stack.add(ch)
            }
        }

        return stack.joinToString("")
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Reverse Words In String

### Problem

Given `s` (string), `nums` (MutableList<String>), `i` (integer), `j` (integer), compute the computed result efficiently.

**Example:**

```
Input: s = "example", nums = input_value, i = 5, j = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **graph traversal**. Choose BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, or topological sort for dependency ordering. Track visited nodes to prevent infinite loops.

### Code

```kotlin
package string

class ReverseWordsInString {
    /**
    * Solves the Reverse Words In String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Reverse Words In String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Reverse Words In String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Reverse Words In String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    fun reverseWords(s: String): String {
        val words = s.split(" ").filter { it.isNotEmpty() }.toMutableList()

        // Two pointers
        var (start, end) = Pair(0, words.lastIndex)

        while (start < end) {
            words[end] = words[start].also { words[start] = words[end] }
            start++
            end--
        }

        return words.joinToString(separator = " ").trim()

    }

    /**
    * Solves the Reverse Words In String problem.
    * Takes `nums` (MutableList<String>), `i` (integer), `j` (integer).
    *
    * @param nums The input MutableList<String>.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Reverse Words In String problem.
    * Takes `nums` (MutableList<String>), `i` (integer), `j` (integer).
    *
    * @param nums The input MutableList<String>.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Reverse Words In String problem.
    * Takes `nums` (MutableList<String>), `i` (integer), `j` (integer).
    *
    * @param nums The input MutableList<String>.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Reverse Words In String problem.
    * Takes `nums` (MutableList<String>), `i` (integer), `j` (integer).
    *
    * @param nums The input MutableList<String>.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    fun swap(nums: MutableList<String>, i: Int, j: Int) {
        nums[j] = nums[i].also { nums[i] = nums[j] }
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Shortest Common Supersequence

### Problem

Given `X` (string), `Y` (string), compute the computed result efficiently.

**Example:**

```
Input: X = "example", Y = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package string.dynamic_programming

class ShortestCommonSupersequence {
    /**
    * Solves the Shortest Common Supersequence problem.
    * Takes `X` (string), `Y` (string).
    *
    * @param X The input string.
    * @param Y The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Shortest Common Supersequence problem.
    * Takes `X` (string), `Y` (string).
    *
    * @param X The input string.
    * @param Y The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Shortest Common Supersequence problem.
    * Takes `X` (string), `Y` (string).
    *
    * @param X The input string.
    * @param Y The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Shortest Common Supersequence problem.
    * Takes `X` (string), `Y` (string).
    *
    * @param X The input string.
    * @param Y The input string.
    * @return The resulting string.
    */
    fun shortestCommonSupersequence(X: String, Y: String): String? {
        val (m, n) = X.length to Y.length
        val dp = Array(m + 1) { IntArray(n + 1) }

        for (i in 1..m) for (j in 1..n) {
            dp[i][j] = if (X[i - 1] == Y[j - 1]) dp[i - 1][j - 1] + 1 else maxOf(dp[i - 1][j], dp[i][j - 1])
        }

        val scs = StringBuilder()
        var (i, j) = m to n

        while (i > 0 && j > 0) {
            when {
                X[i - 1] == Y[j - 1] -> { scs.append(X[i - 1]); i--; j-- }
                dp[i - 1][j] > dp[i][j - 1] -> { scs.append(X[i - 1]); i-- }
                else -> { scs.append(Y[j - 1]); j-- }
            }
        }

        // Add remaining characters from X or Y
        while (i > 0) { scs.append(X[i - 1]); i-- }
        while (j > 0) { scs.append(Y[j - 1]); j-- }

        // Reverse the result and return as string
        return scs.reverse().toString()
    }
}

// abc, axyzabc, yzmnbc

// yzmnbcaxyzabc

// a -> b -> c
// a -> x -> y -> x -> (a -> b -> c)

// y -> z -> m -> n -> b -> c
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Simplify Path

### Problem

Given `path` (string), compute the computed result efficiently.

**Example:**

```
Input: path = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package string.stack

class SimplifyPath {
    /**
    * Solves the Simplify Path problem.
    * Takes `path` (string).
    *
    * @param path The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Simplify Path problem.
    * Takes `path` (string).
    *
    * @param path The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Simplify Path problem.
    * Takes `path` (string).
    *
    * @param path The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Simplify Path problem.
    * Takes `path` (string).
    *
    * @param path The input string.
    * @return The resulting string.
    */
    fun simplifyPath(path: String): String {
        // Split the path by "/"
        val tokens = path.split("/")

        // Initialize a mutable list to store valid directory names
        val stack = mutableListOf<String>()

        for (token in tokens) {
            when (token) {
                "", "." -> {
                    // Ignore empty or current directory tokens
                    continue
                }
                ".." -> {
                    // Pop from the list if it's not empty (go back to the parent directory)
                    if (stack.isNotEmpty()) {
                        stack.removeLast()
                    }
                }
                else -> {
                    // Push valid directory names onto the list
                    stack.add(token)
                }
            }
        }

        // Rebuild the simplified path from the list
        return "/" + stack.joinToString("/")
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## String Compression

### Problem

Given `chars` (CharArray), compute the computed result efficiently.

**Example:**

```
Input: chars = input_value
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string

// Data Compression Algorithm

class StringCompression {
    /**
    * Solves the String Compression problem.
    * Takes `chars` (CharArray).
    *
    * @param chars The input CharArray.
    * @return The computed integer result.
    */
    /**
    * Solves the String Compression problem.
    * Takes `chars` (CharArray).
    *
    * @param chars The input CharArray.
    * @return The computed integer result.
    */
    /**
    * Solves the String Compression problem.
    * Takes `chars` (CharArray).
    *
    * @param chars The input CharArray.
    * @return The computed integer result.
    */
    /**
    * Solves the String Compression problem.
    * Takes `chars` (CharArray).
    *
    * @param chars The input CharArray.
    * @return The computed integer result.
    */
    fun compress(chars: CharArray): Int {
        var count = 0
        val sb = StringBuilder()

        for (i in chars.indices) {
            count++

            if (i  == chars.lastIndex || chars[i] != chars[i+1]) {
                sb.append(chars[i])

                if (count > 1) {
                    sb.append(count)
                }
                count = 0
            }
        }

        for (i in 0 until sb.length) chars[i] = sb.get(i)

        return sb.length
    }

    /**
    * Solves the String Compression problem.
    * Takes `chars` (CharArray).
    *
    * @param chars The input CharArray.
    * @return The computed integer result.
    */
    /**
    * Solves the String Compression problem.
    * Takes `chars` (CharArray).
    *
    * @param chars The input CharArray.
    * @return The computed integer result.
    */
    /**
    * Solves the String Compression problem.
    * Takes `chars` (CharArray).
    *
    * @param chars The input CharArray.
    * @return The computed integer result.
    */
    /**
    * Solves the String Compression problem.
    * Takes `chars` (CharArray).
    *
    * @param chars The input CharArray.
    * @return The computed integer result.
    */
    fun string_compression_inline(chars: CharArray): Int {
        var partitionLength = 0
        var i = 0

        while ( i < chars.size) {
            val currentChar = chars[i]
            var count = 0
            while ( i < chars.size && chars[i] == currentChar) {
                count++
                i++
            }
            chars[partitionLength++] = currentChar

            if (count > 1) {
                count.toString().forEach { ch -> chars[partitionLength++] = ch }
            }
        }

        return partitionLength

    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## String Compression_II

### Problem

Given `word` (string), compute the computed result efficiently.

**Example:**

```
Input: word = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string

class StringCompression_II {
    /**
    * Solves the String Compression_II problem.
    * Takes `word` (string).
    *
    * @param word The input string.
    * @return The resulting string.
    */
    /**
    * Solves the String Compression_II problem.
    * Takes `word` (string).
    *
    * @param word The input string.
    * @return The resulting string.
    */
    /**
    * Solves the String Compression_II problem.
    * Takes `word` (string).
    *
    * @param word The input string.
    * @return The resulting string.
    */
    /**
    * Solves the String Compression_II problem.
    * Takes `word` (string).
    *
    * @param word The input string.
    * @return The resulting string.
    */
    fun compressedString(word: String): String {
        val compressed = StringBuilder()

        var i = 0

        while (i < word.length) {
            val ch = word[i]
            var count = 0

            while (i < word.length && word[i] == ch && count < 9 ) {
                count++
                i++
            }

            compressed.append(count).append(ch)
        }

        return compressed.toString()
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Unique Length3 Palindromic Subsequence

### Problem

Given `s` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package string.hashtable

class UniqueLength3PalindromicSubsequence {
    /**
    * Solves the Unique Length3Palindromic Subsequence problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Unique Length3Palindromic Subsequence problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Unique Length3Palindromic Subsequence problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    /**
    * Solves the Unique Length3Palindromic Subsequence problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The computed integer result.
    */
    fun countPalindromicSubsequence(s: String): Int {
        val charPositions = mutableMapOf<Char, MutableList<Int>>()

        // Step 1: Record positions of each character
        s.forEachIndexed { index, char ->
            charPositions.computeIfAbsent(char) { mutableListOf() }.add(index)
        }

        var count = 0

        // Step 2: Process each character's occurrences
        for ((char, positions) in charPositions) {
            val start = positions.first()
            val end = positions.last()

            // Skip if there's no room between the first and last occurrence
            if (end - start <= 1) continue

            val distinctChars = mutableSetOf<Char>()

            // Count distinct characters between first and last occurrence
            for (i in start + 1 until end) {
                distinctChars.add(s[i])
            }

            count += distinctChars.size
        }

        return count
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(n²) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Valid Anagram

### Problem

Given `s` (string), `t` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example", t = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string

class ValidAnagram {
    /**
    * Solves the Valid Anagram problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Anagram problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Anagram problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Anagram problem.
    * Takes `s` (string), `t` (string).
    *
    * @param s The input string.
    * @param t The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isAnagram(s: String, t: String): Boolean {
        if (s.length != t.length) return false

        val charCount = IntArray(26)

        for (i in s.indices) {
            charCount[s[i] - 'a']++
            charCount[t[i] - 'a']--
        }

        // Check if all counts are zero
        for (count in charCount) {
            if (count != 0) {
                return false
            }
        }

        return true
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Valid Number

### Problem

Given `s` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package string

class ValidNumber {
    /**
    * Solves the Valid Number problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Number problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Number problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Number problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isNumber(s: String): Boolean {
        // Initialize variables
        var (hasNum, hasDot, hasE, hasDigitsAfterE) = listOf(false, false, false, false)

        val str = s.trim() // Remove leading/trailing spaces
        for (i in str.indices) {
            val c = str[i]

            when {
                c in '0'..'9' -> {
                    hasNum = true
                    if (hasE) hasDigitsAfterE = true // Ensure digits appear after 'e'
                }
                c == '.' -> {
                    if (hasDot || hasE) return false // Can't have multiple dots or dots after 'e'
                    hasDot = true
                }
                c == 'e' || c == 'E' -> {
                    if (hasE || !hasNum) return false // Can't have multiple 'e' or 'e' without preceding number
                    hasE = true
                    hasDigitsAfterE = false // Reset this to ensure we validate digits after 'e'
                }
                c == '+' || c == '-' -> {
                    if (i != 0 && str[i - 1] != 'e' && str[i - 1] != 'E') return false // Sign only valid at start or after 'e'
                }
                else -> return false // Invalid character
            }
        }
        // Valid only if we have digits and valid 'e' part
        return hasNum && (!hasE || hasDigitsAfterE)
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Valid Palindrome

### Problem

Given `s` (string), compute the computed result efficiently.

**Example:**

```
Input: s = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package string

class ValidPalindrome {
    /**
    * Solves the Valid Palindrome problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isPalindrome(s: String): Boolean {
        var left = 0
        var right = s.lastIndex
        val isAlpha = {ch: Char -> Character.isAlphabetic(ch.code) || Character.isDigit(ch.code)}

        while (left < right) {
            when {
                isAlpha(s[left]) && isAlpha(s[right])
                        && s[left].lowercaseChar() != s[right].lowercaseChar() -> return false
                isAlpha(s[left]) && !isAlpha(s[right]) ->  right --
                isAlpha(s[right]) && !isAlpha(s[left]) -> left++
                else -> {
                    left++
                    right--
                }

            }
        }

        return true
    }
}
```

### Pattern Insight

**Dynamic Programming Pattern.** Define states (changing parameters), transitions (how to compute one state from others), and base cases. Compute bottom-up (iterative, table) or top-down (recursive, memoization).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(n²) |

### Variations

1. Can you optimize space to O(1) by keeping only the previous row?
1. What if the input size is 10x larger — does the DP table still fit?
1. Can you reconstruct the optimal path, not just the optimal value?
1. What changes if constraints go from unlimited to limited (or vice versa)?
1. Is there a greedy solution? When would greedy fail?

---

## Valid Palindrome_II

### Problem

Given `s` (string), `i` (integer), `j` (integer), compute the computed result efficiently.

**Example:**

```
Input: s = "example", i = 5, j = 5
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package string

class ValidPalindrome_II {
    /**
    * Solves the Valid Palindrome_II problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome_II problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome_II problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome_II problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun validPalindrome(s: String): Boolean {
        var left = 0
        var right = s.lastIndex

        while (left < right) {
            if (s[left] != s[right]) {
                return isPalindrome(s, left, right - 1) || isPalindrome(s, left + 1, right)
            }

            left++
            right--
        }

        return true
    }

    /**
    * Solves the Valid Palindrome_II problem.
    * Takes `s` (string), `i` (integer), `j` (integer).
    *
    * @param s The input string.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome_II problem.
    * Takes `s` (string), `i` (integer), `j` (integer).
    *
    * @param s The input string.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome_II problem.
    * Takes `s` (string), `i` (integer), `j` (integer).
    *
    * @param s The input string.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome_II problem.
    * Takes `s` (string), `i` (integer), `j` (integer).
    *
    * @param s The input string.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isPalindrome(s: String, i: Int, j: Int): Boolean {
        var left = i
        var right = j

        while (left < right) {
            if (s[left++] != s[right--]) {
                return false
            }
        }

        return true
    }
}
```

### Pattern Insight

**Dynamic Programming Pattern.** Define states (changing parameters), transitions (how to compute one state from others), and base cases. Compute bottom-up (iterative, table) or top-down (recursive, memoization).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(n²) |

### Variations

1. Can you optimize space to O(1) by keeping only the previous row?
1. What if the input size is 10x larger — does the DP table still fit?
1. Can you reconstruct the optimal path, not just the optimal value?
1. What changes if constraints go from unlimited to limited (or vice versa)?
1. Is there a greedy solution? When would greedy fail?

---

## Valid Palindrome_III

### Problem

Given `s` (string), `k` (integer), `start` (integer), `length` (integer), compute the computed result efficiently.

**Example:**

```
Input: s = "example", k = 5, start = 5, length = 5
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package string.dynamic_programming

class ValidPalindrome_III {
    /**
    * Solves the Valid Palindrome_III problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome_III problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome_III problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome_III problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isValidPalindrome(s: String, k: Int): Boolean {
        val dp = Array(s.length) { IntArray(s.length) { 0 } }

        /**
        * Solves the Valid Palindrome_III problem.
        * Takes `start` (integer), `length` (integer).
        *
        * @param start The integer parameter representing start.
        * @param length The integer parameter representing length.
        * @return The computed integer result.
        */
        /**
        * Solves the Valid Palindrome_III problem.
        * Takes `start` (integer), `length` (integer).
        *
        * @param start The integer parameter representing start.
        * @param length The integer parameter representing length.
        * @return The computed integer result.
        */
        /**
        * Solves the Valid Palindrome_III problem.
        * Takes `start` (integer), `length` (integer).
        *
        * @param start The integer parameter representing start.
        * @param length The integer parameter representing length.
        * @return The computed integer result.
        */
        /**
        * Solves the Valid Palindrome_III problem.
        * Takes `start` (integer), `length` (integer).
        *
        * @param start The integer parameter representing start.
        * @param length The integer parameter representing length.
        * @return The computed integer result.
        */
        fun lps(start: Int, length: Int): Int {
            val end = start + length - 1
            return when {
                length in 0..1 -> length
                dp[start][end] != 0 -> dp[start][end]
                s[start] == s[end] -> lps(start + 1, length - 2) + 2
                else -> maxOf(lps(start + 1, length - 1), lps(start, length - 1))
            }.also {
                dp[start][end] = it
            }
        }

        // Calculate the length of the longest palindromic subsequence
        val lpsLength = lps(0, s.length)

        // Check if the number of deletions required is less than or equal to k
        return (s.length - lpsLength) <= k
    }
}
```

### Pattern Insight

**Dynamic Programming Pattern.** Define states (changing parameters), transitions (how to compute one state from others), and base cases. Compute bottom-up (iterative, table) or top-down (recursive, memoization).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(n²) |

### Variations

1. Can you optimize space to O(1) by keeping only the previous row?
1. What if the input size is 10x larger — does the DP table still fit?
1. Can you reconstruct the optimal path, not just the optimal value?
1. What changes if constraints go from unlimited to limited (or vice versa)?
1. Is there a greedy solution? When would greedy fail?

---

## Valid Palindrome_III_Space Optimized

### Problem

Given `s` (string), `k` (integer), compute the computed result efficiently.

**Example:**

```
Input: s = "example", k = 5
Output: 42 (expected result)

```

### Why This Approach

This problem has **optimal substructure** (the optimal solution builds from optimal solutions to subproblems) and **overlapping subproblems** (same subproblems recur). Dynamic programming avoids redundant computation by caching results — either top-down with memoization or bottom-up with tabulation.

### Code

```kotlin
package string.dynamic_programming

class ValidPalindrome_III_SpaceOptimized {
    /**
    * Solves the Valid Palindrome_III_Space Optimized problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome_III_Space Optimized problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome_III_Space Optimized problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Palindrome_III_Space Optimized problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun isValidPalindrome(s: String, k: Int): Boolean {
        val n = s.length
        val dp = IntArray(n) { 1 } // Initialize with 1 because each character is a palindrome of length 1

        for (i in n - 1 downTo 0) {
            var prev = 0 // Stores the value of dp[i+1][j-1] from the 2D DP approach
            for (j in i + 1 until n) {
                val temp = dp[j] // Store the current dp[j] before updating it
                if (s[i] == s[j]) {
                    dp[j] = 2 + prev // If characters match, add 2 to the LPS length of the inner substring
                } else {
                    dp[j] = maxOf(dp[j], dp[j - 1]) // Otherwise, take the maximum of excluding s[i] or s[j]
                }
                prev = temp // Update prev for the next iteration
            }
        }

        val lpsLength = dp[n - 1] // The length of the LPS for the entire string
        return (n - lpsLength) <= k
    }
}
```

### Pattern Insight

**Dynamic Programming Pattern.** Define states (changing parameters), transitions (how to compute one state from others), and base cases. Compute bottom-up (iterative, table) or top-down (recursive, memoization).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(n²) |

### Variations

1. Can you optimize space to O(1) by keeping only the previous row?
1. What if the input size is 10x larger — does the DP table still fit?
1. Can you reconstruct the optimal path, not just the optimal value?
1. What changes if constraints go from unlimited to limited (or vice versa)?
1. Is there a greedy solution? When would greedy fail?

---

## Validate IP Address

### Problem

Given `queryIP` (string), `ip` (string), compute the computed result efficiently.

**Example:**

```
Input: queryIP = "example", ip = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem requires choosing the right **data structure and algorithm** based on the constraints. The efficient solution typically replaces a brute-force approach (O(n²)) with a more clever one (O(n) or O(n log n)) using appropriate data structures.

### Code

```kotlin
package string

class ValidateIPAddress {
    /**
    * Solves the Validate IPAddress problem.
    * Takes `queryIP` (string).
    *
    * @param queryIP The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Validate IPAddress problem.
    * Takes `queryIP` (string).
    *
    * @param queryIP The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Validate IPAddress problem.
    * Takes `queryIP` (string).
    *
    * @param queryIP The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Validate IPAddress problem.
    * Takes `queryIP` (string).
    *
    * @param queryIP The input string.
    * @return The resulting string.
    */
    fun validIPAddress(queryIP: String): String {
        return when {
            isValidIPv4(queryIP) -> "IPv4"
            isValidIPv6(queryIP) -> "IPv6"
            else -> "Neither"
        }
    }

    /**
    * Helper: is valid ipv4.
    *
    * @param ip The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is valid ipv4.
    *
    * @param ip The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is valid ipv4.
    *
    * @param ip The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is valid ipv4.
    *
    * @param ip The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    private fun isValidIPv4(ip: String): Boolean {
        if (ip.startsWith('.') || ip.endsWith('.')) return false

        val segments = ip.split('.')

        if (segments.size != 4) return false

        return segments.all { segment ->
            segment.isNotEmpty() &&
                    segment.all { it.isDigit() } &&
                    (segment.length == 1 || segment[0] != '0') &&
                    segment.length <= 3 &&
                    try {
                        segment.toInt() in 0..255
                    } catch (e: NumberFormatException) {
                        false
                    }
        }
    }

    /**
    * Helper: is valid ipv6.
    *
    * @param ip The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is valid ipv6.
    *
    * @param ip The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is valid ipv6.
    *
    * @param ip The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Helper: is valid ipv6.
    *
    * @param ip The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    private fun isValidIPv6(ip: String): Boolean {
        if (ip.startsWith(':') || ip.endsWith(':')) return false

        val segments = ip.split(':')

        if (segments.size != 8) return false

        return segments.all { segment ->
            segment.length in 1..4 &&
                    segment.all { char ->
                        char.isDigit() || char.lowercaseChar() in 'a'..'f'
                    }
        }
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Valid Word Abbreviation

### Problem

Given `word` (string), `abbr` (string), compute the computed result efficiently.

**Example:**

```
Input: word = "example", abbr = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **graph traversal**. Choose BFS for shortest path in unweighted graphs, DFS for connectivity/path existence, or topological sort for dependency ordering. Track visited nodes to prevent infinite loops.

### Code

```kotlin
package string

class ValidWordAbbreviation {
    /**
    * Solves the Valid Word Abbreviation problem.
    * Takes `word` (string), `abbr` (string).
    *
    * @param word The input string.
    * @param abbr The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Word Abbreviation problem.
    * Takes `word` (string), `abbr` (string).
    *
    * @param word The input string.
    * @param abbr The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Word Abbreviation problem.
    * Takes `word` (string), `abbr` (string).
    *
    * @param word The input string.
    * @param abbr The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Valid Word Abbreviation problem.
    * Takes `word` (string), `abbr` (string).
    *
    * @param word The input string.
    * @param abbr The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun validWordAbbreviation(word: String, abbr: String): Boolean {
        var i = 0
        var j = 0

        while (i < word.length && j < abbr.length) {
            if (abbr[j].isDigit()) {
                if (abbr[j] == '0') return false  // Leading zero check

                var count = 0

                while (j < abbr.length && abbr[j].isDigit()) {
                    count = count * 10 + (abbr[j++] - '0')
                }

                i += count
            } else {
                if (word[i++] != abbr[j++]) return false
            }
        }

        return i == word.length && j == abbr.length
    }
}
```

### Pattern Insight

**Algorithmic Pattern.** The right data structure transforms a brute-force O(n²) into O(n) or O(log n). Consider hash maps for O(1) lookup, sorting as preprocessing, or two-pointer passes.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

### Variations

1. What if the input size is much larger — can you optimize?
1. What if O(1) extra space is required?
1. What if there are edge cases (empty input, single element, duplicates)?
1. What if constraints change (positive only, sorted input, distinct values)?
1. Can this be solved with a different algorithmic paradigm?

---

## Maximum Numberof Vowelsin Substringof Given Length

### Problem

Given `s` (string), `k` (integer), compute the computed result efficiently.

**Example:**

```
Input: s = "example", k = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **tree traversal/recursion**. Trees are naturally recursive — each subtree is itself a tree. The key is choosing the right traversal order (preorder, inorder, postorder, level-order) for the specific problem.

### Code

```kotlin
package string.sliding_window

class MaximumNumberofVowelsinSubstringofGivenLength {
    /**
    * Solves the Maximum Numberof Vowelsin Substringof Given Length problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Maximum Numberof Vowelsin Substringof Given Length problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Maximum Numberof Vowelsin Substringof Given Length problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    /**
    * Solves the Maximum Numberof Vowelsin Substringof Given Length problem.
    * Takes `s` (string), `k` (integer).
    *
    * @param s The input string.
    * @param k The integer parameter representing k.
    * @return The computed integer result.
    */
    fun maxVowels(s: String, k: Int): Int {
        var (vowelWindowCount, maxCount) = Pair(0,0)
        val vowels = setOf('a', 'e', 'i', 'o', 'u')

        for (i in 0 until s.length) {

            if (s[i] in vowels ) {
                vowelWindowCount++
            }

            if ( i >= k -1) {
                maxCount = maxOf(maxCount, vowelWindowCount)

                if (s[i - k + 1] in vowels)
                    vowelWindowCount--
            }
        }

        return maxCount
    }
}
```

### Pattern Insight

**Tree Pattern.** Choose traversal based on need: inorder (sorted for BST), preorder (copy/construct), postorder (bottom-up compute), level-order (BFS). Recursion uses O(h) stack space; iteration uses O(1) with Morris traversal.

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(h) where h = tree height |

### Variations

1. What if the tree is skewed (worst case — becomes a linked list)?
1. Can you solve this iteratively instead of recursively?
1. What if the tree is an N-ary tree instead of binary?
1. What if O(1) extra space is required (Morris traversal)?
1. Can this be parallelized for different subtrees?

---

## Permutations In String

### Problem

Given `s1` (string), `s2` (string), compute the computed result efficiently.

**Example:**

```
Input: s1 = "example", s2 = "example"
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string.hashtable

class PermutationsInString {
    /**
    * Solves the Permutations In String problem.
    * Takes `s1` (string), `s2` (string).
    *
    * @param s1 The input string.
    * @param s2 The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Permutations In String problem.
    * Takes `s1` (string), `s2` (string).
    *
    * @param s1 The input string.
    * @param s2 The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Permutations In String problem.
    * Takes `s1` (string), `s2` (string).
    *
    * @param s1 The input string.
    * @param s2 The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    /**
    * Solves the Permutations In String problem.
    * Takes `s1` (string), `s2` (string).
    *
    * @param s1 The input string.
    * @param s2 The input string.
    * @return `true` if the condition is met, `false` otherwise.
    */
    fun checkInclusion(s1: String, s2: String): Boolean {
        val targetFreq = IntArray(26)
        val windowFreq = IntArray(26)

        for(c in s1) targetFreq[c - 'a']++

        for (i in s2.indices) {
            windowFreq[s2[i] - 'a']++
            if (i >= s1.length) {
                windowFreq[s2[i - s1.length] - 'a']--
            }
            if (targetFreq.contentEquals(windowFreq))
                return true
        }

        return false
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

## Reverse Vowel Of String

### Problem

Given `s` (string), `i` (integer), `j` (integer), compute the computed result efficiently.

**Example:**

```
Input: s = "example", i = 5, j = 5
Output: 42 (expected result)

```

### Why This Approach

This problem uses **string processing** techniques. Common approaches include two pointers (palindrome checking), sliding window (substring search), DP (sequence alignment), hashing (pattern matching), or trie (prefix search).

### Code

```kotlin
package string

class ReverseVowelOfString {
    /**
    * Solves the Reverse Vowel Of String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Reverse Vowel Of String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Reverse Vowel Of String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    /**
    * Solves the Reverse Vowel Of String problem.
    * Takes `s` (string).
    *
    * @param s The input string.
    * @return The resulting string.
    */
    fun reverseVowels(s: String): String {
        val vowels = setOf('a', 'e', 'i', 'o', 'u')
        val result = StringBuilder(s)

        var (start, end) = Pair(0, s.lastIndex)

        while (start < end) {
            if (s[start] in vowels && s[end] in vowels) {
                swap (result, start++, end--)
            } else if (s[start].lowercaseChar() !in vowels)  {
                start++
            } else {
                end--
            }
        }

        return result.toString()
    }

    /**
    * Solves the Reverse Vowel Of String problem.
    * Takes `s` (StringBuilder), `i` (integer), `j` (integer).
    *
    * @param s The input string.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Reverse Vowel Of String problem.
    * Takes `s` (StringBuilder), `i` (integer), `j` (integer).
    *
    * @param s The input string.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Reverse Vowel Of String problem.
    * Takes `s` (StringBuilder), `i` (integer), `j` (integer).
    *
    * @param s The input string.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    /**
    * Solves the Reverse Vowel Of String problem.
    * Takes `s` (StringBuilder), `i` (integer), `j` (integer).
    *
    * @param s The input string.
    * @param i The integer parameter representing i.
    * @param j The integer parameter representing j.
    * @return Unit (no return value, modifies state in-place).
    */
    fun swap(s: StringBuilder, i: Int, j: Int) {
        s[j] = s[i].also { s[i] = s[j]}
    }
}
```

### Pattern Insight

**String Pattern.** Two pointers for palindrome/partition. Sliding window for substring. DP for sequence alignment (LCS, edit distance). Hashing for pattern matching (Rabin-Karp).

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) or O(n) |

### Variations

1. What if strings are very long — can you optimize space?
1. What if you need to reconstruct the actual subsequence, not just the length?
1. What if case sensitivity or Unicode characters matter?
1. What if you need to handle 3+ strings simultaneously?
1. Can hashing (Rabin-Karp) be used for faster matching?

---

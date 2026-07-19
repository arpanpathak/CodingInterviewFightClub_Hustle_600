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

> **57 problems** — Master string algorithms: pattern matching, DP on strings, and parsing.

## The Pattern

String problems use: two pointers, sliding window, DP (LCS, edit distance), KMP/Rabin-Karp for pattern matching, and trie for prefix search.

## Complete Problem Set

| # | Problem | Pattern | Difficulty |
|---|---------|-----------|------------|
| 1 | [Apply Substitutions](#applysubstitutions) | — | <span class="badge badge-medium">Medium</span> |
| 2 | [Break A Palindrome](#breakapalindrome) | — | <span class="badge badge-medium">Medium</span> |
| 3 | [Checkifa Parentheses String Can Be Valid](#checkifaparenthesesstringcanbevalid) | — | <span class="badge badge-medium">Medium</span> |
| 4 | [Count And Say](#countandsay) | — | <span class="badge badge-medium">Medium</span> |
| 5 | [Count Words With A Given Prefix](#countwordswithagivenprefix) | — | <span class="badge badge-medium">Medium</span> |
| 6 | [Count Words With A Given Prefix_Trie](#countwordswithagivenprefix_trie) | — | <span class="badge badge-medium">Medium</span> |
| 7 | [Count Words With A Given Prefix_Trie_FP](#countwordswithagivenprefix_trie_fp) | — | <span class="badge badge-medium">Medium</span> |
| 8 | [Custom Sort String](#customsortstring) | — | <span class="badge badge-medium">Medium</span> |
| 9 | [Decode String](#decodestring) | — | <span class="badge badge-medium">Medium</span> |
| 10 | [Determine If Strings Are Close](#determineifstringsareclose) | — | <span class="badge badge-medium">Medium</span> |
| 11 | [Edit Distance](#editdistance) | — | <span class="badge badge-medium">Medium</span> |
| 12 | [Excel Sheet To Column Number](#excelsheettocolumnnumber) | — | <span class="badge badge-medium">Medium</span> |
| 13 | [Find All Anagrams](#findallanagrams) | — | <span class="badge badge-medium">Medium</span> |
| 14 | [Findtheindexofthefirstoccurrenceina String](#findtheindexofthefirstoccurrenceina_string) | — | <span class="badge badge-medium">Medium</span> |
| 15 | [Find The Index Of The First Occurrence In String_Rabin Karp](#findtheindexofthefirstoccurrenceina_string_rabinkarp) | — | <span class="badge badge-medium">Medium</span> |
| 16 | [Find Unique Binary String](#finduniquebinarystring) | — | <span class="badge badge-medium">Medium</span> |
| 17 | [Generate Parantheses](#generateparantheses) | — | <span class="badge badge-medium">Medium</span> |
| 18 | [Goat Latin](#goatlatin) | — | <span class="badge badge-medium">Medium</span> |
| 19 | [Greatest Common Divisor Of Strings](#greatestcommondivisorofstrings) | — | <span class="badge badge-medium">Medium</span> |
| 20 | [Group Anagrams](#groupanagrams) | — | <span class="badge badge-medium">Medium</span> |
| 21 | [Group Shifted Strings](#groupshiftedstrings) | — | <span class="badge badge-medium">Medium</span> |
| 22 | [Interleaving String](#interleavingstring) | — | <span class="badge badge-medium">Medium</span> |
| 23 | [Isomorphic String](#isomorphicstring) | — | <span class="badge badge-medium">Medium</span> |
| 24 | [Is Subsequence](#issubsequence) | — | <span class="badge badge-medium">Medium</span> |
| 25 | [Length Of Last Word](#lengthoflastword) | — | <span class="badge badge-medium">Medium</span> |
| 26 | [Longest Common Prefix](#longestcommonprefix) | — | <span class="badge badge-medium">Medium</span> |
| 27 | [Longest Common Subsequence](#longestcommonsubsequence) | — | <span class="badge badge-medium">Medium</span> |
| 28 | [Longest Common Substring](#longestcommonsubstring) | — | <span class="badge badge-medium">Medium</span> |
| 29 | [Longest Palidnromic Substring](#longestpalidnromicsubstring) | — | <span class="badge badge-medium">Medium</span> |
| 30 | [Longest Palindromic Subsequence](#longestpalindromicsubsequence) | — | <span class="badge badge-medium">Medium</span> |
| 31 | [Longest Palindromic Subsequence_Bottom Up](#longestpalindromicsubsequence_bottomup) | — | <span class="badge badge-medium">Medium</span> |
| 32 | [Longest Repeating Character Replacement](#longestrepeatingcharacterreplacement) | — | <span class="badge badge-medium">Medium</span> |
| 33 | [Longest String Chain](#longeststringchain) | — | <span class="badge badge-medium">Medium</span> |
| 34 | [Maximum Lengthofa Concatenated Stringwith Unique Characters](#maximumlengthofaconcatenatedstringwithuniquecharacters) | — | <span class="badge badge-medium">Medium</span> |
| 35 | [Maximum Value Of A String Is An Array](#maximumvalueofastringisanarray) | — | <span class="badge badge-medium">Medium</span> |
| 36 | [Merge String Alternatively](#mergestringalternatively) | — | <span class="badge badge-medium">Medium</span> |
| 37 | [Minimum Deletion To Make Character Frequencies Unique](#minimumdeletiontomakecharacterfrequenciesunique) | — | <span class="badge badge-medium">Medium</span> |
| 38 | [Minimum Window Substring](#minimumwindowsubstring) | — | <span class="badge badge-medium">Medium</span> |
| 39 | [Remove All Adjacent Duplicates In String](#removealladjacentduplicatesinstring) | — | <span class="badge badge-medium">Medium</span> |
| 40 | [Reverse Words In String](#reversewordsinstring) | — | <span class="badge badge-medium">Medium</span> |
| 41 | [Shortest Common Supersequence](#shortestcommonsupersequence) | — | <span class="badge badge-medium">Medium</span> |
| 42 | [Simplify Path](#simplifypath) | — | <span class="badge badge-medium">Medium</span> |
| 43 | [String Compression](#stringcompression) | — | <span class="badge badge-medium">Medium</span> |
| 44 | [String Compression_II](#stringcompression_ii) | — | <span class="badge badge-medium">Medium</span> |
| 45 | [Unique Length3 Palindromic Subsequence](#uniquelength3palindromicsubsequence) | — | <span class="badge badge-medium">Medium</span> |
| 46 | [Unique Substring With Equal Digit Frequency](#uniquesubstringwithequaldigitfrequency) | — | <span class="badge badge-medium">Medium</span> |
| 47 | [Valid Anagram](#validanagram) | — | <span class="badge badge-medium">Medium</span> |
| 48 | [Valid Number](#validnumber) | — | <span class="badge badge-medium">Medium</span> |
| 49 | [Valid Palindrome](#validpalindrome) | — | <span class="badge badge-medium">Medium</span> |
| 50 | [Valid Palindrome_II](#validpalindrome_ii) | — | <span class="badge badge-medium">Medium</span> |
| 51 | [Valid Palindrome_III](#validpalindrome_iii) | — | <span class="badge badge-medium">Medium</span> |
| 52 | [Valid Palindrome_III_Space Optimized](#validpalindrome_iii_spaceoptimized) | — | <span class="badge badge-medium">Medium</span> |
| 53 | [Validate IP Address](#validateipaddress) | — | <span class="badge badge-medium">Medium</span> |
| 54 | [Valid Word Abbreviation](#validwordabbreviation) | — | <span class="badge badge-medium">Medium</span> |
| 55 | [Maximum Numberof Vowelsin Substringof Given Length](#maximumnumberofvowelsinsubstringofgivenlength) | — | <span class="badge badge-medium">Medium</span> |
| 56 | [Permutations In String](#permutationsinstring) | — | <span class="badge badge-medium">Medium</span> |
| 57 | [Reverse Vowel Of String](#reversevowelofstring) | — | <span class="badge badge-medium">Medium</span> |

---

## Apply Substitutions

<span id="applysubstitutions"></span>

### Problem

**Applysubstitutions**

**Function:** `Apply Substitutions` takes `replacements` (List<List<string>>), `text` (string) and returns **string**.

**Key logic:**
- Replace if found, else keep original
- Move past the placeholder
- Continue resolving if changed



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `map`, `sb`, `i`, `key`, `result`

**Execution flow:**
- Replace if found, else keep original
- Move past the placeholder
- Continue resolving if changed

### Code

```kotlin
package string

class ApplySubstitutions {
    fun applySubstitutions(replacements: List<List<String>>, text: String): String {
        val map = mutableMapOf<String, String>()

        for ((key, value) in replacements) {
            map[key] = value
        }

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Break A Palindrome

<span id="breakapalindrome"></span>

### Problem

**Breakapalindrome**

**Function:** `Break Palindrome` takes `palindrome` (string) and returns **string**.

**Key logic:**
- If all characters are 'a', change the last character to 'b'



### Approach

**Solution Approach:**
1. The main function `breakPalindrome` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `arr`

**Execution flow:**
- If all characters are 'a', change the last character to 'b'

### Code

```kotlin
package string.greedy

class BreakAPalindrome {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Checkifa Parentheses String Can Be Valid

<span id="checkifaparenthesesstringcanbevalid"></span>

### Problem

**Checkifaparenthesesstringcanbevalid**

**Function:** `Can Be Valid` takes `s` (string), `locked` (string) and returns **boolean**.

**Key logic:**
- Odd number of brackets
- Second pass: Right to left
- If it's locked as ')' or can be treated as ')'
- If at any point we have more opening parentheses than closing
- If both counts are valid, the string is balanced



### Approach

**Solution Approach:**
1. The main function `canBeValid` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `openCount`, `closeCount`

**Execution flow:**
- Odd number of brackets
- Second pass: Right to left
- If it's locked as ')' or can be treated as ')'
- If at any point we have more opening parentheses than closing
- If both counts are valid, the string is balanced

### Code

```kotlin
package string

class CheckifaParenthesesStringCanBeValid {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Count And Say

<span id="countandsay"></span>

### Problem

**Countandsay**

**Function:** `Count And Say` takes `n` (integer) and returns **string**.



### Approach

**Solution Approach:**
1. The main function `countAndSay` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `nextSequence`, `count`

### Code

```kotlin
package string

class CountAndSay {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Count Words With A Given Prefix

<span id="countwordswithagivenprefix"></span>

### Problem

**Countwordswithagivenprefix**

**Function:** `Prefix Count` takes `words` (Array<string>), `prefix` (string) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `prefixCount` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `count`

### Code

```kotlin
package string

class CountWordsWithAGivenPrefix {
    fun prefixCount(words: Array<String>, prefix: String): Int {
        var count = 0

        for (word in words) {
            if (word.startsWith(prefix)) {
                count++
            }
        }

        return count
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

## Count Words With A Given Prefix_Trie

<span id="countwordswithagivenprefix_trie"></span>

### Problem

**Countwordswithagivenprefix Trie**

**Function:** `Prefix Count` takes `words` (Array<string>), `prefix` (string) and returns **integer**.

**Key logic:**
- Method to count the words with the given prefix
- Build the trie using the words
- Traverse the trie to find the node corresponding to the given prefix
- Method to build the trie
- Move to the child node or create a new one



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `ch`, `children`, `prefixCount`, `root`, `current`, `current`

**Execution flow:**
- Method to count the words with the given prefix
- Build the trie using the words
- Traverse the trie to find the node corresponding to the given prefix
- Method to build the trie
- Move to the child node or create a new one
- Increment prefix count for every node along the way
- Method to find the node corresponding to the last character of the prefix
- If prefix doesn't exist, return null

### Code

```kotlin
package trie

class CountWordsWithAGivenPrefix_Trie {
    data class TrieNode(
        val ch: Char = '_',
        val children: MutableMap<Char, TrieNode> = mutableMapOf(),
        var prefixCount: Int = 0
    )

    var root = TrieNode()

    // Method to count the words with the given prefix
    fun prefixCount(words: Array<String>, prefix: String): Int {
        // Build the trie using the words
        buildTrie(words, root)

        // Traverse the trie to find the node corresponding to the given prefix
        return findPrefixNode(prefix)?.prefixCount ?: 0
    }

    // Method to build the trie
    private fun buildTrie(words: Array<String>, root: TrieNode) {
        for (word in words) {
            var current = root
            for (ch in word) {
                // Move to the child node or create a new one
                current = current.children.getOrPut(ch) { TrieNode(ch) }
                current.prefixCount++  // Increment prefix count for every node along the way
            }
        }
    }

    // Method to find the node corresponding to the last character of the prefix
    private fun findPrefixNode(prefix: String): TrieNode? {
        var current = root
        for (ch in prefix) {
            current = current.children[ch] ?: return null  // If prefix doesn't exist, return null
        }
        return current
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Count Words With A Given Prefix_Trie_FP

<span id="countwordswithagivenprefix_trie_fp"></span>

### Problem

**Countwordswithagivenprefix Trie Fp**

**Function:** `Prefix Count` takes `words` (Array<string>), `prefix` (string) and returns **integer**.



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `children`, `prefixCount`, `root`

### Code

```kotlin
package trie

class CountWordsWithAGivenPrefix_Trie_FP {
    data class TrieNode(val children: MutableMap<Char, TrieNode> = mutableMapOf(), var prefixCount: Int = 0)

    private val root = TrieNode()

    fun prefixCount(words: Array<String>, prefix: String): Int {
        words.forEach { word ->
            word.fold(root) { node, ch ->
                node.children.getOrPut(ch) { TrieNode() }.apply { prefixCount++ }
            }
        }
        return prefixSearch(prefix)?.prefixCount ?: 0
    }

    private fun prefixSearch(prefix: String): TrieNode? = prefix.fold(root) { node, ch -> node.children[ch] ?: return null }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Custom Sort String

<span id="customsortstring"></span>

### Problem

**Customsortstring**

**Function:** `Custom Sort String` takes `order` (string), `s` (string) and returns **string**.



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `orderMap`

### Code

```kotlin
package string.sorting

class CustomSortString {
    fun customSortString(order: String, s: String): String {
        val orderMap = mutableMapOf<Char, Int>()
        order.forEachIndexed{ index, ch -> orderMap[ch] = index }

        return s.toCharArray().sortedBy{ ch -> orderMap[ch] ?: Int.MAX_VALUE }
            .joinToString("")
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Decode String

<span id="decodestring"></span>

### Problem

**Decodestring**

**Function:** `Decode String` takes `s` (string) and returns **string**.

**Key logic:**
- Skip the opening bracket '['
- Skip the closing bracket ']'
- Short code



### Approach

**Stack-Based Approach:**
1. Process elements left to right
2. Maintain a stack that tracks relevant previous elements
3. Pop from stack when current element breaks a monotonic property


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `index`, `result`, `ch`, `k`, `nestedDecodedString`, `index`, `result`, `num`

**Execution flow:**
- Skip the opening bracket '['
- Skip the closing bracket ']'

### Code

```kotlin
package string.stack

class DecodeString {
    private var index = 0

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
    fun decodeString1(s: String): String {
        var index = 0
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Determine If Strings Are Close

<span id="determineifstringsareclose"></span>

### Problem

**Determineifstringsareclose**

**Function:** `Close Strings` takes `word1` (string), `word2` (string) and returns **boolean**.



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `freq1`, `freq2`

### Code

```kotlin
package string.hashtable

class DetermineIfStringsAreClose {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Edit Distance

<span id="editdistance"></span>

### Problem

**Editdistance**

**Function:** `Min Distance` takes `word1` (string), `word2` (string) and returns **integer**.



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`, `state`, `insert`, `remove`, `replace`

### Code

```kotlin
package string.dynamic_programming

class EditDistance {
    private var dp = mutableMapOf<String,Int>()

    fun minDistance(word1: String, word2: String): Int {
        return minDistance(word1, word2, word1.length, word2.length)
    }

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
        fun main(args: Array<String>) {
        }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n × m) |
| **Space** | O(n) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n × m). The memoization/table stores one entry per state (O(n)).

---

## Excel Sheet To Column Number

<span id="excelsheettocolumnnumber"></span>

### Problem

**Excelsheettocolumnnumber**

**Function:** `Title To Number` takes `columnTitle` (string) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `titleToNumber` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `base`, `sum`

### Code

```kotlin
package string

class ExcelSheetToColumnNumber {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Find All Anagrams

<span id="findallanagrams"></span>

### Problem

**Findallanagrams**

**Function:** `Find Anagrams` takes `s` (string), `p` (string) and returns **List**.

**Key logic:**
- Initialize frequency counts for p and the first window of s
- Compare the initial window and check every subsequent window
- Add new character to the window
- Remove the old character from the window



### Approach

**Solution Approach:**
1. The main function `findAnagrams` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`, `pCount`, `sCount`

**Execution flow:**
- Initialize frequency counts for p and the first window of s
- Compare the initial window and check every subsequent window
- Add new character to the window
- Remove the old character from the window

### Code

```kotlin
package string.sliding_window

class FindAllAnagrams {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Findtheindexofthefirstoccurrenceina String

<span id="findtheindexofthefirstoccurrenceina_string"></span>

### Problem

**Findtheindexofthefirstoccurrenceina String**

**Function:** `Str Str` takes `haystack` (string), `needle` (string) and returns **integer**.

**Key logic:**
- If the needle is empty, return 0
- Use 'to' to assign both m and n in one line
- Step 1: Build the LPS array for the needle
- Step 2: Search for the needle in the haystack using KMP algorithm
- Pairing to initialize indices for haystack and needle



### Approach

**Stack-Based Approach:**
1. Process elements left to right
2. Maintain a stack that tracks relevant previous elements
3. Pop from stack when current element breaks a monotonic property


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `lps`, `lps`

**Execution flow:**
- If the needle is empty, return 0
- Use 'to' to assign both m and n in one line
- Step 1: Build the LPS array for the needle
- Step 2: Search for the needle in the haystack using KMP algorithm
- Pairing to initialize indices for haystack and needle
- Characters match
- Mismatch after some matches, use LPS array to skip ahead
- No matches yet, move to the next character in the haystack

### Code

```kotlin
package string.pattern_matching

import oracle.net.aso.m

class `FindTheIndexofTheFirstOccurrenceIna String` {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Find The Index Of The First Occurrence In String_Rabin Karp

<span id="findtheindexofthefirstoccurrenceina_string_rabinkarp"></span>

### Problem

**Findtheindexofthefirstoccurrenceina String Rabinkarp**

**Function:** `Str Str` takes `haystack` (string), `needle` (string) and returns **integer**.

**Key logic:**
- Precompute needle hash and initial window hash
- Early check for match at index 0
- Slide the window and update hash
- Remove leftmost character and add new character
- Check for match



### Approach

**Stack-Based Approach:**
1. Process elements left to right
2. Maintain a stack that tracks relevant previous elements
3. Pop from stack when current element breaks a monotonic property


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `base`, `mod`, `m`, `targetHash`, `windowHash`, `power`, `startIndex`

**Execution flow:**
- Precompute needle hash and initial window hash
- Early check for match at index 0
- Slide the window and update hash
- Remove leftmost character and add new character
- Check for match

### Code

```kotlin
package string.pattern_matching

import oracle.net.aso.m

class FindTheIndexOfTheFirstOccurrenceInString_RabinKarp {
    fun strStr(haystack: String, needle: String): Int {
        if (needle.isEmpty()) return 0
        if (haystack.length < needle.length) return -1

        val base = 26
        val mod = 1_000_000_007
        val m = needle.length
        var targetHash = 0L
        var windowHash = 0L
        var power = 1L

        // Precompute needle hash and initial window hash
        for (i in 0 until m) {
            targetHash = (targetHash * base + charValue(needle[i])) % mod
            windowHash = (windowHash * base + charValue(haystack[i])) % mod
            if (i < m - 1) power = (power * base) % mod
        }

        // Early check for match at index 0
        if (windowHash == targetHash && matches(haystack, needle, 0)) {
            return 0
        }

        // Slide the window and update hash
        for (i in m until haystack.length) {
            // Remove leftmost character and add new character
            windowHash = (windowHash - charValue(haystack[i - m]) * power % mod + mod) % mod
            windowHash = (windowHash * base + charValue(haystack[i])) % mod

            // Check for match
            val startIndex = i - m + 1
            if (windowHash == targetHash && matches(haystack, needle, startIndex)) {
                return startIndex
            }
        }

        return -1
    }

    private fun charValue(c: Char): Int = c - 'a'

    private fun matches(text: String, pattern: String, start: Int): Boolean {
        for (i in pattern.indices) {
            if (text[start + i] != pattern[i]) return false
        }
        return true
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

## Find Unique Binary String

<span id="finduniquebinarystring"></span>

### Problem

**Finduniquebinarystring**

**Function:** `Find Different Binary String` takes `nums` (Array<string>) and returns **string**.

**Key logic:**
- Cantor’s Diagonalization Trick



### Approach

**Solution Approach:**
1. The main function `findDifferentBinaryString` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `n`, `sb`

**Execution flow:**
- Cantor’s Diagonalization Trick

### Code

```kotlin
package string

// Cantor’s Diagonalization Trick
class FindUniqueBinaryString {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Generate Parantheses

<span id="generateparantheses"></span>

### Problem

**Generateparantheses**

**Function:** `Generate Parenthesis` takes `n` (integer) and returns **List**.

**Key logic:**
- backtrack



### Approach

**Solution Approach:**
1. The main function `generateParenthesis` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `result`

**Execution flow:**

### Code

```kotlin
package string.backtracking

import java.lang.StringBuilder

class GenerateParantheses {
    fun generateParenthesis(n: Int): List<String> {
        val result = mutableListOf<String>()
        generate(n, n, StringBuilder(), result)
        return result
    }

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Goat Latin

<span id="goatlatin"></span>

### Problem

**Goatlatin**

**Function:** `To Goat Latin` takes `sentence` (string) and returns **string**.

**Key logic:**
- Define a set of vowels for faster lookup
- Process the sentence word by word
- Check if the word starts with a vowel
- If the word starts with a vowel, append "ma" and the appropriate number of 'a's
- If the word starts with a consonant, move the first letter to the end, append "ma", and the appropriate number of 'a's



### Approach

**Solution Approach:**
1. The main function `toGoatLatin` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `vowels`

**Execution flow:**
- Define a set of vowels for faster lookup
- Process the sentence word by word
- Check if the word starts with a vowel
- If the word starts with a vowel, append "ma" and the appropriate number of 'a's
- If the word starts with a consonant, move the first letter to the end, append "ma", and the appropriate number of 'a's
- Join the words back into a single string

### Code

```kotlin
package string

class GoatLatin {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Greatest Common Divisor Of Strings

<span id="greatestcommondivisorofstrings"></span>

### Problem

**Greatestcommondivisorofstrings**

**Function:** `Gcd` takes `a` (integer), `b` (integer) and returns **integer**.

**Key logic:**
- Dhoyasha Foggy I didn't understand.



### Approach

**Solution Approach:**
1. The main function `gcd` processes the input
2. Uses helper functions: gcdOfStrings

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `gcdLength`

**Execution flow:**
- Dhoyasha Foggy I didn't understand.

### Code

```kotlin
package string

class GreatestCommonDivisorOfStrings {
    fun gcd(a: Int, b: Int): Int {
        return when {
            a == b -> a
            a > b -> gcd(a - b , b)
            else -> gcd(a, b - a)
        }
    }

    fun gcdOfStrings(str1: String, str2: String): String {
        // Dhoyasha Foggy I didn't understand.
        if ((str1 + str2) != (str2 + str1))
            return ""

        val gcdLength = gcd(str1.length, str2.length)

        return str1.substring(0, gcdLength)
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

## Group Anagrams

<span id="groupanagrams"></span>

### Problem

**Groupanagrams**

**Function:** `Group Anagrams` takes `strs` (Array<string>) and returns **List**.

**Key logic:**
- Using List<Int> as the key
- Count the frequency of each character
- Return the list of grouped anagrams



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `anagramMap`, `count`

**Execution flow:**
- Using List<Int> as the key
- Count the frequency of each character
- Return the list of grouped anagrams

### Code

```kotlin
package string

class GroupAnagrams {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Group Shifted Strings

<span id="groupshiftedstrings"></span>

### Problem

**Groupshiftedstrings**

**Function:** `Group Strings` takes `strings` (Array<string>) and returns **List**.



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `map`, `key`

### Code

```kotlin
package string.hashtable

class GroupShiftedStrings {
    fun groupStrings(strings: Array<String>): List<List<String>> {
        val map = mutableMapOf<String, MutableList<String>>()

        for (str in strings) {
            val key = getKey(str)
            map.computeIfAbsent(key) { mutableListOf() }.add(str)
        }

        return map.values.toList()
    }

    private fun getKey(str: String): String {
        return buildString {
            for (i in 1 until str.length) {
                append( ((str[i] - str[i - 1] + 26) % 26).toString() )
            }
        }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Interleaving String

<span id="interleavingstring"></span>

### Problem

**Interleavingstring**

**Function:** `Is Interleave` takes `s1` (string), `s2` (string), `s3` (string) and returns **boolean**.



### Approach

**Top-Down DP (Memoization) Approach:**
1. Define a recursive function that explores all possibilities
2. Cache results in a table/dictionary to avoid redundant work
3. The state is defined by the function parameters that change between calls


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `memo`, `k`, `result`

### Code

```kotlin
package string.dynamic_programming

class InterleavingString {
    fun isInterleave(s1: String, s2: String, s3: String): Boolean {
        if (s1.length + s2.length != s3.length) return false

        val memo = mutableMapOf<Pair<Int, Int>, Boolean>()

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n × m) |
| **Space** | O(n) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n × m). The memoization/table stores one entry per state (O(n)).

---

## Isomorphic String

<span id="isomorphicstring"></span>

### Problem

**Isomorphicstring**

**Function:** `Encode` takes `s` (string) and returns **string**.



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `map`, `sb`, `code`

### Code

```kotlin
package string

class IsomorphicString {
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

    fun isIsomorphic(s: String, t: String): Boolean {
        return encode(s) == encode(t)
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Is Subsequence

<span id="issubsequence"></span>

### Problem

**Issubsequence**

**Function:** `Is Subsequence` takes `s` (string), `t` (string) and returns **boolean**.

**Key logic:**
- Match found



### Approach

**Solution Approach:**
1. The main function `isSubsequence` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `i`, `j`

**Execution flow:**
- Match found

### Code

```kotlin
package string

class IsSubsequence {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Length Of Last Word

<span id="lengthoflastword"></span>

### Problem

**Lengthoflastword**

**Function:** `Length Of Last Word` takes `s` (string) and returns **integer**.

**Key logic:**
- skip trailing spaces



### Approach

**Solution Approach:**
1. The main function `lengthOfLastWord` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `i`, `len`

**Execution flow:**
- skip trailing spaces

### Code

```kotlin
package string

class LengthOfLastWord {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Longest Common Prefix

<span id="longestcommonprefix"></span>

### Problem

**Longestcommonprefix**

**Function:** `Longest Common Prefix` takes `strs` (Array<string>) and returns **string**.

**Key logic:**
- Use the first string as the reference
- Compare this character with the corresponding character in all other strings
- If the current string is shorter or the characters don't match, return the prefix so far
- If no mismatch is found, the entire first string is the common prefix



### Approach

**Solution Approach:**
1. The main function `longestCommonPrefix` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `char`

**Execution flow:**
- Use the first string as the reference
- Compare this character with the corresponding character in all other strings
- If the current string is shorter or the characters don't match, return the prefix so far
- If no mismatch is found, the entire first string is the common prefix

### Code

```kotlin
package string

class LongestCommonPrefix {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Longest Common Subsequence

<span id="longestcommonsubsequence"></span>

### Problem

**Longestcommonsubsequence**

**Function:** `Lcs` takes `str1` (string), `str2` (string) and returns **integer**.

**Key logic:**
- Print in reverse order



### Approach

**Solution Approach:**
1. The main function `lcs` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `M`

**Execution flow:**
- Print in reverse order

### Code

```kotlin
package string.dynamic_programming

class LongestCommonSubsequence {
    companion object {
        private lateinit var M: Array<IntArray>

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
        fun main(args: Array<String>) {
            println(lcs("abcxgzggmn", "acttvvmnvt"))
            printLCS("acttvvmnvt", "abcxgzggmn".length, "acttvvmnvt".length) // Print in reverse order
        }
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

## Longest Common Substring

<span id="longestcommonsubstring"></span>

### Problem

**Longestcommonsubstring**



### Approach



### Code Walkthrough

Let's trace through the code to understand how it processes the input:

### Code

```kotlin
package string.dynamic_programming

class LongestCommonSubstring {
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(1) space comes from the auxiliary data structures used.

---

## Longest Palidnromic Substring

<span id="longestpalidnromicsubstring"></span>

### Problem

**Longestpalidnromicsubstring**

**Function:** `Longest Palindrome` takes `s` (string) and returns **string**.

**Key logic:**
- Helper function to expand around the center
- Return the length of the palindrome
- Check for odd length palindrome (center is s[i])
- Check for even length palindrome (center is between s[i] and s[i + 1])
- Calculate the start of the palindrome



### Approach

**Solution Approach:**
1. The main function `longestPalindrome` processes the input
2. Uses helper functions: expandAroundCenter

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `start`, `maxLength`, `l`, `r`, `len1`, `len2`, `len`

**Execution flow:**
- Helper function to expand around the center
- Return the length of the palindrome
- Check for odd length palindrome (center is s[i])
- Check for even length palindrome (center is between s[i] and s[i + 1])
- Calculate the start of the palindrome

### Code

```kotlin
package string

class LongestPalidnromicSubstring {
    fun longestPalindrome(s: String): String {
        if (s.isEmpty()) return ""

        var start = 0
        var maxLength = 1

        // Helper function to expand around the center
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Longest Palindromic Subsequence

<span id="longestpalindromicsubsequence"></span>

### Problem

**Longestpalindromicsubsequence**

**Function:** `Longest Palindrome Subseq` takes `s` (string) and returns **integer**.

**Key logic:**
- Value already cached



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`, `end`

**Execution flow:**
- Value already cached

### Code

```kotlin
package string.dynamic_programming

class LongestPalindromicSubsequence {
    fun longestPalindromeSubseq(s: String): Int {
        val dp = Array(s.length) { IntArray(s.length) }

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n × m) |
| **Space** | O(n) |

**Analysis:**

The DP table has dimensions proportional to the input size, giving O(n) space. Each cell requires O(1) or O(n) work, totaling O(n × m).

---

## Longest Palindromic Subsequence_Bottom Up

<span id="longestpalindromicsubsequence_bottomup"></span>

### Problem

**Longestpalindromicsubsequence Bottomup**

**Function:** `Longest Palindrome Subseq` takes `s` (string) and returns **integer**.

**Key logic:**
- Bottom-up fill the dp table for substrings of increasing length
- Iterate over all substring lengths
- Iterate over all possible start indices
- Calculate the end index of the substring
- Base case: single character is a palindrome of length 1



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `n`, `dp`, `end`

**Execution flow:**
- Bottom-up fill the dp table for substrings of increasing length
- Iterate over all substring lengths
- Iterate over all possible start indices
- Calculate the end index of the substring
- Base case: single character is a palindrome of length 1
- Palindrome formed by adding the two matching characters
- Max of ignoring one end
- The result is stored in dp[0][n-1] (the entire string)

### Code

```kotlin
package string.dynamic_programming

class LongestPalindromicSubsequence_BottomUp {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

The DP table has dimensions proportional to the input size, giving O(n²) space. Each cell requires O(1) or O(n) work, totaling O(n³).

---

## Longest Repeating Character Replacement

<span id="longestrepeatingcharacterreplacement"></span>

### Problem

**Longestrepeatingcharacterreplacement**

**Function:** `Character Replacement` takes `s` (string), `k` (integer) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `characterReplacement` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `count`, `maxLength`, `left`, `maxCount`, `char`

### Code

```kotlin
package sliding_window

class LongestRepeatingCharacterReplacement {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Longest String Chain

<span id="longeststringchain"></span>

### Problem

**Longeststringchain**

**Function:** `Longest Str Chain` takes `words` (Array<string>) and returns **integer**.

**Key logic:**
- Sort words by length
- Default length of chain ending at word is 1
- Remove one character



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`, `maxLen`, `prev`

**Execution flow:**
- Sort words by length
- Default length of chain ending at word is 1
- Remove one character

### Code

```kotlin
package string.dynamic_programming

class LongestStringChain {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n³). The memoization/table stores one entry per state (O(n²)).

---

## Maximum Lengthofa Concatenated Stringwith Unique Characters

<span id="maximumlengthofaconcatenatedstringwithuniquecharacters"></span>

### Problem

**Maximumlengthofaconcatenatedstringwithuniquecharacters**

**Function:** `Max Length` takes `arr` (List<string>) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `maxLength` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `maxLen`, `uniqueStrings`, `str`, `newMask`, `canAdd`, `bit`

### Code

```kotlin
package string

class MaximumLengthofaConcatenatedStringwithUniqueCharacters {
    fun maxLength(arr: List<String>): Int {
        var maxLen = 0
        val uniqueStrings = arr.filter { it.toCharArray().toSet().size == it.length }

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Maximum Value Of A String Is An Array

<span id="maximumvalueofastringisanarray"></span>

### Problem

**Maximumvalueofastringisanarray**

**Function:** `Maximum Value` takes `strs` (Array<string>) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `maximumValue` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `numericValue`

### Code

```kotlin
package string

class MaximumValueOfAStringIsAnArray {
    fun maximumValue(strs: Array<String>): Int {
        return strs.maxOf {
            val numericValue = it.toIntOrNull()
            numericValue?: it.length
        }
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

## Merge String Alternatively

<span id="mergestringalternatively"></span>

### Problem

**Mergestringalternatively**

**Function:** `Merge Alternately` takes `word1` (string), `word2` (string) and returns **string**.



### Approach

**Solution Approach:**
1. The main function `mergeAlternately` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `mergedString`

### Code

```kotlin
package string

class MergeStringAlternatively {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Minimum Deletion To Make Character Frequencies Unique

<span id="minimumdeletiontomakecharacterfrequenciesunique"></span>

### Problem

**Minimumdeletiontomakecharacterfrequenciesunique**

**Function:** `Min Deletions` takes `s` (string) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `minDeletions` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `freq`, `seen`, `deletions`, `currentFreq`

### Code

```kotlin
package string

class MinimumDeletionToMakeCharacterFrequenciesUnique {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Minimum Window Substring

<span id="minimumwindowsubstring"></span>

### Problem

**Minimumwindowsubstring**

**Function:** `Min Window` takes `s` (string), `t` (string) and returns **string**.

**Key logic:**
- Return early if either string is empty
- Frequency map for characters in t (required characters)
- Frequency map for the current window in s
- Track the number of characters matched from the required set
- Destructuring initialization for left and right pointers



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `required`, `window`, `matched`, `rightChar`, `currentLength`, `leftChar`

**Execution flow:**
- Return early if either string is empty
- Frequency map for characters in t (required characters)
- Frequency map for the current window in s
- Track the number of characters matched from the required set
- Destructuring initialization for left and right pointers
- Initialize minLength and minStart in a single line
- Sliding window logic
- Expand the window by moving the right pointer

### Code

```kotlin
package string.sliding_window

class MinimumWindowSubstring {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Remove All Adjacent Duplicates In String

<span id="removealladjacentduplicatesinstring"></span>

### Problem

**Removealladjacentduplicatesinstring**

**Function:** `Remove Duplicates` takes `s` (string) and returns **string**.



### Approach

**Stack-Based Approach:**
1. Process elements left to right
2. Maintain a stack that tracks relevant previous elements
3. Pop from stack when current element breaks a monotonic property


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `stack`

### Code

```kotlin
package string.stack

class RemoveAllAdjacentDuplicatesInString {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Reverse Words In String

<span id="reversewordsinstring"></span>

### Problem

**Reversewordsinstring**

**Function:** `Reverse Words` takes `s` (string) and returns **string**.

**Key logic:**
- Two pointers



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `words`

**Execution flow:**
- Two pointers

### Code

```kotlin
package string

class ReverseWordsInString {
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

    fun swap(nums: MutableList<String>, i: Int, j: Int) {
        nums[j] = nums[i].also { nums[i] = nums[j] }
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Shortest Common Supersequence

<span id="shortestcommonsupersequence"></span>

### Problem

**Shortestcommonsupersequence**

**Function:** `Shortest Common Supersequence` takes `X` (string), `Y` (string) and returns **string**.

**Key logic:**
- Add remaining characters from X or Y
- Reverse the result and return as string
- abc, axyzabc, yzmnbc
- yzmnbcaxyzabc
- a -> b -> c



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`, `scs`

**Execution flow:**
- Add remaining characters from X or Y
- Reverse the result and return as string
- abc, axyzabc, yzmnbc
- yzmnbcaxyzabc
- a -> b -> c
- a -> x -> y -> x -> (a -> b -> c)
- y -> z -> m -> n -> b -> c

### Code

```kotlin
package string.dynamic_programming

class ShortestCommonSupersequence {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

The DP table has dimensions proportional to the input size, giving O(n²) space. Each cell requires O(1) or O(n) work, totaling O(n³).

---

## Simplify Path

<span id="simplifypath"></span>

### Problem

**Simplifypath**

**Function:** `Simplify Path` takes `path` (string) and returns **string**.

**Key logic:**
- Split the path by "/"
- Initialize a mutable list to store valid directory names
- Ignore empty or current directory tokens
- Pop from the list if it's not empty (go back to the parent directory)
- Push valid directory names onto the list



### Approach

**Stack-Based Approach:**
1. Process elements left to right
2. Maintain a stack that tracks relevant previous elements
3. Pop from stack when current element breaks a monotonic property


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `tokens`, `stack`

**Execution flow:**
- Split the path by "/"
- Initialize a mutable list to store valid directory names
- Ignore empty or current directory tokens
- Pop from the list if it's not empty (go back to the parent directory)
- Push valid directory names onto the list
- Rebuild the simplified path from the list

### Code

```kotlin
package string.stack

class SimplifyPath {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## String Compression

<span id="stringcompression"></span>

### Problem

**Stringcompression**

**Function:** `Compress` takes `chars` (CharArray) and returns **integer**.

**Key logic:**
- Data Compression Algorithm



### Approach

**Solution Approach:**
1. The main function `compress` processes the input
2. Uses helper functions: string_compression_inline

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `count`, `sb`, `partitionLength`, `i`, `currentChar`, `count`

**Execution flow:**
- Data Compression Algorithm

### Code

```kotlin
package string

// Data Compression Algorithm

class StringCompression {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## String Compression_II

<span id="stringcompression_ii"></span>

### Problem

**Stringcompression Ii**

**Function:** `Compressed String` takes `word` (string) and returns **string**.



### Approach

**Solution Approach:**
1. The main function `compressedString` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `compressed`, `i`, `ch`, `count`

### Code

```kotlin
package string

class StringCompression_II {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Unique Length3 Palindromic Subsequence

<span id="uniquelength3palindromicsubsequence"></span>

### Problem

**Uniquelength3Palindromicsubsequence**

**Function:** `Count Palindromic Subsequence` takes `s` (string) and returns **integer**.

**Key logic:**
- Step 1: Record positions of each character
- Step 2: Process each character's occurrences
- Skip if there's no room between the first and last occurrence
- Count distinct characters between first and last occurrence



### Approach

**Hash Map Approach:**
1. Use a hash map for O(1) average lookups
2. Store key-value pairs where the key enables fast retrieval
3. Trade off memory for time


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `charPositions`, `count`, `start`, `end`, `distinctChars`

**Execution flow:**
- Step 1: Record positions of each character
- Step 2: Process each character's occurrences
- Skip if there's no room between the first and last occurrence
- Count distinct characters between first and last occurrence

### Code

```kotlin
package string.hashtable

class UniqueLength3PalindromicSubsequence {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(n) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n). The O(n) space comes from the auxiliary data structures used.

---

## Unique Substring With Equal Digit Frequency

<span id="uniquesubstringwithequaldigitfrequency"></span>

### Problem

**Uniquesubstringwithequaldigitfrequency**

**Function:** `Equal Digit Frequency` takes `s` (string) and returns **integer**.

**Key logic:**
- Precompute prefix frequency arrays
- Iterate over all possible substrings



### Approach

**Solution Approach:**
1. The main function `equalDigitFrequency` processes the input
2. Uses helper functions: hasEqualFrequency

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `n`, `uniqueSubstrings`, `prefixFreq`, `freq`, `uniqueFreq`

**Execution flow:**
- Precompute prefix frequency arrays
- Iterate over all possible substrings

### Code

```kotlin
package string.hashtable

class UniqueSubstringWithEqualDigitFrequency {
    fun equalDigitFrequency(s: String): Int {
        val n = s.length
        val uniqueSubstrings = mutableSetOf<String>()

        // Precompute prefix frequency arrays
        val prefixFreq = Array(n + 1) { IntArray(10) }
        for (i in 1..n) {
            for (d in 0..9) {
                prefixFreq[i][d] = prefixFreq[i - 1][d]
            }
            prefixFreq[i][s[i - 1] - '0']++
        }

        // Iterate over all possible substrings
        for (i in 0 until n) {
            for (j in i + 1..n) {
                val freq = IntArray(10)
                for (d in 0..9) {
                    freq[d] = prefixFreq[j][d] - prefixFreq[i][d]
                }

                if (hasEqualFrequency(freq)) {
                    uniqueSubstrings.add(s.substring(i, j))
                }
            }
        }

        return uniqueSubstrings.size
    }

    private fun hasEqualFrequency(freq: IntArray): Boolean {
        var uniqueFreq = -1
        for (count in freq) {
            if (count > 0) {
                if (uniqueFreq == -1) {
                    uniqueFreq = count
                } else if (count != uniqueFreq) {
                    return false
                }
            }
        }
        return true
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

## Valid Anagram

<span id="validanagram"></span>

### Problem

**Validanagram**

**Function:** `Is Anagram` takes `s` (string), `t` (string) and returns **boolean**.

**Key logic:**
- Check if all counts are zero



### Approach

**Solution Approach:**
1. The main function `isAnagram` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `charCount`

**Execution flow:**
- Check if all counts are zero

### Code

```kotlin
package string

class ValidAnagram {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Valid Number

<span id="validnumber"></span>

### Problem

**Validnumber**

**Function:** `Is Number` takes `s` (string) and returns **boolean**.

**Key logic:**
- Initialize variables
- Remove leading/trailing spaces
- Ensure digits appear after 'e'
- Can't have multiple dots or dots after 'e'
- Can't have multiple 'e' or 'e' without preceding number



### Approach

**Solution Approach:**
1. The main function `isNumber` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `str`, `c`

**Execution flow:**
- Initialize variables
- Remove leading/trailing spaces
- Ensure digits appear after 'e'
- Can't have multiple dots or dots after 'e'
- Can't have multiple 'e' or 'e' without preceding number
- Reset this to ensure we validate digits after 'e'
- Sign only valid at start or after 'e'
- Invalid character

### Code

```kotlin
package string

class ValidNumber {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Valid Palindrome

<span id="validpalindrome"></span>

### Problem

**Validpalindrome**

**Function:** `Is Palindrome` takes `s` (string) and returns **boolean**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `isAlpha`

### Code

```kotlin
package string

class ValidPalindrome {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Valid Palindrome_II

<span id="validpalindrome_ii"></span>

### Problem

**Validpalindrome Ii**

**Function:** `Valid Palindrome` takes `s` (string) and returns **boolean**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `left`, `right`, `left`, `right`

### Code

```kotlin
package string

class ValidPalindrome_II {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Valid Palindrome_III

<span id="validpalindrome_iii"></span>

### Problem

**Validpalindrome Iii**

**Function:** `Is Valid Palindrome` takes `s` (string), `k` (integer) and returns **boolean**.

**Key logic:**
- Calculate the length of the longest palindromic subsequence
- Check if the number of deletions required is less than or equal to k



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `dp`, `end`, `lpsLength`

**Execution flow:**
- Calculate the length of the longest palindromic subsequence
- Check if the number of deletions required is less than or equal to k

### Code

```kotlin
package string.dynamic_programming

class ValidPalindrome_III {
    fun isValidPalindrome(s: String, k: Int): Boolean {
        val dp = Array(s.length) { IntArray(s.length) { 0 } }

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n × m) |
| **Space** | O(n) |

**Analysis:**

The DP table has dimensions proportional to the input size, giving O(n) space. Each cell requires O(1) or O(n) work, totaling O(n × m).

---

## Valid Palindrome_III_Space Optimized

<span id="validpalindrome_iii_spaceoptimized"></span>

### Problem

**Validpalindrome Iii Spaceoptimized**

**Function:** `Is Valid Palindrome` takes `s` (string), `k` (integer) and returns **boolean**.

**Key logic:**
- Initialize with 1 because each character is a palindrome of length 1
- Stores the value of dp[i+1][j-1] from the 2D DP approach
- Store the current dp[j] before updating it
- If characters match, add 2 to the LPS length of the inner substring
- Otherwise, take the maximum of excluding s[i] or s[j]



### Approach

**Bottom-Up DP (Tabulation) Approach:**
1. Define the DP table dimensions based on state variables
2. Initialize base cases
3. Fill the table iteratively from smallest to largest subproblems
4. The answer is in dp[final_state]


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `n`, `dp`, `prev`, `temp`, `lpsLength`

**Execution flow:**
- Initialize with 1 because each character is a palindrome of length 1
- Stores the value of dp[i+1][j-1] from the 2D DP approach
- Store the current dp[j] before updating it
- If characters match, add 2 to the LPS length of the inner substring
- Otherwise, take the maximum of excluding s[i] or s[j]
- Update prev for the next iteration
- The length of the LPS for the entire string

### Code

```kotlin
package string.dynamic_programming

class ValidPalindrome_III_SpaceOptimized {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Analysis:**

We compute each state exactly once and each state takes O(1) to O(n) transitions, giving O(n³). The memoization/table stores one entry per state (O(n²)).

---

## Validate IP Address

<span id="validateipaddress"></span>

### Problem

**Validateipaddress**

**Function:** `Valid Ipaddress` takes `queryIP` (string) and returns **string**.



### Approach

**Solution Approach:**
1. The main function `validIPAddress` processes the input
2. Uses helper functions: isValidIPv4, isValidIPv6

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `segments`, `segments`

### Code

```kotlin
package string

class ValidateIPAddress {
    fun validIPAddress(queryIP: String): String {
        return when {
            isValidIPv4(queryIP) -> "IPv4"
            isValidIPv6(queryIP) -> "IPv6"
            else -> "Neither"
        }
    }

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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Valid Word Abbreviation

<span id="validwordabbreviation"></span>

### Problem

**Validwordabbreviation**

**Function:** `Valid Word Abbreviation` takes `word` (string), `abbr` (string) and returns **boolean**.

**Key logic:**
- Leading zero check



### Approach

**Solution Approach:**
1. The main function `validWordAbbreviation` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `i`, `j`, `count`

**Execution flow:**
- Leading zero check

### Code

```kotlin
package string

class ValidWordAbbreviation {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Maximum Numberof Vowelsin Substringof Given Length

<span id="maximumnumberofvowelsinsubstringofgivenlength"></span>

### Problem

**Maximumnumberofvowelsinsubstringofgivenlength**

**Function:** `Max Vowels` takes `s` (string), `k` (integer) and returns **integer**.



### Approach

**Solution Approach:**
1. The main function `maxVowels` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `vowels`

### Code

```kotlin
package string.sliding_window

class MaximumNumberofVowelsinSubstringofGivenLength {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Permutations In String

<span id="permutationsinstring"></span>

### Problem

**Permutationsinstring**

**Function:** `Check Inclusion` takes `s1` (string), `s2` (string) and returns **boolean**.



### Approach

**Solution Approach:**
1. The main function `checkInclusion` processes the input

### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `targetFreq`, `windowFreq`

### Code

```kotlin
package string.hashtable

class PermutationsInString {
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

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) |
| **Space** | O(1) |

**Analysis:**

The algorithm processes each element a constant number of times, giving O(n²). The O(1) space comes from the auxiliary data structures used.

---

## Reverse Vowel Of String

<span id="reversevowelofstring"></span>

### Problem

**Reversevowelofstring**

**Function:** `Reverse Vowels` takes `s` (string) and returns **string**.



### Approach

**Binary Search Approach:**
1. Define the search space and feasibility predicate
2. Repeatedly halve the search range until finding the optimal value
3. The predicate must be monotonic for binary search to work


### Code Walkthrough

Let's trace through the code to understand how it processes the input:

**Key variables:** `vowels`, `result`

### Code

```kotlin
package string

class ReverseVowelOfString {
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

    fun swap(s: StringBuilder, i: Int, j: Int) {
        s[j] = s[i].also { s[i] = s[j]}
    }
}
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

**Analysis:**

Each iteration halves the search space, giving O(log n) time. Only constant extra space is needed beyond the input (O(1)).

---

## Key Takeaways

1. **Core pattern recognition** — String problems use: two pointers, sliding window, DP (LCS, edit distance), KMP/Rabin-Karp for pattern matching, and trie for prefix search.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

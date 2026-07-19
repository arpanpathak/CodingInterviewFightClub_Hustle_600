---
layout: chapter
title: "String Matching - KMP, Rabin-Karp & More"
chapter_number: 10
chapter_title: "String Matching"
toc: true
prev_chapter:
  url: "/chapters/09-disjoint-set-union"
  title: "Disjoint Set Union - Union-Find"
next_chapter:
  url: "/chapters/11-backtracking"
  title: "Backtracking - Exhaustive Search Mastery"
---

# String Matching: Pattern Recognition at Scale

## Complete Problem Set (45+ problems)

### String General (28 problems)
| # | Problem | File |
|---|---------|------|
| 1 | Valid Palindrome | string/ValidPalindrome.kt |
| 2 | Valid Palindrome II | string/ValidPalindrome_II.kt |
| 3 | Valid Anagram | string/ValidAnagram.kt |
| 4 | Group Anagrams | string/GroupAnagrams.kt |
| 5 | Longest Common Prefix | string/LongestCommonPrefix.kt |
| 6 | Longest Palindromic Substring | string/LongestPalidnromicSubstring.kt |
| 7 | Reverse Words in String | string/ReverseWordsInString.kt |
| 8 | Reverse Vowels | string/ReverseVowelOfString.kt |
| 9 | String Compression | string/StringCompression.kt |
| 10 | String Compression II | string/StringCompression_II.kt |
| 11 | Count and Say | string/CountAndSay.kt |
| 12 | Is Subsequence | string/IsSubsequence.kt |
| 13 | Isomorphic Strings | string/IsomorphicString.kt |
| 14 | Valid Number | string/ValidNumber.kt |
| 15 | Valid IP Address | string/ValidateIPAddress.kt |
| 16 | Valid Word Abbreviation | string/ValidWordAbbreviation.kt |
| 17 | Length of Last Word | string/LengthOfLastWord.kt |
| 18 | Excel Sheet Column Number | string/ExcelSheetToColumnNumber.kt |
| 19 | Greatest Common Divisor of Strings | string/GreatestCommonDivisorOfStrings.kt |
| 20 | Merge Strings Alternately | string/MergeStringAlternatively.kt |
| 21 | Find Unique Binary String | string/FindUniqueBinaryString.kt |
| 22 | Goat Latin | string/GoatLatin.kt |
| 23 | Break a Palindrome | string/BreakAPalindrome.kt |
| 24 | Min Deletions Unique Freq | string/MinimumDeletionToMakeCharacterFrequenciesUnique.kt |

### Pattern Matching (2 problems)
| # | Problem | File |
|---|---------|------|
| 25 | Find First Occurrence (KMP) | string/pattern_matching/FindTheIndexofTheFirstOccurrenceInaString.kt |
| 26 | Find First Occurrence (Rabin-Karp) | string/pattern_matching/FindTheIndexofTheFirstOccurrenceInaString_RabinKarp.kt |

### String DP (11 problems)
| # | Problem | File |
|---|---------|------|
| 27 | Longest Common Subsequence | string/dynamic_programming/LongestCommonSubsequence.kt |
| 28 | Longest Common Substring | string/dynamic_programming/LongestCommonSubstring.kt |
| 29 | Edit Distance | string/dynamic_programming/EditDistance.kt |
| 30 | Longest Palindromic Subsequence | string/dynamic_programming/LongestPalindromicSubsequence.kt |
| 31 | Interleaving String | string/dynamic_programming/InterleavingString.kt |
| 32 | Regular Expression Matching | string/dynamic_programming/RegularExpressionMatching.kt |
| 33 | Shortest Common Supersequence | string/dynamic_programming/ShortestCommonSupersequence.kt |
| 34 | Longest String Chain | string/dynamic_programming/LongestStringChain.kt |
| 35 | Valid Palindrome III | string/dynamic_programming/ValidPalindrome_III.kt |

### String Hash Table (5 problems)
| # | Problem | File |
|---|---------|------|
| 36 | Word Break II | hashtable/WorkBreak_II.kt |
| 37 | Word Break I (DP) | hashtable/WorlBreak_I_DP.kt |

### String Backtracking (1 problem)
| # | Problem | File |
|---|---------|------|
| 38 | Restore IP Addresses | string/backtracking/restoreIpAddresses.kt |

### Key Solutions

```kotlin
// Valid Palindrome
fun isPalindrome(s: String): Boolean {
    var l = 0; var r = s.lastIndex
    while (l < r) {
        while (l < r && !s[l].isLetterOrDigit()) l++
        while (l < r && !s[r].isLetterOrDigit()) r--
        if (s[l].lowercase() != s[r].lowercase()) return false
        l++; r--
    }
    return true
}

// Group Anagrams
fun groupAnagrams(strs: Array<String>): List<List<String>> {
    return strs.groupBy { String(it.toCharArray().sortedArray()) }.values.toList()
}

// Longest Common Prefix
fun longestCommonPrefix(strs: Array<String>): String {
    if (strs.isEmpty()) return ""
    var prefix = strs[0]
    for (i in 1 until strs.size) {
        while (strs[i].indexOf(prefix) != 0) prefix = prefix.dropLast(1)
    }
    return prefix
}

// Rabin-Karp
fun strStrRabinKarp(haystack: String, needle: String): Int {
    if (needle.isEmpty()) return 0
    val base = 31; val mod = 1_000_000_007L
    var needleHash = 0L; var haystackHash = 0L; var pow = 1L
    for (i in 0 until needle.length) {
        needleHash = (needleHash * base + needle[i].toLong()) % mod
        haystackHash = (haystackHash * base + haystack[i].toLong()) % mod
        if (i < needle.length - 1) pow = (pow * base) % mod
    }
    if (needleHash == haystackHash && haystack.startsWith(needle)) return 0
    for (i in 1..(haystack.length - needle.length)) {
        haystackHash = ((haystackHash - haystack[i-1].toLong() * pow % mod + mod) % mod * base + haystack[i+needle.length-1].toLong()) % mod
        if (needleHash == haystackHash && haystack.substring(i, i+needle.length) == needle) return i
    }
    return -1
}
```

---

> **Next up: [Backtracking ->](./11-backtracking.md)**

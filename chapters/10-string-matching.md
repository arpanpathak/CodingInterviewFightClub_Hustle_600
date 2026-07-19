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
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(n) |
---
## Break A Palindrome
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Checkifa Parentheses String Can Be Valid
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Count And Say
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Count Words With A Given Prefix
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Count Words With A Given Prefix_Trie
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(n) |
---
## Count Words With A Given Prefix_Trie_FP
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(n) |
---
## Custom Sort String
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(n) |
---
## Decode String
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Determine If Strings Are Close
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(n) |
---
## Edit Distance
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n × m) |
| **Space** | O(n) |
---
## Excel Sheet To Column Number
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Find All Anagrams
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Findtheindexofthefirstoccurrenceina String
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Find The Index Of The First Occurrence In String_Rabin Karp
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Find Unique Binary String
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Generate Parantheses
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Goat Latin
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Greatest Common Divisor Of Strings
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Group Anagrams
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(n) |
---
## Group Shifted Strings
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(n) |
---
## Interleaving String
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n × m) |
| **Space** | O(n) |
---
## Isomorphic String
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(n) |
---
## Is Subsequence
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Length Of Last Word
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Longest Common Prefix
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Longest Common Subsequence
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Longest Common Substring
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(1) |
---
## Longest Palidnromic Substring
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Longest Palindromic Subsequence
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n × m) |
| **Space** | O(n) |
---
## Longest Palindromic Subsequence_Bottom Up
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n³) |
| **Space** | O(n²) |
---
## Longest Repeating Character Replacement
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Longest String Chain
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n³) |
| **Space** | O(n²) |
---
## Maximum Lengthofa Concatenated Stringwith Unique Characters
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Maximum Value Of A String Is An Array
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Merge String Alternatively
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Minimum Deletion To Make Character Frequencies Unique
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Minimum Window Substring
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(n) |
---
## Remove All Adjacent Duplicates In String
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Reverse Words In String
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Shortest Common Supersequence
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n³) |
| **Space** | O(n²) |
---
## Simplify Path
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## String Compression
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## String Compression_II
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Unique Length3 Palindromic Subsequence
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n) |
| **Space** | O(n) |
---
## Unique Substring With Equal Digit Frequency
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Valid Anagram
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Valid Number
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Valid Palindrome
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Valid Palindrome_II
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Valid Palindrome_III
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n × m) |
| **Space** | O(n) |
---
## Valid Palindrome_III_Space Optimized
### Code
```kotlin
class ValidPalindrome_III_SpaceOptimized {
```
### Complexity
| Metric | Value |
| **Time** | O(n³) |
| **Space** | O(n²) |
---
## Validate IP Address
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Valid Word Abbreviation
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Maximum Numberof Vowelsin Substringof Given Length
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Permutations In String
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(n²) |
| **Space** | O(1) |
---
## Reverse Vowel Of String
### Code
```kotlin
```
### Complexity
| Metric | Value |
| **Time** | O(log n) |
| **Space** | O(1) |
---
## Key Takeaways

1. **Core pattern recognition** — String problems use: two pointers, sliding window, DP (LCS, edit distance), KMP/Rabin-Karp for pattern matching, and trie for prefix search.
2. **Practice systematically** — Work through each problem to internalize the patterns
3. **Understand why, not just how** — The explanations above focus on the reasoning, not just the code

---

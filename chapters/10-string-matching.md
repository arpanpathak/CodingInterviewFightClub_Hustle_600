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

{% include code-tabs-file.html problem="applysubstitutions" %}

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

{% include code-tabs-file.html problem="breakapalindrome" %}

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

{% include code-tabs-file.html problem="checkifaparenthesesstringcanbevalid" %}

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

{% include code-tabs-file.html problem="countandsay" %}

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

{% include code-tabs-file.html problem="countwordswithagivenprefix" %}

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

{% include code-tabs-file.html problem="countwordswithagivenprefix_trie" %}

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

{% include code-tabs-file.html problem="countwordswithagivenprefix_trie_fp" %}

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

{% include code-tabs-file.html problem="customsortstring" %}

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

{% include code-tabs-file.html problem="decodestring" %}

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

{% include code-tabs-file.html problem="determineifstringsareclose" %}

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

{% include code-tabs-file.html problem="editdistance" %}

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

{% include code-tabs-file.html problem="excelsheettocolumnnumber" %}

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

{% include code-tabs-file.html problem="findallanagrams" %}

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

{% include code-tabs-file.html problem="findtheindexofthefirstoccurrenceina_string" %}

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

{% include code-tabs-file.html problem="findtheindexofthefirstoccurrenceina_string_rabinkarp" %}

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

{% include code-tabs-file.html problem="finduniquebinarystring" %}

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

{% include code-tabs-file.html problem="generateparantheses" %}

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

{% include code-tabs-file.html problem="goatlatin" %}

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

{% include code-tabs-file.html problem="greatestcommondivisorofstrings" %}

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

{% include code-tabs-file.html problem="groupanagrams" %}

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

{% include code-tabs-file.html problem="groupshiftedstrings" %}

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

{% include code-tabs-file.html problem="interleavingstring" %}

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

{% include code-tabs-file.html problem="isomorphicstring" %}

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

{% include code-tabs-file.html problem="issubsequence" %}

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

{% include code-tabs-file.html problem="lengthoflastword" %}

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

{% include code-tabs-file.html problem="longestcommonprefix" %}

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

{% include code-tabs-file.html problem="longestcommonsubsequence" %}

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

{% include code-tabs-file.html problem="longestcommonsubstring" %}

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

{% include code-tabs-file.html problem="longestpalidnromicsubstring" %}

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

{% include code-tabs-file.html problem="longestpalindromicsubsequence" %}

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

{% include code-tabs-file.html problem="longestpalindromicsubsequence_bottomup" %}

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

{% include code-tabs-file.html problem="longestrepeatingcharacterreplacement" %}

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

{% include code-tabs-file.html problem="longeststringchain" %}

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

{% include code-tabs-file.html problem="maximumlengthofaconcatenatedstringwithuniquecharacters" %}

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

{% include code-tabs-file.html problem="maximumvalueofastringisanarray" %}

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

{% include code-tabs-file.html problem="mergestringalternatively" %}

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

{% include code-tabs-file.html problem="minimumdeletiontomakecharacterfrequenciesunique" %}

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

{% include code-tabs-file.html problem="minimumwindowsubstring" %}

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

{% include code-tabs-file.html problem="removealladjacentduplicatesinstring" %}

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

{% include code-tabs-file.html problem="reversewordsinstring" %}

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

{% include code-tabs-file.html problem="shortestcommonsupersequence" %}

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

{% include code-tabs-file.html problem="simplifypath" %}

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

{% include code-tabs-file.html problem="stringcompression" %}

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

{% include code-tabs-file.html problem="stringcompression_ii" %}

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

{% include code-tabs-file.html problem="uniquelength3palindromicsubsequence" %}

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

{% include code-tabs-file.html problem="uniquesubstringwithequaldigitfrequency" %}

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

{% include code-tabs-file.html problem="validanagram" %}

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

{% include code-tabs-file.html problem="validnumber" %}

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

{% include code-tabs-file.html problem="validpalindrome" %}

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

{% include code-tabs-file.html problem="validpalindrome_ii" %}

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

{% include code-tabs-file.html problem="validpalindrome_iii" %}

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

{% include code-tabs-file.html problem="validpalindrome_iii_spaceoptimized" %}

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

{% include code-tabs-file.html problem="validateipaddress" %}

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

{% include code-tabs-file.html problem="validwordabbreviation" %}

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

{% include code-tabs-file.html problem="maximumnumberofvowelsinsubstringofgivenlength" %}

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

{% include code-tabs-file.html problem="permutationsinstring" %}

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

{% include code-tabs-file.html problem="reversevowelofstring" %}

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

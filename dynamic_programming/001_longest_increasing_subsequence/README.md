> **Category:** Dynamic Programming  
> **Difficulty:** Medium  
> **Status:** In Progress  
> **Techniques:** Dynamic Programming

# Longest Increasing Subsequence

## Category

Dynamic Programming

## Difficulty

Medium

---

## Problem

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

---

## Examples

### Example 1

Input

nums = [10,9,2,5,3,7,101,18]

Output

4

Explanation

The longest increasing subsequence is:

[2,3,7,101]

---

### Example 2

Input

nums = [0,1,0,3,2,3]

Output

4

---

### Example 3

Input

nums = [7,7,7,7]

Output

1

---

## Approach

We'll solve this problem using Dynamic Programming.

For every position in the array, determine the length of the longest increasing subsequence ending at that position.

The final answer is the maximum value found across all positions.

---

## Complexity

Time Complexity: O(n²)

Space Complexity: O(n)

---

## Tags

- Dynamic Programming
- Arrays
- Interview
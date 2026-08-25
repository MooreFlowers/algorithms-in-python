> **Category:** Dynamic Programming
> **Difficulty:** Medium
> **Status:** Complete
> **Techniques:** Dynamic Programming

# Longest Increasing Subsequence

## Problem

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

The values in the subsequence must be **strictly increasing**, meaning duplicate values cannot extend the subsequence.

---

## Examples

### Example 1

**Input**

```text
nums = [10, 9, 2, 5, 3, 7, 101, 18]
```

**Output**

```text
4
```

**Explanation**

One longest increasing subsequence is:

```text
[2, 3, 7, 101]
```

Its length is `4`.

---

### Example 2

**Input**

```text
nums = [0, 1, 0, 3, 2, 3]
```

**Output**

```text
4
```

One longest increasing subsequence is:

```text
[0, 1, 2, 3]
```

---

### Example 3

**Input**

```text
nums = [7, 7, 7, 7]
```

**Output**

```text
1
```

Because the subsequence must be strictly increasing, equal values cannot extend it.

---

## Approach

This solution uses Dynamic Programming.

For each position in `nums`, we determine the length of the longest increasing subsequence that **ends at that specific position**.

We create a list called `notes` with the same length as `nums`:

```python
notes = [1] * len(nums)
```

Every position begins with a value of `1` because any individual number forms an increasing subsequence of length `1`.

For each `current` position, we examine every `previous` position that comes before it.

```python
for current in range(len(nums)):
    for previous in range(current):
```

If the previous value is smaller than the current value:

```python
if nums[previous] < nums[current]:
```

then the current number can extend the increasing subsequence that ends at the previous position.

We update the current position with:

```python
notes[current] = max(
    notes[current],
    notes[previous] + 1,
)
```

Using `max()` ensures that a shorter subsequence discovered later does not overwrite a longer subsequence that was already found.

After every position has been processed, each value in `notes` represents the longest increasing subsequence ending at that position.

The overall longest increasing subsequence does not necessarily end at the final position in `nums`, so the final answer is:

```python
return max(notes)
```

If the input is empty, the function returns `0`.

---

## Complexity

### Time Complexity — O(n²)

For each position in the input, the algorithm checks the positions that came before it.

As the input grows, the number of comparisons grows quadratically, resulting in **O(n²)** time complexity.

### Space Complexity — O(n)

The `notes` list contains one value for every value in the input.

As the input grows, `notes` grows proportionally with it, resulting in **O(n)** additional space.

---

## Testing

The solution includes unit tests covering:

* Empty input
* A single element
* Equal values
* A strictly increasing sequence
* A strictly decreasing sequence
* Mixed sequences

These tests verify both normal behavior and important edge cases.

---

## Tags

* Dynamic Programming
* Arrays
* Subsequences
* Interview Preparation
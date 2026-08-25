# Notes

## Core Idea

The main idea behind this solution is:

> For every position, remember the length of the longest increasing subsequence that ends at that specific position.

This lets us reuse work that has already been completed instead of rediscovering previous subsequences.

---

## Brute Force

A brute-force solution could generate every possible subsequence and check whether each one is strictly increasing.

There are exponentially many possible subsequences.

**Time Complexity:** `O(2ⁿ)`

This becomes too expensive as the input grows.

---

## Dynamic Programming

The Dynamic Programming solution stores previously calculated information in a list:

```python
notes = [1] * len(nums)
```

Each position in `notes` answers:

> What is the longest increasing subsequence ending at this specific position?

Every position starts at `1` because a number by itself is always an increasing subsequence of length `1`.

Example:

```text
nums:   [3, 1, 4, 2, 5]
notes:  [1, 1, 1, 1, 1]
```

After processing the entire input:

```text
nums:   [3, 1, 4, 2, 5]
notes:  [1, 1, 2, 2, 3]
```

The largest value in `notes` is therefore the answer.

---

## The Sticky-Note Mental Model

A useful way to visualize the Dynamic Programming list is to imagine placing a sticky note on every number.

Each sticky note remembers:

> The longest increasing path that ends here.

If an earlier position already has a sticky note containing `3`, and its value can connect to the current value, we know that earlier path can potentially become a path of length `4`.

We do not need to rediscover how we reached the earlier position.

The sticky note already remembers that information.

This helped make the purpose of Dynamic Programming much clearer: **save useful results from smaller problems so they can be reused when solving larger ones.**

---

## Current and Previous

The solution uses two loop variables:

```python
for current in range(len(nums)):
    for previous in range(current):
```

A useful mental model is:

* `current` — the position currently being solved.
* `previous` — an earlier position currently being checked against it.

`current` remains at one position while `previous` walks through every position behind it.

For example, if:

```python
current = 3
```

then:

```python
range(current)
```

produces:

```text
0, 1, 2
```

and `previous` takes each of those values one at a time.

An important Python lesson was that the loop itself assigns the loop variable. `previous` does not need to be created beforehand.

---

## Indexes vs. Values

`current` and `previous` contain **indexes**, not the actual numbers from `nums`.

For example:

```text
INDEX:    0    1    2
nums:    [10, 20, 30]
```

If:

```python
current = 1
```

then:

```text
current       = 1
nums[current] = 20
```

Therefore:

```python
nums[previous] < nums[current]
```

compares the actual values stored at those positions.

---

## Checking a Valid Increase

We check:

```python
if nums[previous] < nums[current]:
```

This determines whether the current value can extend an increasing subsequence ending at the previous position.

The comparison uses `<` rather than `<=` because the subsequence must be **strictly increasing**.

Duplicate values cannot extend the subsequence.

---

## Why `max()` Matters

When a valid increase is found, we update:

```python
notes[current] = max(
    notes[current],
    notes[previous] + 1,
)
```

There may be several earlier positions that can connect to the current position.

Not all of them provide equally long subsequences.

Using `max()` prevents a shorter path discovered later from overwriting a better path that was already found.

This was an important realization:

> A valid previous position is not necessarily the best previous position.

---

## Why We Return `max(notes)`

Each value in `notes` represents the best subsequence **ending at that specific position**.

The longest increasing subsequence does not necessarily end at the final element.

Example:

```text
nums:   [1, 5, 2, 3, 4, 0]
notes:  [1, 2, 2, 3, 4, 1]
```

The last position has a value of `1`, but the overall longest increasing subsequence has length `4`.

Therefore:

```python
return max(notes)
```

returns the largest subsequence found anywhere in the input.

---

## Empty Input

An empty input requires special handling.

Without:

```python
if not nums:
    return 0
```

the algorithm would eventually attempt:

```python
max([])
```

which is invalid.

The Longest Increasing Subsequence length of an empty list is `0`.

This is also an important edge case to include in the unit tests.

---

## Complexity

### Time Complexity

The algorithm uses nested loops.

For each `current` position, it checks the positions that came before it.

The amount of work therefore grows quadratically with the size of the input.

**Time Complexity:** `O(n²)`

### Space Complexity

The `notes` list contains one entry for every element in `nums`.

Its size grows proportionally with the input.

**Space Complexity:** `O(n)`

---

## Testing Lessons

Tests should not just use random inputs.

Each test should represent a particular behavior or edge case that the algorithm needs to handle.

Useful cases for this problem include:

* Empty input
* Single element
* All equal values
* Strictly increasing values
* Strictly decreasing values
* Mixed sequences

Python's `unittest` framework uses assertions such as:

```python
self.assertEqual(actual, expected)
```

to verify that the function's actual result matches the expected result.

---

## Common Interview Question

### Can Longest Increasing Subsequence be solved faster?

Yes.

A more advanced solution can achieve:

**Time Complexity:** `O(n log n)`

using binary search and a separate tracking structure.

The `O(n²)` Dynamic Programming solution is kept here because it clearly demonstrates the Dynamic Programming reasoning and is the approach implemented and understood in this problem.

The optimized approach can be explored separately later.

---

## Key Takeaways

* Dynamic Programming can reuse solutions to smaller subproblems instead of recalculating them.
* Each stored value should have a precise meaning.
* A loop variable such as `previous` is assigned automatically by the `for` loop.
* Indexes and the values stored at those indexes are different things.
* A valid previous result is not necessarily the best previous result.
* `max()` protects the best result found so far.
* Edge cases discovered while implementing a solution should usually become tests.
* Time complexity describes how the amount of work grows as the input grows.
* Space complexity describes how additional memory usage grows as the input grows.
* Confusion in an algorithm can sometimes come from unfamiliar language syntax rather than the algorithm itself.
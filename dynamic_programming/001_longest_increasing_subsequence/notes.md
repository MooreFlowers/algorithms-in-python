# Notes

## Brute Force

Try every subsequence.

Time Complexity:

O(2ⁿ)

Clearly too slow.

---

## Dynamic Programming

Let

dp[i]

represent the longest increasing subsequence ending at index i.

Initially

dp[i] = 1

because every number forms a subsequence by itself.

Then compare every previous element.

If

nums[j] < nums[i]

we can extend the subsequence.

Update

dp[i] accordingly.

---

## Why this works

Every increasing subsequence ending at i must come from some earlier position j.

DP stores the best answer we've already computed.

---

## Common Interview Questions

Can you solve it in O(n log n)?

Answer:

Yes.

Using binary search with a tails array.

---

## Takeaways

- Great introductory DP problem
- Shows how to build solutions from smaller subproblems
- Frequently asked in interviews
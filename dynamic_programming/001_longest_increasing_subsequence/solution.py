"""
Problem:
Longest Increasing Subsequence

Category:
Dynamic Programming

Time Complexity:
O(n²)

Space Complexity:
O(n)

Key Terms: 
Subarray - a continuous portion of the original array
Subsequence - preserves relative order but may skip elements 
Dynamic Programming - remembering answers to to smaller problems so you dont have to solve them again
"""

from typing import List

"""
Return the length of the longest strictly increasing subsequence.
"""
def length_of_lis(nums: List[int]) -> int:
    if not nums:
        return 0

    notes = [1] * len(nums)

    for current in range(len(nums)):
        for previous in range(current):
            if nums[previous] < nums[current]:
                notes[current] = max(
                    notes[current],
                    notes[previous] + 1,
                )

    return max(notes)
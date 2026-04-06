
"""
Problem: Two Sum
Platform: LeetCode #1
Difficulty: Easy
URL: https://leetcode.com/problems/two-sum/

Pattern: Array + Hashmap

Approach:
For each number, compute its complement (target - num). Check if the
complement already exists in the hashmap. If yes, return both indices.
If no, store the current number and its index.

Time complexity: O(n)
Space complexity: O(n)

Alternative: Brute force O(n²) — check every pair with nested loops
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    
    prev_nums = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in prev_nums:
            return [prev_nums[diff], i]
        prev_nums[num] = i
    return

if __name__ == "__main__":
    assert twoSum(nums = [3,4,5,6], target = 7) == [0,1]
    assert twoSum(nums = [4,5,6], target = 10) == [0,2]
    assert twoSum(nums = [5,5], target = 10) == [0,1]
    print("All tests passed!")



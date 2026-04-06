"""
Problem: Contains Duplicate
Platform: LeetCode #217
Difficulty: Easy
URL: https://leetcode.com/problems/contains-duplicate/

Pattern: Array + Set

Approach:
Iterate through the array, checking if each number already exists in a set.
If it does, we have a duplicate. If not, add it to the set.

Time complexity: O(n)
Space complexity: O(n)
"""

def hasDuplicate(nums: list[int]) -> bool:  
    
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

if __name__ == "__main__":
    assert hasDuplicate([1, 2, 3, 1])
    assert not hasDuplicate([1, 2, 3, 4])
    assert hasDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    print("All tests passed")
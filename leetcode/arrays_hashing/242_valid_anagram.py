"""
Problem: Valid Anagram
Platform: LeetCode #242
Difficulty: Easy
URL: https://leetcode.com/problems/valid-anagram/

Pattern: Array + Hashmap

Approach:
Early exit if lengths differ. Build a character count hashmap for
each string and compare them. Equal hashmaps means same characters
with same frequencies.

Time complexity: O(n)
Space complexity: O(n)

Alternative: sorted(s) == sorted(t) — simpler but O(n log n)
"""

def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    counts_s = {}
    counts_t = {}
    for char in s:
        counts_s[char] = counts_s.get(char, 0) + 1
    for char in t:
        counts_t[char] = counts_t.get(char, 0) + 1

    return counts_s == counts_t

if __name__ == "__main__":
    assert isAnagram(s = "racecar", t = "carrace")
    assert not isAnagram(s = "jar", t = "jam")
    assert isAnagram("", "")
    print("All tests passed")
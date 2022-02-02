class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s ==  None or len(s) == 0:
            return 0
        count = 0
        hashset = set()
        for char in s:
            if char not in hashset:
                hashset.add(char)
            else:
                count += 2
                hashset.remove(char)
        if len(hashset) != 0:
            return count + 1
        else:
            return count

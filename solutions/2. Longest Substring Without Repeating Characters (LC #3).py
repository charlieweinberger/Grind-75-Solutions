# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """ sliding window + set, O(n) """

        if self.isUnique(s):
            return len(s)

        left = 0
        right = 0

        maxLen = 0
        currentSubstring = set()

        while left != len(s):

            if s[right] in currentSubstring:
                maxLen = maxLen if maxLen > len(currentSubstring) else len(currentSubstring)
                currentSubstring.remove(s[left])
                left += 1
            else:
                currentSubstring.add(s[right])
                if right < len(s) - 1:
                    right += 1
                else:
                    left += 1

        return maxLen

        """ brute force solution, O(n^2) """

        # maxLen = 0

        # for i in range(1, len(s) + 1): # length of substring
        #     for j in range(len(s) - i + 1): # starting index of substring
        #         if self.isUnique(s[j : j + i]):
        #             maxLen = i
        
        # return maxLen

    def isUnique(self, s: str) -> str:
        return len(s) == len(set(s))
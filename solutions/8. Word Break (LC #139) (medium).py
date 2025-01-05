# https://leetcode.com/problems/word-break

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def recursiveWordBreak(currentString: str) -> bool:

            if currentString in memo:
                return memo[currentString]

            if len(currentString) == 0:
                return True

            for word in wordDict:
                if currentString.startswith(word):
                    if recursiveWordBreak(currentString[len(word):]):
                        memo[currentString] = True
                        return True

            memo[currentString] = False
            return False
        
        return recursiveWordBreak(s)
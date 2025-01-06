# https://leetcode.com/problems/ransom-note

from typing import Dict

class Solution:

    """ Slightly slightly faster solution """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False

        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False

        return True

    """ Slightly faster solution """

    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:

    #     magazineCounts = {}
        
    #     for letter in magazine:
    #         if letter not in magazineCounts:
    #             magazineCounts[letter] = 0
    #         magazineCounts[letter] += 1
        
    #     for letter in ransomNote:
    #         if letter not in magazine or magazineCounts[letter] <= 0:
    #             return False
    #         magazineCounts[letter] -= 1

    #     return True

    """ Initial solution """

    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
    #     ransomNoteCounts = self.getLetterCountMap(ransomNote)
    #     magazineCounts = self.getLetterCountMap(magazine)
        
    #     for letter in ransomNote:
    #         if letter not in magazine or ransomNoteCounts[letter] > magazineCounts[letter]:
    #             return False

    #     return True

    # def getLetterCountMap(self, string: str) -> Dict[str, int]:
        
    #     letterCountMap = {}
        
    #     for letter in string:
    #         if letter not in letterCountMap:
    #             letterCountMap[letter] = 0
    #         letterCountMap[letter] += 1
        
    #     return letterCountMap
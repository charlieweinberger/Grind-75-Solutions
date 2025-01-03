# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if self.isPalindrome(s):
            return s

        """ dynamic programming, O(n^2) """

        longestPalindrome = ""
        palindromes = {""}

        for i in range(1, len(s) + 1): # length of substring
            for j in range(len(s) - i + 1): # starting index of substring
                substring = s[j : j + i]
                if substring[0] == substring[-1] and substring[1:-1] in palindromes:
                    palindromes.add(substring)
                    longestPalindrome = substring
        
        return longestPalindrome

        """ brute force, O(n^3) """
    
        # longestPalindrome = ""
        
        # for i in range(1, len(s) + 1): # length of substring
        #     for j in range(len(s) - i + 1): # starting index of substring
        #         substring = s[j : j + i]
        #         if self.isPalindrome(substring):
        #             longestPalindrome = substring
        
        # return longestPalindrome

    def isPalindrome(self, s: str) -> bool:
        return all(s[i] == s[len(s) - i - 1] for i in range(len(s) // 2))
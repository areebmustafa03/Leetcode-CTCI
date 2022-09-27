
"""

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

LC # 1456  - Medium
"""

class Solution(object):
    
    def isVowel(self,c):
        return c == 'a' or c == 'e' or c == 'i' or  c == 'o' or c == 'u'
    def maxVowels(self, s, k):
        
        i = 0
        j = 0
        maximum = float("-inf")
        count = 0
        while i < len(s):
            
            if self.isVowel(s[i]):
                count += 1
            if i + 1 >= k:
                maximum = max(maximum,count)
                if self.isVowel(s[j]):
                    count -= 1
                j += 1
            i += 1
        return maximum
                
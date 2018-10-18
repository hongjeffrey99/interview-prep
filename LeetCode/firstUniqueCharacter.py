class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        
        for char in s:
            d[char] = d.get(char, 0) + 1
            
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
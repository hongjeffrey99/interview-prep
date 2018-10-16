class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = len(s)
        for length in range(2, len(s) + 1):
            for start in range(len(s)):
                if start + length <= len(s) and self.isPalindrome(s[start : start + length]):
                    count += 1
        return count           
 
    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False 

    """
    LeetCode Approaches:

    1. Expand around centers
    If string is length N, middle of palindrome could be at 2N - 1 positions (a letter or a space between letters)
    For each center, count palindromes with this center. If [a, b] is a palindromic interval, then [a+1, b-1] is also
    a palindrome.
    For each palindrome center, expand candidate palindrome on interval [left, right] as much as possible.
    Condition: left >= 0 and right < N and S[left] == S[right]
    Time Complexity: O(N^2) since each expansion can do up to O(N) work
    Space: O(1)

    2. DP?
    Build table with all possible string[start:end] combos. Store which are palindromes and which aren't.
    If you're checking if string[i:j] is a palindrome:
        1. Is string[i] == string[j]?
        2. Is string[i+1:j-2] a palindrome?
    If both are met, table[i][j] marked as True, count += 1
    """
    def alternateCountSubstrings(self, s):
        if not s:
            return 0

        n = len(s)
        table = [[False for x in range(e)] for y in range(n)]
        count = 0

        # Single characters are palindromes
        for i in range(n):
            table[i][i] == True
            count += 1

        # Window of size 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                count += 1

        # Check windows of size 3+
        for k in range(3, n + 1):
            for i in range (n - k + 1):
                j = i + k - 1
                if table[i + 1][j - 1] and s[i] == s[j]:
                    table[i][j] == True
                    count += 1

        return count
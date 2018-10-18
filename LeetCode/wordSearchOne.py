class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.dfs(board, x, y, word):
                    return True
        return False

    def dfs(self, board, x, y, word):
        if len(word) == 0:
            return True
        if x < 0 or x >= len(board):
            return False
        if y < 0 or y >= len(board[0]):
            return False
        if word[0] != board[x][y]:
            return False
        temp = board[x][y]
        board[x][y] = "!"
        result = self.dfs(board, x - 1, y, word[1:]) or \
                 self.dfs(board, x + 1, y, word[1:]) or \
                 self.dfs(board, x, y - 1, word[1:]) or \
                 self.dfs(board, x, y + 1, word[1:])
        board[x][y] = temp
        return result             
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        steps = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m = len(board)
        n = len(board[0])

        def dfs(seen, i, j, c_i):
            seen.add((i, j))
            if board[i][j] == word[c_i]:
                if c_i == len(word) - 1:
                    return True
                for stepi, stepj in steps:
                    newi, newj = i + stepi, j + stepj
                    if (newi, newj) in seen:
                        continue
                    if newi < 0 or newi > m-1:
                        continue
                    if newj < 0 or newj > n-1:
                        continue
                    if dfs(seen, newi, newj, c_i + 1):
                        return True
            seen.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(set(), i, j, 0):
                    return True
        return False

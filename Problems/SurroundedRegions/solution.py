class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        https://leetcode.com/problems/surrounded-regions/solutions/1552435/easy-explained-solution-with-images/
        """
        m, n = len(board), len(board[0])
        badCoordQ = deque()

        # Find coords in edge of matrix that are not 'X', and add them to queue
        for row in range(m):
            if (board[row][0] == 'O'):
                badCoordQ.append((row, 0))
            if (board[row][n - 1] == 'O'):
                badCoordQ.append((row, n - 1))
        for col in range(n):
            if (board[0][col] == 'O'):
                badCoordQ.append((0, col))
            if (board[m - 1][col] == 'O'):
                badCoordQ.append((m - 1, col))


        def inBounds(row, col):
            rowOk = False
            colOk = False
            if row >= 0 and row < m:
                rowOk = True
            if col >= 0 and col < n:
                colOk = True
            return rowOk and colOk


        # Go through queue, changing groups that extend to edges to '#'
        while badCoordQ:
            row, col = badCoordQ.popleft()
            board[row][col] = '#'

            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for neighbor in neighbors:
                r, c = neighbor
                if inBounds(r, c) and board[r][c] == 'O':
                    badCoordQ.append((r, c))
                    board[r][c] = '#'

        # Go through matrix flipping remainder 'O' to 'X', and change '#' back to 'O'
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'
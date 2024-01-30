class Solution:
    '''
    https://www.youtube.com/watch?v=y704fEOx0s0
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0

        # Count fresh fruit and add rotten fruit to q
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        # Iterate through rotten fruit with row level traversal.
        # That will emulate each rotten fruit spoiling its neighbor
        # at the same time.
        time = 0
        neighbors = [[0,1], [0,-1], [1,0], [-1,0]]

        while fresh > 0 and q:
            qLen = len(q)
            for _ in range(qLen):
                r, c = q.popleft()
                for rr, cc in neighbors:
                    row, col = r + rr, c + cc
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append([row,col])
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1
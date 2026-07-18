class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols=len(grid[0])

        queue = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
            
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh +=1
                
        if fresh == 0:
            return 0

        return self.bsf(grid, queue, fresh)


    def bsf(self, grid, queue, fresh):

        rows= len(grid)
        cols=len(grid[0])

        minutes = 0
        
        directions = [
            (1, 0),   # jos
            (-1, 0),  # sus
            (0, 1),   # dreapta
            (0, -1)   # stânga
        ]

        while queue and fresh >0:
            
            for k in range(len(queue)):
                i,j=queue.popleft()

                for di, dj in directions:
                    new_i = i+ di
                    new_j = j+ dj

                    if (
                        new_i >= 0 and
                        new_i < rows and
                        new_j >= 0 and
                        new_j < cols and
                        grid[new_i][new_j] == 1
                    ):
                        grid[new_i][new_j] = 2
                        fresh -= 1
                        queue.append((new_i, new_j))
                
            minutes +=1

        if fresh>0:
            return -1

        return minutes

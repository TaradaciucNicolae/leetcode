class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return 0

        dist = [[-1] * m for _ in range(n)]


        queue = deque()

        for i in range(n):
            for j in range(m):
                
                if grid[i][j] == 1:

                    dist[i][j] = 0
                    queue.append((i,j)) # adaugam toti hotii in coada si
                                                   # distanta pana la ei e 0

        directions = [
            ( 1, 0), #jos
            (-1, 0), #sus
            ( 0,-1), #stanga
            ( 0, 1)  #dreapta
        ]

        while queue:

            (row,col) = queue.popleft()

            for di, dj in directions:
                
                new_i = row + di
                new_j = col + dj

                if new_i>=0 and new_i<n and new_j>=0 and new_j<m and dist[new_i][new_j] == -1:

                    dist[new_i][new_j] = dist[row][col] +1
                    queue.append((new_i,new_j))

        # asa am facut anterior BFS ca sa cream acea mapare a distantelor si acum
        # trebuie sa cautam practic distanta cea mai scumpa sa zic asa
        # iar noi vom folosi heap si vom inversa distanta spre negativ ca sa folosim abilitatea lui 
        heap de a scoate valoarea cea mai mica

        best = [[-1] *n for _ in range(m)]
        best[0][0] = dist[0][0]

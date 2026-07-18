class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return 0

        dist = [[-1] * m for _ in range(n)]


        queue = deque()

        for i in range(n):
            for j in range(m):
                
                if grid[i][j] == 1:

                    dist[i][j] = 0
                    queue.append((i,j)) # adaugam toti hotii in coada si
                                                   # distanta pana la ei e 0

        directions = [
            ( 1, 0), #jos
            (-1, 0), #sus
            ( 0,-1), #stanga
            ( 0, 1)  #dreapta
        ]

        while queue:

            (row,col) = queue.popleft()

            for di, dj in directions:
                
                new_i = row + di
                new_j = col + dj

                if new_i>=0 and new_i<n and new_j>=0 and new_j<m and dist[new_i][new_j] == -1:

                    dist[new_i][new_j] = dist[row][col] +1
                    queue.append((new_i,new_j))

        # asa am facut anterior BFS ca sa cream acea mapare a distantelor si acum
        # trebuie sa cautam practic distanta cea mai scumpa sa zic asa
        # iar noi vom folosi heap si vom inversa distanta spre negativ ca sa folosim abilitatea lui heap de a scoate valoarea cea mai mica

        best = [[-1] *n for _ in range(m)]
        best[0][0] = dist[0][0]

        heap = []
        heapq.heappush(heap, (-1 * dist[0][0], 0, 0)) # adica am adaugat distanta negativa, row,col

        while heap:
            distanta_negata, row, col = heapq.heappop(heap)
            
            distanta_casuta_actuala = -1 * distanta_negata

            for di, dj in directions:
                
                new_i = row + di
                new_j = col + dj
                
                if new_i>=0 and new_i<n and new_j>=0 and new_j<m:

                    # e minimul pt ca e ca un drum, ni mergem prin el si daca candva am fost nevoiti sa vim mai aproape de thief, chiar daca ne indepartam, tot minim tre sa ramana pt ca la un moment dat ala era scorul de siguranta
                    new_safety = min(distanta_casuta_actuala, dist[new_i][new_j])

                    # Păstrăm doar drumul care oferă un safeness mai bun pentru acest vecin.
                    if new_safety > best[new_i][new_j]:
                        best[new_i][new_j] = new_safety

                        # Punem vecinul în heap ca să continuăm mai târziu de acolo.
                        # Folosim minus pentru că Python are min-heap, iar noi vrem maxim.
                        heapq.heappush(heap, (-new_safety, new_i, new_j))

            if row == n - 1 and col == m - 1:
                return distanta_casuta_actuala

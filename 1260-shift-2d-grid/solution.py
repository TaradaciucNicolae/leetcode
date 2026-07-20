class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        one_d_grid = []

        for i in range(m):
            for j in range(n):
                one_d_grid.append(grid[i][j])

        k = k % (m*n)

        # i'll take the kast k value from the 1d grid
        last_k_values = one_d_grid[-k:]
        # pornește de la indexul -k și ia până la final



        # than I'll take the first m*n -k values
        first_values = one_d_grid[:-k]

        one_d_grid[:] = last_k_values + first_values

        id_one_d = 0

        for i in range(m):
            for j in range(n):
                grid[i][j] = one_d_grid[id_one_d]
                id_one_d +=1




        return grid

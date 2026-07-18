class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        
        n = len(board) # e suficient ca e patrat
        MOD = 10**9 + 7

        directions={

            (-1, 0), # sus
            ( 0,-1), # stanga
            (-1,-1), #diagonal sus-stanga
        }

        best_score = [[float("-inf")] * n for _ in range(n)] # o sa avem -inf in celul in care inca nu putem ajunge
        paths = [[0] * n for _ in range(n)]

        best_score[n-1][n-1] = 0 # ce mai mare scor cu care pot ajunge in n-1, n-1
        paths[n-1][n-1] = 1 # Cate path-uri ating acel scor maxim de la best_score


        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                best_scor_curent = best_score[i][j]

                if best_scor_curent == float("-inf"): # daca celula e imposibil de atins, nu are rost sa continuam cu ea
                    continue


                for i_d, j_d in directions:
                    new_i = i + i_d
                    new_j = j + j_d

                    if new_i >= 0 and new_i <=n-1 and new_j >=0 and new_j <=n-1:
                        
                        if board[new_i][new_j] == 'X':
                            continue


                        if board[new_i][new_j] == 'E':
                            de_adaugat = 0
                        else:
                            de_adaugat = int(board[new_i][new_j])

                        new_score = best_scor_curent + de_adaugat
                        

                        if new_score > best_score[new_i][new_j]:
                            best_score[new_i][new_j] = new_score
                            paths[new_i][new_j] = paths[i][j]

                            next_dest = (new_i,new_j)

                        elif new_score == best_score[new_i][new_j]:
                            paths[new_i][new_j] = (paths[new_i][new_j] + paths[i][j]) % MOD
                    

        if paths[0][0] == 0:
            return [0, 0]



        return [best_score[0][0],paths[0][0]]

        # Calcul complexitate: 
        '''
        n = nr de randuri  = nr coloane -> board-ul are n*n celule

        Time complexity: 

        Avem 2 bucle for -> parcurgem toate celulele -> n*n = O (n^2)

        pt fiecare celula mai avem si o bucla peste directions ce are mereu 3 elemente = 3 = O(1)

        deci Tinme complexity = O(n^2 *3) = O(n^2)


        Space complexity:

        avem 2 matrici de dimensiune n x n ( best_score si paths) => Fiecare matrice ocupa O(n^2), iar impreuna ele 2->
        -> O(n^2) + O(n^2) = O(n^2)

        directions are doar 3 elemente -> O(1)
        variabiele i,j,new_i, new_j, new_score sunt tot O(1):

        Deci Space complexity O(n^2)

        '''

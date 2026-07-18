class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # Connected component Logic

        result=[]

        connections = [0] * n  #practic avem connections si vom avea aveam nr, gen 0 la membrii grupului 0 si 1 la membrii grupului 1 si daca avem [0,0,0,1,1], inseamna ca primii 3 sunt din grup 0 si restul grup 1

        grup_curent=0

        for i in range(1,n): # incepem cu 1 ca oricum daca incepeam cu 0 trebuia sa punem if i==0, diff = nums[i] - nums[i]
    
            diff = nums[i] - nums[i-1]

            if diff > maxDiff:
                grup_curent +=1 # putem face asa pt ca valorile sunt sortate si daca inaintam si cream un nou grup, automat celelalte ce urmeaza nu au cum sa faca parte din grupul de la care am inceput sau altul din trecut
            
            connections[i] = grup_curent

            
        for u,v in queries:

            if connections[u] == connections[v]:
                result.append(True)
            else:
                result.append(False)


        return result


'''

Space complexity: O(n) pt connections


Time complexity: O(n) pt for si q pt len de queries si ar fi un O(n+q)

'''

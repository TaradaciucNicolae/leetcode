class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        unique_arr = set(arr)
        unique_sorted_arr  = sorted(unique_arr)

        rank_map = {}

        for i, num in enumerate(unique_sorted_arr):
            rank_map[num] = i + 1

        n = len(arr)
        result = []

        for num in arr:
            result.append(rank_map[num])

        return result

        # unique_arr = set(arr)
        # unique_sorted_arr  = sorted(unique_arr)

        # n = len(arr)

        # rank_list= [0]*n


        # for i in range(n):

        #     rank_list[i] = unique_sorted_arr.index(arr[i]) +1

        
        # return rank_list

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        

        set_no_duplicates = set(arr)  # a set can't have duplicates

        sorted_array_no_duplicate = sorted(set_no_duplicates)


        rank_map = {} # we create a map for a smaller complexity (when searching for index)

        for i, val in enumerate(sorted_array_no_duplicate):
            rank_map[val] = i + 1


        n=len(arr)
        result = [0]* n

        for i in range(n):
            result[i] = rank_map[arr[i]]

        return result

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict_of_nums = defaultdict(int)

        for num in nums:
            dict_of_nums[num] +=1


        #aici are forma num: frecventa

        sorted_nums = sorted(dict_of_nums, key=lambda num:dict_of_nums[num], reverse=True)

        return sorted_nums[:k]

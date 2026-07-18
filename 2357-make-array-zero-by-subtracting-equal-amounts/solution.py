class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nr_of_op = 0
        
        while sum(nums) != 0:
            nr_of_op = nr_of_op+1

            min_nr=101
            for nr in nums:
                if nr< min_nr and nr != 0:
                    min_nr=nr

            for id, nr in enumerate(nums):
                if nr > 0:
                    nums[id]= nr-min_nr
            
        
        return nr_of_op

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        i_for_no_dup = 1  # cause i=0 already is in place

        for i in range(1,n):

            if nums[i] != nums[i-1]:

                nums[i_for_no_dup] = nums[i]
                i_for_no_dup +=1


        
        return i_for_no_dup

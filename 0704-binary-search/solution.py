class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left =0
        right = len(nums) -1

        while left <= right:
            mid = (left + right) // 2 

            if nums[mid] > target:
                right = mid -1
                #self.search(nums[left:right], target) # as fi pasat astia doar daca aveam in acel search si limitele low si high

            elif nums[mid] < target:
                left = mid +1
                #self.search(nums[left:right], target)
            else:
                return mid
        
        return -1

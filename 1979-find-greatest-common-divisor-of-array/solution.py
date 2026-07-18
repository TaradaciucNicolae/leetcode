class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        smallest = min(nums)

        largest = max(nums)

        reversed_counter = smallest

        while reversed_counter != 0:

            if smallest % reversed_counter == 0 and largest % reversed_counter == 0:
                return reversed_counter

            reversed_counter -= 1

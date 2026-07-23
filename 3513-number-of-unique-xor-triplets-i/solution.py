class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        # values_seen = set()

        # n = len(nums)

        # for i in range(n):
        #     for j in range(i,n):
        #         for k in range(j,n):

        #             value = nums[i] ^ nums[j] ^ nums[k]
        #             values_seen.add( value )

        # return len(values_seen)


        # After adding many testcases i realised that 

        n = len(nums)


        if n < 3:
            return n
            
        bit_len= n.bit_length()
        return pow(2,bit_len)

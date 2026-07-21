class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        
        aug_s = "1" + s + "1"

        segments = []

        current_char = aug_s[0]
        count = 1

        for i in range(1, len(aug_s)):

            if aug_s[i] == current_char:
                count +=1
            else:
                segments.append([current_char, count])
                current_char = aug_s[i]
                count = 1
        
        segments.append([current_char, count])
            
        #print(segments)


        ones = s.count("1")
        max_gain = 0

        for i in range(1, len(segments)-1):
            
            prev_val, prev_count = segments[i-1]
            curr_val, curr_count = segments[i]
            future_val, future_count = segments[i+1]

            if prev_val == "0" and curr_val == "1" and future_val == "0":

                max_gain = max(max_gain, prev_count +  future_count )




        return ones + max_gain

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0

        curr_window = set()

        max_length =0

        for right, every_char in enumerate(s):
            #print(curr_window)
            while every_char in curr_window: # e while si nu if pt ca avem si duplicate
                #print(curr_window)
                curr_window.remove(s[left])
                left+=1
                #print(curr_window)

            curr_window.add(every_char)
            #print(curr_window)
            max_length=max(max_length, right-left+1)
        #print(curr_window)
        return max_length

        

        # starter_i = 0
        # longest_substring = ""
        # substring =""

        # for i, every_char in enumerate(s):
        #     if every_char not in substring:
        #         if substring == "":
        #             starter_i = i

        #         substring += every_char
        #     else:
        #         s = s[1:]
        #         every_char = s[0]
        #         i = starter_i
        #         substring = ""



        #     if len(substring) > len(longest_substring):
        #         longest_substring = substring
            
        # return len(longest_substring)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        seq = ""

        last_pos_of = {} # last[char] = ultima pozitie unde apare char in s 
        #populam last
        for i, char in enumerate(s):
            last_pos_of[char] = i
        

        for i, char in enumerate(s):

            if char in seq:
                continue

            
            while seq and seq[-1] > char and last_pos_of[seq[-1]] > i:

                seq = seq[:-1]
            
            seq = seq + char

        return seq

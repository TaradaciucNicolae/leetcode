from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # dp[(g1, g2)] = numărul de moduri de a forma două subsequences
        # cu gcd-urile g1 și g2
        dp = {(0, 0): 1}
        
        for x in nums:
            new_dp = dp.copy()  # cazul în care nu folosim x
            
            for (g1, g2), count in dp.items():
                # punem x în seq1
                ng1 = gcd(g1, x)
                new_dp[(ng1, g2)] = (new_dp.get((ng1, g2), 0) + count) % MOD
                
                # punem x în seq2
                ng2 = gcd(g2, x)
                new_dp[(g1, ng2)] = (new_dp.get((g1, ng2), 0) + count) % MOD
            
            dp = new_dp
        
        ans = 0
        
        for (g1, g2), count in dp.items():
            # ambele subsequences trebuie să fie non-empty,
            # deci gcd-ul lor nu poate fi 0
            if g1 == g2 and g1 != 0:
                ans = (ans + count) % MOD
        
        return ans

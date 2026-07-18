class Solution:
    def sumAndMultiply(self, n: int) -> int:

        if n == 0: return 0

        string = str(n)
        string_nou=""
        suma = 0
        for i, val in enumerate(string):

            suma += int(val)
            if val != "0":
                string_nou = string_nou + val


        return int(string_nou)*suma

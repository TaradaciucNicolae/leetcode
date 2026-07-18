class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        output = []

        for length in range(2, 10):
            for start_digit in range(1, 11 - length):
                number = 0
                digit = start_digit

                for _ in range(length):
                    number = number * 10 + digit
                    digit += 1

                if low <= number <= high:
                    output.append(number)


        return output

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if(digits[len(digits) - 1] + 1 < 10):
            digits[len(digits) - 1] += 1
            return digits

        carry_bit = 1

        for i in range(len(digits) - 1, -1, -1):

            print(digits)
            print(carry_bit)

            temp = digits[i]

            digits[i] = (digits[i] + carry_bit) % 10

            print(digits[i])

            carry_bit = (temp + carry_bit) // 10

            if(i == 0 and digits[i] == 0):

                digits.insert(0,1) 

        print(digits)
        return digits




        
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1

        sol = [0] * len(nums)

        num_zeros = 0
        zero_index = 0

        for i in range(len(nums)):

            if(nums[i] == 0):

                num_zeros += 1
                zero_index = i 

                continue

            prod *= nums[i]
        
        print(prod)

        if(num_zeros == 1):

            sol[zero_index] = prod
        
        print(sol)

        if(num_zeros == 0):

            for i in range(len(nums)):

                sol[i] = int(prod/nums[i])
        
        print(sol)

        return sol




        
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #without division = product of ranges

        # nums[0:i - 1] * nums[i+1:len(nums) - 1]

        #how to compute?
        #precompute? but for every pair of indices, is n^2
        
        # forwards + backwards!

        # forwards[0:i-1] * reverse[0:(nums - i - 1)]

        #forwards prefix array

        prod = 1
        reverse_prod = 1

        forwards = []
        reverse = []

        for elem in nums:

            prod *= elem

            forwards.append(prod)
        
        print(forwards)

        #reverse prefix array 
        
        for elem in reversed(nums):

            reverse_prod *= elem

            reverse.append(reverse_prod)
        
        print(reverse)
        
        sol = []
        for i in range(len(nums)):

            if(i == 0):

                sol.append(reverse[len(nums) - (i + 1) - 1])
            
            elif(i == len(nums) - 1):

                sol.append(forwards[i-1])

            else:

                sol.append(forwards[i-1] * reverse[len(nums) - (i + 1) - 1])
        
        print(sol)
        return sol




            









        
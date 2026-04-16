class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        return self.bs(0, len(nums) - 1, nums, target)

    def bs(self, low, high, arr, targ):

        #not found
        if(low > high):

            return low
        
        mid = (high  + low) // 2

        #left half
        
        if(targ < arr[mid]):

            return self.bs(low, mid - 1, arr, targ)
        
        #right half
        elif(targ > arr[mid]):

            return self.bs(mid + 1, high, arr, targ)
        
        else:

            #found at mid

            return mid


        

        
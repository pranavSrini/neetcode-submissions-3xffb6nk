class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bs(0, len(nums) - 1, nums, target)

    def bs(self, l, r, arr, targ):

        if(r < l):
            return -1

        mid = (l + r)//2

        if(arr[mid] == targ):
            return mid
        elif(arr[mid] < targ):
            l = mid + 1
        else:
            r = mid - 1
        
        return self.bs(l, r, arr, targ)

        
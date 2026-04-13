class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            print(res, n)
            res = res ^ n

        return res


         

            








        
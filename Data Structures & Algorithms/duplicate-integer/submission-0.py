class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct = set()
        for elem in nums:
            if(elem in distinct):
                return True
            else:
                distinct.add(elem)
        return False


        
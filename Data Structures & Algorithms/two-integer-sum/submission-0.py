class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #need to know two things:
        #all a[i], and all target - a[i].
        # one member of all a[i] and one member of all target - a[i]
        # are in 
        #both computable in o(1) and target - a[i] storable in o(1) with hashmap
        # if you encounter 

        seen = dict()
        ans = []
        for i in range(len(nums)):
            if target - nums[i] not in seen.keys():
                seen[nums[i]] = i
            else:
                ans.append(seen[target - nums[i]])
                ans.append(i)
        return ans
        


        
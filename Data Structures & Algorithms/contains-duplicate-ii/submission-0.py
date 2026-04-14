class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        i = 0
        j = 0
        while(i < len(nums)):

            print("i: " + str(i))
            print("j: " + str(j))

            #valid window?

            if(i < j):

                #found sol
                if(j < len(nums) and nums[i] == nums[j]):
                    return True
                
                else:
                
                    # <= k
                    if(abs(i - j) < k):

                        j += 1
                    
                    #shift
                    
                    else:

                        i += 1
            else:

                j += 1
        
        return False




            



        
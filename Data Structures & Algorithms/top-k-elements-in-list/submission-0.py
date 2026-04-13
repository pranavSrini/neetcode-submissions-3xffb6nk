import heapq

class Solution:

    #trying heapq

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #compute frequencies

        freqs = dict()
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        
        #put in pq
        sorted_freqs = []
        
        for num in freqs:
            #each elem is a tuple(priority, value)
        
            heapq.heappush(sorted_freqs, (-freqs[num], num))
        
        to_pop = k
        ans = []
        while(to_pop > 0):
            ans.append(heapq.heappop(sorted_freqs)[1])
            to_pop -= 1
        return ans










        
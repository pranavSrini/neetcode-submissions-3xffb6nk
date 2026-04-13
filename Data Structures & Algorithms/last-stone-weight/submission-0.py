import heapq
class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        #max heap - max elem on top. negate the elem before adding because by default is min heap

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        print(heap)
        
        while(len(heap) > 1):

            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            if a - b > 0: heapq.heappush(heap, b-a)

        ans = 0 if len(heap) == 0 else -heap[0]
        return ans


        
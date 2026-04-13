import heapq 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.kstream = []
        self.k = k

        for elem in nums:

            heapq.heappush(self.kstream, elem)
            if(len(self.kstream) > k):
                heapq.heappop(self.kstream)
        


        

    def add(self, val: int) -> int:

        print(self.kstream)
        heapq.heappush(self.kstream, val)
        if(len(self.kstream) > self.k):
            heapq.heappop(self.kstream)


        return self.kstream[0]

        


        

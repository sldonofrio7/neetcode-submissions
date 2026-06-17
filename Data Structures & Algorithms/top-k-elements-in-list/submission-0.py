import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = defaultdict(int)
        pq = []
        res1 = []

        for i in nums:
            res[i] += 1

        for j in res:
            heapq.heappush_max(pq, (res[j], j))

        for l in range(k):
            res1.append(heapq.heappop_max(pq)[1])

        return res1

                
        
        
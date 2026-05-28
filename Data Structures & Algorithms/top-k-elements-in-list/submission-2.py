from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for key ,value in freq.items():  
            buckets[value].append(key)
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i] == []:
                continue
            else:
                for num in buckets[i]:
                    output.append(num)
                    if len(output) == k:
                        return output
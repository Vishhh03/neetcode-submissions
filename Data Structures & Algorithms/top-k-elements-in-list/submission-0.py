class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        n = len(nums)
        for num in nums:
               counter[num] = counter.get(num, 0) + 1

        bucket = [[] for _ in range(n+1)] 
        for key, value in counter.items():
            if bucket[value] == 0:
                bucket[value] == [key]
            else:
                bucket[value].append(key)

        result = []

        for i in range(n, -1, -1):
            if bucket[i] != 0:
                result.extend(bucket[i])
            if len(result) >= k:
                break
        return result
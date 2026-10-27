class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        buckets = {}
        l = []

        for num in nums:
            count = d.get(num, 0)
            count += 1
            d[num] = count
        
        for i in range(1, len(nums) + 1):
            buckets[i] = []

        for num, count in d.items():
            buckets[count].append(num)

        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                l.append(num)
                if len(l) == k:
                    return l

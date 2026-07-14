class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        res = []
        for key, value in sorted(dict.items(),key= lambda x: x[1], reverse=True):
            if len(res) < k:
                res.append(key)
        return res
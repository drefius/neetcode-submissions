class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        res = []
        for key in sorted(dict.keys(),key= lambda x: dict[x], reverse=True):
            if len(res) < k:
                res.append(key)
                continue
            if len(res) == k:
                break
        return res
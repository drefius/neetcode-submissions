class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_one = {}
        response = []
        for idx, num in enumerate(nums):
            num_2 = target - num
            if num_2 in d_one.keys():
                response.extend([idx,nums.index(num_2)])
                break
            d_one[num] = idx
        return sorted(response, reverse = False)
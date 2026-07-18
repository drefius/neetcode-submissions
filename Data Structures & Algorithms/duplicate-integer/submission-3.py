class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_temp = set()
        for num in nums:
            if num in set_temp:
                return True
            set_temp.add(num)
        return False
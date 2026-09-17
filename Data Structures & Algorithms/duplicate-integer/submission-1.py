class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a dict to then check the if the value at the index is a key in the dict
        if not nums: return False
        d = {}

        for num in nums:
            if num in d:
                return True
            else:
                d[num] = "blah"
        return False


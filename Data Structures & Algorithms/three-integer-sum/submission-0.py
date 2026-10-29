class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the list from least to greatest
        # Create a list that will contain the list of triplets
        # A loop that naturally goes through each value of the list
        # A left pointer that starts at index + 1
        # A right pointer that starts at length of the list - 1
        # A while loop that keeps running until the left and right pointer cross each other
        # Each iteration of the loop it needs to check if the current index + the pointer values = 0
        # If not, is the sum greater than or less than 0?
        # This should determine which pointer to move in which direction

        nums.sort()
        answer = []

        for i in range (0, len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
        return answer

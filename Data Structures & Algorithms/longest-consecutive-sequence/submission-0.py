class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Need to be able to check every other value within the list (a set)
        # Some comparison of current sequence number and if the next one is equal to + 1 of previous
        # If there is a match, then it needs to be appended to answer list

        this_set = set(nums)
        best_sequence = 0

        for num in this_set:
            if (num - 1) not in this_set:
                sequence_length = 1
                counter = num
                while (counter + 1) in this_set:
                    sequence_length += 1
                    counter += 1
                best_sequence = max(best_sequence, sequence_length)
        return best_sequence

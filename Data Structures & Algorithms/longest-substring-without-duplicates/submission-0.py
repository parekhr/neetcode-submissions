class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Pseudocode:
        # if s is empty, return 0
        #
        # window = ""          # the current window (consecutive, no repeats)
        # longest = 0          # best length seen so far
        #
        # for each char in s:
        #     while char is already in window:
        #         drop the first character of window
        #
        #     add char to the end of window
        #
        #     if window is longer than longest:
        #         update longest
        #
        # return longest

        if not s:
            return 0

        window = ""
        longest = 0

        for char in s:
            while char in window:
                window = window[1:]
            window += char

            if len(window) > longest:
                longest = len(window)
        return longest
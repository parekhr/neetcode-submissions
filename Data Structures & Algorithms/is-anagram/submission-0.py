class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        front = ""
        end = ""
        for char in s:
            front += char
        for char in t:
            end += char
        check1 = ''.join(sorted(front))
        check2 = ''.join(sorted(end))

        if check1 == check2:
            return True
        else:
            return False
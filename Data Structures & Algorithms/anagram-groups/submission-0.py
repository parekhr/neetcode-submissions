class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create empty dictionary
        # need to sort each word of the given list in alphabetical order so we can identify anagrams easier
        # check if the sorted string is a key in the dictionary, if it is not then add it as a key with an empty list of values []
        # the original unsorted word needs to also exist in the value list
        # when finished going through the given list, return the value lists into the answer [] list
        answer = {}
        sorted_list = []
        for word in strs:
            temp = ''.join(sorted(word))
            if temp not in answer:
                answer[temp] = []
            answer[temp].append(word)
        return list(answer.values())
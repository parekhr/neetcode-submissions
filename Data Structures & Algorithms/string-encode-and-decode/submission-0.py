class Solution:

    def encode(self, strs: List[str]) -> str:

        # Take the strs list and append string length and concatenate _ after, need to loop through strs. Overwrite that value at the index so that we're doing it in place
        new_list = []

        for word in strs:
            new_list.append(str(len(word)) + "_" + word)
        encoded_word = ''.join(new_list)
        return encoded_word

    def decode(self, s: str) -> List[str]:

        decoded_list = []

        # Starting point
        i = 0

        # First loop to go through the entire encoded string, j will help move it forward to the next starting point
        while i < len(s):
            j = i
            # j's purpose is to get the the point of the encoded string such that it's an underscore "_"
            while s[j] != "_":
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length
            
            decoded_list.append(s[start:end])

            i = end

        return decoded_list




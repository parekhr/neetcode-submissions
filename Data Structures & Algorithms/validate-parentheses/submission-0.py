class Solution:
    def isValid(self, s: str) -> bool:
        # High Level Plan
        # What defines an open and closed bracket?
        # The left side of it and the right side
        # Can we define all of these brackets in a dictionary and make use of key: value?
        # If an opening of a bracket is defined in the dictionary ( for example (, {, [ ), then proceed to the next character
        # Keep going until that key does not exist in the dictionary while pushing these opening brackets into the stack in order
        # Once a closing bracket is the next character, check if the value of that key of that closing bracket is equal. If it is then pop from stack, otherwise return False
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []
        # If first char of s is a key in the dictionary, push to stack and continue
        # Continue until the char is NOT in the dictionary
        # If char is NOT in the dictionary, then check current key's value pair

        for bracket in s:
            # If current bracket is a key in the dictionary
            if bracket in pairs:
                stack.append(bracket)
            else:
                # If the stack is empty or the top of the stack does not match key: value, then return false
                if not stack or pairs.get(stack[-1]) != bracket:
                    return False
                stack.pop()
        return not stack
        # stack [ '(', ')']

            


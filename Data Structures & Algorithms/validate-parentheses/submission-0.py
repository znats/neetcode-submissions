class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in pairs:
                # If stack is not empty and top matches the required open bracket
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)

        # Valid only if all opened brackets were closed
        return len(stack) == 0
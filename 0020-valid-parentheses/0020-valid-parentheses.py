class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if non-empty, else use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped bracket matches the expected opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto stack
                stack.append(char)
                
        # If stack is empty, all opening brackets were properly closed
        return not stack
class Solution(object):
    def backspaceCompare(self, s, t):
        def build(string):
            stack = []
            for c in string:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)
        
        return build(s) == build(t)             

        
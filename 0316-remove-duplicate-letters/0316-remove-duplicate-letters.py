
class Solution(object):
    def removeDuplicateLetters(self, s):
        stack = []
        seen = set()
        count = {} 
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in s:
            count[c] -= 1
            if c in seen:
                continue
            while stack and c < stack[-1] and count[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        
        return "".join(stack)

        
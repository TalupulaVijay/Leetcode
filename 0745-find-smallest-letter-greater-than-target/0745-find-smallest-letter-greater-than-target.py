class Solution(object):
    def nextGreatestLetter(self, letters, target):
        letters=sorted(letters)
        for ch in letters:
            if ch>target:
                return ch
                break
        return letters[0]       


        
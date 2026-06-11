class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        for i in range(len(citations), 0, -1):

            if citations[-i] >= i:
                return i

        return 0
        
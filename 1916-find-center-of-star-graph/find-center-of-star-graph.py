class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first = edges[0]
        second = edges[1]

        if first[0] == second[0] or first[0] == second[1]:
            return first[0]
        else:
            return first[1]
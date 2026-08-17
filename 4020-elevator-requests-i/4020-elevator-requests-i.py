class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        tot=requests[0]
        for i in range(1,len(requests)):
            tot+=abs(requests[i-1]-requests[i])
        return tot
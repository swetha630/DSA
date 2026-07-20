class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        l=m*n
        arr=[grid[i][j] for i in range(m) for j in range(n)]
        k=k%l 
        rev=arr[-k:]+arr[:-k]
        res=[]
        for i in range(m):
            res.append(rev[i*n:(i+1)*n])
        return res
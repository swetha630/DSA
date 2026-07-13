class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        r1=[12,23,34,45,56,67,78,89]
        r2=[123,234,345,456,567,678,789]
        r3=[1234,2345,3456,4567,5678,6789]
        r4=[12345,23456,34567,45678,56789]
        r5=[123456,234567,345678,456789]
        r6=[1234567,2345678,3456789]
        r7=[12345678,23456789]
        r8=[123456789]
        r=r1+r2+r3+r4+r5+r6+r7+r8
        res=[]
        for i in r:
            if low<=i<=high:
                res.append(i)
        return res
        

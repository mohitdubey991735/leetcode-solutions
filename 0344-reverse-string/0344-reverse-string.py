class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s,0,len(s)-1)
    def reverse(self, a, start, end):
        while start < end:
            a[start], a[end] = a[end], a[start]
            start+=1
            end-=1
    
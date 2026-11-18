class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        self.reverse(nums, 0,  n-1)
        self.reverse(nums, 0,  k-1)
        self.reverse(nums, k,  n-1)
    def reverse(self, a, start, end):
        while start < end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1


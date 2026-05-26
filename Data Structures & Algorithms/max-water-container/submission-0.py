class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        area = 0

        while left < right:
            if min(heights[left], heights[right]) * (right - left) > area:
                area = min(heights[left], heights[right]) * (right - left)
            left += 1

        return area
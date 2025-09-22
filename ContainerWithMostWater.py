class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers
        left = 0
        right = len(height) - 1
        
        # Variable to store the maximum area found
        max_area = 0
        
        # Loop until the two pointers meet
        while left < right:
            # Calculate the current area
            area = min(height[left], height[right]) * (right - left)
            
            # Update max_area if this area is larger
            max_area = max(max_area, area)
            
            # Move the pointer pointing to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        # Return the maximum area found
        return max_area

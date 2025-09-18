class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # stores number -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:   # if the pair exists
                return [hashmap[complement], i]
            hashmap[num] = i   # store the index of the current number

# ---- Static input ----
nums = [2, 7, 11, 15]
target = 9

obj = Solution()
print("Indices:", obj.twoSum(nums, target))

# ---- Dynamic input ----
nums = list(map(int, input("Enter the numbers separated by space: ").split()))
target = int(input("Enter the target value: "))

obj = Solution()
print("Indices:", obj.twoSum(nums, target))

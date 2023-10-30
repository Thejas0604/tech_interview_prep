class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            to_target = target - int(nums[i])
            if (to_target in nums) and (nums.index(to_target) != i):
                return [i, nums.index(to_target)]
            else:
                continue


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))

# total time complexity: O(n)

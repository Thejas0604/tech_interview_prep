class Solution:
    def twoSum(self, nums, target):
        to_target = {}
        for i in range(len(nums)):
            to_target[target - nums[i]] = i  # O(n)

        for i in range(len(nums)):
            if (nums[i] in to_target) and (to_target[nums[i]] != i):
                return [i, to_target[nums[i]]]
            else:
                continue  # O(n)


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))

# total time complexity: O(n)

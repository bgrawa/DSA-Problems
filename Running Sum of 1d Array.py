class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        n = len(nums)

        for i in range(1, n):
            ans.append(nums[i] + ans[-1])

        return ans
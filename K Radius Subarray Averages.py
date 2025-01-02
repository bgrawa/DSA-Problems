class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n

        if k == 0:
            return nums

        window_size = 2 * k + 1
        if window_size > n:
            return result

        window_sum = sum(nums[: window_size])

        for i in range(k, n - k):
            result[i] = window_sum // window_size
            if i < n - k - 1:
                window_sum = window_sum - nums[i - k] + nums[i + k + 1]

        return result
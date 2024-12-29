class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startVal = 1

        while True:
            total = startVal
            isValid = True

            for i in nums:
                total += i

                if total < 1:
                    isValid = False
                    break

            if isValid:
                return startVal
            else:
                startVal += 1
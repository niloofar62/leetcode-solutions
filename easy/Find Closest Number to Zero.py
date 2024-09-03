# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.2239
def findClosestNumber(self, nums: List[int]) -> int:
        closeNum=nums[0]
        for i in nums:
            if abs(i)<abs(closeNum):
                closeNum=i
        if closeNum < 0 and abs(closeNum) in nums: # check for [-1,1,2]

             return abs(closeNum)
        else:
            return closeNum

        #  T=O(N)
        # S=O(1)

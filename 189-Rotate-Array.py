class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        k %= len(nums) 

        # for i in range(k):
        #     for index in range(len(nums) - 1 , 0 , -1):
        #         nums[index - 1] , nums[index] = nums[index], nums[index - 1] 

        # using reverse method        
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

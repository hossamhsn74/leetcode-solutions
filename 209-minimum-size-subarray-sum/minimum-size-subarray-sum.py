class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        start = 0
        current_sum = 0
        min_length = float('inf')

        # Iterate through the array using two pointers (start and end)
        for end in range(len(nums)):
            # Expand window and add current element to the sum
            current_sum += nums[end]

            while current_sum >= target:
                # Update minimum length when valid sum is found
                min_length = min(min_length, end - start + 1)
                # Shrink window from start and subtract the removed value
                current_sum -= nums[start]
                start += 1

        return min_length if min_length != float('inf') else 0
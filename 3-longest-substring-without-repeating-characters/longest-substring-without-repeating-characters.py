class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = list(s)

        start = 0
        max_length = 0

        for end in range(len(arr)):
            # Check if the current character is already in the current substring/window
            if arr[end] in arr[start:end]:
                # Move the start pointer to the next position after the first occurrence of the character
                start = arr.index(arr[end], start, end) + 1
            else:
                # Update the maximum length
                max_length = max(max_length, end - start + 1)
                # expand the window to the right

        return max_length

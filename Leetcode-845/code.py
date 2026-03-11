class Solution:
    def longestMountain(self, arr):
        n = len(arr)
        ans = 0

        for i in range(1, n-1):

            
            if arr[i-1] < arr[i] > arr[i+1]:

                left = i
                right = i

                
                while left > 0 and arr[left] > arr[left-1]:
                    left -= 1

                
                while right < n-1 and arr[right] > arr[right+1]:
                    right += 1

                ans = max(ans, right - left + 1)

        return ans

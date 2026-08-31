# given an array of integers and a number k, find the maximum sum of a subarray of size k

# efficient approach: O(n)
'''
solution is based on the fact that sum of a subarray (or window) of size k can be obtained in O(1) time 
using the sum of the previous subarray (or window) of size k

except for the first subarray of size k, for other subarrays, we compute the sum by 
removing the first element of the last window and adding the last element of the current window
'''
def MaxSubarray(arr, k):
    n = len(arr)
    res = 0
    # sum of the first subarray
    for i in range(0, k):
        res = res + arr[i]

    curr_sum = res
    # compute sum of other subarray: removing first element of last window and add last element of current window
    for i in range(k, n):
        curr_sum = curr_sum + arr[i] - arr[i-k]
        res = max(res, curr_sum)
    return res
    
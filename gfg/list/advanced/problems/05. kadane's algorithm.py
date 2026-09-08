'''
idea: traverse left to right, for each element find max sum subarray ending there
final answer = max of all these values

to find max sum ending at current element (maxEnding), use maxEnding from previous element
2 choices at each element:
- extend previous subarray by adding current element (better if prev maxEnding is positive)
- start a new subarray from current element (better if prev maxEnding is negative)

maxEnding[i] = max(maxEnding[i-1] + arr[i], arr[i])
answer = max value of maxEnding seen across all indices
'''
def maxSubarraySum(arr):
    n = len(arr)
    max_sum = arr[0]
    res = arr[0]
    for i in range(1, n):
        max_sum = max(max_sum+arr[i], arr[i])
        res = max(max_sum, res)
    return res
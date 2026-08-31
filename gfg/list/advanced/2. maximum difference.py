# find the maximum difference between any 2 elements of the array

# naive approach: O(n^2)
def MaxDiff(arr):
    n = len(arr)
    res = arr[1] - arr[0]
    for i in range(0, n-1):
        for j in range(i+1, n):
            res = max(res, arr[j]-arr[i])
    return res

# efficient approach: O(n)
# the max abs-diff in arr will always be the abs-diff between the min(low) and the max(high) element 
def MaxDiff(arr):
    n = len(arr)
    high, low = arr[0], arr[0]
    for i in range(1, n):
        high = max(high, arr[i])
        low = min(low, arr[i])
    return high-low
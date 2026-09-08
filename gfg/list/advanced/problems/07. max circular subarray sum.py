def maxNormalSum(arr):
    # kaden's algorithm
    n = len(arr)
    max_sum, res = arr[0], arr[0]
    for i in range(1, n):
        max_sum = max(max_sum+arr[i], arr[i])
        res = max(res, max_sum)
    return res

def maxCircularSum(arr):
    max_normal = maxNormalSum(arr)
    if max_normal<0:
        return max_normal
    sum = 0
    n = len(arr)
    for i in range(0, n):
        sum = sum + arr[i]
        arr[i] = -arr[i]
    max_circular = sum + maxNormalSum(arr)
    return max(max_normal, max_circular)
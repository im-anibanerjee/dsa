# given a circular array of size n, find the maximum subarray sum of the non-empty subarray

# MaxSub() is kaden's algorithm
def MaxSub(arr):
    n = len(arr)
    res = arr[0]
    max_ending = arr[0]
    for i in range(1, n):
        max_ending = max(max_ending+arr[i], arr[i])
        res = max(res, max_ending)
    return res

def CMaxSub(arr):
    n = len(arr)
    max_normal = MaxSub(arr)
    if max_normal<0:
        return max_normal

    sum = 0
    for i in range(0, n):
        sum = sum + arr[i]
        arr[i] = -arr[i]

    max_circular = sum + MaxSub(arr)
    return max(max_circular, max_normal)
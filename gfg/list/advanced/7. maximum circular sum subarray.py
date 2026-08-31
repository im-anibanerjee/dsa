# given a circular array of size n, find the maximum subarray sum of the non-empty subarray

# MaxSub() is kaden's algorithm to find max subarray sum
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
    # normal max subarray sum
    max_normal = MaxSub(arr)
    if max_normal<0:
        return max_normal

    # circular max subarray sum
    # compute the sum of array
    sum = 0
    for i in range(0, n):
        sum = sum + arr[i]
        # negating the array, to compute minimum subarray sum
        arr[i] = -arr[i]
    # here MaxSub(negated_array) is computing the minimum subarray sum
    max_circular = sum + MaxSub(arr)
    return max(max_circular, max_normal)
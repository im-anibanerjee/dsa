def maxEvenOdd(arr):
    n = len(arr)
    count, res = 1, 1
    for i in range(1, n):
        if (arr[i]%2==0 and arr[i-1]%2!=0) or (arr[i]%2!=0 and arr[i-1]%2==0):
            count = count + 1
            res = max(res, count)
        else:
            count = 1
    return res
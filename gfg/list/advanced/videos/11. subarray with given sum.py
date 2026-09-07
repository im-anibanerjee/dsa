# find subarray with a given sum (gsum)

# naive approach: O(n)
def SubSum(arr, gsum):
    n = len(arr)
    for i in range(0, n):
        sum = 0
        for j in range(i, n):
            sum = sum + arr[j]
            if sum==gsum:
                return True
    return False

def SubSum(arr, gsum):
    n = len(arr)
    # start from index 0
    start, sum = 0
    # i acts as the end (index)
    for i in range(0, n):
        # add current element to current sum
        sum = sum + arr[i]
        # reduce the sum from the left if the current sum exceeds the target
        while sum>gsum:
            # subtract the element at the start of the window
            sum = sum - arr[start]
            # move the start of the window forward
            start = start + 1
        # check if the current sum is equal to the target sum
        if sum==gsum:
            return True
    return False
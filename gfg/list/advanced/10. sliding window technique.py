# find the maximum sum of k consecutive elements
'''
compute sum of 1st k elements from n terms using a linear loop and store the sum
then will move linearly over the array till it reaches the end and simultaneously keep track of maximum sum
to get the current sum of block of k elements just 
    subtract the 1st element from the previous block and 
    add the last element of the current block
'''
def MaxSum(arr, k):
    n = len(arr)
    sum = 0
    # sum of 1st window
    for i in range(0, k):
        sum = sum + arr[i]
    res = sum
    # sum of next windows using sliding technique
    for i in range(k, n):
        sum = sum + arr[i] - arr[i-k]
        res = max(res, sum)
    return res
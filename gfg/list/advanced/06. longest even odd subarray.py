# given an array of N integers, the task is to find the length of the longest alternating-even-odd subarray

# efficient approach: O(n)
def LongEvenOdd(arr):
    n = len(arr)
    res, count = 1, 1
    for i in range(1, n):
        if (arr[i]%2==0 and arr[i-1]%2!=0) or (arr[i]%2!=0 and arr[i-1]%2==0):
            count = count + 1
            res = max(res, count)
        else:
            count = 1
    return res

'''
walking along the array building a "chain" (alternating streak)
each number can join the chain only if it's a different type (odd/even) than the one before it
if same type, chain breaks - but you don't vanish, you start a new chain of just yourself

example: 1, 2, 3, 3, 4
1: alone, chain = 1
2: diff type than 1, join chain, chain = 2
3: diff type than 2, join chain, chain = 3
3: same type as prev 3, chain breaks, start new chain of self, chain = 1 (not 0, you still exist)
4: diff type than prev 3, join new chain, chain = 2

longest chain seen = 3 (that's what 'res' tracks separately)
'''
'''
the cost of a stock on each day is given in an array
find the maximum profit that you can make by buying and selling on those days 

if the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
'''

# efficient approach: O(n)
'''
we just need to find the next greater element and subtract it from the current element 
so that the difference keeps increasing until we reach a minimum 

if the sequence is a decreasing sequence, so the maximum profit possible is 0
'''
def MaxProfit(arr):
    n = len(arr)
    profit = 0
    for i in range(1, n):
        if arr[i]>arr[i-1]:
            profit = profit + (arr[i]-arr[i-1])

    return profit
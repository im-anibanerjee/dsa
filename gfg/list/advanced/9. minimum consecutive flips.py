'''
given a binary array, we need to convert this array into an array that either contains all 1s or all 0s
we need to do it using the minimum number of group flip
'''
'''
there are only 2 groups (groups of 0s and groups of 1s)
either the counts of both groups are same or the difference between counts is atmost 1 i.e. 0 or 1 
for eg:
    {1, 1, 0, 1, 0, 0} there are two groups of 0s and two groups of 1s
    {1, 1, 0, 0, 0, 1, 0, 0, 1, 1} count of groups of 1 is one more than the counts of 0s
so if the start and end are same then group counts differ by 1, and 
if start and end are different then group counts is same

so if we always flip the second group and other groups of the same type as the second group we always get min flips
for 1st case, when group counts are the same, it does not matter which group type we flip as both will lead to min flips  
for 2nd case, when group counts differ by 1, flipping 2nd group will give min flips
'''
def MinFlips(arr):
    n = len(arr)
    for i in range(1, n):
        # new group started
        if arr[i]!= arr[i-1]:
            '''           
            check if this group belongs to the 1st or 2nd group
            if belongs to the 2nd group, start flipping from here
            '''
            if arr[i]!=arr[0]:
                print(f'from: {i} to ', end="")
            # if this belongs to the 1st group, end flip till (i-1)
            else:
                print(i-1)
                print()
    # array ended mid flip-group (never closed inside loop) - close it here using last index
    if arr[n-1]!=arr[0]:
        print(n-1)

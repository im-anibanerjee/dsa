# given an integer x, find its square root;  if x is not a perfect square, then return floor(√x)

def sqRoot(x):
    # base case
    if x==0 or x==1:
        return x

    # binary search for floor(sqrt(x))
    start = 1
    end = x//2
    while start<=end:
        mid = (start+end)//2
        # if x is a perfect square
        if mid**2==x:
            return mid  
        '''
        since we need floor, update ans when mid**2<x, and move closer to sqrt(x)
        
        want floor(sqrt(x)), largest integer whose square doesn't exceed x
        not searching for one exact match, tracking best valid candidate seen so far
        '''
        if mid**2<x:
            start = mid+1
            ans = mid
        else:
            # mid**2>x
            end = mid-1
    return ans
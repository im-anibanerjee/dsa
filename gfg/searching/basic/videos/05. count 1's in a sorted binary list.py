# count 1's in a sorted binary list

def fOccurrence(arr, l, r, x):
    while l<=r:
        mid = l+(r-l)//2
        # if x is greater ignore left half; go to right half
        if arr[mid]<x:
            l = mid+1
        # if x is smaller ignore right half; go to left half
        elif arr[mid]>x:
            r = mid-1
        else:
            '''
            arr[mid]==x 
                and mid==0 or arr[mid]!=arr[mid-1]: confirms 1st occurrence; return mid
                and mid!=0 or arr[mid]==arr[mid-1]: confirms this is not the 1st occurrence; ignore right half; move to left half
            '''
            if (mid==0 or arr[mid]!=arr[mid-1]):
                return mid
            else:
                r = mid-1
    return -1

def count1(arr):
    n = len(arr)
    first = fOccurrence(arr, l=0, r=(n-1), x=1)
    # 1 is not there in the list
    if first==-1:
        return -1
    else:
        '''
        sorted binary list can be all 0, all 1 or mix of 0 and 1
        so if we have the first occurrence, the last occurrence will always be (n-1)
        '''
        # return (last-first)+1
        return ((n-1)-first)+1
# count occurrences in a sorted array
def fOccurrence(arr, x, l, r):
    while l<=r:
        mid = l+(r-l)//2
        # if x is greater ignore left half; go to right half
        if arr[mid]<x:
            l = mid+1
        elif arr[mid]>x:
        # if x is smaller ignore right half; go to left half
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

def lOccurrence(arr, x, l, r):
    n = len(arr)
    while l<=r:
        mid = l+(r-1)//2
        # if x is greater ignore left half; go to right half
        if arr[mid]<x:
            l = mid+1
        # if x is smaller ignore right half; go to left half
        elif arr[mid]>x:
            r = mid-1
        else:
            '''
            arr[mid]==x 
                and mid==(n-1) or arr[mid]!=arr[mid+1]: confirms last occurrence; return mid
                and mid!=(n-1) or arr[mid]==arr[mid+1]: confirms this is not the last occurrence; ignore left half; move to right half
            '''
            if (mid==(n-1) or arr[mid]!=arr[mid+1]):
                return mid
            else:
                l = mid+1

    
def countOccurrences(arr, x):
    n = len(arr)
    first = fOccurrence(arr, x, l=0, r=(n-1))
    last = lOccurrence(arr, x, l=0, r=(n-1))
    return (last-first)+1
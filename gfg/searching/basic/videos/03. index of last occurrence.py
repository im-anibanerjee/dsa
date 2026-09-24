# find the last occurrence in a sorted array; possibly duplicate elements

def lOccurrence(arr, l, r, x):
    n = len(arr)
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
                and mid==(n-1) or arr[mid]!=arr[mid+1]: confirms last occurrence; return mid
                and mid!=(n-1) or arr[mid]==arr[mid+1]: confirms this is not the last occurrence; ignore left half; move to right half
            '''
            if (mid==(n-1) or arr[mid]!=arr[mid+1]):
                return mid
            else:
                l = mid+1
    # if reached here, element is not present
    return -1



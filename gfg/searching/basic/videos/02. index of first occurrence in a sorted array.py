# find the first occurrence in a sorted array; possibly duplicate elements

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
    # if reached here, element is not present
    return -1



# binary search; search in a sorted array

'''
l: left half of the array; index=0
r: right half of the array; index=(n-1)

mid = (l+r)//2 and mid = l+(r-l)//2 always give the exact same result mathematically
both find the same midpoint, difference is only about a rare technical safety issue

in fixed-size integer languages (java, c++), l+r is computed first as its own value
if l and r are both very large, l+r can exceed the max integer limit and overflow
overflow wraps the number into garbage, corrupting the whole calculation

l+(r-l)//2 avoids this, since r-l is always small (just the search range size)
never creates a large intermediate value, so nothing can overflow

python integers have no fixed size, they grow as needed automatically
so l+r can never overflow in python, both versions are equally safe here
'''
def binarySearch(arr, l, r, x):
    while l<=r:
        mid = l+(r-l)//2
        # if x is at mid
        if arr[mid]==x:
            return mid
        # if x is greater ignore left half; go to right half
        elif arr[mid]<x:
            l = mid+1
        # if x is smaller ignore right half; go to left half
        else:
            # arr[mid]>x
            r = mid-1
    # if reached here, element is not present
    return -1

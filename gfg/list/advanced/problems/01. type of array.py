'''
sorted array never breaks pattern - always going up, or always going down
rotated sorted array has exactly ONE break - because rotation cuts the array
once and glues that piece to the other end, creating one seam

example: deck of cards sorted king to ace, cut once and bottom chunk moved to top
flipping through still decreases smoothly, except at exactly one point where
it jumps from a low card back to a high card - that's the one "cut point"

so instead of finding rotation amount, just count the breaks:
- 0 breaks -> purely sorted (ascending or descending)
- 1 break  -> rotated version

walk through array once, comparing arr[i] and arr[i+1]:
- rises = count of arr[i] < arr[i+1] (went up)
- dips  = count of arr[i] > arr[i+1] (went down)
since elements are unique, rises + dips always = n-1
'''

def typeOfArr(arr):
    n = len(arr)
    raises = 0  # arr[i]<arr[i+1] or arr[i+1]>arr[i], going up
    dips = 0    # arr[i]>arr[i+1] or arr[i+1]<arr[i], going down 
    for i in range(0, n-1):
        if arr[i]<arr[i+1]:
            raises = raises + 1
        if arr[i]>arr[i+1]:
            dips = dips + 1

    if raises==0:
        return 2 # pure descending order
    if dips==0:
        return 1 # pure ascending order
    if raises==1: 
        return 3 # descending rotated order
    if dips==1:
        return 4 # ascending rotated order

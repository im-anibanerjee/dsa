def maxIndexDiff(arr):
    n = len(arr)
    left = [0]*n 
    right = [0]*n
    '''
    left[]: left_min[], right: right_max[]
    so for an index i: 
        left[i] or left_min[i] denotes its corresponding min element on left
        right[i] or right_max[i] desnotes the correspinding max element on right
    '''
    # filling the left[]
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = min(left[i-1], arr[i])

    # filling the right[]
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    # calculating the max diff
    i, j = 0, 0
    max_diff = -1
    while i<n and j<n:
        if left[i]<=right[j]:
            max_diff = max(max_diff, j-i)
            j = j+1
        else:
            i = i+1

    return max_diff
# left rotate by d places

def LRotate(arr, d):
    # slicing technique
    arr = arr[d:] + arr[:d]
    '''
    for right rotate: arr = arr[-d:] + arr[:-d]
    '''
    return arr

'''
find the majority element in the array 
a majority element in an array  of size n is an element that appears more than n/2 times
'''

# naive approach: O(n^2)
def Majority(arr):
    n = len(arr)
    for i in range(0, n):
        count = 1
        for j in range(i+1, n):
            if arr[i]==arr[j]:
                count = count + 1
        if count>n/2:
            return i
    return -1

# efficient approach: O(n)
'''
majority element using moore's voting algorithm
the first step gives the element that may be the majority element in the array 
if there is a majority element in an array, then this step will definitely return majority element
otherwise, it will return candidate for majority element

the second step checks if the element obtained from the above step is the majority element
this step is necessary as there might be no majority element

if the question mentions that there will always be a majority element, then no need to run the second step as mentioned above
also this solution doesnot guarantee that it will always return the index of the first occurrence of the majority element
'''
def Majority(arr):
    n = len(arr)
    # first step: returns the candidate
    # assuming arr[0] is the majority element
    res = 0
    count = 1
    for i in range(1, n):
        if arr[res]==arr[i]:
            count = count + 1
        else:
            count = count - 1
        if count==0:
            res = i
            count = 1
    # second step: checks if the candidate is the majority element
    count = 0
    for i in range(0, n):
        if arr[res]==arr[i]:
            count = count + 1
    if count<=n/2:
        return -1
    return res
'''
array [4, 0, 2, 1, 3] can be thought of as 5 boxes, indices 0 to 4
each box should become the value in the box it points to, that's the whole task

broken way: just overwrite box by box, left to right
box 0 points to box 4, overwrite box 0 with 3, now box 0 = 3
box 1 points to box 0, but box 0 already got destroyed, no longer holds original 4
later boxes lose the original value of earlier boxes before they can read it

fix: don't fully erase old value, hide a trace of it inside the new stored number
new stored number = old_value + new_value * n
old_value is small, always less than n, lives safely in the ones place
new_value * n is a big multiple of n, sits on top of it

% n always removes any exact multiple of n, only new_value*n is a multiple of n
so old_value + new_value*n, when modded by n, always leaves just old_value behind
this works no matter how big new_value is, or whether the box was touched already

redo the walk with protection:
box 0: old=4, points to box 4 (still 3, untouched), new = 4 + 3*5 = 19
box 1: old=0, points to box 0 (now 19), 19%5=4 recovers original box 0 value, new = 0 + 4*5 = 20
box 2: old=2, points to itself (still 2, untouched), 2%5=2, new = 2 + 2*5 = 12
box 3: old=1, points to box 1 (now 20), 20%5=0 recovers original box 1 value, new = 1 + 0*5 = 1
box 4: old=3, points to box 3 (now 1), 1%5=1 recovers original box 3 value, new = 3 + 1*5 = 8

after this pass: [19, 20, 12, 1, 8]
final pass, divide by n to strip old value, keep only new: [3, 4, 2, 0, 1]
matches expected output

core idea: each box holds old and new stacked together
% n always digs out the true original value, even after that box was already updated
nothing is lost, just disguised, until the final // n pass strips the disguise everywhere
'''
def inPlace(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] + (arr[arr[i]]%n)*n
    for i in range(n):
        arr[i] = arr[i]//n
    return arr
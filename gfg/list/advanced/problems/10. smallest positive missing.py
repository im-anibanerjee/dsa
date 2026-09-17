'''
goal: find smallest positive number missing from arr, array can have negatives and duplicates too

brute force: check 1, 2, 3... one by one if present in arr, stop at first missing
too slow, checking presence each time scans whole array, overall O(n^2)

key insight: answer can never be bigger than n+1
with n boxes, to have every number 1 to n present needs exactly n slots
so answer always lies in range [1, n+1], never care about numbers bigger than n
this is why the while loop only checks values in range 1 to n, anything outside
can never be the answer, so no point placing it anywhere, just skip it
this is also why the fallback answer is exactly n+1, not some other guess
if 1 to n are all present, n+1 is the smallest positive number that could not fit

idea: use array positions themselves as a checklist, no extra array needed
rule: a value v (only if 1<=v<=n) belongs at position v-1
so value 1 belongs at position 0, value 2 belongs at position 1, and so on

example: arr = [2, -3, 4, 1, 1, 7], n = 6
position0: holds 2, home is position 1, not here, swap -> arr becomes [-3,2,4,1,1,7]
position0 now holds -3, out of range, stop, move on
position1: holds 2, home is position 1, already correct, move on
position2: holds 4, home is position 3, not here, swap -> arr becomes [-3,2,1,4,1,7]
position2 now holds 1, home is position 0, not here, swap -> arr becomes [1,2,-3,4,1,7]
position2 now holds -3, out of range, stop, move on
position3: holds 4, home is position 3, already correct, move on
position4: holds 1, home is position 0, already holds 1 (duplicate), dont swap, move on
position5: holds 7, out of range for n=6, skip entirely

final array: [1, 2, -3, 4, 1, 7]
scan: position0 holds 1, expected 1, match
position1 holds 2, expected 2, match
position2 holds -3, expected 3, mismatch -> answer is 3

why negatives dont break anything: caught by 1<=arr[i]<=n check, skipped immediately, never swapped
why duplicates dont break anything: caught by arr[arr[i]-1]!=arr[i] check
if home position already holds the same value, dont swap, avoids infinite loop and wrong overwrite

why swap works for correctness:
overwriting directly would destroy original value before it gets checked/placed
swapping never deletes a value, it only relocates it, so nothing is lost mid-process

while loop inside for loop is needed because after one swap, the new value landing
at this position might also be out of place, so keep checking and swapping until
either value is at correct home, or value is out of range (no home exists)

final scan: check each position i, does it hold i+1
first mismatch found -> that i+1 is the missing number
if no mismatch found anywhere -> every number 1 to n was present, answer is n+1
'''
def missingNumber(arr):
    n = len(arr)
    # visit every position once
    for i in range(n):
         # place every value v (1<=v<=n) at its correct position, v-1
         # keep going while value is in range and not already at its home position
        while (1<=arr[i]<=n) and (arr[arr[i]-1]!=arr[i]):
            # home position for the current value
            corr_pos = arr[i]-1
             # swap current value into its home, pull back whatever was there
            arr[i], arr[corr_pos] = arr[corr_pos], arr[i]

    # scan for the first position that doesn't hold position+1
    for i in range(n):
        if arr[i]!= i+1:
            return i+1

    # everything from 1 to n was present, so the answer is n+1
    return n+1
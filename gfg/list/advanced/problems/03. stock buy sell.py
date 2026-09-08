def stockBuySell(arr):
    n = len(arr)
    profit = 0
    for i in range(1, n):
        if arr[i]>arr[i-1]:
            profit = profit + (arr[i]-arr[i-1])
    return profit
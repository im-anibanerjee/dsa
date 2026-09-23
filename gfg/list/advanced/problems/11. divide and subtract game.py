def divAndSub(n):
    arr = [False]*(n+1)
    # arr[i]= True means: the player to move at i can win
    # arr[0] stays False; no legal move from 0, so whoever's turn it is loses

    # fill the table left to right, i=1 is never a real state we sit at
    for i in range(2, n+1):
        moves = []
        # divide
        for d in [2,3,4,5]:
            moves.append(i//d)   
        # subtract      
        for s in [2,3,4,5]:
            if (i-s)>=0:
                moves.append(i-s)       

        can_win = False
        for j in moves:
            if j==1:
                # moving to 1 makes the mover lose; this move is bad, skip it as a winning option
                continue
            if j==0:
                # moving to 0, opponent has no move; current player wins
                can_win = True
                break
            if not arr[j]:
                 # opponent lands on a losing position, current player wins
                can_win = True
                break
        arr[i] = can_win

    return 'Jon' if arr[n] else 'Arya'

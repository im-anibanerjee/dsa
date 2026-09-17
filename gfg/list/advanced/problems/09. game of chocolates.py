'''
game: two boxes with a and b chocolates, eat L from one box or same L from both, last to eat wins
both players want dolly to win, need to find who should play first

position = the pair (a,b), that alone fully describes the game state
losing position = whoever moves next here loses no matter what they do
winning position = whoever moves next here can find some move that traps the opponent

base case (0,0): no chocolates left, no moves possible, previous player already ate last one and won
so (0,0) is a losing position for whoever's turn it is there

rule to classify any position:
winning if any move leads to a losing position for opponent
losing if every possible move only leads to winning positions, no escape

brute forced small positions by simulating every move recursively
found losing positions: (0,0), (1,2), (3,5), (4,7), (6,10)
notice the difference b-a increases by exactly 1 each time: 0,1,2,3,4
notice the smaller number does not follow a simple pattern like 0,1,2,3,4, it skips numbers

build the same table by hand using a simple greedy rule instead of guessing a formula
rule: smaller number of row k = smallest number not used in any earlier row
bigger number of row k = smaller number + k
this greedy table exactly matches the brute forced losing positions

turns out this greedy table's smaller number always equals floor(k * golden ratio)
golden ratio phi = (1 + sqrt(5)) / 2, approximately 1.618
this is a proven mathematical fact, not something derived from scratch here
it just gives a fast formula instead of building the whole table by hand

why table entries are losing positions: no move from one table row can ever reach another table row
every move from a table entry lands off the table, handing opponent a winning spot
that property is what makes them genuinely losing positions

so in short: every losing position sits in a table built by that simple greedy rule
k = |a - b| tells us which row of the table to check against
floor(k * phi) tells us what the smaller number of that row should be
if actual smaller number matches -> genuinely a losing position -> bunty goes first
if it does not match -> not on the table -> winning position -> dolly goes first

verified against given examples
a=1,b=2: k=1, expected smaller=floor(1*1.618)=1, matches actual smaller 1, so false
a=1,b=3: k=2, expected smaller=floor(2*1.618)=3, actual smaller is 1, no match, so true
'''
def game(a, b):
    phi = (1+5**0.5)/2  # golden ratio
    k = abs(a-b)
    actual_small = min(a,b)
    expected_small = int(k*phi)

    if actual_small==expected_small:
        return False # losing pos; bunty should move first
    else:
        return True # winning pos; dolly should move first
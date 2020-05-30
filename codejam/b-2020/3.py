t = int(input())


global_moves = []

def calc(R, S, swaps = 0):

    if R == 1:

        return swaps

    else:

        for i in range(1, S     ):
            global_moves.append((R * S - S * i, R - 1))

        print(R -1 ,S)
        return calc(R - 1, S , swaps + S - 1)

for i in range(1, t + 1):
    
    R, S = [int(n) for n in input().split()]


    print("Case #{}: {}".format(i, calc(R,S)))
    for move in global_moves:
        print(move)
    global_moves = []
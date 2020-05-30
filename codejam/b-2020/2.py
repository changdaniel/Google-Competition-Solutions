from sys import stdin


def calc_throw(miss_throws, hit_throws):

    if hit_throws:
        
        hit = hit_throws[0]

        x1 = y1 = x2 = y2 = 0

        for x,y in miss_throws:

            if x:
                pass

    
t, a, b = [int(n) for n in stdin.readline().split()]
status =  "MISS"


for _ in range(t):

    miss_throws = []
    hit_throws = []

    good_x = [-500000000, 0, 500000000]
    good_throws = [(x,y) for x in good_x for y in good_x]

    while status is not "CENTER":

        throw = good_throws.pop() if good_throws else (1,1)

        print("{} {}".format(throw[0], throw[1]), flush = True)

        status = input()

        if status == "HIT":
            hit_throws.append(throw)
        else:
            miss_throws.append(throw)
        





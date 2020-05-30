from sys import stdin

l1,r1,l2,r2,k=[int(i) for i in stdin.readline().split(" ")]

# l = [(l1,r1), (l2, r2)]
# l.sort(key=lambda x:x[0])


total =  min(r1, r2) - max(l1, l2) + 1

if max(l1,l2) <= k <= min(r1,r2):
    total -= 1

if total < 0:

    print(0)
else:
    print(total)
import sys

n = int(sys.stdin.readline())
line = [int(x) for x in sys.stdin.readline().split()]

set1 = set()
set2 = set()
set3 = set()
counter = 0

for x in line:
    if x in set3:
        counter += 1
    if x in set1:
        continue
    for z in set2:
        set3.add(x + z)
    for y in set1:
        set2.add(x + y)
        set3.add(2*x + y)
    set1.add(x)
    set2.add(2*x)
    set3.add(3*x)

print(counter)
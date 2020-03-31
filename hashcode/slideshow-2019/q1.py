from sys import stdin, argv
from collections import deque

N = int(stdin.readline())

pictures = [(line.split(" ")[0], set([j.split("\n")[0] for j in line.split(" ")[2:]]), i) for i, line in enumerate(stdin.readlines())]
h_pictures = [i for i in pictures if i[0] == "H"]
v_pictures = [i[1:] for i in pictures if i[0] == "V"]


v_pictures.sort(key	= lambda x: len(x[0]), reverse=True)
if len(v_pictures) % 2:
	v_pictures.pop()

for i in range(len(v_pictures)//2):
    new_h = ("V", v_pictures[i][0]|v_pictures[-1* (i+1)][0], (v_pictures[i][1], v_pictures[-1*(i+1)]))
    h_pictures.append(new_h)

# counts = dict()
# for pic in pictures:
#     for theme in pic[1]:
#         counts[theme] = counts.get(theme, 0 ) + 1

def calculate_interest(a, b):
    both = len(a[1] & b[1])
    left = len(b[1]) - both
    right = len(a[1]) - both

    return min(both, left, right)


def calculate_total(a,b):

    return len(a[1] | b[1])

#construct h pictures from v pictures

# new_h_pictures = []
# v_heap = heapq.heapify(v_pictures, lambda x: len(x[1]))
# while v_heap:
#     length = len(v_heap)
#     median = v_heap[length//2]
#     del v_heap[length//2]

    
#     for v in v_heap:

def calculate_max2(a, arr):
    cur_max = -1
    for i in range(len(arr)):
        b = arr[i]
        if calculate_interest(a, b) > cur_max:
            cur_max = calculate_interest(a,b)
            index = i
    
    return (cur_max, index)

def calculate_max(first, last, arr):
    cur_max = -1
    for i in range(len(arr)):
        b = arr[i]
        if calculate_interest(first, b) > cur_max:
            which = True
            cur_max = calculate_interest(first,b)
            index = i
        elif calculate_interest(last, b) > cur_max:
            which = False
            cur_max = calculate_interest(first,b)
            index = i
    
    return (cur_max, index, which)

"""
Algorithm for getting order of all h_pictures
1. Select picture with median themes
2. Calculate interest for first one
"""
length = len(h_pictures)
result = deque()
h_pictures.sort(key = lambda x: len(x[1]))
result.append(h_pictures[length//2])
del h_pictures[length//2]

maximum, i = calculate_max2(result[0], h_pictures)
result.append(h_pictures[i])
del h_pictures[i]
counter = 0
score = 0
while len(result) != length:
    counter += 1
    first, last = result[0], result[-1]
    some_maximum, some_index, which = calculate_max(first, last, h_pictures)


    if which:
        result.appendleft(h_pictures[some_index])
    else:
        result.append(h_pictures[some_maximum])
    
    score += some_maximum
    del h_pictures[some_index]

    print(counter, score)



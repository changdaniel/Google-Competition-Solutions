from itertools import combinations
from sys import argv, stdin
from pprint import pprint
from collections import defaultdict

slices, num_types = [int(i) for i in stdin.readline().split(" ")]
#(val, index)
types = [(int(i), j) for j,i in enumerate(stdin.readline().split(" "))]



dp = [-1 for _ in range(slices)]
best_slices = [0]
best_score = slices - types[0][0]


def subset_sum(types, slices):
    counter = 0
    length = len(types)
    subset = [[False] * (slices + 1) for _ in range(length + 1)]
    #figuring out which is best
    map = defaultdict()
    best = slices
    best_combo = []

    for i in range(length + 1):
        subset[i][0] = True

        for i in range(1,slices+1): 
            subset[0][i]=False
              

        for i in range(1,length+1): 
            for j in range(1,slices+1):
                counter += 1

                # map[(i, j)] = 
                #case when "undershoot"
                if j<types[i-1][0]:
                    subset[i][j] = subset[i-1][j]
                #case when "overshoot"
                if j>=types[i-1][0]: 
                    subset[i][j] = (subset[i-1][j] 
                    or subset[i - 1][j- types[i-1][0]])

                if counter % 10000000 == 0:
                    print(counter)
                    

    
    #perfect case
    if subset[length][slices]:
        print(True)
    else:
        # pprint(subset)
        print(False)



subset_sum(types, slices)


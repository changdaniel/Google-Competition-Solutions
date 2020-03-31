from itertools import combinations
from sys import argv, stdin

slices, num_types = [int(i) for i in stdin.readline().split(" ")]
#(val, index)
types = [(int(i), j) for j,i in enumerate(stdin.readline().split(" "))]



closest_combination = [0]
closest = slices - types[0][0]

for i in range(1, num_types + 1):
    for combination in combinations(types, i):
        
        score = sum([i[0] for i in combination])

        if slices - score >= 0 and slices - score < closest:
            closest = slices - score
            print(closest)
            closest_combination = [i[1] for i in combination]
    

file1 = open(str(argv[1]) + ".txt","a")

output = str(len(closest_combination)) + "\n"
for i in closest_combination: output += str(i) + " "
output += "\n"
file1.write(output)
print(output)

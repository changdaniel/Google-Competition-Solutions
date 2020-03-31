from sys import stdin
sdfdsfsfds

slices, num_types = [int(i) for i in stdin.readline().split(" ")]
types = [(int(i), j) for j,i in enumerate(stdin.readline().split(" "))]
types = sorted(types, key = lambda x: x[0])



counter = 0
arr = []
for t in types:
    if counter + t[0] > slices:
        break
    else:
        counter +=  t[0]
        arr.append(t[1])


file1 = open("f.txt","a")

output = str(len(arr)) + "\n"
for i in arr: output += str(i) + " "
output += "\n"
file1.write(output)
print(output)

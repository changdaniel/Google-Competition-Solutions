from sys import stdin, stdout
T, B = [int(i) for i in stdin.readline().split()]


for cur_t in range(T, 0, -1):

    string = ""

    for j in range(10):
        string += "0"
    
    for i in range(1, 11):
        print(i, flush = True)
        char = input()
        string = list(string)
        string[i - 1] = char
        string = "".join(string)


    print(string, flush =  True)
    if input() == "Y":
        continue
    else:
        break

from sys import stdin

T = int(stdin.readline())
strings = [x for x in stdin.readlines()]


holder = []
for string in strings:

    counter = 0


    arr =  [x for x in string]
    dict = {"I": 0 , "i": 0, "o":0, "O": 0}
    for c in arr:

        if c == "I" or c =="i":
            dict[c] += 1
        if c == "O":

            if dict["I"] > 0:
                dict["I"] -= 1
                counter += 1
            else:
                dict["I"] -= 1
        
        if c == "o":
            if dict["i"] > 0:
                dict["i"] -= 1
            else:
                dict["I"] -= 1
    
    holder.append(counter)



for i in range(1, T + 1):
    
    print("Case #" + str(i) + ": " + str(holder[i - 1]))
    
from collections import Counter

string = input()

def get_moves(s1, s2):

    counter1 = Counter(s1)
    counter2 = Counter(s2)

    # for k, v in c1.items():

    #     c2[k] -= v
    
    # total = 0
    # print(c2)
    # for v in c2.values():

    #     total += abs(v)

    c1 = set(s1)
    c2 =  set(s2)

    outer1 = c1 - c2
    outer2 = c2 - c1

    total = 0

    for c in outer1:
        total += counter1[c]
    
    for c in outer2:
        total += counter2[c]
    
    return total

end = float('inf')
for i in range(len(string)):
    
    end = min(get_moves(string[:i],string[i:]), end)

print(end)

# print(get_moves('bsuitisawe','some'))


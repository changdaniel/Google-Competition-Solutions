from sys import stdin,stdout

T = int(input())

def read_activities():

    N = int(input())
    intervals = []
    for i in range(N):
        intervals.append(([int(n) for n in stdin.readline().split(" ")], i))
    
    return intervals

result = ""

for t in range(1, T+1):

    schedule = read_activities()
    num_activities = len(schedule)
    results = ['' for _ in range(num_activities)]
    occupied = {'C': [0 for _ in range(1440)], 'J': [0 for _ in range(1440)]}
    impossible = False

    schedule.sort(key=lambda x: (x[0][0], x[0][1]))

    for activity in schedule:

        if not sum(occupied['C'][activity[0][0]:activity[0][1]]):
            results[activity[1]] = 'C'

            for i in range(activity[0][0], activity[0][1]):
                occupied['C'][i] = 1

        elif not sum(occupied['J'][activity[0][0]:activity[0][1]]):
            
            results[activity[1]] = 'J'
            for i in range(activity[0][0], activity[0][1]):
                occupied['J'][i] = 1

        else:
            impossible = True
            result += "Case #{}: {}\n".format(t, "IMPOSSIBLE")
            break

    if not impossible:
        answer = ''.join(results)
        result += "Case #{}: {}\n".format(t, answer)

stdout.write(result)
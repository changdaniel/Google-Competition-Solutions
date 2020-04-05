from sys import stdin
import heapq
T = int(input())

def read_activities():

    N = int(input())
    intervals = []
    for i in range(N):
        intervals.append([int(n) for n in stdin.readline().split(" ")] + [i])
    
    return intervals


schedules = []

for i in range(T):
    schedules.append(read_activities())


def assign_schedules(schedule):

    assigned_task = [None for _ in schedule] 
    schedule.sort(key = lambda x: x[0])
    heap = [(schedule[0][1], schedule[0])]
    cur_person = True
    for task in schedule[1:]:
        ignore, latest_task = heapq.heappop(heap)
        start, end, i = task

        if start < latest_task[1]:
            heapq.heappush(heap, (ignore, latest_task))
        else:
            assigned_task[latest_task[2]] = cur_person
            cur_person = not cur_person
        
        heapq.heappush(heap, (task[1], task))
    
    if len(heap) > 2:
        return "IMPOSSIBLE"
    elif not heap:
        pass
    else:
        tasks = []
        while heap:
            ignore, cur_task = heapq.heappop(heap)
            tasks.append(cur_task)
        
        tasks.sort(key = lambda x:x[0])

        for cur_task in tasks:
            assigned_task[cur_task[2]] = cur_person
            cur_person = not cur_person

    assignments = ""
    for task in assigned_task:
        assignments += "C" if task else "J"

    return assignments

for i, schedule in enumerate(schedules,1):

    print("Case #{}: {}".format(i, assign_schedules(schedule)))



    
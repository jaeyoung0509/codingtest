import heapq
def solution(jobs):
    heap = []
    cnt = 0 
    answer = []
    start  , now = -1 , 0
    jobs.sort(key=lambda x: x[1])
    while 1 :
        for job in jobs:
            if start < job[0] <= now :
                #print(start  , now , job)
                heapq.heappush(heap , [job[1] , job[0]]) 
        if heap:
            cnt+=1
            temp = heapq.heappop(heap) #3, 0  3 4
            start = now
            now += temp[0]
            answer.append(now-temp[1])
        elif cnt == len(jobs):
            return int(sum(answer) / len(answer))   
        else:
            now +=1 
jobs=		[[0, 10], [2, 3], [9, 3]]
q = solution(jobs)
print(q)
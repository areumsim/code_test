import heapq


def solution(jobs):
    jobs.sort(key=lambda x: x[0])  # 시작 시간 기준으로 정렬, [st, time]
    cnt = len(jobs)
    now, total_time = 0, 0
    heap = []

    while jobs or heap:
        # 현재 시간 이하로 시작 가능한 모든 작업을 힙에 추가
        while jobs and jobs[0][0] <= now:
            heapq.heappush(
                heap, jobs.pop(0)[::-1]
            )  # 작업 시간을 기준으로 최소 힙 구성, heapq에는 [time, st] 순으로 저장

        if heap:
            # 힙에서 작업 시간이 가장 짧은 작업을 추출
            time, st = heapq.heappop(heap)
            now += time
            total_time += now - st
        else:
            # 힙이 비어있으면 다음 작업의 시작 시간으로 점프
            now = jobs[0][0]

    return total_time // cnt  # 평균 시간 계산


print(solution([[1, 9], [2, 6], [0, 3]]))  # 9
print(solution([[0, 3], [1, 9], [2, 6]]))  # 9

# que.put((2, 'Cherry'))

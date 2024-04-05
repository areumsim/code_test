## 바위를 적게 제거할수록 간격이 작고, 많이 제거할수록 간격이 넓어진다.


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)  # 도착점추가

    start, end = 0, distance
    while start <= end:
        mid = (start + end) // 2  # '최소 거리'
        min_distance = distance  # 최소 거리를 최대로 초기화
        current = 0  # 현재 위치
        remove_count = 0  # 제거한 바위의 수

        for rock in rocks:
            diff = rock - current  # 현재 바위와 'rock' 사이의 거리

            if diff < mid:
                remove_count += 1  # 'rock' 제거
            else:  # mid보다 크거나 같으면, 현재 위치/최소 거리 업데이트
                current = rock
                min_distance = min(min_distance, diff)

        # 제거한 바위의 수가 n보다 많으면, 최대 거리를 줄임
        if remove_count > n:
            end = mid - 1
        else:  # 제거한 바위의 수가 n보다 적거나 같으면, 최소 거리를 늘리고 정답을 갱신
            start = mid + 1
            answer = mid

    return answer


solution(25, [2, 14, 11, 21, 17], 2)

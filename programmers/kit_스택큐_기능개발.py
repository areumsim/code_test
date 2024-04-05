import math


def solution(progresses, speeds):
    releases = []
    days_needed = [
        math.ceil((100 - progress) / speed)
        for progress, speed in zip(progresses, speeds)
    ]

    max_day = days_needed[0]
    cnt = 1

    for day in days_needed[1:]:
        if day <= max_day:
            cnt += 1
        else:
            releases.append(cnt)
            cnt = 1
            max_day = day

    releases.append(cnt)
    return releases


solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])  # [1, 3, 2]
solution([93, 30, 55], [1, 30, 5])  # [2, 1]

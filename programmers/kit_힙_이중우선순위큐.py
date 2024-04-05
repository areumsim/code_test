import heapq


def solution(operations):
    answer = []

    # heapq.heapify(answer)
    for operation in operations:
        op, value = operation.split(" ")
        if op == "I":
            heapq.heappush(answer, int(value))
        elif len(answer) > 0:
            if value == "-1":  # 최소값 삭제
                heapq.heappop(answer)
            elif value == "1":  # 최대값 삭제
                answer.remove(max(answer))

    if len(answer) == 0:
        return [0, 0]

    return [max(answer), min(answer)]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))  # [0,0]
print(
    solution(
        ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    )
)  # 	[333, -45]

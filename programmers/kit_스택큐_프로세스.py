def solution(priorities, location):
    heap_q = [[idx, x] for idx, x in enumerate(priorities)]

    result = []
    while heap_q:
        cur = heap_q.pop(0)
        if any(cur[1] < q[1] for q in heap_q):
            heap_q.append(cur)
        else:
            if cur[0] == location:
                return len(result) + 1

            result.append(cur[0])

    return len(result) + 1


solution([2, 1, 3, 2], 2)  # 	1
solution([1, 1, 9, 1, 1, 1], 0)  # 	5

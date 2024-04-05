# ####### Heap 사용하지 않고 / timeout 발생 #######
# def solution(scoville, K):
#     answer = 0
#     scoville.sort()

#     while scoville[0] < K:
#         if len(scoville) <= 1:
#             return -1
#         new_scoville = scoville.pop(0) + (scoville.pop(0) * 2)
#         scoville.append(new_scoville)
#         scoville.sort()
#         answer += 1

#     return answer


import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        heapq.heappush(
            scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        )
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))

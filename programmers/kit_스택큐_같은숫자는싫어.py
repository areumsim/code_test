def solution(arr):
    answer = []

    tmp = arr[0]
    for i in arr[1:]:
        if i == tmp:
            continue
        else:
            answer.append(tmp)
            tmp = i
    answer.append(tmp)

    return answer


solution([1, 1, 3, 3, 0, 1, 1])  # [1,3,0,1]
solution([4, 4, 4, 3, 3])  # [4,3]

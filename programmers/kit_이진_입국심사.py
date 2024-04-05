# 입국 심사를 기다리는 사람 : n
# 각 심사관이 한명을 심사하는데 걸리는 시간 : times


def solution(n, times):
    answer = 0

    if len(times) == 0:
        return 0

    st = min(times)
    ed = (n // len(times) + 1) * sum(times)  # max(times) * n
    ## ed :  모든 심사관이 동일한 명수를 처리했을 때 걸리는 시간
    ## (원래 ed는 가장 오래 걸리는 심사관이 모두 처리했을 때의 시간(근데 어차피 최대값일수없으니까))

    while st <= ed:
        mid = (st + ed) // 2  # 중간 인덱스

        checked = 0  # 심사관들이 mid 동안 심사한 사람의 수
        for time in times:
            checked += mid // time

            # 심사관 남음 / mid 동안 n명 이상 심사 가능 -> left
            if checked >= n:
                break

        # 심사한 사람의 수가 n보다 큼 / 심사관 남음 -> left
        if checked >= n:
            answer = mid
            ed = mid - 1
        # 심사한 사람의 수가 n보다 적음 / 심사관 부족 -> right
        elif checked < n:
            st = mid + 1

    return answer

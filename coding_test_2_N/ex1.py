def solution(S):
    cnt = 0
    i = 0
    if "X" not in S:
        return 0

    while i < (len(S) - 2):
        if "X" in S[i : i + 3]:
            cnt += 1
            i = i + 3
        else:
            i = i + 1

    if "X" in S[i:]:
        cnt += 1
    return cnt


### 리팩토링
def solution(S):
    cnt = 0
    i = 0
    while i < len(S):
        if S[i] == "X":
            cnt += 1
            i += 3  # 현재 "X"와 다음 두 문자 건너뛰기
        else:
            i += 1

    return cnt

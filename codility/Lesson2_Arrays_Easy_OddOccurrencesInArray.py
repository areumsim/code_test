from collections import Counter


def solution(A):
    cnt = Counter(A)

    return [a for a in cnt if cnt[a] % 2 != 0][0]

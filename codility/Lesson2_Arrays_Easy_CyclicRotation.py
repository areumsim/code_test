def solution(A, K):
    N = len(A)
    if N == 0 or K == 0 or N == K:
        return A

    newIdx = [(x + K) % N for x in range(N)]

    rotatedArray = [None] * N
    for i in range(N):
        rotatedArray[newIdx[i]] = A[i]
    rotatedArray

    return rotatedArray

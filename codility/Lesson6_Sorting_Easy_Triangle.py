from itertools import combinations

# ### 타임 아웃 발생
# def solution(A):
#     A.sort()
#     for a, b, c in combinations(A, 3):
#         if (a + b) > c and (a + c) > b and (c + b) > a:
#             return 1
#     return 0


def solution(A):
    A.sort()  # Sort the array to make the comparison simpler
    for i in range(len(A) - 2):
        # Check if the triplet (A[i], A[i+1], A[i+2]) forms a triangle
        if A[i] + A[i + 1] > A[i + 2]:
            return 1  # Triangular triplet found
    return 0  # No triangular triplet found

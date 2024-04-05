from itertools import combinations

# ### 타임아웃
# def solution(A):
#     triplets = combinations(A, 3)
#     max_product = max(a * b * c for a, b, c in triplets)
#     return max_product


def solution(A):
    A.sort()  # Sort the array to find the largest and smallest values easily
    # The maximal product can be the product of the last three elements
    # or the product of the first two elements (possibly negative) and the last element.
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])

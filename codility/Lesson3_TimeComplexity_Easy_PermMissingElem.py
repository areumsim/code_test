def solution(A):
    if not A:  # More Pythonic way to check for an empty list
        return 1

    N = len(A)
    expected_sum = (N + 1) * (N + 2) // 2  # Sum of numbers from 1 to N+1
    actual_sum = sum(A)

    missing_number = expected_sum - actual_sum
    return missing_number

def solution(N, A):
    counters = [0] * N  # Initialize all N counters to 0
    max_counter = 0  # Keep track of the maximum counter value
    last_max_operation = 0  # Keep track of the last max_counter operation

    for operation in A:
        if 1 <= operation <= N:
            # Increase operation
            counters[operation - 1] = (
                max(counters[operation - 1], last_max_operation) + 1
            )
            max_counter = max(max_counter, counters[operation - 1])
        else:
            # Max counter operation
            last_max_operation = max_counter

    # Update all counters with the maximum value after the last max_counter operation
    for i in range(N):
        counters[i] = max(counters[i], last_max_operation)

    return counters

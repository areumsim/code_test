##### sol. 2 #####
def solution(indices, K):
    N = len(indices)

    if K > N:
        K = N

    base_size = N // K
    extra = N % K

    partitions = []

    start_idx = 0
    for i in range(K):
        if i < extra:
            fold_size = base_size + 1
        else:
            fold_size = base_size

        test_indices = indices[start_idx : start_idx + fold_size]
        train_indices = indices[:start_idx] + indices[start_idx + fold_size :]

        partitions.extend([train_indices, test_indices])
        start_idx += fold_size

    return partitions

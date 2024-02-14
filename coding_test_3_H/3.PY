def longest_matching_length(X, Y):
    len_X = len(X)
    len_Y = len(Y)
    max_length = 0

    for i in range(len_X):
        diff_count = 0
        length = 0
        for j in range(min(len_Y, len_X - i)):
            if X[i + j] != Y[j]:
                diff_count += 1
            if diff_count > 1:
                break
            length += 1
        max_length = max(max_length, length)

    return max_length

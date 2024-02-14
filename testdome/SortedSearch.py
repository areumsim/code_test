### Sorted Search


def count_values_less_than(lst, value):
    left = 0
    right = len(lst) - 1
    count = 0

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] < value:
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1

    return count

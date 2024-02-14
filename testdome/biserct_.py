### bisect


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


def count_numbers(sorted_list, less_than):
    left, right = 0, len(sorted_list) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] < less_than:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    if result == -1:
        return 0
    else:
        return result + 1

### Two Sum


def find_two_sum(numbers, target_sum):
    tmpDict = {value: idx for idx, value in enumerate(numbers)}
    N = len(numbers)
    for i in range(N - 1):
        if (target_sum - numbers[i]) in tmpDict.keys():
            return (i, tmpDict.get(target_sum - numbers[i]))
    return None

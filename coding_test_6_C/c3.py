from itertools import combinations


def solution(M, load):
    if any(item > M for item in load):
        return -1

    n = len(load)
    for trucks in range(1, n + 1):
        for combo in combinations(load, trucks):  # 가능한 모든 조합 생성
            sorted_combo = sorted(combo, reverse=True)
            remaining = list(load)
            for item in sorted_combo:
                if item in remaining:
                    remaining.remove(item)
                    # 현재 트럭에 실을 수 있는 최대 무게 계산
                    capacity = M - item
                    # 남은 물건들 중 현재 트럭에 실을 수 있는 물건 싣기
                    for other in sorted(remaining, reverse=True):
                        if capacity >= other:
                            capacity -= other
                            remaining.remove(other)
            if not remaining:
                return trucks
    return -1


# Test the function
print(solution(10, [2, 3, 7, 8]))  # 2

print(solution(5, [2, 2, 2, 2, 2]))  # 3
print(solution(20, [16, 15, 9, 17, 1, 3]))  # 4


print(solution(3, [4]))  #  -1
print(solution(40, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))  # 2
print(solution(40, [40, 20, 20, 10, 10, 10, 10]))  # 3

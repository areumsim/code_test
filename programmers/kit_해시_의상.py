import collections


def solution(clothes):
    category = collections.Counter([ctgr for _, ctgr in clothes])

    # ###### collections.Counter 안쓰고 ######
    # category = {}
    # for _, kind in clothes:
    #     if kind in category.keys():
    #         category[kind] += 1
    #     else:
    #         category[kind] = 1
    # #########################################

    total = 1
    for _, count in category.items():
        total = (count + 1) * total

    return total - 1


print(
    solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ]
    )
)  # 	5

print(
    solution(
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    )
)  # 	3

print(solution([["crow_mask", "face"]]))  # 1

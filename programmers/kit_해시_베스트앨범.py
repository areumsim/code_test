### original format
# def solution(genres, plays):
#     gen = {x : 0 for x in list(set(genres)) }

#     for item, cnt in zip(genres, plays) :
#         gen[item] = gen[item]+cnt

#     print(sorted(gen.items(), key = lambda item: item[1], reverse = True))


#     answer = []
#     return answer
############


def solution(genres, plays):
    gen = {x: 0 for x in list(set(genres))}

    answer = []
    return answer


solution(
    ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
)  # [4, 1, 3, 0]

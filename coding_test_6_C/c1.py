from math import gcd
from collections import Counter


def get_direction(x, y):
    g = gcd(x, y)
    return (x // g, y // g)


def is_on_path(monster, direction):
    mx, my = monster
    dx, dy = direction

    # 몬스터가 총알 경로 위, 그리고 방향도 맞는지 확인
    if mx * dy == my * dx and mx * dx + my * dy > 0:
        if dx != 0:
            return mx / dx > 0
        else:
            return my / dy > 0
    return False


def solution(monsters, bullets):
    bullet_directions = Counter(get_direction(x, y) for x, y in bullets)
    monster_directions = Counter(get_direction(x, y) for x, y in monsters)

    removed = 0
    for direction, m_count in monster_directions.items():
        b_count = bullet_directions[direction]
        # 같은 방향에 있는 몬스터와 총알의 수를 비교하여, 최소한의 수를 총알로 제거 가능한 몬스터 수로 산정
        removed += min(b_count, m_count)

    if removed == 0:
        return -1
    return removed


# Test the provided examples

monsters = [[-4, 4], [-2, 2], [6, 2], [0, -2]]
bullets = [(3, 1), (-1, 1), (-1, 1), (0, -4), (2, -3)]
print(solution(monsters, bullets))  # 4

monsters = [[2, 3], [4, 5], [3, -3], [2, -4], [3, -6], [-3, -3], [-5, 0], [-4, 4]]
bullets = [[4, 1], [4, 6], [1, -2], [-4, -4], [-3, 0], [-4, 4]]
print(solution(monsters, bullets))  # 5


monsters = [[1, 2], [-2, -1], [1, -2], [3, -1]]
bullets = [[1, 0], [2, 1]]
print(solution(monsters, bullets))  # 1

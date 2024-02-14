##### sol. 1 #####


def solution(S):
    first_b = S.find("b")
    last_a = S.rfind("a")

    return last_a == -1 or first_b == -1 or last_a < first_b

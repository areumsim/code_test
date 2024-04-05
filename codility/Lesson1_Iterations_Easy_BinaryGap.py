def solution(N):
    ss = bin(N)[2:]
    ss = ss.split("1")

    if ss[-1] != "":
        ss = ss[:-1]

    return max([len(x) for x in ss])

def solution(s):
    open = 0

    for now in s:
        if now == "(":
            open += 1
        else:
            open -= 1

        if open < 0:
            return False

    if open == 0:
        return True
    return False


print(solution("()()"))  # true
print(solution("(())()"))  # true
print(solution(")()("))  # false
print(solution("(()("))  # false

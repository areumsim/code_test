def solution(S):
    if not S:
        return S

    digits = list(map(int, S))

    i = 0
    while i < len(digits) - 1:
        tmp_sum = digits[i] + digits[i + 1]

        if tmp_sum <= 9:
            digits[i] = tmp_sum
            del digits[i + 1]

            if i > 0:
                i -= 1
        else:
            i += 1

    return "".join(map(str, digits))


# Example usage:
print(solution("32581"))  # Output: "559"
print(solution("1119812"))  # Output: "3992"
print(solution("226228"))  # Output: "4828"

print(solution("11111111"))  #  "8"
print(solution("11111111111111111111"))  # 992
print(solution("92929292929292929292"))  # 92929292929292929292
print(solution("1111111111"))  # Expected output: "91"

print(solution("1212121212"))  # Expected output: "96"
print(solution("99999"))  # Expected output: "99999"
print(solution("123456789"))  # Expected output: "696789"
print(solution("55555"))  # Expected output: "55555"

print(solution("99999"))  # Output: "99999"
print(solution("1111111111"))  # Output: "91" # output error
print(solution("1212121212"))  # Output: "96" # output error
print(solution("55555"))  # Output: "55555" # output error


print(solution("32581"))  # Output: "559"
print(solution("1119812"))  # Output: "3992"
print(solution("226228"))  # Output: "4828"

print(solution("11111111"))  #  "8"
print(solution("11111111111111111111"))  # 992
print(solution("92929292929292929292"))  # 92929292929292929292
print(solution("1111111111"))  # Expected output: "91"

print(solution("1212121212"))  # Expected output: "96"
print(solution("99999"))  # Expected output: "99999"
print(solution("123456789"))  # Expected output: "696789"
print(solution("55555"))  # Expected output: "55555"

print(solution("99999"))  # Output: "99999"
print(solution("1111111111"))  # Output: "91"
print(solution("1212121212"))  # Output: "96"
print(solution("55555"))  # Output: "55555" #

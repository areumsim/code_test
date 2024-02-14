import re


def solutions(s):
    while 1:
        pattern = re.compile(r"AB|BA|CD|DC")
        result = re.sub(pattern, "", s)

        if s == result or len(result) < 2:
            break
        s = result
    return result


def solutions(s):
    if not s:
        return ""

    while "AB" in s or "BA" in s or "CD" in s or "DC" in s:
        s = s.replace("AB", "").replace("BA", "").replace("CD", "").replace("DC", "")

    return s

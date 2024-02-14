import re


def solution(S, c):
    # 특수문자와 숫자를 제거하고 공백 유지, 단 ;는 제외
    name_list = re.sub(r"[^a-z\s;]", "", S.lower())
    name_list = name_list.split("; ")
    name_set = set()

    result_list = []

    for s in name_list:
        s = s.split(" ")
        if len(s) >= 2:
            tmp = s[0] + "_" + s[-1]
        elif len(s) == 1:
            tmp = s
        else:
            continue

        n = 2
        while tmp in name_set:
            tmp = tmp + str(n)
            n = n + 1
        name_set.add(tmp)

        result_list.append(tmp)

    company = c.lower()
    return "".join(
        [f"{n} <{e}@{company}.com>; " for n, e in zip(S.split("; "), result_list)]
    )[:-2]


## 리팩토링
def solution(S, c):
    def generate_email(name, full_name, company):
        tmp = name
        n = 2
        while tmp in used_names:
            tmp = f"{name}{n}"
            n += 1
        used_names.add(tmp)
        return f"{full_name} <{tmp}@{company}.com>"

    result_list = []
    used_names = set()

    s_list = S.split("; ")
    for s in s_list:
        new_s = re.sub(r"[^a-zA-Z\s;]", "", s.lower())
        s_parts = new_s.split()

        if len(s_parts) >= 2:
            first_name, last_name = s_parts[0], s_parts[-1]
            email = generate_email(f"{first_name}_{last_name}", s, c.lower())
            result_list.append(email)

    return "; ".join(result_list)

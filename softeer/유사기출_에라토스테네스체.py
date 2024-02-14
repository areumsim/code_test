# 소수 찾기(에라토스테네스 체)
# - 임의의 자연수 n이 있으면 그 미만의 소수들을 찾기


################################
def isPrime(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


n = 200
for i in range(n + 1):
    if isPrime(i):
        print(i)

################################


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n**0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:  # i가 소수인 경우

            for j in range(i + i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False
                # #(for문과 동일) i를 제외한 i의 모든 배수를 지우기
                # j = 2
                # while i * j <= n:
                #    sieve[i * j] = False
                #    j += 1

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

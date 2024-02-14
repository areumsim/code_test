### 백준 2559 : 수열
# 첫째 줄에는 입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력한다

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

summ = maxx = sum(arr[:k])
for i in range(k, n):
    summ = summ + arr[i] - arr[i - k]
    maxx = max(maxx, summ)
print(maxx)

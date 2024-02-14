import sys
import heapq

input = sys.stdin.readline
n = int(input())

heap = []
for _ in range(n):
    s, f = map(int, input().split())
    heapq.heappush(heap, (f, s))

cnt = 0
now = 0
for i in range(len(heap)):
    f, s = heapq.heappop(heap)
    if s >= now:
        now = f
        cnt = cnt + 1

print(cnt)

from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]  # 간선들을 저장할 graph
    for a, b in edge:  # 간선 정보 저장
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n + 1)  # idx위치의 노드 방문처리 / 거리
    distance[1] = 0  # idx위치의 노드 방문처리 / 거리

    q = deque([(1, 0)])  # BFS를 구현할 큐(시작노드=1, dist=0) /(now, distance)
    while q:
        now, d = q.popleft()  # 현재 위치와 이동한 거리

        # 현재 노드에 연결된 모든 노드를 탐색
        for node in graph[now]:
            if distance[node] == -1:  # 아직 방문하지 않은 노드라면
                distance[node] = d + 1  # 거리 업데이트
                q.append((node, d + 1))

    # 최댓값과 같은 거리를 가진 노드의 수
    max_distance = max(distance)
    return distance.count(max_distance)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3

import heapq

INF = 10 ** 6

if __name__ == '__main__':
    start = int(input('start: '))
    final = int(input('final: '))

    # 0-индексация
    start -= 1
    final -= 1

    adjacency_list = [
        [(4, 4), (6, 1)],
        [(4, 2), (5, 8)],
        [(6, 3), (7, 9)],
        [(5, 1), (7, 3)],
        [(0, 4), (6, 2), (7, 2), (1, 2)],
        [(4, 7), (7, 1), (3, 1), (1, 8)],
        [(0, 1), (2, 3), (7, 8), (4, 2)],
        [(6, 8), (2, 9), (3, 3), (5, 1), (4, 2)],
    ]

    q = []

    heapq.heappush(q, (0, start))

    dist = [INF for _ in range(len(adjacency_list))]
    dist[start] = 0

    while len(q) > 0:
        l = -q[0][0]
        v = q[0][1]

        heapq.heappop(q)

        if l > dist[v]:
            continue

        for a in adjacency_list[v]:
            to = a[0]
            length = a[1]

            if dist[to] > dist[v] + length:
                dist[to] = dist[v] + length
                heapq.heappush(q, (dist[to], to))

    print(dist[final])

    # восстанавливаем путь по расстояниям
    path = []

    current = final

    while current != start:
        min_dist = INF
        min_vertex = -1

        for i in range(len(adjacency_list[current])):
            if dist[adjacency_list[current][i][0]] + adjacency_list[current][i][1] < min_dist:
                min_dist = dist[adjacency_list[current][i][0]] + adjacency_list[current][i][1]
                min_vertex = adjacency_list[current][i][0]

        path.append(current)
        current = min_vertex

    path.append(start)
    path.reverse()
    path = list(map(lambda v: v + 1, path))

    print(path)

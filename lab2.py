INF = 10 ** 10


def floyd(distances):
    path = [[-1] * len(distances) for _ in range(len(distances))]

    for k in range(len(distances)):
        for i in range(len(distances)):
            for j in range(len(distances)):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    path[i][j] = k

    return distances, path


def print_path(path, i, j):
    k = path[i][j]

    if k == -1:
        return

    print_path(path, i, k)
    print(k + 1, end=' ')
    print_path(path, k, j)


if __name__ == '__main__':
    s = int(input('start:'))
    t = int(input('end:'))
    s -= 1
    t -= 1

    graph = [
        [INF, 3, 6, 8, INF],
        [3, INF, 2, INF, INF],
        [6, 2, INF, INF, 4],
        [8, INF, INF, INF, 12],
        [INF, INF, 4, 12, INF],
    ]

    dist, path = floyd(graph)

    if dist[s][t] == 10 ** 10:
        print(-1)
    else:
        print(dist[s][t])
        print(s + 1, end=' ')
        print_path(path, s, t)
        print(t + 1, end=' ')

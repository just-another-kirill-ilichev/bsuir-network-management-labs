import copy

MAX = 10 ** 9


def solve(capacity, s, t):
    def dfs(visited, u, min_capacity):
        if u == t:
            return min_capacity

        visited[u] = True

        for v in range(len(visited)):
            if not visited[v] and capacity[u][v] > 0:
                new_flow = dfs(visited, v, min(capacity[u][v], min_capacity))

                if new_flow > 0:
                    capacity[u][v] -= new_flow
                    capacity[v][u] += new_flow

                    return new_flow

        return 0

    capacity = copy.deepcopy(capacity)
    flow = 0

    while True:
        path_flow = dfs([False] * len(capacity), s, MAX)
        flow += path_flow

        if path_flow == 0:
            return flow


if __name__ == '__main__':
    # 6 9 103 10 2 3 0 9 18 13 71 2 8
    a, b, c, d, e, f, g, h, i, j, k, l, m = map(int, input('input a-m: ').split())

    graph = [
        [0, a, b, c, d, 0],
        [e, 0, e, f, e, 0],
        [c, g, 0, h, 0, a],
        [i, j, a, 0, l, k],
        [b, f, 0, j, 0, m],
        [0, 0, b, d, e, 0]
    ]

    print('max flow:', solve(graph, 0, 5))

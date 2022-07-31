# Минимальный вес остова

import csv

INF = 10 ** 9
N = 10
number = 4
prev = [None] * N
with open("data.txt") as f:
    data = [list(map(int, row)) for row in csv.reader(f, delimiter=' ')]

R = [(data[column][row], row, column) for row in range(10) for column in range(10) if data[column][row] != 0]

W = {(r[1], r[2]): r[0] for r in R}

F = [INF] * N
F[number] = 0
for k in range(1, N):
    for j, i in W.keys():
        if F[j] + W[j, i] < F[i]:
            F[i] = F[j] + W[j, i]
            prev[i] = j

for n in range(N):
    path = []
    j = n
    while j is not None:
        if prev[j] is not None:
            path.append(prev[j])
        j = prev[j]

    path.reverse()
    path.append(n)
    print(f"Путь из вершины 4 в вершину {n}: {path}, вес пути {F[n]}")


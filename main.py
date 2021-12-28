import csv
from array import array

INF = 10 ** 9
N = 4
number = 0
with open("data.txt") as f:
    data = [list(map(int, row)) for row in csv.reader(f, delimiter=' ')]

R = [(data[column][row], row + 1, column + 1) for row in range(4) for column in range(4) if data[column][row] != 0]

W = {(r[1], r[2]): r[0] for r in R}
print(W)

path = [[] for i in range(N)]

while number < N:
    F = [INF] * N
    F[number] = 0
    for k in range(1, N):
        path[k].append(number+1)
        for j, i in W.keys():
            print(f"{j}\t{i}\t{F[j-1]}\t{F[i-1]}")
            if F[j - 1] + W[j, i] < F[i - 1]:
                print("true")
                F[i - 1] = F[j - 1] + W[j, i]
                path[i-1].append(i)
                path[i - 1].append(j)
                print(path)
    print(path)
    print(F)
    number+=1


[0, 8, 4, 3, 0, 10, 1, 7, 0, 0, 7, 0, 0, 0, 0, 6, 0]
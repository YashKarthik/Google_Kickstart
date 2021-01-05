T = int(input())

for test_case in range(T):
    N, K, P = [int(i) for i in input().split()]
    beauty_values = []

    for stack in range(N):
        beauty_values.append([int(x) for x in input().split()])

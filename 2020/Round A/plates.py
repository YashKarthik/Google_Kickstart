T = int(input())

for test_case in range(T):
    N, K, P = [int(i) for i in input().split()]
    stack_values = []

    for stack in range(N):
        stack_values.append([int(x) for x in input().split()])

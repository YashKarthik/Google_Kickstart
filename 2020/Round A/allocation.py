T = int(input())

result = []
for i in range(T):

    N, B = map(int, input().split(' '))
    costs = list(map(int, input().split(' ')))
    costs.sort()

    for house_index in range(len(costs)):

        B -= costs[house_index]
        if B < 0:
            result.append(house_index)
            break
        elif house_index == len(costs)-1:
            result.append(house_index+1)

for test_case in range(T):
    print("Case #{}: {}".format(test_case + 1, result[test_case]))

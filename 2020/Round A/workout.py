T = int(input())
result = []

for test_case in range(T):

    N, K = [int(x) for x in input().split()]
    minutes = [int(x) for x in input().split()]

    for additional_workout in range(K):

        differences = []
        for index in range(1, len(minutes)):
            differences.append(minutes[index] - minutes[index-1])

            minutes.insert(
                differences.index(max(differences)) + 1, (

                    (minutes[differences.index(
                        max(differences)) + 1] + minutes[differences.index(max(differences))]
                     )//2
                ))

        differences.remove(max(differences))

    diff = []
    for index in range(1, len(minutes)):
        diff.append(minutes[index] - minutes[index-1])
    result.append(max(diff))

for test_case in range(T):
    print("Case #{}: {}".format(test_case + 1, result[test_case]))

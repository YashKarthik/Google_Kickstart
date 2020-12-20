"""
Problem link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434c0e/0000000000434ba7
"""

T = int(input())

for test_case in range(T):

    N = int(input())
    skater_name = [input().lower() for card_num in range(N)]

    alpha_num = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        " ": 0,
    }

    name_value_pairs = {}
    for name in skater_name:
        value = ""
        for alph in name:
            value += str(alpha_num.get(alph))

        name_value_pairs[int(value)] = name

    sorted_dict = {
        k: v for k, v in sorted(name_value_pairs.items(), key=lambda item: item[1])
    }

    sorted_list = [name for name in sorted_dict.values()]
    print(sorted_list)
    print(sorted_dict)
    print(skater_name)

    changes = 0

    for index in range(len(sorted_list)):
        if sorted_list[index] != skater_name[index]:
            changes += 0.5

    print("Case #{}: {}".format(test_case + 1, int(changes)))

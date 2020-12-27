"""
Problem link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434c0e/0000000000434ba7
"""
T = int(input())

for test_case in range(T):

    N = int(input())
    skater_name = [input() for card_num in range(N)]

    alpha_num = {
        " ": 1,

        "A": 2,
        "B": 3,
        "C": 4,
        "D": 5,
        "E": 6,
        "F": 7,
        "G": 8,
        "H": 9,
        "I": 10,
        "J": 11,
        "K": 12,
        "L": 13,
        "M": 14,
        "N": 15,
        "O": 16,
        "P": 17,
        "Q": 18,
        "R": 19,
        "S": 20,
        "T": 21,
        "U": 22,
        "V": 23,
        "W": 24,
        "X": 25,
        "Y": 26,
        "Z": 27,

        "a": 28,
        "b": 29,
        "c": 30,
        "d": 31,
        "e": 32,
        "f": 33,
        "g": 34,
        "h": 35,
        "i": 36,
        "j": 37,
        "k": 38,
        "l": 39,
        "m": 40,
        "n": 41,
        "o": 42,
        "p": 43,
        "q": 44,
        "r": 45,
        "s": 46,
        "t": 47,
        "u": 48,
        "v": 49,
        "w": 50,
        "x": 51,
        "y": 52,
        "z": 53
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
    changes = 0

    for index in range(len(sorted_list)):
        if sorted_list[index] != skater_name[index]:
            changes += 0.5

    print("Case #{}: {}".format(test_case + 1, int(changes)))

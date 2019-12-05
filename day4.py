LOWER_BOUND = 248345
UPPER_BOUND = 746315


def no_decreases(num):
    numbers = [int(x) for x in str(num)]
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


def has_standalone_dupe(num):
    numbers = [int(x) for x in str(num)]
    curr = numbers[0]
    seen = 0
    for i in range(len(numbers)):
        if numbers[i] == curr:
            seen += 1
        else:
            if seen == 2:
                return True
            seen = 1
            curr = numbers[i]
    return seen == 2


def find_combinations():
    num = LOWER_BOUND
    possibilities = 0

    while num < UPPER_BOUND:
        if no_decreases(num) and has_standalone_dupe(num):
            possibilities += 1
        num += 1
    return possibilities


if __name__ == "__main__":
    combos = find_combinations()
    print(combos)

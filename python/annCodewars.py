# Kata: Ann and John Sequence (The Josephus Problem variant)
# Implements a complex sequence where Ann and John alternately determine positions based on
# each other's sequences. Functions return the sequences and their sums up to n elements.

def john(n):
    if n == 0:
        return []

    ann = [1, 1]
    john = [0, 0]

    for i in range(2, n):
        ann.append(i - john[ann[i - 1]])
        john.append(i - ann[john[i - 1]])

    return john[:n]


def ann(n):
    if n == 0:
        return []

    ann = [1, 1]
    john = [0, 0]

    for i in range(2, n):
        ann.append(i - john[ann[i - 1]])
        john.append(i - ann[john[i - 1]])

    return ann[:n]


def sum_john(n):
    return sum(john(n))


def sum_ann(n):
    return sum(ann(n))


def main():
    print(john(11))


if __name__ == "__main__":
    main()

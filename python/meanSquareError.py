# // function accepts two integer arrays of equal length
# // compares the value each member in one array to the corresponding member in the other
# // squares the absolute value difference between those two values
# // and returns the average of those squared absolute value difference between each member pair.


def solution(array_a, array_b):
    return sum([abs(j - i) ** 2 for i, j in zip(array_a, array_b)]) / len(array_b)


def main():
    print(solution([1, 2, 3], [4, 5, 6]))


if __name__ == "__main__":
    main()


# solution: () = lambda a, b: sum([abs(a[i]-b[i])**2 for i in range(len(a))]) / len(a)

# https://www.codewars.com/kata/5672682212c8ecf83e000050


def dbl_linear(n):
    list = [1]
    indexX = 0
    indexY = 0

    while len(list) <= n:
        x = 2 * list[indexX] + 1
        y = 3 * list[indexY] + 1

        next = min(x, y)
        list.append(next)

        if next == x:
            indexX += 1
        if next == y:
            indexY += 1

    return list[n]


def main():
    print(dbl_linear(10))

if __name__ == "__main__":
    main()
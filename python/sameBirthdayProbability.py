# https://www.codewars.com/kata/5419cf8939c5ef0d50000ef2/train/python


def calculate_probability_birthday(n):
    if n < 0:
        return 0
    p_no_match = 1.0
    for i in range(n):
        p_no_match *= (365 - i) / 365

    return round(1 - p_no_match, 2)


def main():
    print(round(calculate_probability_birthday(2), 2))


if __name__ == "__main__":
    main()


# calculate_probability=lambda n:n>(d:=365) or round(1-(f:=__import__('math').factorial)(d)//f(d-n)/d**n,2)

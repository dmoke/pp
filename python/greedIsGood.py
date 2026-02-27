"""
Three 1's => 1000 points
Three 6's =>  600 points
Three 5's =>  500 points
Three 4's =>  400 points
Three 3's =>  300 points
Three 2's =>  200 points
One   1   =>  100 points
One   5   =>   50 point
"""


def score(dice):
    bonuses = {
        "111": 1000,
        "222": 200,
        "333": 300,
        "444": 400,
        "555": 500,
        "666": 600,
        "5": 50,
        "1": 100,
    }

    total = 0
    chars = "".join(map(str, sorted(dice)))
    bonus_found = True

    while bonus_found:
        bonus_found = False

        for bonus in bonuses:
            if bonus in chars:
                bonus_found = True
                total += bonuses[bonus]
                chars = chars.replace(bonus, "", 1)
                break

    return total


def main():
    print(score([5, 1, 3, 4, 1]))


if __name__ == "__main__":
    main()

# everytime you press the button it sends you an array of one-letter strings representing directions
# to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction)
# and you know it takes you one minute to traverse one city block, so create a function that will return
# true if the walk the app gives you will take you exactly ten minutes
# and will, of course, return you to your starting point


def is_valid_walk(walk):
    return (
        len(walk) == 10
        and walk.count("n") == walk.count("s")
        and walk.count("e") == walk.count("w")
    )


def main():
    res = is_valid_walk(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"])
    print(res)


if __name__ == "__main__":

    main()

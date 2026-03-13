# Kata: Increment String Numbers
# Finds the numeric suffix in a string and increments it while preserving leading zeros.
# If no number exists, appends "1" to the string.

import re


def increment_string(string):
    pattern = r"\d+$"
    match = re.search(pattern, string)

    if match is None:
        return string + "1"
    else:
        num = match.group()
        incremented = str(int(num) + 1).zfill(len(num))
        return string[:-len(num)] + incremented



def main():
    print(increment_string("a2asdasd2"))


if __name__ == "__main__":
    main()
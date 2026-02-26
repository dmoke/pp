from collections import Counter


def first_non_repeating_letter(s):
    counts = Counter(s.lower())
    return next((ch for ch in s if counts[ch.lower()] == 1), "")


def main():
    print(first_non_repeating_letter("sTreSS"))


if __name__ == "__main__":
    main()


# first_non_repeating_letter=lambda s: (lambda uniq: ([a for a in s if s.lower().count(a.lower())==1] or [""])[0])(set(s.lower()))

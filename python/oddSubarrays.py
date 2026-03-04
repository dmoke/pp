"""
Implement a function which takes an array of nonnegative integers and
returns the number of subarrays with an odd number of odd numbers. Note,
a subarray is a contiguous subsequence.

"""


def solve(arr):
    count = [1, 0]
    odd = 0
    res = 0
    for x in arr:
        x = x % 2
        odd ^= x
        res += count[1 - odd]
        count[odd] += 1
    return res



def main():
    print(solve([1, 1, 1, 1]))


if __name__ == "__main__":
    main()

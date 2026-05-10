import math


# P(x) = nCx p^x q^n-x
# nCx = n!/(n-x)!x!   C(n, x) = number of ways to choose x items from n, ignoring order - combinations
# nPx = n!/(n-x)!   P(n, x) = number of ordered ways to choose x items from n - permutations
def binomial(n, x, p, q):
    """
    Use when calculating probability of exactly x successes in n trials.
    """
    combinations = math.factorial(n) / (math.factorial(n - x) * math.factorial(x))

    probability = combinations * (p**x) * (q ** (n - x))

    return probability


# P(H|E) = P(E|H) * P(H) /
#          (P(E|H) * P(H) + P(E|¬H) * (1 - P(H)))
def bayes_binary(p_h, p_e_given_h, p_e_given_not_h):
    """
    Use to adjust hypothesis probability based on new evidence
    """
    numerator = p_e_given_h * p_h

    denominator = (p_e_given_h * p_h) + (p_e_given_not_h * (1 - p_h))

    probability = numerator / denominator

    return probability


# P(A|B) = P(B|A) * P(A) / P(B)
# 𝑃(𝐵)=𝑃(𝐵∣𝐴)𝑃(𝐴)+𝑃(𝐵∣¬𝐴)𝑃(¬𝐴)
def bayes(p_b_given_a, p_a, p_b):
    """
    Use when total evidence probability P(B) is already known.
    """
    probability = (p_b_given_a * p_a) / p_b

    return probability


def main():
    probs = [binomial(100, x, 1 / 100, 99 / 100) for x in range(1, 100 + 1)]
    print(probs)
    print(sum(probs))
    print(1 - (99 / 100) ** 100)


if __name__ == "__main__":
    main()

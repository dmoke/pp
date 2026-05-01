import math

# P(x) = nCx p^x q^n-x
# nCx = n!/(n-x)!x!
BINOMIAL = (
    lambda n, x, p, q: (math.factorial(n) / (math.factorial(n - x) * math.factorial(x)))
    * (p**x)
    * (q ** (n - x))
)

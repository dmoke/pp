import math
import matplotlib.pyplot as plt

# parameters
n = 20
p = 1/4
q = 1 - p

# binomial function
def binom(n, x, p):
    return math.comb(n, x) * (p**x) * ((1-p)**(n-x))

# P(X >= k) values
thresholds = list(range(n + 1))
probs = []

for k in thresholds:
    prob = sum(binom(n, x, p) for x in range(k, n + 1))
    probs.append(prob)

# plot
plt.figure(figsize=(10, 5))
plt.plot(thresholds, probs, marker='o')

plt.title("Probability of Getting X or More Correct (20 Questions, p=1/4)")
plt.xlabel("X (minimum correct answers)")
plt.ylabel("P(X ≥ x)")
plt.grid(True)
plt.ylim(0, 1)

plt.show()
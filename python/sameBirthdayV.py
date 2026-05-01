# https://www.codewars.com/kata/5419cf8939c5ef0d50000ef2/train/python

import matplotlib.pyplot as plt

from sameBirthdayProbability import calculate_probability_birthday

values = [calculate_probability_birthday(n) for n in range(1, 60)]

plt.plot(values, label="Probability", alpha=0.7)

plt.axhline(y=0.5, color="r", linestyle="--", label="50%")

n_50 = next(i + 1 for i, v in enumerate(values) if v >= 0.5)

plt.axvline(x=n_50 - 1, color="g", linestyle="--", label=f"n ≈ {n_50}")

plt.xlabel("Number of people")
plt.ylabel("Probability")
plt.legend()
plt.grid()

plt.show()

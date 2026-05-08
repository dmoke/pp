import random
import matplotlib.pyplot as plt
import numpy as np

TOTAL_SLOTS = 38
BLACKS = 18

WIN_PROB = BLACKS / TOTAL_SLOTS

INIT_BET = 10
BETS = 500
SIMS = 300

avg_required = []

for n in range(1, BETS + 1):

    required_values = []

    for _ in range(SIMS):

        max_streak = 0
        current_streak = 0

        for _ in range(n):

            if random.random() < WIN_PROB:
                current_streak = 0
            else:
                current_streak += 1
                max_streak = max(max_streak, current_streak)

        required = INIT_BET * (2**max_streak - 1)
        required_values.append(required)

    avg_required.append(np.mean(required_values))

# -----------------------
# FIGURE: AVERAGE BANK REQUIREMENT
# -----------------------

plt.figure(figsize=(15, 7))

plt.plot(avg_required, linewidth=2)

plt.title("Average Required Starting Bank vs Number of Plays")
plt.xlabel("Number of Spins")
plt.ylabel("Average Required Bank")

plt.grid()
plt.show()
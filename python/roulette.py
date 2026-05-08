import random
import matplotlib.pyplot as plt

TOTAL_SLOTS = 38
BLACKS = 18

WIN_PROB = BLACKS / TOTAL_SLOTS

INIT_BET = 10
BETS = 500

current_bet = INIT_BET
profit = 0

profit_history = []
loss_streak_history = []

current_loss_streak = 0

required_bank_history = []
max_required_bank_history = []

max_required_bank = 0

for _ in range(BETS):

    roll = random.random()

    if roll < WIN_PROB:

        profit += current_bet
        current_bet = INIT_BET
        current_loss_streak = 0

    else:

        profit -= current_bet
        current_bet *= 2
        current_loss_streak += 1

    required_bank = INIT_BET * (2**current_loss_streak - 1)

    max_required_bank = max(max_required_bank, required_bank)

    profit_history.append(profit)
    loss_streak_history.append(current_loss_streak)
    required_bank_history.append(required_bank)
    max_required_bank_history.append(max_required_bank)

final_profit = profit_history[-1]
final_max_required = max_required_bank_history[-1]

# -----------------------
# FIGURE 1
# -----------------------

plt.figure(figsize=(15, 7))

plt.plot(profit_history,
         label=f"Actual Profit ({final_profit})",
         linewidth=2)

plt.plot(
    [-x for x in required_bank_history],
    linestyle="--",
    color="red",
    label=f"Current Required Capital"
)

plt.plot(
    [-x for x in max_required_bank_history],
    linestyle=":",
    color="darkred",
    label=f"Max Required Capital ({final_max_required})"
)

plt.title("Martingale: Profit vs Risk Capital Dynamics")
plt.xlabel("Spin")
plt.ylabel("Money")

plt.legend()
plt.grid()

# -----------------------
# FIGURE 2
# -----------------------

plt.figure(figsize=(18, 5))

plt.bar(
    range(len(loss_streak_history)),
    loss_streak_history,
    color=["red" if x > 0 else "lightgray" for x in loss_streak_history],
    width=1.0,
    alpha=0.75
)

peak = []
m = 0
for v in loss_streak_history:
    m = max(m, v)
    peak.append(m)

plt.plot(
    peak,
    color="black",
    linewidth=2,
    label=f"Peak Loss Streak ({peak[-1]})"
)

plt.title("Loss Streaks + Peak Risk Growth")
plt.xlabel("Spin")
plt.ylabel("Consecutive Losses")

plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.show()
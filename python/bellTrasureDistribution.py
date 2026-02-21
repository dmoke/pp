import random
import matplotlib.pyplot as plt
import numpy as np

def simulate_average_find_days(total_people=10000, find_rate=0.01, batch_size=100):
    all_find_days = []
    batch_averages = []

    for _ in range(0, total_people, batch_size):
        batch_find_days = []
        for _ in range(batch_size):
            day = 0
            while True:
                day += 1
                if random.random() < find_rate:
                    break
            batch_find_days.append(day)
            all_find_days.append(day)
        batch_averages.append(sum(batch_find_days) / batch_size)

    overall_avg = sum(all_find_days) / len(all_find_days)
    central_batch_mean = sum(batch_averages) / len(batch_averages)
    return batch_averages, overall_avg, central_batch_mean

total_people = 100_000
batch_size = 100
find_rate = 0.01

batch_averages, overall_avg, central_batch_mean = simulate_average_find_days(
    total_people, find_rate, batch_size
)

print(f"Overall average days to find treasure: {overall_avg:.5f}")

plt.figure(figsize=(10, 6))

counts, bins, _ = plt.hist(
    batch_averages,
    bins=100,
    color="skyblue",
    edgecolor="black",
    density=True
)

max_bin_index = np.argmax(counts)
max_bin_height = counts[max_bin_index]
max_bin_value = (bins[max_bin_index] + bins[max_bin_index + 1]) / 2

plt.axhline(
    max_bin_height,
    color="orange",
    linestyle="--",
    label=f"Most Frequent Batch Density ≈ {max_bin_height*100:.2f}%"
)

plt.axvline(
    overall_avg,
    color="red",
    linestyle="--",
    label=f"Overall Average = {overall_avg:.2f}"
)

plt.text(
    max_bin_value + 1,
    max_bin_height,
    "This height shows how common\nthe most frequent batch average is",
    color="orange",
    fontsize=10,
    verticalalignment="bottom"
)

plt.xlabel("Average Days per Batch")
plt.ylabel("Probability Density")
plt.title("Distribution of Batch Averages with Most Frequent Batch Highlighted")
plt.legend()
plt.show()
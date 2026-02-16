import random
import matplotlib.pyplot as plt

def simulate_average_find_days(total_people=10000, find_rate=0.01, batch_size=100):
    """
    Simulate find days and compute batch averages.
    """
    all_find_days = []
    batch_averages = []

    # Simulate each person
    for i in range(0, total_people, batch_size):
        batch_find_days = []
        for _ in range(batch_size):
            day = 0
            while True:
                day += 1
                if random.random() < find_rate:
                    break
            batch_find_days.append(day)
            all_find_days.append(day)

        batch_avg = sum(batch_find_days) / batch_size
        batch_averages.append(batch_avg)

    # Overall average with high precision
    overall_avg = sum(all_find_days) / len(all_find_days)

    return batch_averages, overall_avg


# Parameters
total_people = 100000
batch_size = 100
find_rate = 0.01

# Run simulation
batch_averages, overall_avg = simulate_average_find_days(total_people, find_rate, batch_size)

# Print overall average with several digits
print(f"Overall average days to find treasure: {overall_avg:.5f}")

# Plot histogram of batch averages
plt.figure(figsize=(10,6))
plt.hist(batch_averages, bins=100, color='skyblue', edgecolor='black', density=True)
plt.axvline(overall_avg, color='red', linestyle='--', label=f'Overall Average = {overall_avg:.5f}')
plt.xlabel("Average Days per Batch")
plt.ylabel("Probability Density")
plt.title("Distribution of Average Find Days (CLT → Normal)")
plt.legend()
plt.show()

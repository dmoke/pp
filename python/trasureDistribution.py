import random
import matplotlib.pyplot as plt

def simulate_treasure_search(total_people, find_rate=0.01):
    remaining = total_people
    day = 0

    days = []
    found_per_day = []
    remaining_per_day = []
    total_days_accumulated = 0
    average_days_list = []

    while remaining > 0:
        day += 1
        found_today = 0

        for _ in range(remaining):
            if random.random() < find_rate:
                found_today += 1

        remaining -= found_today

        # accumulate total days for people who found treasure
        total_days_accumulated += found_today * day

        # calculate average days so far
        people_found_so_far = total_people - remaining
        average_days = total_days_accumulated / people_found_so_far if people_found_so_far > 0 else 0

        # store for plotting
        days.append(day)
        found_per_day.append(found_today)
        remaining_per_day.append(remaining)
        average_days_list.append(average_days)

    # Plotting
    fig, ax1 = plt.subplots(figsize=(10,6))

    # Bars: people found per day
    ax1.bar(days, found_per_day, color='skyblue', label='Found per Day')
    ax1.set_xlabel("Day")
    ax1.set_ylabel("People Found Treasure")

    # Line 1: remaining people
    ax2 = ax1.twinx()
    ax2.plot(days, remaining_per_day, color='red', label='Remaining People', linewidth=2)

    # Line 2: average days taken for all found so far
    ax2.plot(days, average_days_list, color='green', linestyle='--', label='Average Days to Find', linewidth=2)

    ax2.set_ylabel("Remaining / Average Days")
    ax2.legend(loc='upper right')
    plt.title("Treasure Search Simulation with Average Days Taken (1% chance)")
    plt.show()


# Example usage
simulate_treasure_search(total_people=1000)

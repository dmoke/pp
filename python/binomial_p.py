import time
from probability import binomial

DAYS = 100
CHANCE = 1 / 100

start = time.perf_counter()

probs = [binomial(DAYS, x, CHANCE, 1 - CHANCE) for x in range(1, DAYS + 1)]
result1 = sum(probs)

end = time.perf_counter()
bt = (end - start) * 1000

print(f"{result1} or \n{format(round(result1*100, 2))}%")
print("Binomial time:", bt, "ms")


start = time.perf_counter()

result2 = 1 - (1 - CHANCE) ** DAYS

end = time.perf_counter()
st = (end - start) * 1000

print(f"{result2} or \n{format(round(result2*100, 2))}%")
print("Shortcut time:", st, "ms")


print(bt / st if st > 0 else float("inf"), "times faster")

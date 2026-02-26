def combos(n, max_val=None):
    if max_val is None:
        max_val = n
    if n == 0:
        return [[]] 
    result = []
    for i in range(1, min(n, max_val) + 1):
        for tail in combos(n - i, i):
            result.append([i] + tail)
    return result

print(combos(3))
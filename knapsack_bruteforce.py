import itertools

def knapsack_bruteforce(items, capacity):
    best = -1
    for l in range(len(items) + 1):
        for i in itertools.combinations(items, l):
            if sum(a for a, b in i) <= capacity and sum(b for a, b in i) > best:
                best = sum(b for a, b in i)
    return best

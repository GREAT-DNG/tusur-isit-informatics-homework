def greedy_knapsack(items, capacity):
    items = sorted(items, key=lambda i: i[1], reverse=True)
    weight = 0
    price = 0
    for i in items:
        if weight + i[0] <= capacity:
            weight += i[0]
            price += i[1]
    return price

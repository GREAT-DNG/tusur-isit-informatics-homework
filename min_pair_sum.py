def min_pair_sum(numbers):
    sum = 0
    for i in range(len(numbers) // 2):
        sum += min(numbers) * max(numbers)
        numbers.remove(min(numbers))
        numbers.remove(max(numbers))
    return sum

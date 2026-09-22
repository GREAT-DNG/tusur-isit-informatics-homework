import random

def factorial(n):
    if n < 0: return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def arrangements(n, k):
    if k > n or n < 0 or k < 0: return 0
    return factorial(n) / factorial(n - k) # pyright: ignore

def birthday_probability(people):
    return 1 - arrangements(365, people) / 365 ** people

def simulate_birthday(people, trials):
    match_count = 0
    for i in range(trials):
        birthdays = []
        for i in range(people):
            birthdays.append(random.randint(1, 365))
        if len(birthdays) != len(set(birthdays)):
            match_count += 1
    return match_count / trials

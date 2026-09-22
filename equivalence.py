# Не проходит тесты
# import truth_table # pyright: ignore

def truth_table(n):
    if n == 0: return [()]
    table = []
    for i in range(2**n):
        table.append(tuple(map(int, bin(i).replace("0b", "").zfill(n))))
    return table

def are_equivalent(f, g, n):
    table = truth_table(n)
    result = True
    for i in table:
        if f(*i) != g(*i):
            result = False 
            break
    return result

def de_morgan_left(a, b):
    return not (a and b)

def de_morgan_right(a, b):
    return (not a) or (not b)

def wrong(a, b):
    return (not a) and (not b)

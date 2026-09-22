def truth_table(n):
    if n == 0: return [()]
    table = []
    for i in range(2**n):
        table.append(tuple(map(int, bin(i).replace("0b", "").zfill(n))))
    return table

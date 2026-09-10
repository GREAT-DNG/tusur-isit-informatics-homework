def multiplication_table(n):
    table = []
    for i in range(10):
        table.append(f"{n} x {i+1} = {n*(i+1)}")
    return table

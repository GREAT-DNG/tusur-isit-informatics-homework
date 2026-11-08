def n_queens(n):
    global count
    count = 0
    columns = set()
    diagonal1 = set()
    diagonal2 = set()

    def place(row):
        global count

        if row == n:
            count += 1
            return

        for col in range(n):
            d1 = row + col
            d2 = row - col
            
            if col in columns or d1 in diagonal1 or d2 in diagonal2:
                continue
            
            columns.add(col)
            diagonal1.add(d1)
            diagonal2.add(d2)
            
            place(row + 1)

            columns.remove(col)
            diagonal1.remove(d1)
            diagonal2.remove(d2)

    place(0)
    return count

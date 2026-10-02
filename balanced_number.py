def is_balanced_number(n):
    n = str(n)
    side_len = 0
    if len(n) <= 2: return "Balanced"
    elif len(n) % 2 == 0: side_len = (len(n) - 2) // 2
    else: side_len = (len(n) - 1) // 2
    sides = {"left": 0, "right": 0}
    for i in range(0, side_len):
        sides["left"] += int(n[i])
        sides["right"] += int(n[::-1][i])
    return "Balanced" if sides["left"] == sides["right"] else "Not Balanced"

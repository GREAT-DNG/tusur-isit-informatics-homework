def days_in_month(month, year):
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): return 29
        else: return 28
    if month in [4, 6, 9, 11]:
        return 30
    else: return 31

def month_calendar(start_weekday, days):
    table = ""
    week_counter = start_weekday
    table += " " * 2 * week_counter
    table += " " * (week_counter - 1)
    for i in range(days):
        if week_counter == 7 and i != 0:
            table += "\n"
            week_counter = 0
        table += f" {i+1:2}" if week_counter != 0 else f"{i+1:2}"
        week_counter += 1
    return table

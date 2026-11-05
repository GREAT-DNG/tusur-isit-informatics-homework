class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.date = Date.to_absolute_date(day, month, year)

    @staticmethod
    def is_year_leap(year: int) -> bool:
         return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    @staticmethod
    def to_absolute_date(day: int = 0, month: int = 0, year: int = 0) -> int:
        days_table = [31, 28 + (1 if Date.is_year_leap(year) else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if not (1 <= month <= 12) or not (1 <= day <= days_table[month - 1]): raise ValueError
        result = day + sum(days_table[:month - 1])
        result += (year // 400) * 146097
        for i in range((year // 400) * 400, year):
            result += 366 if Date.is_year_leap(i) else 365
        return result

    @staticmethod
    def from_absolute_date(absolute_date: int) -> tuple:
        year = (absolute_date - 1) // 146097 * 400
        absolute_date -= year // 400 * 146097
        for i in range(400):
            days_in_year = (366 if Date.is_year_leap(year + i) else 365)
            if absolute_date <= days_in_year:
                year += i
                break
            absolute_date -= days_in_year
        days_table = [31, 28 + (1 if Date.is_year_leap(year) else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = -1
        for i in range(12):
            if absolute_date <= days_table[i]:
                month = i + 1
                break
            absolute_date -= days_table[i]
        return absolute_date, month, year

    @property
    def day(self) -> int:
        return Date.from_absolute_date(self.date)[0]

    @property
    def month(self) -> int:
        return Date.from_absolute_date(self.date)[1]

    @property
    def year(self) -> int:
        return Date.from_absolute_date(self.date)[2]

    def __add__(self, operand):
        new_date = Date.from_absolute_date(self.date + operand)
        return Date(new_date[0], new_date[1], new_date[2])

    def __sub__(self, operand):
        return self.date - operand.date

    def __eq__(self, operand):
        return self.date == operand.date

    def __lt__(self, operand):
        return self.date < operand.date

    def __repr__(self):
        return f"Date({self.day}, {self.month}, {self.year})"

    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year}"

d = Date(4, 11, 2026)
print(d.day, d.month, d.year)
d = Date(31, 12, 2025)
print(d.day, d.month, d.year)

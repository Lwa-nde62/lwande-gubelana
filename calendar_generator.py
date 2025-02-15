import calendar

def display_calendar(year):
    cal = calendar.TextCalendar()
    for month in range(1, 13):
        print(cal.formatmonth(year, month))

# Example usage
year = 2025  # Change to desired year
display_calendar(year)

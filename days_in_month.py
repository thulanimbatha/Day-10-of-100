# MODIFIED - determine whether a given year is a leap year

def is_leap_year(year):
    '''Returns True if given month (int) is a Leap year '''    #Docstrings
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    '''Returns int number of days in given month (int)'''   # Docstrings
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31 ,30, 31]
    if is_leap_year(year) and month == 2:
        return 29
    elif is_leap_year(year):
        return f"{year} is a leap year and has {month_days[month - 1]} days"
    return month_days[month - 1]

year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))
days = days_in_month(year, month)
print(days)
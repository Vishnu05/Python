
# to check whether the given year is leap year or not
# this is not simplifed soultion 

year = int(input())


def is_leap_year():
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year == 1800 or year == 1900 or year == 2100 or year == 2200 or year == 2300 or year == 2500:
            return False
        elif year % 4 == 0:
            return True
    else:
        return False


print(is_leap_year())   

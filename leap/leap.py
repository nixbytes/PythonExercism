def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
        #return "{0} is a leap year".format(year)
    else:
        return False
        # return "{0} is not a leap year".format(year) 
    
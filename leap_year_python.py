def leap_year(x):
    if (x%4==0 and x%100!=0) or (x%400==0):
        return "Leap year"
    else:
        return "Not a leap year"

print(leap_year(1900))
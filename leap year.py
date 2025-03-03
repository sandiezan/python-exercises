#This exercise aims to determine whether the year inputted by the user is a leap year or not
year = int(input("Please select a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("This is a leap year")
else:
    print("This is a non leap year")

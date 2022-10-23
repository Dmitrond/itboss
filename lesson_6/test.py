day = int(input("enter day: "))
month = int(input("Enter month: "))
year = int(input("enter year: "))
day1 = True
month1 = True
year1 = True

if day >= 1 and day <= 31:
    print("day true")
else:
    print("day false")

if month >= 1 and month <= 12:
    print("month true")
else:
    print("month false")

if len(str(year)) <= 4 and year > 0:
    print("year true")
else:
    print("year false")







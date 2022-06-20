## This just a quick Exercise in calculating pay with and without overtime.
## It is an exercise in Conditional statements.
Hours_worked = input("\nPlease enter the hours you worked this week: ")
Hourly_rate = input("Please enter your hourly rate: ")
if float(Hours_worked) > 40: ## If you worked overtime this block runs
    Overtime_hours = float(Hours_worked) - 40
    Weekly_pay = (float(Hourly_rate) * 40) + (float(Overtime_hours) * (float(Hourly_rate) * 1.5))
    print("\nYou accrued some overtime this week. ")
    print("Your weekly pay is equal to: ", Weekly_pay)
    print("\n")
else:  ## otherwise this block runs
    Weekly_pay = float(Hourly_rate) * float(Hours_worked)
    print("\nYour weekly pay is equal to: ", Weekly_pay)
    print("\n")

## This part of the code will just tell you what generation your belong to...even if you don't like it. :)
Year_born = input("What year were you born: ")
if int(Year_born) < 1946:
    print("You are a Traditionalist or part fo the Silent Generation. \n")
elif int(Year_born) > 1945 and int(Year_born) < 1965:
    print("You are part of the Baby Boomers Generation. \n")
elif int(Year_born) >= 1965 and int(Year_born) < 1977:
    print("You are part of Generation X. \n")
elif int(Year_born) >= 1977 and int(Year_born) < 1996:
    print("You are part of the Millennials or Gen Y. \n")
elif int(Year_born) >= 1996 and int(Year_born) < 2015:
    print("You are part of the Gen Z, iGen, or Centennials Generation. \n")
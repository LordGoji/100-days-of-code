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

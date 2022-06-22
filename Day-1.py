#Hours_worked = input("\nPlease enter the hours you worked this week: ")
#Hourly_rate = input("Please enter your hourly rate: ")
#if float(Hours_worked) > 40: ## If you worked overtime this block runs
#    Overtime_hours = float(Hours_worked) - 40
#    Weekly_pay = (float(Hourly_rate) * 40) + (float(Overtime_hours) * (float(Hourly_rate) * 1.5))
#    print("\nYou accrued some overtime this week. ")
#    print("Your weekly pay is equal to: ", Weekly_pay)
#    print("\n")
#else:  ## otherwise this block runs
#    Weekly_pay = float(Hourly_rate) * float(Hours_worked)
#    print("\nYour weekly pay is equal to: ", Weekly_pay)
#    print("\n")


#This time I'm going to use Try/Except to look for errors in input for pay calculation.
def main():
    Hours_worked = input("\nPlease enter the hours you worked this week: ")
    try: numeric_input_check = int(Hours_worked)
    except: Hours_worked = -1
    if int(Hours_worked) > 0:
        main2(int(Hours_worked))
    else: 
        print('Error, please enter a numeric input\n')
        main()
    return

def main2(Hours_worked):
    Hourly_rate = input("Please enter your hourly rate: ")
    try: float(Hourly_rate)
    except: Hourly_rate = -1
    if float(Hourly_rate) > 0:
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
    else:
        print('Error, please enter a numeric input\n')
        main2(Hours_worked)
    return

main()
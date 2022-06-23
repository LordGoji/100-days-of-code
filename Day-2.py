def pay_breakdown(Salary):
    x = float(Salary)
    print('\nYou make $', x , ' in one year.')
    monthly_pay = float(Salary)/12
    weekly_pay = float(Salary)/52
    daily_pay = float(Salary)/365
    hourly_pay = (float(Salary)/365)/8
    print('You will make $' , monthly_pay , 'a month before taxes come out.')
    print('You will make $' , weekly_pay , 'a week before taxes come out.')
    print('You will make $' , daily_pay , 'a day before taxes come out.')
    print('You will make $' , hourly_pay , 'an hour before taxes come out.\n')

def main():
    Salary = input('Please enter your yearly salary: ')
    try:
        numeric_input_check = float(Salary)
    except:
        Salary = -1
    if float(Salary) > 0:
        pay_breakdown(float(Salary))
    else:
        print('Error, please input a numeric number! \n')
        main()
    return

main()
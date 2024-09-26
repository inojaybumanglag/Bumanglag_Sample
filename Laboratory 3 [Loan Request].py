salary = int(input("Please enter your monthly salary: "))
loan_amount = int(input("Please enter your desired loan amount: "))

if(salary>=30000):

    if(loan_amount<=salary*10):

        months = int(input("How many months would you like to pay for the loan?: "))
        interest = loan_amount*0.10
        total_payable = loan_amount+interest
        monthly_payment = total_payable/months

        print("Your loan is now approved!")
        print(f"Your loaned amount is {loan_amount}.")
        print(f"The interest for your loan is {interest:.2f}.")
        print(f"Your total payable amount is {total_payable:.2f}.")
        print(f"Payable for {months} months at {monthly_payment:.2f} monthly.")

    else:
        print("Requested loan exceeds the eligible amount.")

else:
    print("Salary is too low for loan application.")
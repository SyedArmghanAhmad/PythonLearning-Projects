#collect the necessary input:  principal , apr, years
#calculate the monthly payment
# show the user

def main():
    print(" This is a monthly payment loan calculator ")
    print("")

    principal = float(input("input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years =int(input("Input amount of years: "))

    monthly_interest_rate = apr/ 1200 #divide by 12 (for 12 months) and 100 (to turn percentage into a decimal).
    amount_of_months = years*12
    monthly_payment = principal * monthly_interest_rate/(1 - ( 1 + monthly_interest_rate)**(-amount_of_months))
    print("The monthly payment for this Loan is: %.2f" % monthly_payment)

main()
